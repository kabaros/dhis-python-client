from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_setting_get_system_setting_or_translation_as_plain_textget_system_setting_or_translation_as_json_response_200 import (
    SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    locale: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/systemSettings/{key}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage
    ]
]:
    if response.status_code == 200:
        response_200 = SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200.from_dict(
            response.json()
        )

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
) -> Response[
    Union[
        SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage
    ]
]:
    """[no description yet]

    Args:
        key (str):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        key=key,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage
    ]
]:
    """[no description yet]

    Args:
        key (str):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage]
    """

    return sync_detailed(
        key=key,
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage
    ]
]:
    """[no description yet]

    Args:
        key (str):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        key=key,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage
    ]
]:
    """[no description yet]

    Args:
        key (str):
        locale (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SystemSettingGetSystemSettingOrTranslationAsPlainTextgetSystemSettingOrTranslationAsJsonResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            locale=locale,
        )
    ).parsed
