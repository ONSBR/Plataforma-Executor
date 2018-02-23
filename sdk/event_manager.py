
from sdk.utils import HttpClient, log
from sdk import settings


def emit_event(event):
    result = HttpClient.put(
        f"{settings.EVENT_MANAGER_URL}:{settings.EVENT_MANAGER_PORT}/sendevent", event)
    return not result.has_error