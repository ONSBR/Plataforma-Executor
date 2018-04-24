import falcon
from runner.resources import ProcessInstanceResource


runner_api = falcon.API()

runner_api.add_route('/instance/create', ProcessInstanceResource())
