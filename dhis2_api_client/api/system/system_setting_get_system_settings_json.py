from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_setting_get_system_settings_json_response_200 import SystemSettingGetSystemSettingsJsonResponse200
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_key: Union[Unset, list[str]] = UNSET
    if not isinstance(key, Unset):
        json_key = key

    params["key"] = json_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systemSettings/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = SystemSettingGetSystemSettingsJsonResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]:
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
) -> Response[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]
    """

    return sync_detailed(
        client=client,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, list[str]] = UNSET,
) -> Response[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]]:
    """[no description yet]

    Args:
        key (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SystemSettingGetSystemSettingsJsonResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            key=key,
        )
    ).parsed
