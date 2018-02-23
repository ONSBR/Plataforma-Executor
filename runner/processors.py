import docker
from sdk import coreapi, process_memory, events
from sdk.utils import log
from runner import settings
from runner import exceptions
import reproduction
import execution

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
        if events.Event().is_reproduction(event):
            reproduction.dispatch(event)
        else:
            execution.start(event)