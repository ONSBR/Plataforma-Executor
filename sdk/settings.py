import os

PROCESS_MEMORY_URL = f"http://{os.getenv('PROCESS_MEMORY_URL', 'localhost')}"
PROCESS_MEMORY_PORT = os.getenv('PROCESS_MEMORY_PORT', 9091)

COREAPI_URL = f"http://{os.getenv('COREAPI_URL', 'localhost')}"
COREAPI_PORT = os.getenv('COREAPI_PORT', 9110)

EVENT_MANAGER_URL = f"http://{os.getenv('EVENT_MANAGER_URL', 'localhost')}"
EVENT_MANAGER_PORT = os.getenv('EVENT_MANAGER_PORT', 8081)


RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'rabbitmq')
RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')
RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', 'plataforma_v1.0')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', 5672)
