from celery import Celery
from sdk.settings import RABBITMQ_URL, RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_VHOST
from runner import settings
from sdk.models import Event
app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_URL}/{RABBITMQ_VHOST}')


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

        if event.name.startswith("system."):
            print("Processing System Event")
            if event.name == "system.executor.enable.debug":
                print("ENABLE DEBUG")
                settings.REMOVE_CONTAINER_AFTER_EXECUTION = False
                return 0
            elif event.name == "system.executor.disable.debug":
                print("DISABLE DEBUG")
                settings.REMOVE_CONTAINER_AFTER_EXECUTION = True
                return 0
        else:
            settings.PROCESSOR.process(event)
        return 0
    except Exception as e:
        tsk.retry(countdown=30, exc=e)