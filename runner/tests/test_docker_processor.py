import mock
import docker

from sdk import coreapi

from runner import settings
from runner.processors import Processor


@mock.patch('docker.client.ContainerCollection')
@mock.patch('sdk.coreapi.get_processes_by_event')
def test_execute_container(mock_get_processes_by_event, mock_containers):
    # mock
    docker_processor = Processor()
    mock_get_processes_by_event.return_value = [
        coreapi.Process(
            name="Dummy Process",
            container=coreapi.Container(
                name="dummy_process",
                tag="latest",
            )
        )
    ]

    # act
    docker_processor.process("event")

    # assert
    docker_processor.client.containers.run.assert_called_with(
        f"{settings.DOCKER_REGISTRY_URL}:{settings.DOCKER_REGISTRY_PORT}/dummy_process:latest",
        stdout=True,
        remove=True,
        detach=True,
    )


