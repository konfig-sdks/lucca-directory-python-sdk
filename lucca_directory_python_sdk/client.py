# coding: utf-8
"""
    Directory-v3

    Welcome on the documentation for the Directory v3 API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

import typing
import inspect
from datetime import date, datetime
from lucca_directory_python_sdk.client_custom import ClientCustom
from lucca_directory_python_sdk.configuration import Configuration
from lucca_directory_python_sdk.api_client import ApiClient
from lucca_directory_python_sdk.type_util import copy_signature
from lucca_directory_python_sdk.apis.tags.users_api import UsersApi



class LuccaDirectory(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.users: UsersApi = UsersApi(api_client)
