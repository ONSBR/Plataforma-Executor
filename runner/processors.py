import docker
from sdk import coreapi, process_memory
from sdk.utils import log
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
        log(f'Processing event {event}')
        operation = coreapi.get_operation_by_event(event)

        if not operation:
            log(f'There is no operation subscribed to this event.\nEvent: {event}\nOperation aborted.')
            return

        if not event.instance_id:
            process_instance = coreapi.create_process_instance(operation)

            if not process_instance:
                log(f'Could not create process instance.\nEvent: {event}\nData: {operation}.\nProcess aborted.')
                return

            if not process_memory.create_memory(process_instance, event.__dict__):
                log(f'Could not create process memory.\nEvent: {event}\nProcess Instance: {process_instance}.\nProcess aborted.')
                return

        self._run_container(process_instance, operation)

    def _run_container(self, process_instance, operation):
        """
        """
        #  import subprocess
        log(f'Executing process app. {operation}')

        #  cmd = f"docker run -d --rm {operation['container']}"
        #  with subprocess.Popen(cmd.split(), stdout=subprocess.PIPE) as proc:
            #  log(proc.stdout.read())

        container = self.client.containers.run(
            operation['container'],
            stdout=True,
            remove=True,
            detach=True,
        )

        log(f'Container logs. {container.logs()}')
