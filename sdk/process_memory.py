from urllib.error import HTTPError
from sdk import settings, models
from sdk.utils import HttpClient


def create_memory(process, data):
    result = HttpClient.post(
        f"{settings.PROCESS_MEMORY_URL}:{settings.PROCESS_MEMORY_PORT}/{process['processId']}/{process['id']}/create")

    return not result.has_error
