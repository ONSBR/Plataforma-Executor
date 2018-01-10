from collections import namedtuple


Event = namedtuple("Event", [
    "name",
    "instance",
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

