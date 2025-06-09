from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dimension_get_items_response_200 import DimensionGetItemsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    orders: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_orders: Union[Unset, list[str]] = UNSET
    if not isinstance(orders, Unset):
        json_orders = orders

    params["orders"] = json_orders

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dimensions/{uid}/items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DimensionGetItemsResponse200]:
    if response.status_code == 200:
        response_200 = DimensionGetItemsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DimensionGetItemsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    orders: Union[Unset, list[str]] = UNSET,
) -> Response[DimensionGetItemsResponse200]:
    """[no description yet]

    Args:
        uid (str):
        orders (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionGetItemsResponse200]
    """

    kwargs = _get_kwargs(
        uid=uid,
        orders=orders,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    orders: Union[Unset, list[str]] = UNSET,
) -> Optional[DimensionGetItemsResponse200]:
    """[no description yet]

    Args:
        uid (str):
        orders (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionGetItemsResponse200
    """

    return sync_detailed(
        uid=uid,
        client=client,
        orders=orders,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    orders: Union[Unset, list[str]] = UNSET,
) -> Response[DimensionGetItemsResponse200]:
    """[no description yet]

    Args:
        uid (str):
        orders (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionGetItemsResponse200]
    """

    kwargs = _get_kwargs(
        uid=uid,
        orders=orders,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    orders: Union[Unset, list[str]] = UNSET,
) -> Optional[DimensionGetItemsResponse200]:
    """[no description yet]

    Args:
        uid (str):
        orders (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionGetItemsResponse200
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            orders=orders,
        )
    ).parsed
