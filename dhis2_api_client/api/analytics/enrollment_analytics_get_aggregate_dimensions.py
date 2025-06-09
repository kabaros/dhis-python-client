from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_criteria import OrderCriteria
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = True,
    program_id: str,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
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

    json_order: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["order"] = json_order

    params["page"] = page

    params["pageSize"] = page_size

    params["pageSizeWithDefault"] = page_size_with_default

    params["pageWithDefault"] = page_with_default

    params["paging"] = paging

    params["programId"] = program_id

    params["skipPaging"] = skip_paging

    params["totalPages"] = total_pages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics/enrollments/aggregate/dimensions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = True,
    program_id: str,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        paging (Union[Unset, bool]):  Default: True.
        program_id (str):
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fields=fields,
        filter_=filter_,
        order=order,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        paging=paging,
        program_id=program_id,
        skip_paging=skip_paging,
        total_pages=total_pages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = True,
    program_id: str,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        paging (Union[Unset, bool]):  Default: True.
        program_id (str):
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fields=fields,
        filter_=filter_,
        order=order,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        paging=paging,
        program_id=program_id,
        skip_paging=skip_paging,
        total_pages=total_pages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
