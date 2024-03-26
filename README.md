<div align="left">

[![Visit Lucca](./header.png)](https://lucca-hr.com)

# Lucca<a id="lucca"></a>

Welcome on the documentation for the Directory v3 API.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`luccadirectory.users.create_new_user`](#luccadirectoryuserscreate_new_user)
  * [`luccadirectory.users.get_by_id`](#luccadirectoryusersget_by_id)
  * [`luccadirectory.users.list_excluded_former`](#luccadirectoryuserslist_excluded_former)
  * [`luccadirectory.users.update_by_id`](#luccadirectoryusersupdate_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Lucca&serviceName=Directory&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from lucca_directory_python_sdk import LuccaDirectory, ApiException

luccadirectory = LuccaDirectory(
    authorization="YOUR_API_KEY",
)

try:
    # Create a new User
    create_new_user_response = luccadirectory.users.create_new_user()
    print(create_new_user_response)
except ApiException as e:
    print("Exception when calling UsersApi.create_new_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from lucca_directory_python_sdk import LuccaDirectory, ApiException

luccadirectory = LuccaDirectory(
    authorization="YOUR_API_KEY",
)


async def main():
    try:
        # Create a new User
        create_new_user_response = await luccadirectory.users.acreate_new_user()
        print(create_new_user_response)
    except ApiException as e:
        print("Exception when calling UsersApi.create_new_user: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from lucca_directory_python_sdk import LuccaDirectory, ApiException

luccadirectory = LuccaDirectory(
    authorization="YOUR_API_KEY",
)

try:
    # Create a new User
    create_new_user_response = luccadirectory.users.raw.create_new_user()
    pprint(create_new_user_response.body)
    pprint(create_new_user_response.body["first_name"])
    pprint(create_new_user_response.body["last_name"])
    pprint(create_new_user_response.body["mail"])
    pprint(create_new_user_response.body["login"])
    pprint(create_new_user_response.body["legal_entity_id"])
    pprint(create_new_user_response.body["dt_contract_start"])
    pprint(create_new_user_response.body["department_id"])
    pprint(create_new_user_response.body["role_principal_id"])
    pprint(create_new_user_response.body["dt_contract_end"])
    pprint(create_new_user_response.body["csp_id"])
    pprint(create_new_user_response.body["calendar_id"])
    pprint(create_new_user_response.body["employee_number"])
    pprint(create_new_user_response.body["birth_date"])
    pprint(create_new_user_response.body["user_work_cycles"])
    pprint(create_new_user_response.body["manager_id"])
    pprint(create_new_user_response.body["habilited_roles"])
    pprint(create_new_user_response.body["culture_id"])
    pprint(create_new_user_response.body["address"])
    pprint(create_new_user_response.body["bank_name"])
    pprint(create_new_user_response.body["direct_line"])
    pprint(create_new_user_response.body["job_title"])
    pprint(create_new_user_response.body["gender"])
    pprint(create_new_user_response.body["nationality"])
    pprint(create_new_user_response.body["personal_email"])
    pprint(create_new_user_response.body["personal_mobile"])
    pprint(create_new_user_response.body["professional_mobile"])
    pprint(create_new_user_response.body["quote"])
    pprint(create_new_user_response.headers)
    pprint(create_new_user_response.status)
    pprint(create_new_user_response.round_trip_time)
except ApiException as e:
    print("Exception when calling UsersApi.create_new_user: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `luccadirectory.users.create_new_user`<a id="luccadirectoryuserscreate_new_user"></a>

Create a new User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = luccadirectory.users.create_new_user()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UsersCreateNewUserResponse`](./lucca_directory_python_sdk/pydantic/users_create_new_user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccadirectory.users.get_by_id`<a id="luccadirectoryusersget_by_id"></a>

Retrieve a single User identified by its unique identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = luccadirectory.users.get_by_id(
    user_id="userId_example",
    fields=[None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_directory_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_directory_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Comma-separated list of fields of the user to include in responses. Extended data can be retrieved with `?fields=extendedData`. 

#### 🔄 Return<a id="🔄-return"></a>

[`UsersGetByIdResponse`](./lucca_directory_python_sdk/pydantic/users_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users/{userId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccadirectory.users.list_excluded_former`<a id="luccadirectoryuserslist_excluded_former"></a>

Retrieve a list of Users.

By default, former employees are excluded from the response. In order to retrieve them, you may add the `?dtContractEnd=notequal,null` query parameter to your request.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_excluded_former_response = luccadirectory.users.list_excluded_former(
    dt_contract_end="string_example",
    dt_contract_start="string_example",
    id=[None],
    modified_at="string_example",
    paging="string_example",
    fields=[None],
    mail="string_example",
    login="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dt_contract_end: `str`<a id="dt_contract_end-str"></a>

`{comparator},{date-time}`. 

##### dt_contract_start: `str`<a id="dt_contract_start-str"></a>

{comparator},{date-time}

##### id: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_directory_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="id-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_directory_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

User's identifier

##### modified_at: `str`<a id="modified_at-str"></a>

{comparator},{date-time}

##### paging: `str`<a id="paging-str"></a>

{offset},{limit}. Defaults to 0,1000.

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_directory_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_directory_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### mail: `str`<a id="mail-str"></a>

User's mail

##### login: `str`<a id="login-str"></a>

User's login

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🔄 Return<a id="🔄-return"></a>

[`UsersListExcludedFormerResponse`](./lucca_directory_python_sdk/pydantic/users_list_excluded_former_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `luccadirectory.users.update_by_id`<a id="luccadirectoryusersupdate_by_id"></a>

Update fields of a single User identified by its unique id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
luccadirectory.users.update_by_id(
    user_id="userId_example",
    first_name="John",
    last_name="Doe",
    mail="jdoe@corp.com",
    login="jdoe",
    legal_entity_id=1,
    csp_id=2,
    calendar_id=None,
    employee_number="000000452",
    birth_date="1989-12-22T00:00:00",
    user_work_cycles=[{}],
    department_id=14,
    manager_id=455,
    role_principal_id=55,
    habilited_roles=[{}],
    culture_id=1040,
    address="13, rue Martin Bernard, 75 Paris",
    bank_name="My Bank",
    direct_line="0123456789",
    job_title="Developer",
    gender="Male",
    nationality="French",
    personal_email="email@test.fr",
    personal_mobile="0612345678",
    professional_mobile="0612345678",
    quote="string",
    fields=[None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### mail: `str`<a id="mail-str"></a>

##### login: `str`<a id="login-str"></a>

##### legal_entity_id: `int`<a id="legal_entity_id-int"></a>

##### csp_id: `int`<a id="csp_id-int"></a>

##### calendar_id: [`none_type`](./lucca_directory_python_sdk/type/none_type.py)<a id="calendar_id-none_typelucca_directory_python_sdktypenone_typepy"></a>

##### employee_number: `str`<a id="employee_number-str"></a>

##### birth_date: `str`<a id="birth_date-str"></a>

##### user_work_cycles: [`UsersUpdateByIdRequestUserWorkCycles`](./lucca_directory_python_sdk/type/users_update_by_id_request_user_work_cycles.py)<a id="user_work_cycles-usersupdatebyidrequestuserworkcycleslucca_directory_python_sdktypeusers_update_by_id_request_user_work_cyclespy"></a>

##### department_id: `int`<a id="department_id-int"></a>

##### manager_id: `int`<a id="manager_id-int"></a>

##### role_principal_id: `int`<a id="role_principal_id-int"></a>

##### habilited_roles: [`UsersUpdateByIdRequestHabilitedRoles`](./lucca_directory_python_sdk/type/users_update_by_id_request_habilited_roles.py)<a id="habilited_roles-usersupdatebyidrequesthabilitedroleslucca_directory_python_sdktypeusers_update_by_id_request_habilited_rolespy"></a>

##### culture_id: `int`<a id="culture_id-int"></a>

##### address: `str`<a id="address-str"></a>

##### bank_name: `str`<a id="bank_name-str"></a>

##### direct_line: `str`<a id="direct_line-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### gender: `str`<a id="gender-str"></a>

##### nationality: `str`<a id="nationality-str"></a>

##### personal_email: `str`<a id="personal_email-str"></a>

##### personal_mobile: `str`<a id="personal_mobile-str"></a>

##### professional_mobile: `str`<a id="professional_mobile-str"></a>

##### quote: `str`<a id="quote-str"></a>

##### fields: List[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lucca_directory_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="fields-listunionbool-date-datetime-dict-float-int-list-str-nonelucca_directory_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Fields of the user, comma separated

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateByIdRequest`](./lucca_directory_python_sdk/type/users_update_by_id_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/v3/users/{userId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
