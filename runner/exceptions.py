from sdk.utils import log


class LoggedException(Exception):
    MESSAGE = None
    CODE = None

    def __init__(self, **kwargs):
        log(self.MESSAGE, **kwargs)


class InvalidEvent(LoggedException):
    MESSAGE = "Event {event} has no subscribed operations."

    def __init__(self, event):
        self.event = event
        super().__init__(event=event)



