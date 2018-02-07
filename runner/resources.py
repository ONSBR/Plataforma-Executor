import json
import falcon
from runner import settings
from sdk.models import Event
from sdk.utils import log

class EventResource:
    """
    """

    def on_get(self, request, response):
        """Returns all enqueued events.
        """
        # TODO: Implement
        body = {
            'events': [],
            'total': 0
        }

        response.body = json.dumps(body)

    def on_put(self, request, response):
        """Enqueue a new event.
        """
        log('Received event: {event}', event=request.media)
        event = Event(**request.media)

        # TODO:
        #   the event must be enqueued on celery or somewhere
        #   else and the process must be invoked asynchronously.
        settings.PROCESSOR.process(event)
        response.status = falcon.HTTP_ACCEPTED


class DebugResource:
    """
    """

    def on_post(self, request, response):
        settings.REMOVE_CONTAINER_AFTER_EXECUTION = False
        response.body = "OK"

    def on_delete(self, request, response):
        settings.REMOVE_CONTAINER_AFTER_EXECUTION = True
        response.body = "OK"

    def on_get(self, request, response):
        response.body = str(settings.REMOVE_CONTAINER_AFTER_EXECUTION)