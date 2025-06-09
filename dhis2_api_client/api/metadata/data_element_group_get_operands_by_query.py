from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    q: str,
    *,
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["locale"] = locale

    params["translate"] = translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dataElementGroups/{uid}/operands/query/{q}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[WebMessage, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
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
) -> Response[Union[WebMessage, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uid: str,
    q: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str):
        q (str):
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        q=q,
        locale=locale,
        translate=translate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    q: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str):
        q (str):
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return sync_detailed(
        uid=uid,
        q=q,
        client=client,
        locale=locale,
        translate=translate,
    ).parsed


async def asyncio_detailed(
    uid: str,
    q: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str):
        q (str):
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        q=q,
        locale=locale,
        translate=translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    q: str,
    *,
    client: Union[AuthenticatedClient, Client],
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str):
        q (str):
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            q=q,
            client=client,
            locale=locale,
            translate=translate,
        )
    ).parsed
