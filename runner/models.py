from uuid import uuid4
import json
from collections import namedtuple


class Event:
    """Event model
    """
    def __init__(self, name, pars):
        self.id = uuid4()
        self.name = name
        self.pars = pars

    @classmethod
    def from_json(cls, data):
        """Returns a new event instance from json data.
        """
        _data = json.loads(data)
        return cls(**_data)


    def to_json(self):
        """Returns a dictonary containing serializable properties
           from an instance.
        """
        return {
            "id": str(self.id)
        }



