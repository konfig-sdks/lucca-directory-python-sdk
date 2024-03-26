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


class RequiredUserPicture(TypedDict):
    id: str

    url: str

    name: str

class OptionalUserPicture(TypedDict, total=False):
    pass

class UserPicture(RequiredUserPicture, OptionalUserPicture):
    pass
