import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enrollment_get_enrollments_ou_mode import EnrollmentGetEnrollmentsOuMode
from ...models.enrollment_get_enrollments_program_status import EnrollmentGetEnrollmentsProgramStatus
from ...models.enrollment_get_enrollments_response_200 import EnrollmentGetEnrollmentsResponse200
from ...models.order_criteria import OrderCriteria
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enrollment: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, EnrollmentGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["enrollment"] = enrollment

    params["followUp"] = follow_up

    params["includeDeleted"] = include_deleted

    json_last_updated: Union[Unset, str] = UNSET
    if not isinstance(last_updated, Unset):
        json_last_updated = last_updated.isoformat()
    params["lastUpdated"] = json_last_updated

    params["lastUpdatedDuration"] = last_updated_duration

    json_order: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["order"] = json_order

    params["ou"] = ou

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    params["page"] = page

    params["pageSize"] = page_size

    params["pageSizeWithDefault"] = page_size_with_default

    params["pageWithDefault"] = page_with_default

    params["paging"] = paging

    params["program"] = program

    json_program_end_date: Union[Unset, str] = UNSET
    if not isinstance(program_end_date, Unset):
        json_program_end_date = program_end_date.isoformat()
    params["programEndDate"] = json_program_end_date

    json_program_start_date: Union[Unset, str] = UNSET
    if not isinstance(program_start_date, Unset):
        json_program_start_date = program_start_date.isoformat()
    params["programStartDate"] = json_program_start_date

    json_program_status: Union[Unset, str] = UNSET
    if not isinstance(program_status, Unset):
        json_program_status = program_status.value

    params["programStatus"] = json_program_status

    params["skipPaging"] = skip_paging

    params["totalPages"] = total_pages

    params["trackedEntityInstance"] = tracked_entity_instance

    params["trackedEntityType"] = tracked_entity_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/enrollments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = EnrollmentGetEnrollmentsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]:
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
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, EnrollmentGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Response[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        order (Union[Unset, list['OrderCriteria']]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentGetEnrollmentsOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        paging (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset, EnrollmentGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        follow_up=follow_up,
        include_deleted=include_deleted,
        last_updated=last_updated,
        last_updated_duration=last_updated_duration,
        order=order,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        paging=paging,
        program=program,
        program_end_date=program_end_date,
        program_start_date=program_start_date,
        program_status=program_status,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity_instance=tracked_entity_instance,
        tracked_entity_type=tracked_entity_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, EnrollmentGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Optional[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        order (Union[Unset, list['OrderCriteria']]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentGetEnrollmentsOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        paging (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset, EnrollmentGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnrollmentGetEnrollmentsResponse200, WebMessage]
    """

    return sync_detailed(
        client=client,
        enrollment=enrollment,
        follow_up=follow_up,
        include_deleted=include_deleted,
        last_updated=last_updated,
        last_updated_duration=last_updated_duration,
        order=order,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        paging=paging,
        program=program,
        program_end_date=program_end_date,
        program_start_date=program_start_date,
        program_status=program_status,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity_instance=tracked_entity_instance,
        tracked_entity_type=tracked_entity_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, EnrollmentGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Response[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        order (Union[Unset, list['OrderCriteria']]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentGetEnrollmentsOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        paging (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset, EnrollmentGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        follow_up=follow_up,
        include_deleted=include_deleted,
        last_updated=last_updated,
        last_updated_duration=last_updated_duration,
        order=order,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        paging=paging,
        program=program,
        program_end_date=program_end_date,
        program_start_date=program_start_date,
        program_status=program_status,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity_instance=tracked_entity_instance,
        tracked_entity_type=tracked_entity_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, EnrollmentGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Optional[Union[EnrollmentGetEnrollmentsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        order (Union[Unset, list['OrderCriteria']]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentGetEnrollmentsOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        paging (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset, EnrollmentGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EnrollmentGetEnrollmentsResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            enrollment=enrollment,
            follow_up=follow_up,
            include_deleted=include_deleted,
            last_updated=last_updated,
            last_updated_duration=last_updated_duration,
            order=order,
            ou=ou,
            ou_mode=ou_mode,
            page=page,
            page_size=page_size,
            page_size_with_default=page_size_with_default,
            page_with_default=page_with_default,
            paging=paging,
            program=program,
            program_end_date=program_end_date,
            program_start_date=program_start_date,
            program_status=program_status,
            skip_paging=skip_paging,
            total_pages=total_pages,
            tracked_entity_instance=tracked_entity_instance,
            tracked_entity_type=tracked_entity_type,
        )
    ).parsed
