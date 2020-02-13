from sdk import coreapi, process_memory, events
from sdk.utils import log
from runner import settings
from runner import exceptions
import execution
from sdk.docker import run_container
from sdk.events import Event
from json import dumps

def create(event):
    """
    creates a new process instance based on event
    """
    if event.version:
        operation = coreapi.get_operation_by_event_and_version(event,event.version)
    else:
        operation = coreapi.get_operation_by_event(event)

    if not operation:
        log(f"Event {event.name} with version {event.version} has no subscribers")
        return

    if event.instanceId:
        log(f"Event {event.name} already have a instance id={event.instanceId}")
        process_instance = coreapi.get_process_instance_by_instance_id(
            event.instanceId)
    else:
        log(f"Creating new process instance to respond event {event.name}")
        process_instance = coreapi.create_process_instance(operation, event)
        event.instanceId = process_instance["id"]
        event.version = operation["version"]
        event.image = operation["image"]
        event.timestamp = process_instance["startExecution"]

        if not process_memory.create_memory(process_instance["id"], event.__dict__ ):
            log("""Could not create process memory. Event: {event} Process Instance: {process_instance}. Process aborted.""",process_instance=process_instance, event=event)
            return

    if not process_instance:
        log("""Could not create process instance. Event: {event} Data: {operation}. Process aborted.""",event=event, operation=operation)
        return

    log(f"event scope is {event.scope}")
    if event.scope in {"execution", "reprocessing"}:
        operation_instance = coreapi.create_operation_instance(operation, event.name, process_instance["id"])
    elif event.scope == "reproduction":
        # recupera a operation que foi executada para uma determinada instancia do processo
        log(f"instance id={process_instance['id']} event={event.name}")
        reproduction_instance = coreapi.get_reproduction_by_instance_id(process_instance["id"])
        operation_instance = coreapi.get_operation_instance_by_instance_id_and_event(reproduction_instance["originalId"], event.name)
        operation_instance.pop("id")
        operation_instance["processInstanceId"] = process_instance["id"]
        coreapi.create_operation_instance(operation_instance, event.name, process_instance["id"])
    else:
        log(f"Scope {event.scope} not supported")
        return
    result = {}
    if process_instance:
        result["process_instance"] = process_instance
    if operation_instance:
        result["operation_instance"] = operation_instance
    return result

