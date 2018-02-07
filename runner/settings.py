import os
import logging
from runner import processors


DEBUG = False

REMOVE_CONTAINER_AFTER_EXECUTION=True

PROCESSOR = processors.DockerProcessor()

DOCKER_REGISTRY_URL = os.getenv('DOCKER_REGISTRY_URL', 'registry')
DOCKER_REGISTRY_PORT = os.getenv('DOCKER_REGISTRY_PORT', 5000)

