from sdk import coreapi, process_memory, events
from sdk.utils import log
from runner import settings
from runner import exceptions
import execution
from sdk.docker import run_container
from sdk.events import Event

def start(event):
    log(" ")
    log(" ")
    log("Execution")
    log("--------------------------------------------------------------------------------------------------------------------")
    operation = coreapi.get_operation_by_event(event)
    if not operation:
        log(f"Event {event.name} has no subscribers")
        log("--------------------------------------------------------------------------------------------------------------------")
        return

    if event.instance_id:
        log(f"Event {event.name} already have a instance id={event.instance_id}")
        process_instance = coreapi.get_process_instance_by_instance_id(event.instance_id)
        log(f"process instance id = {process_instance['id']} image={process_instance['image']}")
        if not process_instance:
            log(f"Instance Id {event.instance_id} not found on Api Core")
            return

        if  event.scope == "execution":
            log(f"Override process instance image from {process_instance['image']} to {operation['image']}")
            process_instance["image"] = operation["image"]
        run_container(process_instance)
        log("--------------------------------------------------------------------------------------------------------------------\n\n")
        return
    else:
        process_instance = coreapi.create_process_instance(operation, event.name)

    if not process_instance:
        log("""
            Could not create process instance.
            Event: {event}
            Data: {operation}.
            Process aborted.
            """,
            event=event, operation=operation)
        log("--------------------------------------------------------------------------------------------------------------------\n\n")
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
        log("--------------------------------------------------------------------------------------------------------------------\n\n")
        return

    run_container(process_instance)
    log("--------------------------------------------------------------------------------------------------------------------\n\n")
