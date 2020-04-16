import process_instance

from sdk.utils import log
from sdk.docker import run_container

def start(event):
    result = process_instance.create(event)
    if result and "operation_instance" in result:
        log("Running container")
        run_container(result["operation_instance"],event.name)
        log(''"--------------------------------------------------------------------------------------------------------------------\n\n")
