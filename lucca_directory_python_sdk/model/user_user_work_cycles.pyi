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


class UserUserWorkCycles(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "OwnerID",
                    "StartsOn",
                    "WorkCycleID",
                    "Id",
                    "EndsOn",
                }
                
                class properties:
                    Id = schemas.NumberSchema
                    OwnerID = schemas.NumberSchema
                    WorkCycleID = schemas.NumberSchema
                    
                    
                    class StartsOn(
                        schemas.StrSchema
                    ):
                        pass
                    
                    
                    class EndsOn(
                        schemas.StrSchema
                    ):
                        pass
                    __annotations__ = {
                        "Id": Id,
                        "OwnerID": OwnerID,
                        "WorkCycleID": WorkCycleID,
                        "StartsOn": StartsOn,
                        "EndsOn": EndsOn,
                    }
        
            
            OwnerID: MetaOapg.properties.OwnerID
            StartsOn: MetaOapg.properties.StartsOn
            WorkCycleID: MetaOapg.properties.WorkCycleID
            Id: MetaOapg.properties.Id
            EndsOn: MetaOapg.properties.EndsOn
            
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
            def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["OwnerID"]) -> MetaOapg.properties.OwnerID: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["WorkCycleID"]) -> MetaOapg.properties.WorkCycleID: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["StartsOn"]) -> MetaOapg.properties.StartsOn: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EndsOn"]) -> MetaOapg.properties.EndsOn: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "OwnerID", "WorkCycleID", "StartsOn", "EndsOn", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                OwnerID: typing.Union[MetaOapg.properties.OwnerID, decimal.Decimal, int, float, ],
                StartsOn: typing.Union[MetaOapg.properties.StartsOn, str, ],
                WorkCycleID: typing.Union[MetaOapg.properties.WorkCycleID, decimal.Decimal, int, float, ],
                Id: typing.Union[MetaOapg.properties.Id, decimal.Decimal, int, float, ],
                EndsOn: typing.Union[MetaOapg.properties.EndsOn, str, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    OwnerID=OwnerID,
                    StartsOn=StartsOn,
                    WorkCycleID=WorkCycleID,
                    Id=Id,
                    EndsOn=EndsOn,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UserUserWorkCycles':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
