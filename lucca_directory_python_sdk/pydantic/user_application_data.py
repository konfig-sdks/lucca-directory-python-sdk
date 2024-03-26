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

from lucca_directory_python_sdk.pydantic.user_application_data_profile_figgo import UserApplicationDataProfileFiggo
from lucca_directory_python_sdk.pydantic.user_application_data_profile_utime import UserApplicationDataProfileUtime

class UserApplicationData(BaseModel):
    profile_figgo: UserApplicationDataProfileFiggo = Field(alias='profile_figgo')

    profile_utime: UserApplicationDataProfileUtime = Field(alias='profile_utime')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
