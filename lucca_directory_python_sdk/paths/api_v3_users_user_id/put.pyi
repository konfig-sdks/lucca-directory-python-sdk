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

from lucca_directory_python_sdk.model.users_update_by_id_request import UsersUpdateByIdRequest as UsersUpdateByIdRequestSchema
from lucca_directory_python_sdk.model.users_update_by_id_request_habilited_roles import UsersUpdateByIdRequestHabilitedRoles as UsersUpdateByIdRequestHabilitedRolesSchema
from lucca_directory_python_sdk.model.users_update_by_id_request_user_work_cycles import UsersUpdateByIdRequestUserWorkCycles as UsersUpdateByIdRequestUserWorkCyclesSchema

from lucca_directory_python_sdk.type.users_update_by_id_request import UsersUpdateByIdRequest
from lucca_directory_python_sdk.type.users_update_by_id_request_habilited_roles import UsersUpdateByIdRequestHabilitedRoles
from lucca_directory_python_sdk.type.users_update_by_id_request_user_work_cycles import UsersUpdateByIdRequestUserWorkCycles

from ...api_client import Dictionary
from lucca_directory_python_sdk.pydantic.users_update_by_id_request_user_work_cycles import UsersUpdateByIdRequestUserWorkCycles as UsersUpdateByIdRequestUserWorkCyclesPydantic
from lucca_directory_python_sdk.pydantic.users_update_by_id_request_habilited_roles import UsersUpdateByIdRequestHabilitedRoles as UsersUpdateByIdRequestHabilitedRolesPydantic
from lucca_directory_python_sdk.pydantic.users_update_by_id_request import UsersUpdateByIdRequest as UsersUpdateByIdRequestPydantic

# Query params


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
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'fields': typing.Union[FieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
# Path params
UserIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'userId': typing.Union[UserIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_user_id = api_client.PathParameter(
    name="userId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UsersUpdateByIdRequestSchema
SchemaForRequestBodyApplicationXml = schemas.DictSchema


request_body_users_update_by_id_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
    },
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
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
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
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


class BaseApi(api_client.Api):

    def _update_by_id_mapped_args(
        self,
        user_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        legal_entity_id: typing.Optional[int] = None,
        csp_id: typing.Optional[int] = None,
        calendar_id: typing.Optional[none_type] = None,
        employee_number: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = None,
        department_id: typing.Optional[int] = None,
        manager_id: typing.Optional[int] = None,
        role_principal_id: typing.Optional[int] = None,
        habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = None,
        culture_id: typing.Optional[int] = None,
        address: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        direct_line: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        nationality: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        professional_mobile: typing.Optional[str] = None,
        quote: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if first_name is not None:
            _body["firstName"] = first_name
        if last_name is not None:
            _body["lastName"] = last_name
        if mail is not None:
            _body["mail"] = mail
        if login is not None:
            _body["login"] = login
        if legal_entity_id is not None:
            _body["legalEntityId"] = legal_entity_id
        if csp_id is not None:
            _body["cspId"] = csp_id
        if calendar_id is not None:
            _body["calendarId"] = calendar_id
        if employee_number is not None:
            _body["employeeNumber"] = employee_number
        if birth_date is not None:
            _body["birthDate"] = birth_date
        if user_work_cycles is not None:
            _body["userWorkCycles"] = user_work_cycles
        if department_id is not None:
            _body["departmentId"] = department_id
        if manager_id is not None:
            _body["managerId"] = manager_id
        if role_principal_id is not None:
            _body["rolePrincipalId"] = role_principal_id
        if habilited_roles is not None:
            _body["habilitedRoles"] = habilited_roles
        if culture_id is not None:
            _body["cultureId"] = culture_id
        if address is not None:
            _body["address"] = address
        if bank_name is not None:
            _body["bankName"] = bank_name
        if direct_line is not None:
            _body["directLine"] = direct_line
        if job_title is not None:
            _body["jobTitle"] = job_title
        if gender is not None:
            _body["gender"] = gender
        if nationality is not None:
            _body["nationality"] = nationality
        if personal_email is not None:
            _body["personalEmail"] = personal_email
        if personal_mobile is not None:
            _body["personalMobile"] = personal_mobile
        if professional_mobile is not None:
            _body["professionalMobile"] = professional_mobile
        if quote is not None:
            _body["quote"] = quote
        args.body = _body
        if fields is not None:
            _query_params["fields"] = fields
        if user_id is not None:
            _path_params["userId"] = user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_by_id_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update a User by id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_fields,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/users/{userId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_users_update_by_id_request.serialize(body, content_type)
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


    def _update_by_id_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update a User by id
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_fields,
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v3/users/{userId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_users_update_by_id_request.serialize(body, content_type)
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


class UpdateByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_by_id(
        self,
        user_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        legal_entity_id: typing.Optional[int] = None,
        csp_id: typing.Optional[int] = None,
        calendar_id: typing.Optional[none_type] = None,
        employee_number: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = None,
        department_id: typing.Optional[int] = None,
        manager_id: typing.Optional[int] = None,
        role_principal_id: typing.Optional[int] = None,
        habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = None,
        culture_id: typing.Optional[int] = None,
        address: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        direct_line: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        nationality: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        professional_mobile: typing.Optional[str] = None,
        quote: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_by_id_mapped_args(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            login=login,
            legal_entity_id=legal_entity_id,
            csp_id=csp_id,
            calendar_id=calendar_id,
            employee_number=employee_number,
            birth_date=birth_date,
            user_work_cycles=user_work_cycles,
            department_id=department_id,
            manager_id=manager_id,
            role_principal_id=role_principal_id,
            habilited_roles=habilited_roles,
            culture_id=culture_id,
            address=address,
            bank_name=bank_name,
            direct_line=direct_line,
            job_title=job_title,
            gender=gender,
            nationality=nationality,
            personal_email=personal_email,
            personal_mobile=personal_mobile,
            professional_mobile=professional_mobile,
            quote=quote,
            fields=fields,
        )
        return await self._aupdate_by_id_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_by_id(
        self,
        user_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        legal_entity_id: typing.Optional[int] = None,
        csp_id: typing.Optional[int] = None,
        calendar_id: typing.Optional[none_type] = None,
        employee_number: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = None,
        department_id: typing.Optional[int] = None,
        manager_id: typing.Optional[int] = None,
        role_principal_id: typing.Optional[int] = None,
        habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = None,
        culture_id: typing.Optional[int] = None,
        address: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        direct_line: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        nationality: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        professional_mobile: typing.Optional[str] = None,
        quote: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_by_id_mapped_args(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            login=login,
            legal_entity_id=legal_entity_id,
            csp_id=csp_id,
            calendar_id=calendar_id,
            employee_number=employee_number,
            birth_date=birth_date,
            user_work_cycles=user_work_cycles,
            department_id=department_id,
            manager_id=manager_id,
            role_principal_id=role_principal_id,
            habilited_roles=habilited_roles,
            culture_id=culture_id,
            address=address,
            bank_name=bank_name,
            direct_line=direct_line,
            job_title=job_title,
            gender=gender,
            nationality=nationality,
            personal_email=personal_email,
            personal_mobile=personal_mobile,
            professional_mobile=professional_mobile,
            quote=quote,
            fields=fields,
        )
        return self._update_by_id_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateById(BaseApi):

    async def aupdate_by_id(
        self,
        user_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        legal_entity_id: typing.Optional[int] = None,
        csp_id: typing.Optional[int] = None,
        calendar_id: typing.Optional[none_type] = None,
        employee_number: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = None,
        department_id: typing.Optional[int] = None,
        manager_id: typing.Optional[int] = None,
        role_principal_id: typing.Optional[int] = None,
        habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = None,
        culture_id: typing.Optional[int] = None,
        address: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        direct_line: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        nationality: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        professional_mobile: typing.Optional[str] = None,
        quote: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_by_id(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            login=login,
            legal_entity_id=legal_entity_id,
            csp_id=csp_id,
            calendar_id=calendar_id,
            employee_number=employee_number,
            birth_date=birth_date,
            user_work_cycles=user_work_cycles,
            department_id=department_id,
            manager_id=manager_id,
            role_principal_id=role_principal_id,
            habilited_roles=habilited_roles,
            culture_id=culture_id,
            address=address,
            bank_name=bank_name,
            direct_line=direct_line,
            job_title=job_title,
            gender=gender,
            nationality=nationality,
            personal_email=personal_email,
            personal_mobile=personal_mobile,
            professional_mobile=professional_mobile,
            quote=quote,
            fields=fields,
            **kwargs,
        )
    
    
    def update_by_id(
        self,
        user_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        legal_entity_id: typing.Optional[int] = None,
        csp_id: typing.Optional[int] = None,
        calendar_id: typing.Optional[none_type] = None,
        employee_number: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = None,
        department_id: typing.Optional[int] = None,
        manager_id: typing.Optional[int] = None,
        role_principal_id: typing.Optional[int] = None,
        habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = None,
        culture_id: typing.Optional[int] = None,
        address: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        direct_line: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        nationality: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        professional_mobile: typing.Optional[str] = None,
        quote: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_by_id(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            login=login,
            legal_entity_id=legal_entity_id,
            csp_id=csp_id,
            calendar_id=calendar_id,
            employee_number=employee_number,
            birth_date=birth_date,
            user_work_cycles=user_work_cycles,
            department_id=department_id,
            manager_id=manager_id,
            role_principal_id=role_principal_id,
            habilited_roles=habilited_roles,
            culture_id=culture_id,
            address=address,
            bank_name=bank_name,
            direct_line=direct_line,
            job_title=job_title,
            gender=gender,
            nationality=nationality,
            personal_email=personal_email,
            personal_mobile=personal_mobile,
            professional_mobile=professional_mobile,
            quote=quote,
            fields=fields,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        user_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        legal_entity_id: typing.Optional[int] = None,
        csp_id: typing.Optional[int] = None,
        calendar_id: typing.Optional[none_type] = None,
        employee_number: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = None,
        department_id: typing.Optional[int] = None,
        manager_id: typing.Optional[int] = None,
        role_principal_id: typing.Optional[int] = None,
        habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = None,
        culture_id: typing.Optional[int] = None,
        address: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        direct_line: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        nationality: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        professional_mobile: typing.Optional[str] = None,
        quote: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_by_id_mapped_args(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            login=login,
            legal_entity_id=legal_entity_id,
            csp_id=csp_id,
            calendar_id=calendar_id,
            employee_number=employee_number,
            birth_date=birth_date,
            user_work_cycles=user_work_cycles,
            department_id=department_id,
            manager_id=manager_id,
            role_principal_id=role_principal_id,
            habilited_roles=habilited_roles,
            culture_id=culture_id,
            address=address,
            bank_name=bank_name,
            direct_line=direct_line,
            job_title=job_title,
            gender=gender,
            nationality=nationality,
            personal_email=personal_email,
            personal_mobile=personal_mobile,
            professional_mobile=professional_mobile,
            quote=quote,
            fields=fields,
        )
        return await self._aupdate_by_id_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        user_id: str,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        mail: typing.Optional[str] = None,
        login: typing.Optional[str] = None,
        legal_entity_id: typing.Optional[int] = None,
        csp_id: typing.Optional[int] = None,
        calendar_id: typing.Optional[none_type] = None,
        employee_number: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        user_work_cycles: typing.Optional[UsersUpdateByIdRequestUserWorkCycles] = None,
        department_id: typing.Optional[int] = None,
        manager_id: typing.Optional[int] = None,
        role_principal_id: typing.Optional[int] = None,
        habilited_roles: typing.Optional[UsersUpdateByIdRequestHabilitedRoles] = None,
        culture_id: typing.Optional[int] = None,
        address: typing.Optional[str] = None,
        bank_name: typing.Optional[str] = None,
        direct_line: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        gender: typing.Optional[str] = None,
        nationality: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        personal_mobile: typing.Optional[str] = None,
        professional_mobile: typing.Optional[str] = None,
        quote: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_by_id_mapped_args(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            mail=mail,
            login=login,
            legal_entity_id=legal_entity_id,
            csp_id=csp_id,
            calendar_id=calendar_id,
            employee_number=employee_number,
            birth_date=birth_date,
            user_work_cycles=user_work_cycles,
            department_id=department_id,
            manager_id=manager_id,
            role_principal_id=role_principal_id,
            habilited_roles=habilited_roles,
            culture_id=culture_id,
            address=address,
            bank_name=bank_name,
            direct_line=direct_line,
            job_title=job_title,
            gender=gender,
            nationality=nationality,
            personal_email=personal_email,
            personal_mobile=personal_mobile,
            professional_mobile=professional_mobile,
            quote=quote,
            fields=fields,
        )
        return self._update_by_id_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

