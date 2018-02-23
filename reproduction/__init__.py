from sdk.coreapi import get_process_instance_by_instance_id, create_process_instance
from sdk.process_memory import clone, first_commit
from sdk.event_manager import emit_event
from sdk.models import Event
def dispatch(event):
    original_instance = get_process_instance_by_instance_id(event.reproduction["instance_id"])
    original_event = first_commit(original_instance["id"])
    process_instance = create_process_instance(original_instance, original_event["name"])
    clone(original_instance["id"], process_instance["id"],2)
    original_event["instance_id"] = process_instance["id"]
    emit_event(original_event)

