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

from lucca_directory_python_sdk.type.user_application_data_profile_figgo import UserApplicationDataProfileFiggo
from lucca_directory_python_sdk.type.user_application_data_profile_utime import UserApplicationDataProfileUtime

class RequiredUserApplicationData(TypedDict):
    profile_figgo: UserApplicationDataProfileFiggo

    profile_utime: UserApplicationDataProfileUtime

class OptionalUserApplicationData(TypedDict, total=False):
    pass

class UserApplicationData(RequiredUserApplicationData, OptionalUserApplicationData):
    pass
