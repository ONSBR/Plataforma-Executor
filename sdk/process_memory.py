from urllib.error import HTTPError
from sdk import settings, models
from sdk.utils import HttpClient


def create_memory(process):
    result = HttpClient.get(
        "{settings.PROCESS_MEMORY_URL}/{process.processId}/{process.instance}/create")

    if not result.has_error:
        return result.data

    # TODO: log error
