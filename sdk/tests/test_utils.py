import mock
import unittest
from sdk.utils import HttpClient, VERBS, ExecutionResult
import requests
import json


class HttpClientTestCase(unittest.TestCase):
    def test_get_method_invokes_requests(self):
        # mock
        VERBS.GET = mock.MagicMock()
        uri = 'http://app.uri.com'

        # act
        result = HttpClient.get(uri)

        # assert
        VERBS.GET.assert_called_with(uri)


class ExecutionResultTestCase(unittest.TestCase):
    def test_create_success_result(self):
        execution_result = ExecutionResult.ok(status_code=200)

        assert execution_result.has_error == False
        assert execution_result.error_message is None
        assert execution_result.status_code == 200

    def test_create_error_result(self):
        execution_result = ExecutionResult.error(status_code=404, message='error')

        assert execution_result.has_error == True
        assert execution_result.error_message == 'error'
        assert execution_result.status_code == 404

