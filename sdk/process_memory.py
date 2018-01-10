from sdk import settings, models
from sdk.utils import HttpClient


def create_memory(process):
    result = HttpClient.get(f"{settings.PROCESS_MEMORY_URL}/{process.solution}/{process.instance}/create")

    if not result.has_error:
        return result.data

    # TODO: log and raise an error.
