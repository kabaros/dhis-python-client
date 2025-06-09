from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.login_config_response import LoginConfigResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    locale: Union[Unset, str] = "en",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/loginConfig/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LoginConfigResponse]:
    if response.status_code == 200:
        response_200 = LoginConfigResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LoginConfigResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = "en",
) -> Response[LoginConfigResponse]:
    """[no description yet]

    Args:
        locale (Union[Unset, str]):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginConfigResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = "en",
) -> Optional[LoginConfigResponse]:
    """[no description yet]

    Args:
        locale (Union[Unset, str]):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginConfigResponse
    """

    return sync_detailed(
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = "en",
) -> Response[LoginConfigResponse]:
    """[no description yet]

    Args:
        locale (Union[Unset, str]):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoginConfigResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = "en",
) -> Optional[LoginConfigResponse]:
    """[no description yet]

    Args:
        locale (Union[Unset, str]):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoginConfigResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
        )
    ).parsed
