from collections import namedtuple


Event = namedtuple("Event", [
    "name",
    "instance",
    "payload",
])


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

