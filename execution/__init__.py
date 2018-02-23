from sdk import coreapi, process_memory, events
from sdk.utils import log
from runner import settings
from runner import exceptions
import execution
from sdk.docker import run_container

def start(event):
    operation = coreapi.get_operation_by_event(event)
    if not operation:
        log(f"Event {event.name} has not subscribers")
        return

    process_instance = coreapi.create_process_instance(operation, event.name)

    if not process_instance:
        log("""
            Could not create process instance.
            Event: {event}
            Data: {operation}.
            Process aborted.
            """,
            event=event, operation=operation)
        return

    if not process_memory.create_memory(process_instance,event):
        log(
            """
            Could not create process memory.
            Event: {event}
            Process Instance: {process_instance}.
            Process aborted.
            """,
            process_instance=process_instance, event=event)
        return

    run_container(process_instance, operation)