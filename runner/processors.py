import docker


class Processor:
    """Executes a new instance of a process app.
    """
    def process(self, event):
        """
        Todo:
            - list processes by event

            - for each process:
                - load process memory
                - enqueue

        """
        pass


class DockerProcessor(Processor):
    """Executes process apps inside docker containers.
    """
    def __init__(self):
        self.client = docker.from_env()

    def process(self, event):
        return



