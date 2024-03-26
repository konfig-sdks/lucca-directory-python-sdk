import typing_extensions

from lucca_directory_python_sdk.apis.tags import TagValues
from lucca_directory_python_sdk.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USERS: UsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USERS: UsersApi,
    }
)
