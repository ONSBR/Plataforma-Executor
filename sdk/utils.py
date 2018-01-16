import requests


def log(*args):
    print(*args)


class VERBS:
    """HTTP Verbs
    """
    GET = requests.get
    POST = requests.post


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
        log('HTTP request error', f'status code: {status_code}', f'message: {message}')
        return cls(status_code=status_code, has_error=True,
                   error_message=message, data=data)


class HttpClient:
    """Simple client to interact with HTTP endpoints.
    """
    @staticmethod
    def _request(uri, verb, **kwargs):
        try:
            r = verb(uri, **kwargs)
            r.raise_for_status()
        except requests.exceptions.ConnectionError:
            return ExecutionResult.error(
                status_code=0,
                message=f'Could not connect to host: {uri}',)
        except Exception:
            return ExecutionResult.error(
                status_code=r.status_code,
                message=f"Request failed",
                data=r.json())

        data = None

        if r.text:
            data = r.json()

        return ExecutionResult.ok(
            status_code=r.status_code,
            data=data)

    @classmethod
    def get(cls, uri):
        return cls._request(uri=uri, verb=VERBS.GET)

    @classmethod
    def post(cls, uri, data=None):
        args = {}

        if data:
            args['json'] = data

        return cls._request(uri=uri, verb=VERBS.POST, **args)


