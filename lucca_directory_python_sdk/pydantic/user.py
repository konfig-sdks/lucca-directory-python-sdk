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

from lucca_directory_python_sdk.pydantic.user_application_data import UserApplicationData
from lucca_directory_python_sdk.pydantic.user_calendar import UserCalendar
from lucca_directory_python_sdk.pydantic.user_culture import UserCulture
from lucca_directory_python_sdk.pydantic.user_department import UserDepartment
from lucca_directory_python_sdk.pydantic.user_habilited_roles import UserHabilitedRoles
from lucca_directory_python_sdk.pydantic.user_legal_entity import UserLegalEntity
from lucca_directory_python_sdk.pydantic.user_manager import UserManager
from lucca_directory_python_sdk.pydantic.user_picture import UserPicture
from lucca_directory_python_sdk.pydantic.user_role_principal import UserRolePrincipal
from lucca_directory_python_sdk.pydantic.user_user_work_cycles import UserUserWorkCycles

class User(BaseModel):
    id: typing.Union[int, float] = Field(alias='id')

    name: str = Field(alias='name')

    url: str = Field(alias='url')

    display_name: str = Field(alias='displayName')

    modified_on: str = Field(alias='modifiedOn')

    last_name: str = Field(alias='lastName')

    first_name: str = Field(alias='firstName')

    login: str = Field(alias='login')

    mail: str = Field(alias='mail')

    dt_contract_start: str = Field(alias='dtContractStart')

    birth_date: str = Field(alias='birthDate')

    employee_number: str = Field(alias='employeeNumber')

    calendar: UserCalendar = Field(alias='calendar')

    culture: UserCulture = Field(alias='culture')

    picture: UserPicture = Field(alias='picture')

    application_data: UserApplicationData = Field(alias='applicationData')

    legal_entity: UserLegalEntity = Field(alias='legalEntity')

    department: UserDepartment = Field(alias='department')

    manager: UserManager = Field(alias='manager')

    role_principal: UserRolePrincipal = Field(alias='rolePrincipal')

    habilited_roles: UserHabilitedRoles = Field(alias='habilitedRoles')

    user_work_cycles: UserUserWorkCycles = Field(alias='userWorkCycles')

    dt_contract_end: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='dtContractEnd')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
