import json
from sdk.models import Process, Container
from sdk.utils import HttpClient
from sdk import settings


def get_operation_by_event(event):
    """ Retrieves the operation subscribed to an event.
    """
    result = HttpClient.get(
        f"{settings.COREAPI_URL}/core/operation?filter=byEvent&event={event.name}")

    if not result.has_error and result.data:
        return result.data[0]

    # TODO: log error


def create_process_instance(process_instance):
    """creates a new process execution instance.
    """
    result = HttpClient.post(
        f"{settings.COREAPI_URL}/core/persist",
        data={
            "systemId": process_instance.systemId,
            "processId": process_instance.processId,
            "startExecution": 1516045449619, # TODO: get datetime as javascript.
            "status": "created",
            "_metadata": {
                "type": "processInstance",
                "changeTrack": "create",
            }
        }
    )

    if not result.has_error:
        return result.data

    # TODO: log error


