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

from lucca_directory_python_sdk.type.users_get_by_id_response_calendar import UsersGetByIdResponseCalendar
from lucca_directory_python_sdk.type.users_get_by_id_response_culture import UsersGetByIdResponseCulture
from lucca_directory_python_sdk.type.users_get_by_id_response_department import UsersGetByIdResponseDepartment
from lucca_directory_python_sdk.type.users_get_by_id_response_habilited_roles import UsersGetByIdResponseHabilitedRoles
from lucca_directory_python_sdk.type.users_get_by_id_response_legal_entity import UsersGetByIdResponseLegalEntity
from lucca_directory_python_sdk.type.users_get_by_id_response_manager import UsersGetByIdResponseManager
from lucca_directory_python_sdk.type.users_get_by_id_response_picture import UsersGetByIdResponsePicture
from lucca_directory_python_sdk.type.users_get_by_id_response_role_principal import UsersGetByIdResponseRolePrincipal
from lucca_directory_python_sdk.type.users_get_by_id_response_user_work_cycles import UsersGetByIdResponseUserWorkCycles

class RequiredUsersGetByIdResponse(TypedDict):
    pass

class OptionalUsersGetByIdResponse(TypedDict, total=False):
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

    calendar: UsersGetByIdResponseCalendar

    culture: UsersGetByIdResponseCulture

    picture: UsersGetByIdResponsePicture

    applicationData: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    legalEntity: UsersGetByIdResponseLegalEntity

    department: UsersGetByIdResponseDepartment

    manager: UsersGetByIdResponseManager

    rolePrincipal: UsersGetByIdResponseRolePrincipal

    habilitedRoles: UsersGetByIdResponseHabilitedRoles

    userWorkCycles: UsersGetByIdResponseUserWorkCycles

class UsersGetByIdResponse(RequiredUsersGetByIdResponse, OptionalUsersGetByIdResponse):
    pass
