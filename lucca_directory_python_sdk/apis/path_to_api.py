import typing_extensions

from lucca_directory_python_sdk.paths import PathValues
from lucca_directory_python_sdk.apis.paths.api_v3_users import ApiV3Users
from lucca_directory_python_sdk.apis.paths.api_v3_users_user_id import ApiV3UsersUserId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V3_USERS: ApiV3Users,
        PathValues.API_V3_USERS_USER_ID: ApiV3UsersUserId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V3_USERS: ApiV3Users,
        PathValues.API_V3_USERS_USER_ID: ApiV3UsersUserId,
    }
)
