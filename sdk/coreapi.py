from sdk.models import Process, Container


def get_processes_by_event(event):
    """ Retrieves a list of processes containing
        operations subscribed to an event.
    """

    # TODO: retrieve from core api.

    return [
        Process(
            name="Dummy Process",
            instance=None,
            systemid="saat",
            container=Container(
                name="Dummy Process",
                tag="1.0",
                operation="Dummy Operation"
            )
        )
    ]
