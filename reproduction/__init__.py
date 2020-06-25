from sdk.coreapi import get_process_instance_by_instance_id, create_process_instance, create_reproduction_instance
from sdk.process_memory import clone, first_commit
from sdk.event_manager import emit_event
from sdk.models import Event
from sdk.utils import log
from sdk import coreapi, process_memory, events, schema
from sdk.docker import run_container


def dispatch(event):
    if not "instanceId" in event.reproduction:
        log(f"Reproduction event should have field instanceId on section reproduction")
        return False

    if event.operationId:
        operation = coreapi.get_operation_by_id(event)
    elif event.version:
        operation = coreapi.get_operation_by_event_and_version(event, event.version)
    else:
        operation = coreapi.get_operation_by_event(event)

    # Pega instancia original no core API, que você quer reproduzir
    original_instance = get_process_instance_by_instance_id(
        event.reproduction["instanceId"])

    if original_instance == None:
        log(f"Instance {event.reproduction['instanceId']} not found in process memory")
        return False

    # Evento que gerou a instancia original na memória de processamento, que você quer reproduzir
    original_event = first_commit(original_instance["id"])

    if original_event == None:
        log(f"Origin event not found for instance {original_instance['id']}")
        return False

    original_event = original_event["event"]
    name = original_event.pop("name")
    original_event["scope"] = "reproduction"

    # Cria instancia de processo para a reproducao no core API
    # TODO: Entender porque passar instancia original e se está certo fazer isto
    process_instance = create_process_instance(original_instance, Event(name, **original_event))

    if process_instance is None:
        log(f"Cannot create a new instance from origin {original_instance['id']} and event {name}")
        return False

    # Clona a memória de processamento e atribui o novo instance ID
    # if not clone(original_instance["id"], process_instance["id"]):
    #   log(f"Cannot clone origin process memory from instance {original_instance['id']} and event {name}")
    #    return False
    
    original_event["name"] = name
    original_event["instanceId"] = process_instance["id"]
    original_event["header"]["instanceId"] = process_instance["id"]
    original_event["reproduction"]["to"] = process_instance["id"]

    if not process_memory.create_memory(process_instance['id'], original_event):
        log(
            """Could not create process memory. Event: {event} Process Instance: {process_instance}. Process aborted.""",
            process_instance=process_instance, event=event)
        return

    log(f"event scope is {original_event['scope']}")
    log(f"running image {operation['image']} for event {event.name} with version {event.version}")
    operation_instance = coreapi.create_operation_instance(operation, event.name, process_instance["id"])
    operation_instance['is_reprocessing'] = event.scope == 'reprocessing'

    run_container(operation_instance, event.name)

    # original_event["instanceId"] = process_instance["id"]
    # log(f"Dispatching reproduction event {name}")
    #
    # original_event["name"] = name
    #
    # log(f"event scope is {event.scope}")
    # log(f"running image {operation['image']} for event {event.name} with version {event.version}")
    # operation_instance = coreapi.create_operation_instance(operation, event.name, process_instance["id"])
    # operation_instance['is_reprocessing'] = event.scope == 'reprocessing'
    #
    # run_container(operation_instance, event.name)

    # reproduction = original_instance.copy()
    # reproduction["originalId"] = original_instance["id"]
    # reproduction["instanceId"] = process_instance["id"]
    # reproduction["owner"] = event.reproduction["owner"]
    # if "externalId" in event.reproduction:
    #     reproduction["externalId"] = event.reproduction["externalId"]
    # else:
    #     reproduction["externalId"] = ""

    # rep_instance = create_reproduction_instance(reproduction)
    # if rep_instance == None:
    #     log(f"Cannot create reproduction instance on API Core")
    #     return False
    # log(f"Created reproduction instance on API Core id={rep_instance['id']}")

    return True
