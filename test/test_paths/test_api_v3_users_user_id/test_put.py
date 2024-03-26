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
from lucca_directory_python_sdk.paths.api_v3_users_user_id import put
from lucca_directory_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV3UsersUserId(ApiTestMixin, unittest.TestCase):
    """
    ApiV3UsersUserId unit test stubs
        Update a User by id
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
