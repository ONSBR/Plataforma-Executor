

from sdk.coreapi import persist
from sdk.process_memory import create_memory, commit
from sdk.models import Event
from sdk.events import Event as SystemEvent
from reproduction import dispatch
import uuid



def create_process_instance():
    id = str(uuid.uuid4())
    p = [
    {
        "processId": "61728cac-a576-4643-8e58-82a83b304053",
        "systemId": str(uuid.uuid4()),
        "startExecution": "2018-01-15T19:44:09.619Z",
        "origin_event_name":"action.request",
        "status": "created",
        "id": id,
        "_metadata": {
            "type": "processInstance",
            "changeTrack": "create"
        }
    }
    ]
    persist(p)
    return id

def create_event(id):
    evt = Event("action.request", **{"payload":{"a":"b"}})
    create_memory({"id":id},evt)

def test_should_start_reproduction():
    id = create_process_instance()
    create_event(id)
    commit(id, {"dataset":"here"})

    reprod = Event(SystemEvent.REPRODUCTION_EVENT, **{"reproduction":{"instanceId":id,"owner":"user"}})
    assert dispatch(reprod) == True

def test_should_stop_reproduction_when_instance_not_exist():
    reprod = Event(SystemEvent.REPRODUCTION_EVENT, **{"reproduction":{"instanceId":"123","owner":"user"}})
    assert dispatch(reprod) == False