from urllib.error import HTTPError
from sdk import settings, models
from sdk.utils import HttpClient


def create_memory(process):
    result = HttpClient.get(
        "{settings.PROCESS_MEMORY_URL}/{process.solution}/{process.instance}/create")

    if result.has_error:
        raise HTTPError()
        # TODO: log and raise an error.
        pass
