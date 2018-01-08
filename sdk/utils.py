import requests


class VERBS:
    GET = requests.get


class HttpClient:
    """Simple client to interact with HTTP endpoints.
    """
    @staticmethod
    def _request(uri, verb):
        r = verb(uri)
        return r.status_code, r.json()

    @classmethod
    def get(cls, uri):
        return cls._request(uri=uri, verb=VERBS.GET)
