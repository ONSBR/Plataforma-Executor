from urllib.error import HTTPError
from sdk import settings, models
from sdk.utils import HttpClient


def commit(id, data):
    result = HttpClient.post(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{id}/commit", data)
    return not result.has_error


def create_memory(process_instance_id, event):
    result = HttpClient.post(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{process_instance_id}", { "event": event})

    return not result.has_error

def first_commit(instance_id):
    """ return first commit from instance id  """
    result = HttpClient.get(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{instance_id}/head")
    if len(result.data) > 0:
        return result.data[0]
    return None

def clone(from_instance_id, to_instance_id):
    """ clone process memory with instance id """
    result = HttpClient.post(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/clone/{from_instance_id}/{to_instance_id}")
    return not result.has_error
