# coding: utf-8

"""
    Directory-v3

    Welcome on the documentation for the Directory v3 API. 

    The version of the OpenAPI document: 1.0
    Contact: developers@lucca.fr
    Created by: https://www.lucca.fr
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from lucca_directory_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from lucca_directory_python_sdk.api_response import AsyncGeneratorResponse
from lucca_directory_python_sdk import api_client, exceptions
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

from lucca_directory_python_sdk.model.users_list_excluded_former_response import UsersListExcludedFormerResponse as UsersListExcludedFormerResponseSchema

from lucca_directory_python_sdk.type.users_list_excluded_former_response import UsersListExcludedFormerResponse

from ...api_client import Dictionary
from lucca_directory_python_sdk.pydantic.users_list_excluded_former_response import UsersListExcludedFormerResponse as UsersListExcludedFormerResponsePydantic

# Query params
DtContractEndSchema = schemas.StrSchema
DtContractStartSchema = schemas.StrSchema


class IdSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.AnyTypeSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IdSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ModifiedAtSchema = schemas.StrSchema
PagingSchema = schemas.StrSchema


class FieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.AnyTypeSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
MailSchema = schemas.StrSchema
LoginSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'dtContractEnd': typing.Union[DtContractEndSchema, str, ],
        'dtContractStart': typing.Union[DtContractStartSchema, str, ],
        'id': typing.Union[IdSchema, list, tuple, ],
        'modifiedAt': typing.Union[ModifiedAtSchema, str, ],
        'paging': typing.Union[PagingSchema, str, ],
        'fields': typing.Union[FieldsSchema, list, tuple, ],
        'mail': typing.Union[MailSchema, str, ],
        'login': typing.Union[LoginSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_dt_contract_end = api_client.QueryParameter(
    name="dtContractEnd",
    style=api_client.ParameterStyle.FORM,
    schema=DtContractEndSchema,
    explode=True,
)
request_query_dt_contract_start = api_client.QueryParameter(
    name="dtContractStart",
    style=api_client.ParameterStyle.FORM,
    schema=DtContractStartSchema,
    explode=True,
)
request_query_id = api_client.QueryParameter(
    name="id",
    style=api_client.ParameterStyle.FORM,
    schema=IdSchema,
    explode=True,
)
request_query_modified_at = api_client.QueryParameter(
    name="modifiedAt",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtSchema,
    explode=True,
)
request_query_paging = api_client.QueryParameter(
    name="paging",
    style=api_client.ParameterStyle.FORM,
    schema=PagingSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_mail = api_client.QueryParameter(
    name="mail",
    style=api_client.ParameterStyle.FORM,
    schema=MailSchema,
    explode=True,
)
request_query_login = api_client.QueryParameter(
    name="login",
    style=api_client.ParameterStyle.FORM,
    schema=LoginSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = schemas.DictSchema


request_body_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = UsersListExcludedFormerResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UsersListExcludedFormerResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsersListExcludedFormerResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_excluded_former_mapped_args(
        self,
        dt_contract_end: typing.Optional[str] = None,
        dt_contract_start: typing.Optional[str] = None,
        id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        paging: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        args.body = _body
        if dt_contract_end is not None:
            _query_params["dtContractEnd"] = dt_contract_end
        if dt_contract_start is not None:
            _query_params["dtContractStart"] = dt_contract_start
        if id is not None:
            _query_params["id"] = id
        if modified_at is not None:
            _query_params["modifiedAt"] = modified_at
        if paging is not None:
            _query_params["paging"] = paging
        if fields is not None:
            _query_params["fields"] = fields
        if mail is not None:
            _query_params["mail"] = mail
        if login is not None:
            _query_params["login"] = login
        args.query = _query_params
        return args

    async def _alist_excluded_former_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List Users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dt_contract_end,
            request_query_dt_contract_start,
            request_query_id,
            request_query_modified_at,
            request_query_paging,
            request_query_fields,
            request_query_mail,
            request_query_login,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_excluded_former_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List Users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dt_contract_end,
            request_query_dt_contract_start,
            request_query_id,
            request_query_modified_at,
            request_query_paging,
            request_query_fields,
            request_query_mail,
            request_query_login,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListExcludedFormerRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_excluded_former(
        self,
        dt_contract_end: typing.Optional[str] = None,
        dt_contract_start: typing.Optional[str] = None,
        id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        paging: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_excluded_former_mapped_args(
            dt_contract_end=dt_contract_end,
            dt_contract_start=dt_contract_start,
            id=id,
            modified_at=modified_at,
            paging=paging,
            fields=fields,
            mail=mail,
            login=login,
        )
        return await self._alist_excluded_former_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def list_excluded_former(
        self,
        dt_contract_end: typing.Optional[str] = None,
        dt_contract_start: typing.Optional[str] = None,
        id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        paging: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_excluded_former_mapped_args(
            dt_contract_end=dt_contract_end,
            dt_contract_start=dt_contract_start,
            id=id,
            modified_at=modified_at,
            paging=paging,
            fields=fields,
            mail=mail,
            login=login,
        )
        return self._list_excluded_former_oapg(
            body=args.body,
            query_params=args.query,
        )

class ListExcludedFormer(BaseApi):

    async def alist_excluded_former(
        self,
        dt_contract_end: typing.Optional[str] = None,
        dt_contract_start: typing.Optional[str] = None,
        id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        paging: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsersListExcludedFormerResponsePydantic:
        raw_response = await self.raw.alist_excluded_former(
            dt_contract_end=dt_contract_end,
            dt_contract_start=dt_contract_start,
            id=id,
            modified_at=modified_at,
            paging=paging,
            fields=fields,
            mail=mail,
            login=login,
            **kwargs,
        )
        if validate:
            return UsersListExcludedFormerResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsersListExcludedFormerResponsePydantic, raw_response.body)
    
    
    def list_excluded_former(
        self,
        dt_contract_end: typing.Optional[str] = None,
        dt_contract_start: typing.Optional[str] = None,
        id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        paging: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UsersListExcludedFormerResponsePydantic:
        raw_response = self.raw.list_excluded_former(
            dt_contract_end=dt_contract_end,
            dt_contract_start=dt_contract_start,
            id=id,
            modified_at=modified_at,
            paging=paging,
            fields=fields,
            mail=mail,
            login=login,
        )
        if validate:
            return UsersListExcludedFormerResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UsersListExcludedFormerResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        dt_contract_end: typing.Optional[str] = None,
        dt_contract_start: typing.Optional[str] = None,
        id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        paging: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_excluded_former_mapped_args(
            dt_contract_end=dt_contract_end,
            dt_contract_start=dt_contract_start,
            id=id,
            modified_at=modified_at,
            paging=paging,
            fields=fields,
            mail=mail,
            login=login,
        )
        return await self._alist_excluded_former_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        dt_contract_end: typing.Optional[str] = None,
        dt_contract_start: typing.Optional[str] = None,
        id: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        modified_at: typing.Optional[str] = None,
        paging: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_excluded_former_mapped_args(
            dt_contract_end=dt_contract_end,
            dt_contract_start=dt_contract_start,
            id=id,
            modified_at=modified_at,
            paging=paging,
            fields=fields,
            mail=mail,
            login=login,
        )
        return self._list_excluded_former_oapg(
            body=args.body,
            query_params=args.query,
        )

