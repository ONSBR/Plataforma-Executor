from sdk.events import Event
from sdk.models import Event as MEvent
def test_should_check_if_event_is_a_reproduction():

    evt = MEvent({"name":""})

    evt1 = MEvent({"name":"wrong"})

    evt2 = MEvent({"name":Event.REPRODUCTION_EVENT})
    evt3 = MEvent(**{"name":Event.REPRODUCTION_EVENT,"reproduction":{"sada":""}})

    evt4 = MEvent(**{"name":Event.REPRODUCTION_EVENT, "reproduction":{"instance_id":"id", "owner":"ow"}})

    assert Event().is_reproduction(evt) == False
    assert Event().is_reproduction(evt1) == False
    assert Event().is_reproduction(evt2) == False
    assert Event().is_reproduction(evt3) == False
    assert Event().is_reproduction(evt4) == True