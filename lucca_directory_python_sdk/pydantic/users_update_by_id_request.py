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

from lucca_directory_python_sdk.pydantic.users_update_by_id_request_habilited_roles import UsersUpdateByIdRequestHabilitedRoles
from lucca_directory_python_sdk.pydantic.users_update_by_id_request_user_work_cycles import UsersUpdateByIdRequestUserWorkCycles

class UsersUpdateByIdRequest(BaseModel):
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    mail: typing.Optional[str] = Field(None, alias='mail')

    login: typing.Optional[str] = Field(None, alias='login')

    legal_entity_id: typing.Optional[int] = Field(None, alias='legalEntityId')

    csp_id: typing.Optional[int] = Field(None, alias='cspId')

    calendar_id: typing.Optional[none_type] = Field(None, alias='calendarId')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    birth_date: typing.Optional[str] = Field(None, alias='birthDate')

    user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = Field(None, alias='userWorkCycles')

    department_id: typing.Optional[int] = Field(None, alias='departmentId')

    manager_id: typing.Optional[int] = Field(None, alias='managerId')

    role_principal_id: typing.Optional[int] = Field(None, alias='rolePrincipalId')

    habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = Field(None, alias='habilitedRoles')

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
