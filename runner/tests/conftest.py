import json
import pytest
from falcon import testing

from runner.api import runner_api


class TestClient(testing.TestClient):
    """Rest Test Client
    """
    def __init__(self):
        super().__init__(runner_api)

    def _split_response(self, response):
        return response.status, json.loads(response.content) if response.content else None

    def get(self, uri):
        return self._split_response(
            self.simulate_get(uri))

    def put(self, uri, data):
        return self._split_response(
            self.simulate_put(uri, body=json.dumps(data)))

    def post(self, uri, data):
        return self._split_response(
            self.simulate_post(uri, body=json.dumps(data)))


@pytest.fixture
def client():
    """HTTP test client fixture
    """
    return TestClient()
