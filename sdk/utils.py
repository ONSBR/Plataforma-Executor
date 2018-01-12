import requests


class VERBS:
    """HTTP Verbs
    """
    GET = requests.get


class ExecutionResult:
    """HTTP requests friendly result.
    """
    def __init__(self, status_code, has_error=False,
                 error_message=None, data=None):
        self.status_code = status_code
        self.has_error = has_error
        self.error_message = error_message
        self.data = data

    @classmethod
    def ok(cls, status_code=200, data=None):
        return cls(status_code=status_code, data=data)

    @classmethod
    def error(cls, status_code, message, data=None):
        return cls(status_code=status_code, has_error=True,
                   error_message=message, data=data)


class HttpClient:
    """Simple client to interact with HTTP endpoints.
    """
    @staticmethod
    def _request(uri, verb):
        r = verb(uri)

        try:
            r.raise_for_status()
        except Exception as ex:
            return ExecutionResult.error(
                status_code=r.status_code,
                message="Request failed",
                data=r.json(),
            )

        return ExecutionResult.ok(status_code=r.status_code, data=r.json())

    @classmethod
    def get(cls, uri):
        return cls._request(uri=uri, verb=VERBS.GET)
