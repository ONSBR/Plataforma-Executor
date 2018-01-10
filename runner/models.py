import json
from uuid import uuid4
from collections import namedtuple


class Model:
    def __init__(self):
        self.id = uuid4()

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


class Event(Model):
    """Event model
    """
    def __init__(self, name, pars):
        super().__init__()
        self.name = name
        self.pars = pars



