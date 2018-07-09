from sdk import coreapi, process_memory, events
from sdk.utils import log
from runner import settings
from runner import exceptions
import execution
from sdk.docker import run_container
from sdk.events import Event
from sdk.docker import run_container

def start(event):
    original_instance_id = event.reprocessing["instance_id"]
    original_instance = coreapi.get_process_instance_by_instance_id(original_instance_id)
    log(f"Creating new process instance to respond event {event.name}")
    log(f"event {event}")
    process_instance = coreapi.create_process_instance(original_instance, event)
    operation = coreapi.get_operation_by_event_and_version(event, event.version)
    if not operation:
        log("Operation not found")
        return
    if not process_memory.create_memory(process_instance, event):
        log(
            """
            Could not create process memory.
            Event: {event}
            Process Instance: {process_instance}.
            Process aborted.
            """,
            process_instance=process_instance, event=event)
        return

    if not process_instance:
        log("""
            Could not create process instance.
            Event: {event}
            Process aborted.
            """,
            event=event)
        return

    log(f"event scope is {event.scope}")
    operation_instance = coreapi.create_operation_instance(operation, event.name, process_instance["id"])
    run_container(operation_instance,event.name)