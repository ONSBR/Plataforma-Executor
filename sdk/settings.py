import os

#FIXME mudar de localhost para process_memory
PROCESS_MEMORY_URL = f"http://{os.getenv('PROCESS_MEMORY_URL', 'localhost')}"
PROCESS_MEMORY_PORT = os.getenv('PROCESS_MEMORY_PORT', 9091)

#FIXME mudar de localhost para apicore
COREAPI_URL = f"http://{os.getenv('COREAPI_URL', 'localhost')}"
COREAPI_PORT = os.getenv('COREAPI_PORT', 9110)

#FIXME mudar de localhost para event_manager
EVENT_MANAGER_URL = f"http://{os.getenv('EVENT_MANAGER_URL', 'localhost')}"
EVENT_MANAGER_PORT = os.getenv('EVENT_MANAGER_PORT', 8081)
