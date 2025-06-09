from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_combo_get_object_list_response_200 import CategoryComboGetObjectListResponse200
from ...models.category_combo_get_object_list_root_junction import CategoryComboGetObjectListRootJunction
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, CategoryComboGetObjectListRootJunction] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    json_orders: Union[Unset, list[str]] = UNSET
    if not isinstance(orders, Unset):
        json_orders = orders

    params["orders"] = json_orders

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/categoryCombos/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CategoryComboGetObjectListResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = CategoryComboGetObjectListResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CategoryComboGetObjectListResponse200, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, CategoryComboGetObjectListRootJunction] = UNSET,
) -> Response[Union[CategoryComboGetObjectListResponse200, WebMessage]]:
    """List all CategoryCombos

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, CategoryComboGetObjectListRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CategoryComboGetObjectListResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        filter_=filter_,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, CategoryComboGetObjectListRootJunction] = UNSET,
) -> Optional[Union[CategoryComboGetObjectListResponse200, WebMessage]]:
    """List all CategoryCombos

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, CategoryComboGetObjectListRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CategoryComboGetObjectListResponse200, WebMessage]
    """

    return sync_detailed(
        client=client,
        fields=fields,
        filter_=filter_,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, CategoryComboGetObjectListRootJunction] = UNSET,
) -> Response[Union[CategoryComboGetObjectListResponse200, WebMessage]]:
    """List all CategoryCombos

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, CategoryComboGetObjectListRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CategoryComboGetObjectListResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        filter_=filter_,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, CategoryComboGetObjectListRootJunction] = UNSET,
) -> Optional[Union[CategoryComboGetObjectListResponse200, WebMessage]]:
    """List all CategoryCombos

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, CategoryComboGetObjectListRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CategoryComboGetObjectListResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            filter_=filter_,
            orders=orders,
            page=page,
            page_size=page_size,
            paging=paging,
            root_junction=root_junction,
        )
    ).parsed
