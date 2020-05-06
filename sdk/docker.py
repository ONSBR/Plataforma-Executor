import docker
from sdk.utils import log
from runner import settings
import os
import random

client = docker.DockerClient(base_url='unix://var/run/docker.sock')


def run_container(operation_instance, event_name):
    delete_container = os.getenv('REMOVE_CONTAINER_AFTER_EXECUTION', "True") == "True"
    """
    """
    log("**********************************************************")
    log('Executing process app. instance id={process_instance_id} image={image}',
        process_instance_id=operation_instance["processInstanceId"], image=operation_instance["image"])
    log(f'Container will be removed after execution? {delete_container}')
    log("**********************************************************")

    ports = None
    # if settings.ENABLE_CONTAINER_DEBUG:
    # ports = {"9229": str(random.randrange(7000, 7999, 2))}
    log(f'Container version: {operation_instance["version"]}')
    log(f'Container image: {operation_instance["image"]}')
    is_reprocessing = 'is_reprocessing' in operation_instance.keys() and operation_instance['is_reprocessing'] == True

    try:
        container = client.containers.run(
            operation_instance['image'],
            environment={
                "INSTANCE_ID": operation_instance["processInstanceId"],
                "PROCESS_ID": operation_instance["processId"],
                "SYSTEM_ID": operation_instance["systemId"],
                "IS_REPROCESSING": is_reprocessing,
                "EVENT": event_name,
                "VERSION": operation_instance["version"],
                "TAG": operation_instance['image']
            },
            network='plataforma_network',
            stdout=True,
            ports=ports,
            remove=delete_container,
            labels={
                "instance_id": operation_instance["processInstanceId"]
            }
        )
    except Exception as ex:
        log(f'Error: {str(ex)}')
