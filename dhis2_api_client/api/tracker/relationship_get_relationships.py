from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deprecated_tracker_relationship import DeprecatedTrackerRelationship
from ...models.order_criteria import OrderCriteria
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["enrollment"] = enrollment

    params["event"] = event

    params["includeDeleted"] = include_deleted

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

    params["skipPaging"] = skip_paging

    params["tei"] = tei

    params["totalPages"] = total_pages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/relationships/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["DeprecatedTrackerRelationship"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DeprecatedTrackerRelationship.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["DeprecatedTrackerRelationship"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
) -> Response[list["DeprecatedTrackerRelationship"]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        skip_paging (Union[Unset, bool]):
        tei (Union[Unset, str]):
        total_pages (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DeprecatedTrackerRelationship']]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        event=event,
        include_deleted=include_deleted,
        order=order,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        skip_paging=skip_paging,
        tei=tei,
        total_pages=total_pages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
) -> Optional[list["DeprecatedTrackerRelationship"]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        skip_paging (Union[Unset, bool]):
        tei (Union[Unset, str]):
        total_pages (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DeprecatedTrackerRelationship']
    """

    return sync_detailed(
        client=client,
        enrollment=enrollment,
        event=event,
        include_deleted=include_deleted,
        order=order,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        skip_paging=skip_paging,
        tei=tei,
        total_pages=total_pages,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
) -> Response[list["DeprecatedTrackerRelationship"]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        skip_paging (Union[Unset, bool]):
        tei (Union[Unset, str]):
        total_pages (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DeprecatedTrackerRelationship']]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        event=event,
        include_deleted=include_deleted,
        order=order,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        skip_paging=skip_paging,
        tei=tei,
        total_pages=total_pages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
) -> Optional[list["DeprecatedTrackerRelationship"]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        skip_paging (Union[Unset, bool]):
        tei (Union[Unset, str]):
        total_pages (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DeprecatedTrackerRelationship']
    """

    return (
        await asyncio_detailed(
            client=client,
            enrollment=enrollment,
            event=event,
            include_deleted=include_deleted,
            order=order,
            page=page,
            page_size=page_size,
            page_size_with_default=page_size_with_default,
            page_with_default=page_with_default,
            skip_paging=skip_paging,
            tei=tei,
            total_pages=total_pages,
        )
    ).parsed
