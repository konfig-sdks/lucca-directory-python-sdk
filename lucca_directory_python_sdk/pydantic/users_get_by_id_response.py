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

from lucca_directory_python_sdk.pydantic.users_get_by_id_response_calendar import UsersGetByIdResponseCalendar
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_culture import UsersGetByIdResponseCulture
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_department import UsersGetByIdResponseDepartment
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_habilited_roles import UsersGetByIdResponseHabilitedRoles
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_legal_entity import UsersGetByIdResponseLegalEntity
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_manager import UsersGetByIdResponseManager
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_picture import UsersGetByIdResponsePicture
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_role_principal import UsersGetByIdResponseRolePrincipal
from lucca_directory_python_sdk.pydantic.users_get_by_id_response_user_work_cycles import UsersGetByIdResponseUserWorkCycles

class UsersGetByIdResponse(BaseModel):
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

    calendar: typing.Optional[UsersGetByIdResponseCalendar] = Field(None, alias='calendar')

    culture: typing.Optional[UsersGetByIdResponseCulture] = Field(None, alias='culture')

    picture: typing.Optional[UsersGetByIdResponsePicture] = Field(None, alias='picture')

    application_data: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='applicationData')

    legal_entity: typing.Optional[UsersGetByIdResponseLegalEntity] = Field(None, alias='legalEntity')

    department: typing.Optional[UsersGetByIdResponseDepartment] = Field(None, alias='department')

    manager: typing.Optional[UsersGetByIdResponseManager] = Field(None, alias='manager')

    role_principal: typing.Optional[UsersGetByIdResponseRolePrincipal] = Field(None, alias='rolePrincipal')

    habilited_roles: typing.Optional[UsersGetByIdResponseHabilitedRoles] = Field(None, alias='habilitedRoles')

    user_work_cycles: typing.Optional[UsersGetByIdResponseUserWorkCycles] = Field(None, alias='userWorkCycles')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
