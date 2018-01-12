from unittest.mock import Mock
import json
import falcon
from runner import api, resources
from runner.settings import PROCESSOR as processor


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


