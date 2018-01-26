from collections import namedtuple


class Event:
    def __init__(self, name, **kwargs):
        self.name = name
        self.instance_id = kwargs.pop('instanceId', None)
        self.reference_date = kwargs.pop('referenceDate', None)
        self.reproduction = kwargs.pop('reproduction', dict())
        self.reprocess = kwargs.pop('reprocess', dict())
        self.payload = kwargs.pop('payload', dict())


Process = namedtuple("Process", [
    "id",
    "name",
    "solution",
    "instance",
    "container",
])


Container = namedtuple("Container", [
    "name",
    "tag",
])

