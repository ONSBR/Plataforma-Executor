import docker
from sdk import coreapi
from runner import settings


class Processor:
    """Executes a new instance of a process app.
    """
    def __init__(self):
        self.client = docker.from_env()

    def process(self, event):
        """
        """
        processes = coreapi.get_processes_by_event(event)

        for process in processes:
            self._run_container(process.container)

    def _run_container(self, container_info):
        """
        """
        self.client.containers.run(
            f"{settings.DOCKER_REGISTRY_URL}:{settings.DOCKER_REGISTRY_PORT}/{container_info.name}:{container_info.tag}",
            stdout=True,
            remove=True,
            detach=True,
        )
