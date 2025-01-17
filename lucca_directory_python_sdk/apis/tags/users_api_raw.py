# coding: utf-8

"""
    Directory-v3

    Welcome on the documentation for the Directory v3 API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from lucca_directory_python_sdk.paths.api_v3_users.post import CreateNewUserRaw
from lucca_directory_python_sdk.paths.api_v3_users_user_id.get import GetByIdRaw
from lucca_directory_python_sdk.paths.api_v3_users.get import ListExcludedFormerRaw
from lucca_directory_python_sdk.paths.api_v3_users_user_id.put import UpdateByIdRaw


class UsersApiRaw(
    CreateNewUserRaw,
    GetByIdRaw,
    ListExcludedFormerRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
