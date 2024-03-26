# coding: utf-8

"""
    Directory-v3

    Welcome on the documentation for the Directory v3 API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from lucca_directory_python_sdk.pydantic.users_get_by_id_response_habilited_roles_item import UsersGetByIdResponseHabilitedRolesItem

UsersGetByIdResponseHabilitedRoles = typing.List[UsersGetByIdResponseHabilitedRolesItem]
