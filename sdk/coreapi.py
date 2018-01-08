from collections import namedtuple


# models
Process = namedtuple("Process", [
    "name",
    "container",
])


Container = namedtuple("Container", [
    "name",
    "tag",
])


def get_processes_by_event(event):
    """ Retrieves a list of processes containing
        operations subscribed to an event.
    """

    # TODO: retrieve from core api.

    return [
        Container(
            name="Dummy Process",
            tag="1.0",
            operation="Dummy Operation"
        )
    ]
