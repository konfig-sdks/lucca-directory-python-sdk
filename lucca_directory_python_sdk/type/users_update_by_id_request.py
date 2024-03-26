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

from lucca_directory_python_sdk.type.users_update_by_id_request_habilited_roles import UsersUpdateByIdRequestHabilitedRoles
from lucca_directory_python_sdk.type.users_update_by_id_request_user_work_cycles import UsersUpdateByIdRequestUserWorkCycles

class RequiredUsersUpdateByIdRequest(TypedDict):
    pass

class OptionalUsersUpdateByIdRequest(TypedDict, total=False):
    firstName: str

    lastName: str

    mail: str

    login: str

    legalEntityId: int

    cspId: int

    calendarId: none_type

    employeeNumber: str

    birthDate: str

    userWorkCycles: UsersUpdateByIdRequestUserWorkCycles

    departmentId: int

    managerId: int

    rolePrincipalId: int

    habilitedRoles: UsersUpdateByIdRequestHabilitedRoles

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

class UsersUpdateByIdRequest(RequiredUsersUpdateByIdRequest, OptionalUsersUpdateByIdRequest):
    pass
