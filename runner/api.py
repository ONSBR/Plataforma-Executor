from uuid import uuid4
import json
import falcon


class Processor:
    """TODO: move to another namespace
    """
    @staticmethod
    def process(event):
        """
        Todo:
            - list processes by event

            - for each process:
                - load process memory
                - enqueue

        """
        pass


class Event:
    """TODO: move to another namespace
    """
    def __init__(self, name, pars):
        self.id = uuid4()
        self.name = name
        self.pars = pars

    @classmethod
    def from_json(cls, data):
        """Returns a new event instance from json data.
        """
        _data = json.loads(data)
        return cls(**_data)


    def to_json(self):
        """Returns a dictonary containing serializable properties
           from an instance.
        """
        return {
            "id": str(self.id)
        }


class EventResource:
    """
    """

    def on_get(self, request, response):
        """Returns all enqueued events.
        """
        body = {
            'events': [],
            'total': 0
        }

        response.body = json.dumps(body)

    def on_put(self, request, response):
        """Enqueue a new event.
        """
        event = Event(**request.media)

        Processor.process(event)
        response.media = event.to_json()
        response.status = falcon.HTTP_ACCEPTED


api = falcon.API()
api.add_route('/event', EventResource())
