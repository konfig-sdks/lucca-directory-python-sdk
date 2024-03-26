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


class UsersListExcludedFormerResponseItemsItem(
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
            def calendar() -> typing.Type['UsersListExcludedFormerResponseItemsItemCalendar']:
                return UsersListExcludedFormerResponseItemsItemCalendar
        
            @staticmethod
            def culture() -> typing.Type['UsersListExcludedFormerResponseItemsItemCulture']:
                return UsersListExcludedFormerResponseItemsItemCulture
        
            @staticmethod
            def picture() -> typing.Type['UsersListExcludedFormerResponseItemsItemPicture']:
                return UsersListExcludedFormerResponseItemsItemPicture
            applicationData = schemas.DictSchema
        
            @staticmethod
            def legalEntity() -> typing.Type['UsersListExcludedFormerResponseItemsItemLegalEntity']:
                return UsersListExcludedFormerResponseItemsItemLegalEntity
        
            @staticmethod
            def department() -> typing.Type['UsersListExcludedFormerResponseItemsItemDepartment']:
                return UsersListExcludedFormerResponseItemsItemDepartment
        
            @staticmethod
            def manager() -> typing.Type['UsersListExcludedFormerResponseItemsItemManager']:
                return UsersListExcludedFormerResponseItemsItemManager
        
            @staticmethod
            def rolePrincipal() -> typing.Type['UsersListExcludedFormerResponseItemsItemRolePrincipal']:
                return UsersListExcludedFormerResponseItemsItemRolePrincipal
        
            @staticmethod
            def habilitedRoles() -> typing.Type['UsersListExcludedFormerResponseItemsItemHabilitedRoles']:
                return UsersListExcludedFormerResponseItemsItemHabilitedRoles
        
            @staticmethod
            def userWorkCycles() -> typing.Type['UsersListExcludedFormerResponseItemsItemUserWorkCycles']:
                return UsersListExcludedFormerResponseItemsItemUserWorkCycles
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
    def __getitem__(self, name: typing_extensions.Literal["calendar"]) -> 'UsersListExcludedFormerResponseItemsItemCalendar': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["culture"]) -> 'UsersListExcludedFormerResponseItemsItemCulture': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["picture"]) -> 'UsersListExcludedFormerResponseItemsItemPicture': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicationData"]) -> MetaOapg.properties.applicationData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalEntity"]) -> 'UsersListExcludedFormerResponseItemsItemLegalEntity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> 'UsersListExcludedFormerResponseItemsItemDepartment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manager"]) -> 'UsersListExcludedFormerResponseItemsItemManager': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rolePrincipal"]) -> 'UsersListExcludedFormerResponseItemsItemRolePrincipal': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["habilitedRoles"]) -> 'UsersListExcludedFormerResponseItemsItemHabilitedRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userWorkCycles"]) -> 'UsersListExcludedFormerResponseItemsItemUserWorkCycles': ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["calendar"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemCalendar', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["culture"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemCulture', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["picture"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemPicture', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicationData"]) -> typing.Union[MetaOapg.properties.applicationData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalEntity"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemLegalEntity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemDepartment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manager"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemManager', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rolePrincipal"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemRolePrincipal', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["habilitedRoles"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemHabilitedRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userWorkCycles"]) -> typing.Union['UsersListExcludedFormerResponseItemsItemUserWorkCycles', schemas.Unset]: ...
    
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
        calendar: typing.Union['UsersListExcludedFormerResponseItemsItemCalendar', schemas.Unset] = schemas.unset,
        culture: typing.Union['UsersListExcludedFormerResponseItemsItemCulture', schemas.Unset] = schemas.unset,
        picture: typing.Union['UsersListExcludedFormerResponseItemsItemPicture', schemas.Unset] = schemas.unset,
        applicationData: typing.Union[MetaOapg.properties.applicationData, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        legalEntity: typing.Union['UsersListExcludedFormerResponseItemsItemLegalEntity', schemas.Unset] = schemas.unset,
        department: typing.Union['UsersListExcludedFormerResponseItemsItemDepartment', schemas.Unset] = schemas.unset,
        manager: typing.Union['UsersListExcludedFormerResponseItemsItemManager', schemas.Unset] = schemas.unset,
        rolePrincipal: typing.Union['UsersListExcludedFormerResponseItemsItemRolePrincipal', schemas.Unset] = schemas.unset,
        habilitedRoles: typing.Union['UsersListExcludedFormerResponseItemsItemHabilitedRoles', schemas.Unset] = schemas.unset,
        userWorkCycles: typing.Union['UsersListExcludedFormerResponseItemsItemUserWorkCycles', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersListExcludedFormerResponseItemsItem':
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

from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_calendar import UsersListExcludedFormerResponseItemsItemCalendar
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_culture import UsersListExcludedFormerResponseItemsItemCulture
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_department import UsersListExcludedFormerResponseItemsItemDepartment
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_habilited_roles import UsersListExcludedFormerResponseItemsItemHabilitedRoles
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_legal_entity import UsersListExcludedFormerResponseItemsItemLegalEntity
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_manager import UsersListExcludedFormerResponseItemsItemManager
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_picture import UsersListExcludedFormerResponseItemsItemPicture
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_role_principal import UsersListExcludedFormerResponseItemsItemRolePrincipal
from lucca_directory_python_sdk.model.users_list_excluded_former_response_items_item_user_work_cycles import UsersListExcludedFormerResponseItemsItemUserWorkCycles