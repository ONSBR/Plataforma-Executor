from unittest.mock import Mock
import json
import mock
import falcon
from runner import api, resources
from runner.settings import PROCESSOR as processor
from sdk.events import Event
import uuid
import process_instance


original_process = processor.process

def test_list_enqueued_events(client):
    # act
    status, resp_body = client.get('/event')

    # assert
    assert status == falcon.HTTP_OK
    assert resp_body['total'] == 0
    assert len(resp_body['events']) == 0


def test_put_new_event(client):
    # mock
    processor.process = Mock()

    data = {
        "name": "fake event",
        "instance": "",
        "payload": ""
    }

    # act
    status, resp_body = client.put('/event', data)

    # assert
    processor.process.assert_called_once()
    assert status == falcon.HTTP_ACCEPTED

@mock.patch('process_instance.create')
def test_create_process_instance_on_api(mock_process_instance_create, client):
    # mock

    data = {
        "name": "fake event",
        "instance": "",
        "payload": ""
    }
    mock_process_instance_create.return_value = {"process_instance":{"id":"instance_id"}}
    # act
    status, resp_body = client.post('/instance/create', data)

    # assert
    mock_process_instance_create.assert_called_once()
    assert "id" in resp_body
    assert status == falcon.HTTP_CREATED



