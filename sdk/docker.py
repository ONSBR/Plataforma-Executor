import docker
from sdk.utils import log
from runner import settings

client = docker.DockerClient(base_url='unix://var/run/docker.sock')


def run_container(process_instance):
    """
    """
    log("**********************************************************")
    log('Executing process app. instance id={process_instance_id} image={image}', process_instance_id=process_instance["id"], image=process_instance["image"])
    log(f'Container will be removed after execution? {settings.REMOVE_CONTAINER_AFTER_EXECUTION}')
    log("**********************************************************")
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
