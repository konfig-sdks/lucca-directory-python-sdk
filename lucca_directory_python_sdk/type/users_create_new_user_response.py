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

from lucca_directory_python_sdk.type.users_create_new_user_response_habilited_roles import UsersCreateNewUserResponseHabilitedRoles
from lucca_directory_python_sdk.type.users_create_new_user_response_user_work_cycles import UsersCreateNewUserResponseUserWorkCycles

class RequiredUsersCreateNewUserResponse(TypedDict):
    firstName: str

    lastName: str

    mail: str

    login: str

    legalEntityId: int

    dtContractStart: str

    departmentId: int

    rolePrincipalId: int

class OptionalUsersCreateNewUserResponse(TypedDict, total=False):
    dtContractEnd: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    cspId: int

    calendarId: none_type

    employeeNumber: str

    birthDate: str

    userWorkCycles: UsersCreateNewUserResponseUserWorkCycles

    managerId: int

    habilitedRoles: UsersCreateNewUserResponseHabilitedRoles

    cultureId: int

    address: str

    bankName: str

    directLine: str

    jobTitle: str

    gender: str

    nationality: str

    personalEmail: str

    personalMobile: str

    professionalMobile: str

    quote: str

class UsersCreateNewUserResponse(RequiredUsersCreateNewUserResponse, OptionalUsersCreateNewUserResponse):
    pass
