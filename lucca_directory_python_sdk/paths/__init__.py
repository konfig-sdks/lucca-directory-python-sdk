# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lucca_directory_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V3_USERS = "/api/v3/users"
    API_V3_USERS_USER_ID = "/api/v3/users/{userId}"
