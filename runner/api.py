import falcon


class EventResource:
    """
    """

    def on_get(self, request, response):
        """Returns information about enqueued events.
        """
        body = {
            'events': [],
            'total': 0
        }

        response.media = body

    def on_put(self, request, response):
        response.media = {
            'id': 1
        }
        response.status = falcon.HTTP_ACCEPTED 

api = falcon.API()
api.add_route('/event', EventResource())
