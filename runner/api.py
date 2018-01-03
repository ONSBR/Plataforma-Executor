import falcon
from runner.resources import EventResource


runner_api = falcon.API()
runner_api.add_route('/event', EventResource())
