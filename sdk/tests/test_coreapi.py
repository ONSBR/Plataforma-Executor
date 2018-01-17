import mock
from sdk.models import Event
from sdk.utils import ExecutionResult
from sdk.coreapi import get_operation_by_event, create_process_instance


def test_get_operation_by_event():
    event = Event(name='event')

    with mock.patch('sdk.coreapi.HttpClient') as mock_client:
        mock_client.get.return_value = ExecutionResult.ok(data=[1])
        operation = get_operation_by_event(event)

        assert operation == 1


def test_get_operation_by_event_fail():
    event = Event(name='event')

    with mock.patch('sdk.coreapi.HttpClient') as mock_client:
        mock_client.get.return_value = ExecutionResult.error(status_code=404, message='error')
        operation = get_operation_by_event(event)

        assert operation is None



def test_create_process_instance():
    operation = {
        'systemId': 'asdf',
        'processId': 'fdsa'
    }

    with mock.patch('sdk.coreapi.HttpClient') as mock_client:
        mock_client.post.return_value = ExecutionResult.ok(data=[1])
        instance = create_process_instance(operation)

        assert instance == 1


def test_create_process_instance_fail():
    operation = {
        'systemId': 'asdf',
        'processId': 'fdsa'
    }

    with mock.patch('sdk.coreapi.HttpClient') as mock_client:
        mock_client.post.return_value = ExecutionResult.error(status_code=404, message='error')
        instance = create_process_instance(operation)

        assert instance is None
