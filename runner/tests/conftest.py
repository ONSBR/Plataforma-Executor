import json
from falcon import testing
import pytest

from runner.api import api


class TestClient(testing.TestClient):
    """Rest Test Client
    """
    def __init__(self):
        super().__init__(api)
   
    def _split_response(self, response):
        return response.status, json.loads(response.content)

    def get(self, uri):
        return self._split_response(
            self.simulate_get(uri))

    def put(self, uri, data):
        return self._split_response(
            self.simulate_put(uri, **data))

@pytest.fixture
def client():
    """HTTP test client fixture
    """
    return TestClient()
