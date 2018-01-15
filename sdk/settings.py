import os


PROCESS_MEMORY_URL = os.getenv('PROCESS_MEMORY_URL', 'http://process_memory')
PROCESS_MEMORY_PORT = os.getenv('PROCESS_MEMORY_PORT', 80)

COREAPI_URL = os.getenv('COREAPI_URL', 'http://apicore')
COREAPI_PORT = os.getenv('COREAPI_PORT', 9110)
