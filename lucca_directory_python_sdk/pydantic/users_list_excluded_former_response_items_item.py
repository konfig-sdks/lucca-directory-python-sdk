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

from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_calendar import UsersListExcludedFormerResponseItemsItemCalendar
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_culture import UsersListExcludedFormerResponseItemsItemCulture
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_department import UsersListExcludedFormerResponseItemsItemDepartment
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_habilited_roles import UsersListExcludedFormerResponseItemsItemHabilitedRoles
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_legal_entity import UsersListExcludedFormerResponseItemsItemLegalEntity
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_manager import UsersListExcludedFormerResponseItemsItemManager
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_picture import UsersListExcludedFormerResponseItemsItemPicture
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_role_principal import UsersListExcludedFormerResponseItemsItemRolePrincipal
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response_items_item_user_work_cycles import UsersListExcludedFormerResponseItemsItemUserWorkCycles

class UsersListExcludedFormerResponseItemsItem(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    url: typing.Optional[str] = Field(None, alias='url')

    display_name: typing.Optional[str] = Field(None, alias='displayName')

    modified_on: typing.Optional[str] = Field(None, alias='modifiedOn')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    login: typing.Optional[str] = Field(None, alias='login')

    mail: typing.Optional[str] = Field(None, alias='mail')

    dt_contract_start: typing.Optional[str] = Field(None, alias='dtContractStart')

    dt_contract_end: typing.Optional[none_type] = Field(None, alias='dtContractEnd')

    birth_date: typing.Optional[str] = Field(None, alias='birthDate')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    calendar: typing.Optional[UsersListExcludedFormerResponseItemsItemCalendar] = Field(None, alias='calendar')

    culture: typing.Optional[UsersListExcludedFormerResponseItemsItemCulture] = Field(None, alias='culture')

    picture: typing.Optional[UsersListExcludedFormerResponseItemsItemPicture] = Field(None, alias='picture')

    application_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='applicationData')

    legal_entity: typing.Optional[UsersListExcludedFormerResponseItemsItemLegalEntity] = Field(None, alias='legalEntity')

    department: typing.Optional[UsersListExcludedFormerResponseItemsItemDepartment] = Field(None, alias='department')

    manager: typing.Optional[UsersListExcludedFormerResponseItemsItemManager] = Field(None, alias='manager')

    role_principal: typing.Optional[UsersListExcludedFormerResponseItemsItemRolePrincipal] = Field(None, alias='rolePrincipal')

    habilited_roles: typing.Optional[UsersListExcludedFormerResponseItemsItemHabilitedRoles] = Field(None, alias='habilitedRoles')

    user_work_cycles: typing.Optional[UsersListExcludedFormerResponseItemsItemUserWorkCycles] = Field(None, alias='userWorkCycles')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
