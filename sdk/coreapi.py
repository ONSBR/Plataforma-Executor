import json
from sdk.models import Process, Container
from sdk.utils import HttpClient, log
from sdk import settings



def persist(data):
    return HttpClient.post(
        f"{settings.COREAPI_URL}:{settings.COREAPI_PORT}/core/persist",
        data=data)


def get_operation_by_event(event):
    """ Retrieves the operation subscribed to an event.
    """
    result = HttpClient.get(
        f"{settings.COREAPI_URL}:{settings.COREAPI_PORT}/core/operation?filter=byEvent&event={event.name}")

    if not result.has_error and result.data:
        return result.data[0]

def get_process_instance_by_instance_id(instance_id):
    result = HttpClient.get(
        f"{settings.COREAPI_URL}:{settings.COREAPI_PORT}/core/processInstance?filter=byId&id={instance_id}")

    if not result.has_error and result.data:
        return result.data[0]


def create_process_instance(operation, event_name):
    """creates a new process execution instance.
    """
    log("Create process instance {operation}", operation=operation)
    result = persist([{
            "systemId": operation['systemId'],
            "processId": operation['processId'],
            "origin_event_name": event_name,
            "startExecution": 1516045449619,  # TODO: get datetime as javascript.
            "status": "created",
            "_metadata": {
                "type": "processInstance",
                "changeTrack": "create",
            }
        }])
    if not result.has_error and result.data:
        return result.data[0]

