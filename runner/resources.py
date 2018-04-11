import json
import falcon
from runner import settings
from sdk.models import Event
from sdk.utils import log
import process_instance

class ProcessInstanceResource:
    """
    Creates a process instance on APICore and ProcessMemory
    """

    def on_post(self, request, response):
        log('Create process instance to event: {event}', event=request.media)
        event = Event(**request.media)
        result = process_instance.create(event)
        if result and "process_instance" in result:
            response.body = json.dumps(result["process_instance"])
            response.status = falcon.HTTP_CREATED
        else:
            response.body = json.dumps({"error":"Cannot create process instance"})
            response.status = falcon.HTTP_INTERNAL_SERVER_ERROR
