from celery import Celery
from sdk.settings import RABBITMQ_URL, RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_VHOST
from runner import settings
from sdk.models import Event
import os

app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_URL}/{RABBITMQ_VHOST}')



@app.task(serializer='json', bind=True)
def process(tsk, dict_event):
    try:
        DEBUG = os.environ.get("DEBUG_MODE", True)
        event = Event(**dict_event)
        if event.name in {"system.executor.enable.debug", "system.executor.disable.debug"}:
            if event.name == "system.executor.enable.debug":
                DEBUG = True
                return 0
            elif event.name == "system.executor.disable.debug":
                DEBUG = False
                return 0
        else:
            settings.PROCESSOR.process(event)
        return 0
    except Exception as e:
        tsk.retry(countdown=30, exc=e)