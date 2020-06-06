
class Event:
    REPRODUCTION_EVENT = "system.events.reproduction.request"
    REPROCESSING_EVENT = "system.events.reprocessing.request"
    SYSTEM_EVENT_LIST = [REPROCESSING_EVENT, REPRODUCTION_EVENT]

    def is_system_event(self, evt):
        return evt.name in Event.SYSTEM_EVENT_LIST

    def is_reproduction(self, evt):
        """ check if a received event is a reprocessing event by looking on event scope """
        if evt.scope != "reproduction":
            return False
        return True

    def is_reprocessing(self, evt):
        """ check if a received event is a reprocessing event by looking on event scope """
        if evt.scope != "reprocessing":
            return False
        return True