import mock
from sdk.models import Process
from sdk.process_memory import create_memory, HttpClient


@mock.patch('sdk.process_memory.HttpClient', auto_spec=True)
def test_create_memory(mock_client):
   process = Process(
       id="id", name='name', solution="solution",
       nstance="instance", container=None)
   memory = create_memory(process)
