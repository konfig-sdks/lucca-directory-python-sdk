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


class UsersGetByIdResponseUserWorkCyclesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            Id = schemas.IntSchema
            OwnerID = schemas.IntSchema
            WorkCycleID = schemas.IntSchema
            StartsOn = schemas.StrSchema
            EndsOn = schemas.StrSchema
            __annotations__ = {
                "Id": Id,
                "OwnerID": OwnerID,
                "WorkCycleID": WorkCycleID,
                "StartsOn": StartsOn,
                "EndsOn": EndsOn,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OwnerID"]) -> MetaOapg.properties.OwnerID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkCycleID"]) -> MetaOapg.properties.WorkCycleID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StartsOn"]) -> MetaOapg.properties.StartsOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EndsOn"]) -> MetaOapg.properties.EndsOn: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Id", "OwnerID", "WorkCycleID", "StartsOn", "EndsOn", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OwnerID"]) -> typing.Union[MetaOapg.properties.OwnerID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkCycleID"]) -> typing.Union[MetaOapg.properties.WorkCycleID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StartsOn"]) -> typing.Union[MetaOapg.properties.StartsOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EndsOn"]) -> typing.Union[MetaOapg.properties.EndsOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "OwnerID", "WorkCycleID", "StartsOn", "EndsOn", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Id: typing.Union[MetaOapg.properties.Id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        OwnerID: typing.Union[MetaOapg.properties.OwnerID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        WorkCycleID: typing.Union[MetaOapg.properties.WorkCycleID, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        StartsOn: typing.Union[MetaOapg.properties.StartsOn, str, schemas.Unset] = schemas.unset,
        EndsOn: typing.Union[MetaOapg.properties.EndsOn, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersGetByIdResponseUserWorkCyclesItem':
        return super().__new__(
            cls,
            *args,
            Id=Id,
            OwnerID=OwnerID,
            WorkCycleID=WorkCycleID,
            StartsOn=StartsOn,
            EndsOn=EndsOn,
            _configuration=_configuration,
            **kwargs,
        )
