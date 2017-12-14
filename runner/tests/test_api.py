import falcon


def test_list_enqueued_events(client):
    status, resp_body = client.get('/event')
    
    assert status == falcon.HTTP_OK
    assert resp_body['total'] == 0
    assert len(resp_body['events']) == 0


def test_put_new_event(client):
    status, resp_body = client.put('/event', {})

    assert status == falcon.HTTP_ACCEPTED
    assert resp_body['id'] == 1
