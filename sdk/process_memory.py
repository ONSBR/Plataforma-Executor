from urllib.error import HTTPError
from sdk import settings, models
from sdk.utils import HttpClient


def commit(id, data):
    result = HttpClient.post(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{id}/commit", data)
    return not result.has_error


def create_memory(process, event):
    result = HttpClient.post(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{process['id']}/create", event.__dict__)

    return not result.has_error

def first_commit(instance_id):
    """ return first commit from instance id  """
    result = HttpClient.get(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{instance_id}/first")
    if len(result.data) > 0:
        return result.data[0]
    return None

def clone(from_instance_id, to_instance_id, n):
    """ clone process memory with instance id from commit 0 to n  """
    result = HttpClient.post(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{from_instance_id}/{to_instance_id}/clone")
    return not result.has_error
