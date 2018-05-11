import json
from sdk.models import Process, Container
from sdk.utils import HttpClient, log
from sdk import settings
import datetime


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

def get_operation_instance_by_instance_id_and_event(instance_id,event_name):
    result = HttpClient.get(
        f"{settings.COREAPI_URL}:{settings.COREAPI_PORT}/core/operationInstance?filter=byInstanceIdEventName&processInstanceId={instance_id}&eventName={event_name}")

    if not result.has_error and result.data:
        return result.data[0]

def get_reproduction_by_instance_id(instance_id):
    result = HttpClient.get(
        f"{settings.COREAPI_URL}:{settings.COREAPI_PORT}/core/reproduction?filter=byInstance&instance={instance_id}")

    if not result.has_error and result.data:
        return result.data[0]

def create_reproduction_instance(reproduction_instance):
    """creates a new reproduction execution instance.
    """
    log("Create reproduction instance {reproduction_instance}", reproduction_instance=reproduction_instance)
    result = persist([{
            "systemId": reproduction_instance['systemId'],
            "processId": reproduction_instance['processId'],
            "originalId": reproduction_instance['originalId'],
            "instanceId": reproduction_instance['instanceId'],
            "owner": reproduction_instance['owner'],
            "externalId": reproduction_instance['externalId'],
            "start_date": str(datetime.datetime.now()),
            "_metadata": {
                "type": "reproduction",
                "changeTrack": "create",
            }
        }])
    if not result.has_error and result.data:
        return result.data[0]

def create_process_instance(operation, event_name):
    """creates a new process execution instance.
    """
    log("Create process instance {operation}", operation=operation)
    result = persist([{
            "systemId": operation['systemId'],
            "processId": operation['processId'],
            "version": operation.get('version'),
            "origin_event_name": event_name,
            "startExecution": str(datetime.datetime.now()),
            "status": "created",
            "_metadata": {
                "type": "processInstance",
                "changeTrack": "create",
            }
        }])
    if not result.has_error and result.data:
        return result.data[0]

def create_operation_instance(operation, event_name, process_instance_id):
    """creates a new operation instance.
    """
    log("Create operation instance {operation}", operation=operation)
    result = persist([{
            "systemId": operation['systemId'],
            "processId": operation['processId'],
            "eventName": event_name,
            "processInstanceId": process_instance_id,
            "image": operation["image"],
            "status": "created",
            "_metadata": {
                "type": "operationInstance",
                "changeTrack": "create",
            }
        }])
    if not result.has_error and result.data:
        return result.data[0]

