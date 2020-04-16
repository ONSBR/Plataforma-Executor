from collections import namedtuple


class Event:
    def __init__(self, name, **kwargs):
        self.name = name
        self.timestamp = kwargs.pop('timestamp', None)
        self.instanceId = kwargs.pop('instanceId', None)
        self.referenceDate = kwargs.pop('referenceDate', None)
        self.processId = kwargs.pop('processId', None)
        self.operationId = kwargs.pop('operationId', None)
        self.tag = kwargs.pop('tag', None)
        self.version  = kwargs.pop('version', None)
        self.owner = kwargs.pop('owner', 'anonymous')
        self.image = kwargs.pop('image', None)
        self.scope = kwargs.pop('scope', 'execution')
        self.branch = kwargs.pop('branch', 'master')
        self.systemId = kwargs.pop('systemId', None)
        self.idempotencyKey = kwargs.pop('idempotencyKey', None)
        self.reproduction = kwargs.pop('reproduction', dict())
        self.reprocessing = kwargs.pop('reprocessing', dict())
        self.payload = kwargs.pop('payload', dict())

    def __str__(self):
        return (f"Name: {self.name}"
                f"Instance Id: {self.instanceId}"
                f"Payload: {self.payload}")

Process = namedtuple("Process", [
    "id",
    "name",
    "solution",
    "instance",
    "image",
])


Container = namedtuple("Container", [
    "name",
    "tag",
])

