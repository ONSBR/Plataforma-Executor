import docker
from sdk import coreapi, process_memory
from sdk.utils import log
from runner import settings
from runner import exceptions


class DockerProcessor:
    """Executes a new instance of a process app.
    """
    def __init__(self):
        """
        """
        self.client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    def process(self, event):
        """
        Process receives an event an tries to get a subcribed operation.
        """
        log('Processing event {event}', event=event)
        operation = coreapi.get_operation_by_event(event)

        if not operation:
            raise exceptions.InvalidEvent(event)

        process_instance = coreapi.create_process_instance(operation)

        if not process_instance:
            log("""
                Could not create process instance.
                Event: {event}
                Data: {operation}.
                Process aborted.
                """,
                event=event, operation=operation)
            return

        if not process_memory.create_memory(process_instance,event):
            log(
                """
                Could not create process memory.
                Event: {event}
                Process Instance: {process_instance}.
                Process aborted.
                """,
                process_instance=process_instance, event=event)
            return

        self._run_container(process_instance, operation)

    def _run_container(self, process_instance, operation):
        """
        """
        log('Executing process app. {operation}', operation=operation)

        container = self.client.containers.run(
            operation['container'],
            environment={
                "INSTANCE_ID": process_instance["id"],
                "PROCESS_ID": operation["processId"],
                "SYSTEM_ID": operation["systemId"]
            },
            network='plataforma_network',
            stdout=True,
            remove=settings.REMOVE_CONTAINER_AFTER_EXECUTION,
            detach=True,
        )
