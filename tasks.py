from celery import Celery
from sdk.settings import RABBITMQ_URL, RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_VHOST
from runner import settings
from sdk.models import Event
app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_URL}/{RABBITMQ_VHOST}')

DEBUG =  os.environ.get("DEBUG_MODE", False)

@app.task(serializer='json', bind=True)
def process(tsk, dict_event):
    try:
        print("******************************************")
        print("executing task")
        print("Config-------------------------------------------")
        print(f"REMOVE_CONTAINER_AFTER_EXECUTION {settings.REMOVE_CONTAINER_AFTER_EXECUTION}")
        print("-------------------------------------------------")
        print("******************************************")
        event = Event(**dict_event)
        settings.REMOVE_CONTAINER_AFTER_EXECUTION = not DEBUG
        if event.name.startswith("system."):
            print("Processing System Event")
            if event.name == "system.executor.enable.debug":
                print("ENABLE DEBUG")
                DEBUG = True
                return 0
            elif event.name == "system.executor.disable.debug":
                DEBUG = False
                print("DISABLE DEBUG")
                return 0
        else:
            settings.PROCESSOR.process(event)
        return 0
    except Exception as e:
        tsk.retry(countdown=30, exc=e)