from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reserved_value import ReservedValue
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    expiration: Union[Unset, int] = 3,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["expiration"] = expiration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/trackedEntityAttributes/{id}/generate",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ReservedValue]:
    if response.status_code == 200:
        response_200 = ReservedValue.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ReservedValue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expiration: Union[Unset, int] = 3,
) -> Response[ReservedValue]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReservedValue]
    """

    kwargs = _get_kwargs(
        id=id,
        expiration=expiration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expiration: Union[Unset, int] = 3,
) -> Optional[ReservedValue]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReservedValue
    """

    return sync_detailed(
        id=id,
        client=client,
        expiration=expiration,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expiration: Union[Unset, int] = 3,
) -> Response[ReservedValue]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReservedValue]
    """

    kwargs = _get_kwargs(
        id=id,
        expiration=expiration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expiration: Union[Unset, int] = 3,
) -> Optional[ReservedValue]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReservedValue
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            expiration=expiration,
        )
    ).parsed
