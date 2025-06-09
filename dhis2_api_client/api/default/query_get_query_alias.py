from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import Response


def _get_kwargs(
    hash_: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/query/alias/{hash_}",
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
    hash_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        hash_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        hash_=hash_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hash_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        hash_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return sync_detailed(
        hash_=hash_,
        client=client,
    ).parsed


async def asyncio_detailed(
    hash_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        hash_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        hash_=hash_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hash_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        hash_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return (
        await asyncio_detailed(
            hash_=hash_,
            client=client,
        )
    ).parsed
