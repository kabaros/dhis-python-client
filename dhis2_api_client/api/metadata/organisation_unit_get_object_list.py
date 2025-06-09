from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organisation_unit_get_object_list_response_200 import OrganisationUnitGetObjectListResponse200
from ...models.organisation_unit_get_object_list_root_junction import OrganisationUnitGetObjectListRootJunction
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    member_collection: Union[Unset, str] = UNSET,
    member_object: Union[Unset, str] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGetObjectListRootJunction] = UNSET,
    within_user_hierarchy: Union[Unset, bool] = UNSET,
    within_user_search_hierarchy: Union[Unset, bool] = UNSET,
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

    params["level"] = level

    params["maxLevel"] = max_level

    params["memberCollection"] = member_collection

    params["memberObject"] = member_object

    json_orders: Union[Unset, list[str]] = UNSET
    if not isinstance(orders, Unset):
        json_orders = orders

    params["orders"] = json_orders

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["query"] = query

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params["withinUserHierarchy"] = within_user_hierarchy

    params["withinUserSearchHierarchy"] = within_user_search_hierarchy

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organisationUnits/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = OrganisationUnitGetObjectListResponse200.from_dict(response.json())

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
) -> Response[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]:
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
    level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    member_collection: Union[Unset, str] = UNSET,
    member_object: Union[Unset, str] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGetObjectListRootJunction] = UNSET,
    within_user_hierarchy: Union[Unset, bool] = UNSET,
    within_user_search_hierarchy: Union[Unset, bool] = UNSET,
) -> Response[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]:
    """List all OrganisationUnits

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        level (Union[Unset, int]):
        max_level (Union[Unset, int]):
        member_collection (Union[Unset, str]):
        member_object (Union[Unset, str]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        query (Union[Unset, str]):
        root_junction (Union[Unset, OrganisationUnitGetObjectListRootJunction]):
        within_user_hierarchy (Union[Unset, bool]):
        within_user_search_hierarchy (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        filter_=filter_,
        level=level,
        max_level=max_level,
        member_collection=member_collection,
        member_object=member_object,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        query=query,
        root_junction=root_junction,
        within_user_hierarchy=within_user_hierarchy,
        within_user_search_hierarchy=within_user_search_hierarchy,
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
    level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    member_collection: Union[Unset, str] = UNSET,
    member_object: Union[Unset, str] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGetObjectListRootJunction] = UNSET,
    within_user_hierarchy: Union[Unset, bool] = UNSET,
    within_user_search_hierarchy: Union[Unset, bool] = UNSET,
) -> Optional[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]:
    """List all OrganisationUnits

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        level (Union[Unset, int]):
        max_level (Union[Unset, int]):
        member_collection (Union[Unset, str]):
        member_object (Union[Unset, str]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        query (Union[Unset, str]):
        root_junction (Union[Unset, OrganisationUnitGetObjectListRootJunction]):
        within_user_hierarchy (Union[Unset, bool]):
        within_user_search_hierarchy (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganisationUnitGetObjectListResponse200, WebMessage]
    """

    return sync_detailed(
        client=client,
        fields=fields,
        filter_=filter_,
        level=level,
        max_level=max_level,
        member_collection=member_collection,
        member_object=member_object,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        query=query,
        root_junction=root_junction,
        within_user_hierarchy=within_user_hierarchy,
        within_user_search_hierarchy=within_user_search_hierarchy,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    member_collection: Union[Unset, str] = UNSET,
    member_object: Union[Unset, str] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGetObjectListRootJunction] = UNSET,
    within_user_hierarchy: Union[Unset, bool] = UNSET,
    within_user_search_hierarchy: Union[Unset, bool] = UNSET,
) -> Response[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]:
    """List all OrganisationUnits

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        level (Union[Unset, int]):
        max_level (Union[Unset, int]):
        member_collection (Union[Unset, str]):
        member_object (Union[Unset, str]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        query (Union[Unset, str]):
        root_junction (Union[Unset, OrganisationUnitGetObjectListRootJunction]):
        within_user_hierarchy (Union[Unset, bool]):
        within_user_search_hierarchy (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        fields=fields,
        filter_=filter_,
        level=level,
        max_level=max_level,
        member_collection=member_collection,
        member_object=member_object,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        query=query,
        root_junction=root_junction,
        within_user_hierarchy=within_user_hierarchy,
        within_user_search_hierarchy=within_user_search_hierarchy,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    level: Union[Unset, int] = UNSET,
    max_level: Union[Unset, int] = UNSET,
    member_collection: Union[Unset, str] = UNSET,
    member_object: Union[Unset, str] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    query: Union[Unset, str] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGetObjectListRootJunction] = UNSET,
    within_user_hierarchy: Union[Unset, bool] = UNSET,
    within_user_search_hierarchy: Union[Unset, bool] = UNSET,
) -> Optional[Union[OrganisationUnitGetObjectListResponse200, WebMessage]]:
    """List all OrganisationUnits

    Args:
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        level (Union[Unset, int]):
        max_level (Union[Unset, int]):
        member_collection (Union[Unset, str]):
        member_object (Union[Unset, str]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        query (Union[Unset, str]):
        root_junction (Union[Unset, OrganisationUnitGetObjectListRootJunction]):
        within_user_hierarchy (Union[Unset, bool]):
        within_user_search_hierarchy (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganisationUnitGetObjectListResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
            filter_=filter_,
            level=level,
            max_level=max_level,
            member_collection=member_collection,
            member_object=member_object,
            orders=orders,
            page=page,
            page_size=page_size,
            paging=paging,
            query=query,
            root_junction=root_junction,
            within_user_hierarchy=within_user_hierarchy,
            within_user_search_hierarchy=within_user_search_hierarchy,
        )
    ).parsed
