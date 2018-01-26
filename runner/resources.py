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

