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

from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_user_work_cycles_item import UsersListExcludedFormerResponseItemsItemUserWorkCyclesItem

UsersListExcludedFormerResponseItemsItemUserWorkCycles = typing.List[UsersListExcludedFormerResponseItemsItemUserWorkCyclesItem]
