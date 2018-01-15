import falcon
from runner.resources import EventResource
from runner import settings


runner_api = falcon.API()
runner_api.add_route('/event', EventResource())
