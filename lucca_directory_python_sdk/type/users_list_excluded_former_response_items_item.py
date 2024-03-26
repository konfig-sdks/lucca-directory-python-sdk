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

from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_calendar import UsersListExcludedFormerResponseItemsItemCalendar
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_culture import UsersListExcludedFormerResponseItemsItemCulture
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_department import UsersListExcludedFormerResponseItemsItemDepartment
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_habilited_roles import UsersListExcludedFormerResponseItemsItemHabilitedRoles
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_legal_entity import UsersListExcludedFormerResponseItemsItemLegalEntity
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_manager import UsersListExcludedFormerResponseItemsItemManager
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_picture import UsersListExcludedFormerResponseItemsItemPicture
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_role_principal import UsersListExcludedFormerResponseItemsItemRolePrincipal
from lucca_directory_python_sdk.type.users_list_excluded_former_response_items_item_user_work_cycles import UsersListExcludedFormerResponseItemsItemUserWorkCycles

class RequiredUsersListExcludedFormerResponseItemsItem(TypedDict):
    pass

class OptionalUsersListExcludedFormerResponseItemsItem(TypedDict, total=False):
    id: int

    name: str

    url: str

    displayName: str

    modifiedOn: str

    lastName: str

    firstName: str

    login: str

    mail: str

    dtContractStart: str

    dtContractEnd: none_type

    birthDate: str

    employeeNumber: str

    calendar: UsersListExcludedFormerResponseItemsItemCalendar

    culture: UsersListExcludedFormerResponseItemsItemCulture

    picture: UsersListExcludedFormerResponseItemsItemPicture

    applicationData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    legalEntity: UsersListExcludedFormerResponseItemsItemLegalEntity

    department: UsersListExcludedFormerResponseItemsItemDepartment

    manager: UsersListExcludedFormerResponseItemsItemManager

    rolePrincipal: UsersListExcludedFormerResponseItemsItemRolePrincipal

    habilitedRoles: UsersListExcludedFormerResponseItemsItemHabilitedRoles

    userWorkCycles: UsersListExcludedFormerResponseItemsItemUserWorkCycles

class UsersListExcludedFormerResponseItemsItem(RequiredUsersListExcludedFormerResponseItemsItem, OptionalUsersListExcludedFormerResponseItemsItem):
    pass
