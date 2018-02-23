from collections import namedtuple


class Event:
    def __init__(self, name, **kwargs):
        self.name = name
        self.instance_id = kwargs.pop('instance_id', None)
        self.reference_date = kwargs.pop('reference_date', None)
        self.reproduction = kwargs.pop('reproduction', dict())
        self.reprocess = kwargs.pop('reprocess', dict())
        self.payload = kwargs.pop('payload', dict())

    def __str__(self):
        return (f"Name: {self.name}"
                f"Instance Id: {self.instance_id}"
                f"Payload: {self.payload}")

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

