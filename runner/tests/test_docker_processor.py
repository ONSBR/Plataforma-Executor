import mock
import docker

from sdk import coreapi

from runner import settings
from runner.processors import DockerProcessor


@mock.patch('docker.client.ContainerCollection')
@mock.patch('sdk.coreapi.get_operation_by_event')
@mock.patch('sdk.process_memory.create_memory')
def test_execute_container(mock_create_memory, mock_get_operation_by_event, mock_containers):
    # mock
    docker_processor = DockerProcessor()
    mock_get_operation_by_event.return_value = [
        coreapi.Process(
            id="id",
            name="Dummy Process",
            solution="Solution",
            instance=None,
            container=coreapi.Container(
                name="dummy_process",
                tag="latest",
            )
        )
    ]

    # act
    docker_processor.process("event")

    # assert
    mock_create_memory.assert_called_once()
    docker_processor.client.containers.run.assert_called_with(
        f"{settings.DOCKER_REGISTRY_URL}:{settings.DOCKER_REGISTRY_PORT}/dummy_process:latest",
        stdout=True,
        remove=True,
        detach=True,
    )


