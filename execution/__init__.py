from sdk import coreapi, process_memory, events
from sdk.utils import log
from runner import settings
from runner import exceptions
import execution
import process_instance
from sdk.docker import run_container
from sdk.events import Event

def start(event):
    result = process_instance.create(event)
    if result and "operation_instance" in result:
        log("Running container")
        run_container(result["operation_instance"],event.name)
        log(''"--------------------------------------------------------------------------------------------------------------------\n\n")
