import os


PROCESS_MEMORY_URL = f"http://{os.getenv('PROCESS_MEMORY_URL', 'process_memory')}"
PROCESS_MEMORY_PORT = os.getenv('PROCESS_MEMORY_PORT', 9091)


COREAPI_URL = f"http://{os.getenv('COREAPI_URL', 'apicore')}"
COREAPI_PORT = os.getenv('COREAPI_PORT', 9110)
