import mock
import unittest
from sdk.utils import HttpClient, VERBS
import requests
import json

class HttpClientTestCase(unittest.TestCase):

    def test_get_method_invokes_requests(self):
        # mock
        VERBS.GET = mock.MagicMock()
        uri = 'http://app.uri.com'

        # act
        HttpClient.get(uri)

        # assert
        VERBS.GET.assert_called_with(uri)

