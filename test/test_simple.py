# coding: utf-8

"""
    Directory-v3

    Welcome on the documentation for the Directory v3 API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import unittest

import os
from pprint import pprint
from lucca_directory_python_sdk import LuccaDirectory

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        luccadirectory = LuccaDirectory(
        
                        authorization = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(luccadirectory)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
