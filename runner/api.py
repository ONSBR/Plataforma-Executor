import falcon
from runner.resources import EventResource, DebugResource


runner_api = falcon.API()
runner_api.add_route('/event', EventResource())

runner_api.add_route('/debug', DebugResource())
