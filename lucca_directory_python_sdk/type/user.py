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

from lucca_directory_python_sdk.type.user_application_data import UserApplicationData
from lucca_directory_python_sdk.type.user_calendar import UserCalendar
from lucca_directory_python_sdk.type.user_culture import UserCulture
from lucca_directory_python_sdk.type.user_department import UserDepartment
from lucca_directory_python_sdk.type.user_habilited_roles import UserHabilitedRoles
from lucca_directory_python_sdk.type.user_legal_entity import UserLegalEntity
from lucca_directory_python_sdk.type.user_manager import UserManager
from lucca_directory_python_sdk.type.user_picture import UserPicture
from lucca_directory_python_sdk.type.user_role_principal import UserRolePrincipal
from lucca_directory_python_sdk.type.user_user_work_cycles import UserUserWorkCycles

class RequiredUser(TypedDict):
    id: typing.Union[int, float]

    name: str

    url: str

    displayName: str

    modifiedOn: str

    lastName: str

    firstName: str

    login: str

    mail: str

    dtContractStart: str

    birthDate: str

    employeeNumber: str

    calendar: UserCalendar

    culture: UserCulture

    picture: UserPicture

    applicationData: UserApplicationData

    legalEntity: UserLegalEntity

    department: UserDepartment

    manager: UserManager

    rolePrincipal: UserRolePrincipal

    habilitedRoles: UserHabilitedRoles

    userWorkCycles: UserUserWorkCycles

class OptionalUser(TypedDict, total=False):
    dtContractEnd: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class User(RequiredUser, OptionalUser):
    pass
