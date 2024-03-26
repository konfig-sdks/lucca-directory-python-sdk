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


class UsersUpdateByIdRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            mail = schemas.StrSchema
            login = schemas.StrSchema
            legalEntityId = schemas.IntSchema
            cspId = schemas.IntSchema
            calendarId = schemas.NoneSchema
            employeeNumber = schemas.StrSchema
            birthDate = schemas.StrSchema
        
            @staticmethod
            def userWorkCycles() -> typing.Type['UsersUpdateByIdRequestUserWorkCycles']:
                return UsersUpdateByIdRequestUserWorkCycles
            departmentId = schemas.IntSchema
            managerId = schemas.IntSchema
            rolePrincipalId = schemas.IntSchema
        
            @staticmethod
            def habilitedRoles() -> typing.Type['UsersUpdateByIdRequestHabilitedRoles']:
                return UsersUpdateByIdRequestHabilitedRoles
            cultureId = schemas.IntSchema
            address = schemas.StrSchema
            bankName = schemas.StrSchema
            directLine = schemas.StrSchema
            jobTitle = schemas.StrSchema
            gender = schemas.StrSchema
            nationality = schemas.StrSchema
            personalEmail = schemas.StrSchema
            personalMobile = schemas.StrSchema
            professionalMobile = schemas.StrSchema
            quote = schemas.StrSchema
            __annotations__ = {
                "firstName": firstName,
                "lastName": lastName,
                "mail": mail,
                "login": login,
                "legalEntityId": legalEntityId,
                "cspId": cspId,
                "calendarId": calendarId,
                "employeeNumber": employeeNumber,
                "birthDate": birthDate,
                "userWorkCycles": userWorkCycles,
                "departmentId": departmentId,
                "managerId": managerId,
                "rolePrincipalId": rolePrincipalId,
                "habilitedRoles": habilitedRoles,
                "cultureId": cultureId,
                "address": address,
                "bankName": bankName,
                "directLine": directLine,
                "jobTitle": jobTitle,
                "gender": gender,
                "nationality": nationality,
                "personalEmail": personalEmail,
                "personalMobile": personalMobile,
                "professionalMobile": professionalMobile,
                "quote": quote,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mail"]) -> MetaOapg.properties.mail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["login"]) -> MetaOapg.properties.login: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legalEntityId"]) -> MetaOapg.properties.legalEntityId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cspId"]) -> MetaOapg.properties.cspId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["calendarId"]) -> MetaOapg.properties.calendarId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employeeNumber"]) -> MetaOapg.properties.employeeNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthDate"]) -> MetaOapg.properties.birthDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userWorkCycles"]) -> 'UsersUpdateByIdRequestUserWorkCycles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departmentId"]) -> MetaOapg.properties.departmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managerId"]) -> MetaOapg.properties.managerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rolePrincipalId"]) -> MetaOapg.properties.rolePrincipalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["habilitedRoles"]) -> 'UsersUpdateByIdRequestHabilitedRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cultureId"]) -> MetaOapg.properties.cultureId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankName"]) -> MetaOapg.properties.bankName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directLine"]) -> MetaOapg.properties.directLine: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jobTitle"]) -> MetaOapg.properties.jobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationality"]) -> MetaOapg.properties.nationality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalEmail"]) -> MetaOapg.properties.personalEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["personalMobile"]) -> MetaOapg.properties.personalMobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["professionalMobile"]) -> MetaOapg.properties.professionalMobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quote"]) -> MetaOapg.properties.quote: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "mail", "login", "legalEntityId", "cspId", "calendarId", "employeeNumber", "birthDate", "userWorkCycles", "departmentId", "managerId", "rolePrincipalId", "habilitedRoles", "cultureId", "address", "bankName", "directLine", "jobTitle", "gender", "nationality", "personalEmail", "personalMobile", "professionalMobile", "quote", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mail"]) -> typing.Union[MetaOapg.properties.mail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["login"]) -> typing.Union[MetaOapg.properties.login, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legalEntityId"]) -> typing.Union[MetaOapg.properties.legalEntityId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cspId"]) -> typing.Union[MetaOapg.properties.cspId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["calendarId"]) -> typing.Union[MetaOapg.properties.calendarId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employeeNumber"]) -> typing.Union[MetaOapg.properties.employeeNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthDate"]) -> typing.Union[MetaOapg.properties.birthDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userWorkCycles"]) -> typing.Union['UsersUpdateByIdRequestUserWorkCycles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departmentId"]) -> typing.Union[MetaOapg.properties.departmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managerId"]) -> typing.Union[MetaOapg.properties.managerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rolePrincipalId"]) -> typing.Union[MetaOapg.properties.rolePrincipalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["habilitedRoles"]) -> typing.Union['UsersUpdateByIdRequestHabilitedRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cultureId"]) -> typing.Union[MetaOapg.properties.cultureId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankName"]) -> typing.Union[MetaOapg.properties.bankName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directLine"]) -> typing.Union[MetaOapg.properties.directLine, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jobTitle"]) -> typing.Union[MetaOapg.properties.jobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationality"]) -> typing.Union[MetaOapg.properties.nationality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalEmail"]) -> typing.Union[MetaOapg.properties.personalEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["personalMobile"]) -> typing.Union[MetaOapg.properties.personalMobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["professionalMobile"]) -> typing.Union[MetaOapg.properties.professionalMobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quote"]) -> typing.Union[MetaOapg.properties.quote, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "mail", "login", "legalEntityId", "cspId", "calendarId", "employeeNumber", "birthDate", "userWorkCycles", "departmentId", "managerId", "rolePrincipalId", "habilitedRoles", "cultureId", "address", "bankName", "directLine", "jobTitle", "gender", "nationality", "personalEmail", "personalMobile", "professionalMobile", "quote", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        mail: typing.Union[MetaOapg.properties.mail, str, schemas.Unset] = schemas.unset,
        login: typing.Union[MetaOapg.properties.login, str, schemas.Unset] = schemas.unset,
        legalEntityId: typing.Union[MetaOapg.properties.legalEntityId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        cspId: typing.Union[MetaOapg.properties.cspId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        calendarId: typing.Union[MetaOapg.properties.calendarId, None, schemas.Unset] = schemas.unset,
        employeeNumber: typing.Union[MetaOapg.properties.employeeNumber, str, schemas.Unset] = schemas.unset,
        birthDate: typing.Union[MetaOapg.properties.birthDate, str, schemas.Unset] = schemas.unset,
        userWorkCycles: typing.Union['UsersUpdateByIdRequestUserWorkCycles', schemas.Unset] = schemas.unset,
        departmentId: typing.Union[MetaOapg.properties.departmentId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        managerId: typing.Union[MetaOapg.properties.managerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rolePrincipalId: typing.Union[MetaOapg.properties.rolePrincipalId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        habilitedRoles: typing.Union['UsersUpdateByIdRequestHabilitedRoles', schemas.Unset] = schemas.unset,
        cultureId: typing.Union[MetaOapg.properties.cultureId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        bankName: typing.Union[MetaOapg.properties.bankName, str, schemas.Unset] = schemas.unset,
        directLine: typing.Union[MetaOapg.properties.directLine, str, schemas.Unset] = schemas.unset,
        jobTitle: typing.Union[MetaOapg.properties.jobTitle, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        nationality: typing.Union[MetaOapg.properties.nationality, str, schemas.Unset] = schemas.unset,
        personalEmail: typing.Union[MetaOapg.properties.personalEmail, str, schemas.Unset] = schemas.unset,
        personalMobile: typing.Union[MetaOapg.properties.personalMobile, str, schemas.Unset] = schemas.unset,
        professionalMobile: typing.Union[MetaOapg.properties.professionalMobile, str, schemas.Unset] = schemas.unset,
        quote: typing.Union[MetaOapg.properties.quote, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersUpdateByIdRequest':
        return super().__new__(
            cls,
            *args,
            firstName=firstName,
            lastName=lastName,
            mail=mail,
            login=login,
            legalEntityId=legalEntityId,
            cspId=cspId,
            calendarId=calendarId,
            employeeNumber=employeeNumber,
            birthDate=birthDate,
            userWorkCycles=userWorkCycles,
            departmentId=departmentId,
            managerId=managerId,
            rolePrincipalId=rolePrincipalId,
            habilitedRoles=habilitedRoles,
            cultureId=cultureId,
            address=address,
            bankName=bankName,
            directLine=directLine,
            jobTitle=jobTitle,
            gender=gender,
            nationality=nationality,
            personalEmail=personalEmail,
            personalMobile=personalMobile,
            professionalMobile=professionalMobile,
            quote=quote,
            _configuration=_configuration,
            **kwargs,
        )

from lucca_directory_python_sdk.model.users_update_by_id_request_habilited_roles import UsersUpdateByIdRequestHabilitedRoles
from lucca_directory_python_sdk.model.users_update_by_id_request_user_work_cycles import UsersUpdateByIdRequestUserWorkCycles