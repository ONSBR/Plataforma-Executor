import mock
from sdk.models import Process
from sdk.utils import ExecutionResult
from sdk.process_memory import create_memory


def test_create_memory():
    process = Process(
       id="id", name='name', solution="solution",
       instance="instance", container=None)

    with mock.patch('sdk.process_memory.HttpClient') as mock_client:
        mock_client.get.return_value = ExecutionResult.ok()
        create_memory(process)


def test_create_memory_fail():
    process = Process(
       id="id", name='name', solution="solution",
       instance="instance", container=None)

    with mock.patch('sdk.process_memory.HttpClient') as mock_client:
        mock_client.get.return_value = ExecutionResult.error(message="an error", status_code=404)
        create_memory(process)



