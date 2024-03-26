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


class UsersListExcludedFormerResponseItemsItemUserWorkCyclesItem(BaseModel):
    id: typing.Optional[int] = Field(None, alias='Id')

    owner_i_d: typing.Optional[int] = Field(None, alias='OwnerID')

    work_cycle_i_d: typing.Optional[int] = Field(None, alias='WorkCycleID')

    starts_on: typing.Optional[str] = Field(None, alias='StartsOn')

    ends_on: typing.Optional[str] = Field(None, alias='EndsOn')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
