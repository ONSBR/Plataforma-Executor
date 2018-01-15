import docker
from sdk import coreapi, process_memory
from runner import settings


class DockerProcessor:
    """Executes a new instance of a process app.
    """
    def __init__(self):
        """
        """
        self.client = docker.from_env()

    def process(self, event):
        """
        Process receives an event an tries to get a subcribed operation.
        """
        operation = coreapi.get_operation_by_event(event)

        if not operation:
            # TODO: log an event without associated operations.
            return

        if not event.instanceId:
            process_instance = coreapi.create_process_instance(operation.processId)
            process_memory.create_memory(process_instance)

        self._run_container(process_instance, operation)

    def _run_container(self, process_instance, operation):
        """
        """
        self.client.containers.run(
            operation.container,
            f"{operation.name} {operation.systemId} {process_instance}",
            stdout=True,
            remove=True,
            detach=True,
        )
