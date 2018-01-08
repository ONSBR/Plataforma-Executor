import os
import logging
from runner import processors


DEBUG = False

PROCESSOR = processors.Processor()

DOCKER_REGISTRY_URL = os.getenv('DOCKER_REGISTRY_URL', 'registry')
DOCKER_REGISTRY_PORT = os.getenv('DOCKER_REGISTRY_PORT', 5000)

