import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.field_path import FieldPath
from ...models.icon_get_all_icons_type import IconGetAllIconsType
from ...models.icon_list_response import IconListResponse
from ...models.order_criteria import OrderCriteria
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_end_date: Union[Unset, datetime.datetime] = UNSET,
    created_start_date: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    keys: Union[Unset, list[str]] = UNSET,
    keywords: Union[Unset, list[str]] = UNSET,
    last_updated_end_date: Union[Unset, bool] = UNSET,
    last_updated_start_date: Union[Unset, bool] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    search: Union[Unset, bool] = UNSET,
    type_: Union[Unset, IconGetAllIconsType] = IconGetAllIconsType.ALL,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created_end_date: Union[Unset, str] = UNSET
    if not isinstance(created_end_date, Unset):
        json_created_end_date = created_end_date.isoformat()
    params["createdEndDate"] = json_created_end_date

    json_created_start_date: Union[Unset, str] = UNSET
    if not isinstance(created_start_date, Unset):
        json_created_start_date = created_start_date.isoformat()
    params["createdStartDate"] = json_created_start_date

    json_fields: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.to_dict()
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_keys: Union[Unset, list[str]] = UNSET
    if not isinstance(keys, Unset):
        json_keys = keys

    params["keys"] = json_keys

    json_keywords: Union[Unset, list[str]] = UNSET
    if not isinstance(keywords, Unset):
        json_keywords = keywords

    params["keywords"] = json_keywords

    params["lastUpdatedEndDate"] = last_updated_end_date

    params["lastUpdatedStartDate"] = last_updated_start_date

    json_order: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["order"] = json_order

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["search"] = search

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/icons/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[IconListResponse, WebMessage]]:
    if response.status_code == 200:
        response_200 = IconListResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[IconListResponse, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_end_date: Union[Unset, datetime.datetime] = UNSET,
    created_start_date: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    keys: Union[Unset, list[str]] = UNSET,
    keywords: Union[Unset, list[str]] = UNSET,
    last_updated_end_date: Union[Unset, bool] = UNSET,
    last_updated_start_date: Union[Unset, bool] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    search: Union[Unset, bool] = UNSET,
    type_: Union[Unset, IconGetAllIconsType] = IconGetAllIconsType.ALL,
) -> Response[Union[IconListResponse, WebMessage]]:
    """[no description yet]

    Args:
        created_end_date (Union[Unset, datetime.datetime]):
        created_start_date (Union[Unset, datetime.datetime]):
        fields (Union[Unset, list['FieldPath']]):
        keys (Union[Unset, list[str]]):
        keywords (Union[Unset, list[str]]):
        last_updated_end_date (Union[Unset, bool]):
        last_updated_start_date (Union[Unset, bool]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        search (Union[Unset, bool]):
        type_ (Union[Unset, IconGetAllIconsType]):  Default: IconGetAllIconsType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IconListResponse, WebMessage]]
    """

    kwargs = _get_kwargs(
        created_end_date=created_end_date,
        created_start_date=created_start_date,
        fields=fields,
        keys=keys,
        keywords=keywords,
        last_updated_end_date=last_updated_end_date,
        last_updated_start_date=last_updated_start_date,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        search=search,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    created_end_date: Union[Unset, datetime.datetime] = UNSET,
    created_start_date: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    keys: Union[Unset, list[str]] = UNSET,
    keywords: Union[Unset, list[str]] = UNSET,
    last_updated_end_date: Union[Unset, bool] = UNSET,
    last_updated_start_date: Union[Unset, bool] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    search: Union[Unset, bool] = UNSET,
    type_: Union[Unset, IconGetAllIconsType] = IconGetAllIconsType.ALL,
) -> Optional[Union[IconListResponse, WebMessage]]:
    """[no description yet]

    Args:
        created_end_date (Union[Unset, datetime.datetime]):
        created_start_date (Union[Unset, datetime.datetime]):
        fields (Union[Unset, list['FieldPath']]):
        keys (Union[Unset, list[str]]):
        keywords (Union[Unset, list[str]]):
        last_updated_end_date (Union[Unset, bool]):
        last_updated_start_date (Union[Unset, bool]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        search (Union[Unset, bool]):
        type_ (Union[Unset, IconGetAllIconsType]):  Default: IconGetAllIconsType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IconListResponse, WebMessage]
    """

    return sync_detailed(
        client=client,
        created_end_date=created_end_date,
        created_start_date=created_start_date,
        fields=fields,
        keys=keys,
        keywords=keywords,
        last_updated_end_date=last_updated_end_date,
        last_updated_start_date=last_updated_start_date,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        search=search,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_end_date: Union[Unset, datetime.datetime] = UNSET,
    created_start_date: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    keys: Union[Unset, list[str]] = UNSET,
    keywords: Union[Unset, list[str]] = UNSET,
    last_updated_end_date: Union[Unset, bool] = UNSET,
    last_updated_start_date: Union[Unset, bool] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    search: Union[Unset, bool] = UNSET,
    type_: Union[Unset, IconGetAllIconsType] = IconGetAllIconsType.ALL,
) -> Response[Union[IconListResponse, WebMessage]]:
    """[no description yet]

    Args:
        created_end_date (Union[Unset, datetime.datetime]):
        created_start_date (Union[Unset, datetime.datetime]):
        fields (Union[Unset, list['FieldPath']]):
        keys (Union[Unset, list[str]]):
        keywords (Union[Unset, list[str]]):
        last_updated_end_date (Union[Unset, bool]):
        last_updated_start_date (Union[Unset, bool]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        search (Union[Unset, bool]):
        type_ (Union[Unset, IconGetAllIconsType]):  Default: IconGetAllIconsType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IconListResponse, WebMessage]]
    """

    kwargs = _get_kwargs(
        created_end_date=created_end_date,
        created_start_date=created_start_date,
        fields=fields,
        keys=keys,
        keywords=keywords,
        last_updated_end_date=last_updated_end_date,
        last_updated_start_date=last_updated_start_date,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        search=search,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_end_date: Union[Unset, datetime.datetime] = UNSET,
    created_start_date: Union[Unset, datetime.datetime] = UNSET,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    keys: Union[Unset, list[str]] = UNSET,
    keywords: Union[Unset, list[str]] = UNSET,
    last_updated_end_date: Union[Unset, bool] = UNSET,
    last_updated_start_date: Union[Unset, bool] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    search: Union[Unset, bool] = UNSET,
    type_: Union[Unset, IconGetAllIconsType] = IconGetAllIconsType.ALL,
) -> Optional[Union[IconListResponse, WebMessage]]:
    """[no description yet]

    Args:
        created_end_date (Union[Unset, datetime.datetime]):
        created_start_date (Union[Unset, datetime.datetime]):
        fields (Union[Unset, list['FieldPath']]):
        keys (Union[Unset, list[str]]):
        keywords (Union[Unset, list[str]]):
        last_updated_end_date (Union[Unset, bool]):
        last_updated_start_date (Union[Unset, bool]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        search (Union[Unset, bool]):
        type_ (Union[Unset, IconGetAllIconsType]):  Default: IconGetAllIconsType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[IconListResponse, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            created_end_date=created_end_date,
            created_start_date=created_start_date,
            fields=fields,
            keys=keys,
            keywords=keywords,
            last_updated_end_date=last_updated_end_date,
            last_updated_start_date=last_updated_start_date,
            order=order,
            page=page,
            page_size=page_size,
            paging=paging,
            search=search,
            type_=type_,
        )
    ).parsed
