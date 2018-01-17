import mock
import docker

from sdk import coreapi, models

from runner import settings
from runner.processors import DockerProcessor


@mock.patch('docker.client.ContainerCollection')
@mock.patch('sdk.coreapi.get_operation_by_event')
def test_execute_container_aborts_if_event_has_not_operation(mock_get_operation_by_event,
                                                             mock_containers):

    docker_processor = DockerProcessor()
    mock_get_operation_by_event.return_value = None

    # act
    docker_processor.process(models.Event(name="event"))

    # assert
    docker_processor.client.containers.run.assert_not_called()


@mock.patch('docker.client.ContainerCollection')
@mock.patch('sdk.coreapi.get_operation_by_event')
@mock.patch('sdk.process_memory.create_memory')
@mock.patch('sdk.coreapi.create_process_instance')
def test_execute_creates_process_instance(mock_create_process_instance,
                                          mock_create_process_memory,
                                          mock_get_operation_by_event,
                                          mock_containers):
    docker_processor = DockerProcessor()
    operation = {"container": "container"}
    mock_get_operation_by_event.return_value = operation
    mock_create_process_instance.return_value = None

    # act
    docker_processor.process(models.Event(name="event"))

    # assert
    mock_create_process_instance.assert_called_with(operation)
    mock_create_process_memory.assert_not_called()


@mock.patch('docker.client.ContainerCollection')
@mock.patch('sdk.coreapi.get_operation_by_event')
@mock.patch('sdk.process_memory.create_memory')
@mock.patch('sdk.coreapi.create_process_instance')
def test_execute_creates_process_memory(mock_create_process_instance,
                                                         mock_create_process_memory,
                                                         mock_get_operation_by_event,
                                                         mock_containers):
    docker_processor = DockerProcessor()
    operation = {"container": "container"}
    mock_get_operation_by_event.return_value = operation
    mock_create_process_instance.return_value = "abcdef"

    # act
    docker_processor.process(models.Event(name="event"))

    # assert
    mock_create_process_instance.assert_called_with(operation)
    mock_create_process_memory.assert_called_with("abcdef")


@mock.patch('docker.client.ContainerCollection')
@mock.patch('sdk.coreapi.get_operation_by_event')
@mock.patch('sdk.process_memory.create_memory')
@mock.patch('sdk.coreapi.create_process_instance')
def test_execute_new_instance(mock_create_process_instance,
                              mock_create_process_memory,
                              mock_get_operation_by_event,
                              mock_containers):
    # mock
    docker_processor = DockerProcessor()
    operation = {"container": "container"}
    mock_get_operation_by_event.return_value = operation
    mock_create_process_instance.return_value = "abcdef"

    # act
    docker_processor.process(models.Event(name="event"))

    # assert
    docker_processor.client.containers.run.assert_called_with(
        "container",
        remove=True,
        detach=True,
        stdout=True,
    )
