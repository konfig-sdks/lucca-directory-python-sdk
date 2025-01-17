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


class User(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "calendar",
            "dtContractStart",
            "lastName",
            "mail",
            "manager",
            "displayName",
            "login",
            "birthDate",
            "picture",
            "url",
            "employeeNumber",
            "legalEntity",
            "firstName",
            "habilitedRoles",
            "modifiedOn",
            "culture",
            "name",
            "applicationData",
            "id",
            "department",
            "userWorkCycles",
            "rolePrincipal",
        }
        
        class properties:
            id = schemas.NumberSchema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class url(
                schemas.StrSchema
            ):
                pass
            
            
            class displayName(
                schemas.StrSchema
            ):
                pass
            
            
            class modifiedOn(
                schemas.StrSchema
            ):
                pass
            
            
            class lastName(
                schemas.StrSchema
            ):
                pass
            
            
            class firstName(
                schemas.StrSchema
            ):
                pass
            
            
            class login(
                schemas.StrSchema
            ):
                pass
            
            
            class mail(
                schemas.StrSchema
            ):
                pass
            
            
            class dtContractStart(
                schemas.StrSchema
            ):
                pass
            
            
            class birthDate(
                schemas.StrSchema
            ):
                pass
            
            
            class employeeNumber(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def calendar() -> typing.Type['UserCalendar']:
                return UserCalendar
        
            @staticmethod
            def culture() -> typing.Type['UserCulture']:
                return UserCulture
        
            @staticmethod
            def picture() -> typing.Type['UserPicture']:
                return UserPicture
        
            @staticmethod
            def applicationData() -> typing.Type['UserApplicationData']:
                return UserApplicationData
        
            @staticmethod
            def legalEntity() -> typing.Type['UserLegalEntity']:
                return UserLegalEntity
        
            @staticmethod
            def department() -> typing.Type['UserDepartment']:
                return UserDepartment
        
            @staticmethod
            def manager() -> typing.Type['UserManager']:
                return UserManager
        
            @staticmethod
            def rolePrincipal() -> typing.Type['UserRolePrincipal']:
                return UserRolePrincipal
        
            @staticmethod
            def habilitedRoles() -> typing.Type['UserHabilitedRoles']:
                return UserHabilitedRoles
        
            @staticmethod
            def userWorkCycles() -> typing.Type['UserUserWorkCycles']:
                return UserUserWorkCycles
            dtContractEnd = schemas.AnyTypeSchema
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
                "dtContractEnd": dtContractEnd,
            }
    
    calendar: 'UserCalendar'
    dtContractStart: MetaOapg.properties.dtContractStart
    lastName: MetaOapg.properties.lastName
    mail: MetaOapg.properties.mail
    manager: 'UserManager'
    displayName: MetaOapg.properties.displayName
    login: MetaOapg.properties.login
    birthDate: MetaOapg.properties.birthDate
    picture: 'UserPicture'
    url: MetaOapg.properties.url
    employeeNumber: MetaOapg.properties.employeeNumber
    legalEntity: 'UserLegalEntity'
    firstName: MetaOapg.properties.firstName
    habilitedRoles: 'UserHabilitedRoles'
    modifiedOn: MetaOapg.properties.modifiedOn
    culture: 'UserCulture'
    name: MetaOapg.properties.name
    applicationData: 'UserApplicationData'
    id: MetaOapg.properties.id
    department: 'UserDepartment'
    userWorkCycles: 'UserUserWorkCycles'
    rolePrincipal: 'UserRolePrincipal'
    
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
    def __getitem__(self, name: typing_extensions.Literal["birthDate"]) -> MetaOapg.properties.birthDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calendar"]) -> 'UserCalendar': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["culture"]) -> 'UserCulture': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["picture"]) -> 'UserPicture': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationData"]) -> 'UserApplicationData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalEntity"]) -> 'UserLegalEntity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> 'UserDepartment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manager"]) -> 'UserManager': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rolePrincipal"]) -> 'UserRolePrincipal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["habilitedRoles"]) -> 'UserHabilitedRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userWorkCycles"]) -> 'UserUserWorkCycles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dtContractEnd"]) -> MetaOapg.properties.dtContractEnd: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "url", "displayName", "modifiedOn", "lastName", "firstName", "login", "mail", "dtContractStart", "birthDate", "employeeNumber", "calendar", "culture", "picture", "applicationData", "legalEntity", "department", "manager", "rolePrincipal", "habilitedRoles", "userWorkCycles", "dtContractEnd", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modifiedOn"]) -> MetaOapg.properties.modifiedOn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mail"]) -> MetaOapg.properties.mail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dtContractStart"]) -> MetaOapg.properties.dtContractStart: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthDate"]) -> MetaOapg.properties.birthDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calendar"]) -> 'UserCalendar': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["culture"]) -> 'UserCulture': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["picture"]) -> 'UserPicture': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationData"]) -> 'UserApplicationData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalEntity"]) -> 'UserLegalEntity': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> 'UserDepartment': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manager"]) -> 'UserManager': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rolePrincipal"]) -> 'UserRolePrincipal': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["habilitedRoles"]) -> 'UserHabilitedRoles': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userWorkCycles"]) -> 'UserUserWorkCycles': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dtContractEnd"]) -> typing.Union[MetaOapg.properties.dtContractEnd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "url", "displayName", "modifiedOn", "lastName", "firstName", "login", "mail", "dtContractStart", "birthDate", "employeeNumber", "calendar", "culture", "picture", "applicationData", "legalEntity", "department", "manager", "rolePrincipal", "habilitedRoles", "userWorkCycles", "dtContractEnd", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        calendar: 'UserCalendar',
        dtContractStart: typing.Union[MetaOapg.properties.dtContractStart, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        mail: typing.Union[MetaOapg.properties.mail, str, ],
        manager: 'UserManager',
        displayName: typing.Union[MetaOapg.properties.displayName, str, ],
        login: typing.Union[MetaOapg.properties.login, str, ],
        birthDate: typing.Union[MetaOapg.properties.birthDate, str, ],
        picture: 'UserPicture',
        url: typing.Union[MetaOapg.properties.url, str, ],
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, str, ],
        legalEntity: 'UserLegalEntity',
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        habilitedRoles: 'UserHabilitedRoles',
        modifiedOn: typing.Union[MetaOapg.properties.modifiedOn, str, ],
        culture: 'UserCulture',
        name: typing.Union[MetaOapg.properties.name, str, ],
        applicationData: 'UserApplicationData',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, ],
        department: 'UserDepartment',
        userWorkCycles: 'UserUserWorkCycles',
        rolePrincipal: 'UserRolePrincipal',
        dtContractEnd: typing.Union[MetaOapg.properties.dtContractEnd, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *args,
            calendar=calendar,
            dtContractStart=dtContractStart,
            lastName=lastName,
            mail=mail,
            manager=manager,
            displayName=displayName,
            login=login,
            birthDate=birthDate,
            picture=picture,
            url=url,
            employeeNumber=employeeNumber,
            legalEntity=legalEntity,
            firstName=firstName,
            habilitedRoles=habilitedRoles,
            modifiedOn=modifiedOn,
            culture=culture,
            name=name,
            applicationData=applicationData,
            id=id,
            department=department,
            userWorkCycles=userWorkCycles,
            rolePrincipal=rolePrincipal,
            dtContractEnd=dtContractEnd,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_directory_python_sdk.model.user_application_data import UserApplicationData
from lucca_directory_python_sdk.model.user_calendar import UserCalendar
from lucca_directory_python_sdk.model.user_culture import UserCulture
from lucca_directory_python_sdk.model.user_department import UserDepartment
from lucca_directory_python_sdk.model.user_habilited_roles import UserHabilitedRoles
from lucca_directory_python_sdk.model.user_legal_entity import UserLegalEntity
from lucca_directory_python_sdk.model.user_manager import UserManager
from lucca_directory_python_sdk.model.user_picture import UserPicture
from lucca_directory_python_sdk.model.user_role_principal import UserRolePrincipal
from lucca_directory_python_sdk.model.user_user_work_cycles import UserUserWorkCycles
