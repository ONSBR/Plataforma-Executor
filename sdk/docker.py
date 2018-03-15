import docker
from sdk.utils import log
from runner import settings

client = docker.DockerClient(base_url='unix://var/run/docker.sock')


def run_container(process_instance):
    """
    """
    log('Executing process app. {process_instance}', process_instance=process_instance)
    log(f'Container will be removed after execution? {settings.REMOVE_CONTAINER_AFTER_EXECUTION}')
    container = client.containers.run(
        process_instance['image'],
        environment={
            "INSTANCE_ID": process_instance["id"],
            "PROCESS_ID": process_instance["processId"],
            "SYSTEM_ID": process_instance["systemId"]
        },
        network='plataforma_network',
        stdout=True,
        remove=settings.REMOVE_CONTAINER_AFTER_EXECUTION,
        detach=True,
    )
