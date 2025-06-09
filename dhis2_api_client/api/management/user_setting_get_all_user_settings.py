from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_setting_get_all_user_settings_response_200 import UserSettingGetAllUserSettingsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key: Union[Unset, list[str]] = UNSET,
    use_fallback: Union[Unset, bool] = True,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_key: Union[Unset, list[str]] = UNSET
    if not isinstance(key, Unset):
        json_key = key

    params["key"] = json_key

    params["useFallback"] = use_fallback

    params["user"] = user

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/userSettings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserSettingGetAllUserSettingsResponse200]:
    if response.status_code == 200:
        response_200 = UserSettingGetAllUserSettingsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserSettingGetAllUserSettingsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, list[str]] = UNSET,
    use_fallback: Union[Unset, bool] = True,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Response[UserSettingGetAllUserSettingsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):
        use_fallback (Union[Unset, bool]):  Default: True.
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserSettingGetAllUserSettingsResponse200]
    """

    kwargs = _get_kwargs(
        key=key,
        use_fallback=use_fallback,
        user=user,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, list[str]] = UNSET,
    use_fallback: Union[Unset, bool] = True,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[UserSettingGetAllUserSettingsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):
        use_fallback (Union[Unset, bool]):  Default: True.
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserSettingGetAllUserSettingsResponse200
    """

    return sync_detailed(
        client=client,
        key=key,
        use_fallback=use_fallback,
        user=user,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, list[str]] = UNSET,
    use_fallback: Union[Unset, bool] = True,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Response[UserSettingGetAllUserSettingsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):
        use_fallback (Union[Unset, bool]):  Default: True.
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserSettingGetAllUserSettingsResponse200]
    """

    kwargs = _get_kwargs(
        key=key,
        use_fallback=use_fallback,
        user=user,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, list[str]] = UNSET,
    use_fallback: Union[Unset, bool] = True,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
) -> Optional[UserSettingGetAllUserSettingsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):
        use_fallback (Union[Unset, bool]):  Default: True.
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserSettingGetAllUserSettingsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            key=key,
            use_fallback=use_fallback,
            user=user,
            user_id=user_id,
        )
    ).parsed
