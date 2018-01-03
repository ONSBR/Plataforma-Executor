from unittest.mock import Mock
import json
import falcon
from runner import api, models, resources
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
        "pars": {
            "parm_1": 1,
            "parm_2": 2
        }
    }

    # act
    status, resp_body = client.put('/event', data)

    # assert
    processor.process.assert_called_once()
    assert status == falcon.HTTP_ACCEPTED
    assert resp_body['id'] is not None


def test_parse_event_from_json():
    # mock
    data = json.dumps({
        "name": "fake event",
        "pars": {
            "parm_1": 1,
            "parm_2": 2
        }
    })

    # act
    event = models.Event.from_json(data)

    # assert
    assert event.name == "fake event"
    assert len(event.pars) == 2
    assert "parm_1" in event.pars
    assert "parm_2" in event.pars


def test_event_to_json():
    # mock
    event = models.Event(name="fake event", pars=None)

    # act
    event_json = event.to_json()

    # assert
    assert event_json["id"] is not None
