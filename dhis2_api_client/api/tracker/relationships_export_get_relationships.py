from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_criteria import OrderCriteria
from ...models.tracker_page import TrackerPage
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    skip_paging: Union[Unset, bool] = False,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["enrollment"] = enrollment

    params["event"] = event

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

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

    params["paging"] = paging

    params["skipPaging"] = skip_paging

    params["tei"] = tei

    params["totalPages"] = total_pages

    params["trackedEntity"] = tracked_entity

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tracker/relationships/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[TrackerPage, WebMessage]]:
    if response.status_code == 200:
        response_200 = TrackerPage.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[TrackerPage, WebMessage]]:
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
    fields: Union[Unset, list[str]] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    skip_paging: Union[Unset, bool] = False,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
) -> Response[Union[TrackerPage, WebMessage]]:
    """Get relationships matching the given query parameters.

    Exactly one parameter of `trackedEntity` (`tei`), `enrollment` or `event` has to be specified.

    Args:
        enrollment (Union[Unset, str]): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        event (Union[Unset, str]): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list[str]]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        skip_paging (Union[Unset, bool]):  Default: False.
        tei (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TrackerPage, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        event=event,
        fields=fields,
        include_deleted=include_deleted,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        tei=tei,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
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
    fields: Union[Unset, list[str]] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    skip_paging: Union[Unset, bool] = False,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
) -> Optional[Union[TrackerPage, WebMessage]]:
    """Get relationships matching the given query parameters.

    Exactly one parameter of `trackedEntity` (`tei`), `enrollment` or `event` has to be specified.

    Args:
        enrollment (Union[Unset, str]): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        event (Union[Unset, str]): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list[str]]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        skip_paging (Union[Unset, bool]):  Default: False.
        tei (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrackerPage, WebMessage]
    """

    return sync_detailed(
        client=client,
        enrollment=enrollment,
        event=event,
        fields=fields,
        include_deleted=include_deleted,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        tei=tei,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    skip_paging: Union[Unset, bool] = False,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
) -> Response[Union[TrackerPage, WebMessage]]:
    """Get relationships matching the given query parameters.

    Exactly one parameter of `trackedEntity` (`tei`), `enrollment` or `event` has to be specified.

    Args:
        enrollment (Union[Unset, str]): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        event (Union[Unset, str]): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list[str]]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        skip_paging (Union[Unset, bool]):  Default: False.
        tei (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TrackerPage, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        event=event,
        fields=fields,
        include_deleted=include_deleted,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        tei=tei,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    skip_paging: Union[Unset, bool] = False,
    tei: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
) -> Optional[Union[TrackerPage, WebMessage]]:
    """Get relationships matching the given query parameters.

    Exactly one parameter of `trackedEntity` (`tei`), `enrollment` or `event` has to be specified.

    Args:
        enrollment (Union[Unset, str]): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        event (Union[Unset, str]): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list[str]]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        skip_paging (Union[Unset, bool]):  Default: False.
        tei (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrackerPage, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            enrollment=enrollment,
            event=event,
            fields=fields,
            include_deleted=include_deleted,
            order=order,
            page=page,
            page_size=page_size,
            paging=paging,
            skip_paging=skip_paging,
            tei=tei,
            total_pages=total_pages,
            tracked_entity=tracked_entity,
        )
    ).parsed
