from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.end_date_time import EndDateTime
from ...models.enrollments_export_get_enrollments_org_unit_mode import EnrollmentsExportGetEnrollmentsOrgUnitMode
from ...models.enrollments_export_get_enrollments_ou_mode import EnrollmentsExportGetEnrollmentsOuMode
from ...models.enrollments_export_get_enrollments_program_status import EnrollmentsExportGetEnrollmentsProgramStatus
from ...models.order_criteria import OrderCriteria
from ...models.start_date_time import StartDateTime
from ...models.tracker_page import TrackerPage
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment: Union[Unset, list[str]] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_enrolled_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(enrolled_after, Unset):
        json_enrolled_after = enrolled_after.to_dict()
    if not isinstance(json_enrolled_after, Unset):
        params.update(json_enrolled_after)

    json_enrolled_before: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(enrolled_before, Unset):
        json_enrolled_before = enrolled_before.to_dict()
    if not isinstance(json_enrolled_before, Unset):
        params.update(json_enrolled_before)

    json_enrollment: Union[Unset, list[str]] = UNSET
    if not isinstance(enrollment, Unset):
        json_enrollment = enrollment

    params["enrollment"] = json_enrollment

    json_enrollments: Union[Unset, list[str]] = UNSET
    if not isinstance(enrollments, Unset):
        json_enrollments = enrollments

    params["enrollments"] = json_enrollments

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["followUp"] = follow_up

    params["includeDeleted"] = include_deleted

    json_order: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["order"] = json_order

    json_org_unit: Union[Unset, list[str]] = UNSET
    if not isinstance(org_unit, Unset):
        json_org_unit = org_unit

    params["orgUnit"] = json_org_unit

    json_org_unit_mode: Union[Unset, str] = UNSET
    if not isinstance(org_unit_mode, Unset):
        json_org_unit_mode = org_unit_mode.value

    params["orgUnitMode"] = json_org_unit_mode

    json_org_units: Union[Unset, list[str]] = UNSET
    if not isinstance(org_units, Unset):
        json_org_units = org_units

    params["orgUnits"] = json_org_units

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["program"] = program

    json_program_status: Union[Unset, str] = UNSET
    if not isinstance(program_status, Unset):
        json_program_status = program_status.value

    params["programStatus"] = json_program_status

    params["skipPaging"] = skip_paging

    params["totalPages"] = total_pages

    params["trackedEntity"] = tracked_entity

    params["trackedEntityType"] = tracked_entity_type

    json_updated_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.to_dict()
    if not isinstance(json_updated_after, Unset):
        params.update(json_updated_after)

    params["updatedWithin"] = updated_within

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tracker/enrollments/",
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
    enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment: Union[Unset, list[str]] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Response[Union[TrackerPage, WebMessage]]:
    """Get enrollments matching given query parameters.

    Args:
        enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment (Union[Unset, list[str]]):
        enrollments (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_status (Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TrackerPage, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrolled_after=enrolled_after,
        enrolled_before=enrolled_before,
        enrollment=enrollment,
        enrollments=enrollments,
        fields=fields,
        follow_up=follow_up,
        include_deleted=include_deleted,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        org_units=org_units,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        program=program,
        program_status=program_status,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        tracked_entity_type=tracked_entity_type,
        updated_after=updated_after,
        updated_within=updated_within,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment: Union[Unset, list[str]] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Optional[Union[TrackerPage, WebMessage]]:
    """Get enrollments matching given query parameters.

    Args:
        enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment (Union[Unset, list[str]]):
        enrollments (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_status (Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrackerPage, WebMessage]
    """

    return sync_detailed(
        client=client,
        enrolled_after=enrolled_after,
        enrolled_before=enrolled_before,
        enrollment=enrollment,
        enrollments=enrollments,
        fields=fields,
        follow_up=follow_up,
        include_deleted=include_deleted,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        org_units=org_units,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        program=program,
        program_status=program_status,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        tracked_entity_type=tracked_entity_type,
        updated_after=updated_after,
        updated_within=updated_within,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment: Union[Unset, list[str]] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Response[Union[TrackerPage, WebMessage]]:
    """Get enrollments matching given query parameters.

    Args:
        enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment (Union[Unset, list[str]]):
        enrollments (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_status (Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TrackerPage, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrolled_after=enrolled_after,
        enrolled_before=enrolled_before,
        enrollment=enrollment,
        enrollments=enrollments,
        fields=fields,
        follow_up=follow_up,
        include_deleted=include_deleted,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        org_units=org_units,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        program=program,
        program_status=program_status,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        tracked_entity_type=tracked_entity_type,
        updated_after=updated_after,
        updated_within=updated_within,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment: Union[Unset, list[str]] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, EnrollmentsExportGetEnrollmentsOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus] = UNSET,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Optional[Union[TrackerPage, WebMessage]]:
    """Get enrollments matching given query parameters.

    Args:
        enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment (Union[Unset, list[str]]):
        enrollments (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, EnrollmentsExportGetEnrollmentsOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_status (Union[Unset, EnrollmentsExportGetEnrollmentsProgramStatus]):
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrackerPage, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            enrolled_after=enrolled_after,
            enrolled_before=enrolled_before,
            enrollment=enrollment,
            enrollments=enrollments,
            fields=fields,
            follow_up=follow_up,
            include_deleted=include_deleted,
            order=order,
            org_unit=org_unit,
            org_unit_mode=org_unit_mode,
            org_units=org_units,
            ou_mode=ou_mode,
            page=page,
            page_size=page_size,
            paging=paging,
            program=program,
            program_status=program_status,
            skip_paging=skip_paging,
            total_pages=total_pages,
            tracked_entity=tracked_entity,
            tracked_entity_type=tracked_entity_type,
            updated_after=updated_after,
            updated_within=updated_within,
        )
    ).parsed
