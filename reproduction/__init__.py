from sdk.coreapi import get_process_instance_by_instance_id, create_process_instance, create_reproduction_instance
from sdk.process_memory import clone, first_commit
from sdk.event_manager import emit_event
from sdk.models import Event
from sdk.utils import log


def dispatch(event):
    original_instance = get_process_instance_by_instance_id(
        event.reproduction["instanceId"])
    if original_instance == None:
        log(f"Instance {event.reproduction['instanceId']} not found in process memory")
        return False

    original_event = first_commit(original_instance["id"])
    if original_event == None:
        log(f"Origin event not found for instance {original_instance['id']}")
        return False

    process_instance = create_process_instance(original_instance, original_event["name"])

    if process_instance == None:
        log(f"Cannot create a new instance from origin {original_instance['id']} and event {original_event['name']}")
        return False

    if not clone(original_instance["id"], process_instance["id"]):
        log(f"Cannot clone origin process memory from instance {original_instance['id']} and event {original_event['name']}")
        return False

    original_event["instanceId"] = process_instance["id"]
    log(f"Dispatching reproduction event {original_event['name']}")
    original_event["scope"] = "reproduction"
    emit_event(original_event)

    reproduction = original_instance.copy()
    reproduction["originalId"] = original_instance["id"]
    reproduction["instanceId"] = process_instance["id"]
    reproduction["owner"] = event.reproduction["owner"]
    reproduction["externalId"] = event.reproduction["externalId"]

    rep_instance = create_reproduction_instance(reproduction)
    if rep_instance == None:
        log(f"Cannot create reproduction instance on API Core")
        return False
    log(f"Created reproduction instance on API Core id={rep_instance['id']}")

    return True
