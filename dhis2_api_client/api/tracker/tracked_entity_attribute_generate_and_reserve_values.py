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
    expiration: Union[Unset, int] = 60,
    number_to_reserve: Union[Unset, int] = 1,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["expiration"] = expiration

    params["numberToReserve"] = number_to_reserve

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/trackedEntityAttributes/{id}/generateAndReserve",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ReservedValue"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ReservedValue.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ReservedValue"]]:
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
    expiration: Union[Unset, int] = 60,
    number_to_reserve: Union[Unset, int] = 1,
) -> Response[list["ReservedValue"]]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 60.
        number_to_reserve (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ReservedValue']]
    """

    kwargs = _get_kwargs(
        id=id,
        expiration=expiration,
        number_to_reserve=number_to_reserve,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expiration: Union[Unset, int] = 60,
    number_to_reserve: Union[Unset, int] = 1,
) -> Optional[list["ReservedValue"]]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 60.
        number_to_reserve (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ReservedValue']
    """

    return sync_detailed(
        id=id,
        client=client,
        expiration=expiration,
        number_to_reserve=number_to_reserve,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expiration: Union[Unset, int] = 60,
    number_to_reserve: Union[Unset, int] = 1,
) -> Response[list["ReservedValue"]]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 60.
        number_to_reserve (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ReservedValue']]
    """

    kwargs = _get_kwargs(
        id=id,
        expiration=expiration,
        number_to_reserve=number_to_reserve,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    expiration: Union[Unset, int] = 60,
    number_to_reserve: Union[Unset, int] = 1,
) -> Optional[list["ReservedValue"]]:
    """[no description yet]

    Args:
        id (str):
        expiration (Union[Unset, int]):  Default: 60.
        number_to_reserve (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ReservedValue']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            expiration=expiration,
            number_to_reserve=number_to_reserve,
        )
    ).parsed
