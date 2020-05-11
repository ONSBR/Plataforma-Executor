from sdk import coreapi, process_memory, events, schema
from sdk.utils import log
from runner import settings
from runner import exceptions
import execution
from sdk.docker import run_container
from sdk.events import Event
from sdk.docker import run_container
from json import dumps


def start(event):
    log(f"Version: {event.version} and reference_date: {event.referenceDate} and processId {event.processId}")

    operation = coreapi.get_operation_by_event_and_version(event, event.version)
    if not operation:
        log("""event {event} has no subscribers""", event=event)
        return

    app_version = schema.get_app_version(event.referenceDate, operation["processId"])
    if app_version:
        operation["version"] = app_version[0]["version"]
        operation["image"] = app_version[0]["tag"]

    original_instance_id = event.reprocessing["instance_id"]
    if original_instance_id:
        original_instance = coreapi.get_process_instance_by_instance_id(original_instance_id)
    else:
        """Reprocess without original instance"""
        original_instance = {
            'systemId': operation['systemId'],
            'processId': operation['processId']
        }

    log(f"Creating new process instance to respond event {event.name}")
    log("""event {event}""", event=event)
    process_instance = coreapi.create_process_instance(original_instance, event)

    event.instanceId = process_instance["id"]
    event.reprocessing["to"] = process_instance["id"]

    if not process_memory.create_memory(process_instance['id'], event.__dict__):
        log(
            """Could not create process memory. Event: {event} Process Instance: {process_instance}. Process aborted.""",
            process_instance=process_instance, event=event)
        return

    if not process_instance:
        log("""Could not create process instance. Event: {event} Process aborted.""", event=event)
        return

    log(f"event scope is {event.scope}")
    log(f"running image {operation['image']} for event {event.name} with version {event.version}")
    operation_instance = coreapi.create_operation_instance(operation, event.name, process_instance["id"])
    operation_instance['is_reprocessing'] = event.scope == 'reprocessing'

    run_container(operation_instance, event.name)
