import docker
from sdk.utils import log
from runner import settings

client = docker.DockerClient(base_url='unix://var/run/docker.sock')


def run_container(process_instance, operation):
    """
    """
    log('Executing process app. {operation}', operation=operation)
    log(f'Container will be removed after execution? {settings.REMOVE_CONTAINER_AFTER_EXECUTION}')
    container = client.containers.run(
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
