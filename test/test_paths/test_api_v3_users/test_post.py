# coding: utf-8

"""
    Directory-v3

    Welcome on the documentation for the Directory v3 API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest
from unittest.mock import patch

import urllib3

import lucca_directory_python_sdk
from lucca_directory_python_sdk.paths.api_v3_users import post
from lucca_directory_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV3Users(ApiTestMixin, unittest.TestCase):
    """
    ApiV3Users unit test stubs
        Create a new User
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
