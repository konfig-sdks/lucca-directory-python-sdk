# coding: utf-8

"""
    Directory-v3

    Welcome on the documentation for the Directory v3 API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lucca_directory_python_sdk import schemas  # noqa: F401


class UsersGetByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            name = schemas.StrSchema
            url = schemas.StrSchema
            displayName = schemas.StrSchema
            modifiedOn = schemas.StrSchema
            lastName = schemas.StrSchema
            firstName = schemas.StrSchema
            login = schemas.StrSchema
            mail = schemas.StrSchema
            dtContractStart = schemas.StrSchema
            dtContractEnd = schemas.NoneSchema
            birthDate = schemas.StrSchema
            employeeNumber = schemas.StrSchema
        
            @staticmethod
            def calendar() -> typing.Type['UsersGetByIdResponseCalendar']:
                return UsersGetByIdResponseCalendar
        
            @staticmethod
            def culture() -> typing.Type['UsersGetByIdResponseCulture']:
                return UsersGetByIdResponseCulture
        
            @staticmethod
            def picture() -> typing.Type['UsersGetByIdResponsePicture']:
                return UsersGetByIdResponsePicture
            applicationData = schemas.DictSchema
        
            @staticmethod
            def legalEntity() -> typing.Type['UsersGetByIdResponseLegalEntity']:
                return UsersGetByIdResponseLegalEntity
        
            @staticmethod
            def department() -> typing.Type['UsersGetByIdResponseDepartment']:
                return UsersGetByIdResponseDepartment
        
            @staticmethod
            def manager() -> typing.Type['UsersGetByIdResponseManager']:
                return UsersGetByIdResponseManager
        
            @staticmethod
            def rolePrincipal() -> typing.Type['UsersGetByIdResponseRolePrincipal']:
                return UsersGetByIdResponseRolePrincipal
        
            @staticmethod
            def habilitedRoles() -> typing.Type['UsersGetByIdResponseHabilitedRoles']:
                return UsersGetByIdResponseHabilitedRoles
        
            @staticmethod
            def userWorkCycles() -> typing.Type['UsersGetByIdResponseUserWorkCycles']:
                return UsersGetByIdResponseUserWorkCycles
            __annotations__ = {
                "id": id,
                "name": name,
                "url": url,
                "displayName": displayName,
                "modifiedOn": modifiedOn,
                "lastName": lastName,
                "firstName": firstName,
                "login": login,
                "mail": mail,
                "dtContractStart": dtContractStart,
                "dtContractEnd": dtContractEnd,
                "birthDate": birthDate,
                "employeeNumber": employeeNumber,
                "calendar": calendar,
                "culture": culture,
                "picture": picture,
                "applicationData": applicationData,
                "legalEntity": legalEntity,
                "department": department,
                "manager": manager,
                "rolePrincipal": rolePrincipal,
                "habilitedRoles": habilitedRoles,
                "userWorkCycles": userWorkCycles,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modifiedOn"]) -> MetaOapg.properties.modifiedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mail"]) -> MetaOapg.properties.mail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dtContractStart"]) -> MetaOapg.properties.dtContractStart: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dtContractEnd"]) -> MetaOapg.properties.dtContractEnd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthDate"]) -> MetaOapg.properties.birthDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calendar"]) -> 'UsersGetByIdResponseCalendar': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["culture"]) -> 'UsersGetByIdResponseCulture': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["picture"]) -> 'UsersGetByIdResponsePicture': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationData"]) -> MetaOapg.properties.applicationData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalEntity"]) -> 'UsersGetByIdResponseLegalEntity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> 'UsersGetByIdResponseDepartment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manager"]) -> 'UsersGetByIdResponseManager': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rolePrincipal"]) -> 'UsersGetByIdResponseRolePrincipal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["habilitedRoles"]) -> 'UsersGetByIdResponseHabilitedRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userWorkCycles"]) -> 'UsersGetByIdResponseUserWorkCycles': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "url", "displayName", "modifiedOn", "lastName", "firstName", "login", "mail", "dtContractStart", "dtContractEnd", "birthDate", "employeeNumber", "calendar", "culture", "picture", "applicationData", "legalEntity", "department", "manager", "rolePrincipal", "habilitedRoles", "userWorkCycles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedOn"]) -> typing.Union[MetaOapg.properties.modifiedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> typing.Union[MetaOapg.properties.login, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mail"]) -> typing.Union[MetaOapg.properties.mail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dtContractStart"]) -> typing.Union[MetaOapg.properties.dtContractStart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dtContractEnd"]) -> typing.Union[MetaOapg.properties.dtContractEnd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthDate"]) -> typing.Union[MetaOapg.properties.birthDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calendar"]) -> typing.Union['UsersGetByIdResponseCalendar', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["culture"]) -> typing.Union['UsersGetByIdResponseCulture', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["picture"]) -> typing.Union['UsersGetByIdResponsePicture', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationData"]) -> typing.Union[MetaOapg.properties.applicationData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalEntity"]) -> typing.Union['UsersGetByIdResponseLegalEntity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union['UsersGetByIdResponseDepartment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manager"]) -> typing.Union['UsersGetByIdResponseManager', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rolePrincipal"]) -> typing.Union['UsersGetByIdResponseRolePrincipal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["habilitedRoles"]) -> typing.Union['UsersGetByIdResponseHabilitedRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userWorkCycles"]) -> typing.Union['UsersGetByIdResponseUserWorkCycles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "url", "displayName", "modifiedOn", "lastName", "firstName", "login", "mail", "dtContractStart", "dtContractEnd", "birthDate", "employeeNumber", "calendar", "culture", "picture", "applicationData", "legalEntity", "department", "manager", "rolePrincipal", "habilitedRoles", "userWorkCycles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        modifiedOn: typing.Union[MetaOapg.properties.modifiedOn, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        login: typing.Union[MetaOapg.properties.login, str, schemas.Unset] = schemas.unset,
        mail: typing.Union[MetaOapg.properties.mail, str, schemas.Unset] = schemas.unset,
        dtContractStart: typing.Union[MetaOapg.properties.dtContractStart, str, schemas.Unset] = schemas.unset,
        dtContractEnd: typing.Union[MetaOapg.properties.dtContractEnd, None, schemas.Unset] = schemas.unset,
        birthDate: typing.Union[MetaOapg.properties.birthDate, str, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, str, schemas.Unset] = schemas.unset,
        calendar: typing.Union['UsersGetByIdResponseCalendar', schemas.Unset] = schemas.unset,
        culture: typing.Union['UsersGetByIdResponseCulture', schemas.Unset] = schemas.unset,
        picture: typing.Union['UsersGetByIdResponsePicture', schemas.Unset] = schemas.unset,
        applicationData: typing.Union[MetaOapg.properties.applicationData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        legalEntity: typing.Union['UsersGetByIdResponseLegalEntity', schemas.Unset] = schemas.unset,
        department: typing.Union['UsersGetByIdResponseDepartment', schemas.Unset] = schemas.unset,
        manager: typing.Union['UsersGetByIdResponseManager', schemas.Unset] = schemas.unset,
        rolePrincipal: typing.Union['UsersGetByIdResponseRolePrincipal', schemas.Unset] = schemas.unset,
        habilitedRoles: typing.Union['UsersGetByIdResponseHabilitedRoles', schemas.Unset] = schemas.unset,
        userWorkCycles: typing.Union['UsersGetByIdResponseUserWorkCycles', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersGetByIdResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            url=url,
            displayName=displayName,
            modifiedOn=modifiedOn,
            lastName=lastName,
            firstName=firstName,
            login=login,
            mail=mail,
            dtContractStart=dtContractStart,
            dtContractEnd=dtContractEnd,
            birthDate=birthDate,
            employeeNumber=employeeNumber,
            calendar=calendar,
            culture=culture,
            picture=picture,
            applicationData=applicationData,
            legalEntity=legalEntity,
            department=department,
            manager=manager,
            rolePrincipal=rolePrincipal,
            habilitedRoles=habilitedRoles,
            userWorkCycles=userWorkCycles,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_directory_python_sdk.model.users_get_by_id_response_calendar import UsersGetByIdResponseCalendar
from lucca_directory_python_sdk.model.users_get_by_id_response_culture import UsersGetByIdResponseCulture
from lucca_directory_python_sdk.model.users_get_by_id_response_department import UsersGetByIdResponseDepartment
from lucca_directory_python_sdk.model.users_get_by_id_response_habilited_roles import UsersGetByIdResponseHabilitedRoles
from lucca_directory_python_sdk.model.users_get_by_id_response_legal_entity import UsersGetByIdResponseLegalEntity
from lucca_directory_python_sdk.model.users_get_by_id_response_manager import UsersGetByIdResponseManager
from lucca_directory_python_sdk.model.users_get_by_id_response_picture import UsersGetByIdResponsePicture
from lucca_directory_python_sdk.model.users_get_by_id_response_role_principal import UsersGetByIdResponseRolePrincipal
from lucca_directory_python_sdk.model.users_get_by_id_response_user_work_cycles import UsersGetByIdResponseUserWorkCycles