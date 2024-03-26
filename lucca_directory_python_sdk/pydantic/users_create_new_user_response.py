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

from lucca_directory_python_sdk.pydantic.users_create_new_user_response_habilited_roles import UsersCreateNewUserResponseHabilitedRoles
from lucca_directory_python_sdk.pydantic.users_create_new_user_response_user_work_cycles import UsersCreateNewUserResponseUserWorkCycles

class UsersCreateNewUserResponse(BaseModel):
    first_name: str = Field(alias='firstName')

    last_name: str = Field(alias='lastName')

    mail: str = Field(alias='mail')

    login: str = Field(alias='login')

    legal_entity_id: int = Field(alias='legalEntityId')

    dt_contract_start: str = Field(alias='dtContractStart')

    department_id: int = Field(alias='departmentId')

    role_principal_id: int = Field(alias='rolePrincipalId')

    dt_contract_end: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='dtContractEnd')

    csp_id: typing.Optional[int] = Field(None, alias='cspId')

    calendar_id: typing.Optional[none_type] = Field(None, alias='calendarId')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    birth_date: typing.Optional[str] = Field(None, alias='birthDate')

    user_work_cycles: typing.Optional[UsersCreateNewUserResponseUserWorkCycles] = Field(None, alias='userWorkCycles')

    manager_id: typing.Optional[int] = Field(None, alias='managerId')

    habilited_roles: typing.Optional[UsersCreateNewUserResponseHabilitedRoles] = Field(None, alias='habilitedRoles')

    culture_id: typing.Optional[int] = Field(None, alias='cultureId')

    address: typing.Optional[str] = Field(None, alias='address')

    bank_name: typing.Optional[str] = Field(None, alias='bankName')

    direct_line: typing.Optional[str] = Field(None, alias='directLine')

    job_title: typing.Optional[str] = Field(None, alias='jobTitle')

    gender: typing.Optional[str] = Field(None, alias='gender')

    nationality: typing.Optional[str] = Field(None, alias='nationality')

    personal_email: typing.Optional[str] = Field(None, alias='personalEmail')

    personal_mobile: typing.Optional[str] = Field(None, alias='personalMobile')

    professional_mobile: typing.Optional[str] = Field(None, alias='professionalMobile')

    quote: typing.Optional[str] = Field(None, alias='quote')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
