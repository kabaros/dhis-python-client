from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.end_date_time import EndDateTime
from ...models.events_export_get_events_as_csv_zip_assigned_user_mode import (
    EventsExportGetEventsAsCsvZipAssignedUserMode,
)
from ...models.events_export_get_events_as_csv_zip_org_unit_mode import EventsExportGetEventsAsCsvZipOrgUnitMode
from ...models.events_export_get_events_as_csv_zip_ou_mode import EventsExportGetEventsAsCsvZipOuMode
from ...models.events_export_get_events_as_csv_zip_program_status import EventsExportGetEventsAsCsvZipProgramStatus
from ...models.events_export_get_events_as_csv_zip_status import EventsExportGetEventsAsCsvZipStatus
from ...models.order_criteria import OrderCriteria
from ...models.start_date_time import StartDateTime
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assigned_user: Union[Unset, list[str]] = UNSET,
    assigned_user_mode: Union[Unset, EventsExportGetEventsAsCsvZipAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute_category_combo: Union[Unset, str] = UNSET,
    attribute_category_options: Union[Unset, list[str]] = UNSET,
    attribute_cc: Union[Unset, str] = UNSET,
    attribute_cos: Union[Unset, list[str]] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    event: Union[Unset, list[str]] = UNSET,
    events: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_attributes: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, str] = UNSET,
    org_unit_mode: Union[Unset, EventsExportGetEventsAsCsvZipOrgUnitMode] = UNSET,
    ou_mode: Union[Unset, EventsExportGetEventsAsCsvZipOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EventsExportGetEventsAsCsvZipProgramStatus] = UNSET,
    scheduled_after: Union[Unset, "StartDateTime"] = UNSET,
    scheduled_before: Union[Unset, "EndDateTime"] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    status: Union[Unset, EventsExportGetEventsAsCsvZipStatus] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_before: Union[Unset, "EndDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_assigned_user: Union[Unset, list[str]] = UNSET
    if not isinstance(assigned_user, Unset):
        json_assigned_user = assigned_user

    params["assignedUser"] = json_assigned_user

    json_assigned_user_mode: Union[Unset, str] = UNSET
    if not isinstance(assigned_user_mode, Unset):
        json_assigned_user_mode = assigned_user_mode.value

    params["assignedUserMode"] = json_assigned_user_mode

    json_assigned_users: Union[Unset, list[str]] = UNSET
    if not isinstance(assigned_users, Unset):
        json_assigned_users = assigned_users

    params["assignedUsers"] = json_assigned_users

    params["attributeCategoryCombo"] = attribute_category_combo

    json_attribute_category_options: Union[Unset, list[str]] = UNSET
    if not isinstance(attribute_category_options, Unset):
        json_attribute_category_options = attribute_category_options

    params["attributeCategoryOptions"] = json_attribute_category_options

    params["attributeCc"] = attribute_cc

    json_attribute_cos: Union[Unset, list[str]] = UNSET
    if not isinstance(attribute_cos, Unset):
        json_attribute_cos = attribute_cos

    params["attributeCos"] = json_attribute_cos

    json_enrollment_enrolled_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(enrollment_enrolled_after, Unset):
        json_enrollment_enrolled_after = enrollment_enrolled_after.to_dict()
    if not isinstance(json_enrollment_enrolled_after, Unset):
        params.update(json_enrollment_enrolled_after)

    json_enrollment_enrolled_before: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(enrollment_enrolled_before, Unset):
        json_enrollment_enrolled_before = enrollment_enrolled_before.to_dict()
    if not isinstance(json_enrollment_enrolled_before, Unset):
        params.update(json_enrollment_enrolled_before)

    json_enrollment_occurred_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(enrollment_occurred_after, Unset):
        json_enrollment_occurred_after = enrollment_occurred_after.to_dict()
    if not isinstance(json_enrollment_occurred_after, Unset):
        params.update(json_enrollment_occurred_after)

    json_enrollment_occurred_before: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(enrollment_occurred_before, Unset):
        json_enrollment_occurred_before = enrollment_occurred_before.to_dict()
    if not isinstance(json_enrollment_occurred_before, Unset):
        params.update(json_enrollment_occurred_before)

    json_enrollments: Union[Unset, list[str]] = UNSET
    if not isinstance(enrollments, Unset):
        json_enrollments = enrollments

    params["enrollments"] = json_enrollments

    json_event: Union[Unset, list[str]] = UNSET
    if not isinstance(event, Unset):
        json_event = event

    params["event"] = json_event

    json_events: Union[Unset, list[str]] = UNSET
    if not isinstance(events, Unset):
        json_events = events

    params["events"] = json_events

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["filter"] = filter_

    params["filterAttributes"] = filter_attributes

    params["followUp"] = follow_up

    params["includeDeleted"] = include_deleted

    json_occurred_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(occurred_after, Unset):
        json_occurred_after = occurred_after.to_dict()
    if not isinstance(json_occurred_after, Unset):
        params.update(json_occurred_after)

    json_occurred_before: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(occurred_before, Unset):
        json_occurred_before = occurred_before.to_dict()
    if not isinstance(json_occurred_before, Unset):
        params.update(json_occurred_before)

    json_order: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["order"] = json_order

    params["orgUnit"] = org_unit

    json_org_unit_mode: Union[Unset, str] = UNSET
    if not isinstance(org_unit_mode, Unset):
        json_org_unit_mode = org_unit_mode.value

    params["orgUnitMode"] = json_org_unit_mode

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["program"] = program

    params["programStage"] = program_stage

    json_program_status: Union[Unset, str] = UNSET
    if not isinstance(program_status, Unset):
        json_program_status = program_status.value

    params["programStatus"] = json_program_status

    json_scheduled_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(scheduled_after, Unset):
        json_scheduled_after = scheduled_after.to_dict()
    if not isinstance(json_scheduled_after, Unset):
        params.update(json_scheduled_after)

    json_scheduled_before: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(scheduled_before, Unset):
        json_scheduled_before = scheduled_before.to_dict()
    if not isinstance(json_scheduled_before, Unset):
        params.update(json_scheduled_before)

    params["skipHeader"] = skip_header

    params["skipPaging"] = skip_paging

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["totalPages"] = total_pages

    params["trackedEntity"] = tracked_entity

    json_updated_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(updated_after, Unset):
        json_updated_after = updated_after.to_dict()
    if not isinstance(json_updated_after, Unset):
        params.update(json_updated_after)

    json_updated_before: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(updated_before, Unset):
        json_updated_before = updated_before.to_dict()
    if not isinstance(json_updated_before, Unset):
        params.update(json_updated_before)

    params["updatedWithin"] = updated_within

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tracker/events/#getEventsAsCsvZip",
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
    assigned_user: Union[Unset, list[str]] = UNSET,
    assigned_user_mode: Union[Unset, EventsExportGetEventsAsCsvZipAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute_category_combo: Union[Unset, str] = UNSET,
    attribute_category_options: Union[Unset, list[str]] = UNSET,
    attribute_cc: Union[Unset, str] = UNSET,
    attribute_cos: Union[Unset, list[str]] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    event: Union[Unset, list[str]] = UNSET,
    events: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_attributes: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, str] = UNSET,
    org_unit_mode: Union[Unset, EventsExportGetEventsAsCsvZipOrgUnitMode] = UNSET,
    ou_mode: Union[Unset, EventsExportGetEventsAsCsvZipOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EventsExportGetEventsAsCsvZipProgramStatus] = UNSET,
    scheduled_after: Union[Unset, "StartDateTime"] = UNSET,
    scheduled_before: Union[Unset, "EndDateTime"] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    status: Union[Unset, EventsExportGetEventsAsCsvZipStatus] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_before: Union[Unset, "EndDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, list[str]]):
        assigned_user_mode (Union[Unset, EventsExportGetEventsAsCsvZipAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attribute_category_combo (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        attribute_category_options (Union[Unset, list[str]]):
        attribute_cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        attribute_cos (Union[Unset, list[str]]):
        enrollment_enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollments (Union[Unset, list[str]]):
        event (Union[Unset, list[str]]):
        events (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        filter_attributes (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        org_unit_mode (Union[Unset, EventsExportGetEventsAsCsvZipOrgUnitMode]):
        ou_mode (Union[Unset, EventsExportGetEventsAsCsvZipOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_stage (Union[Unset, str]): A UID for an ProgramStage object
            (Java name `org.hisp.dhis.program.ProgramStage`) Example: uf8uS7d0KE2.
        program_status (Union[Unset, EventsExportGetEventsAsCsvZipProgramStatus]):
        scheduled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        scheduled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        skip_header (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):  Default: False.
        status (Union[Unset, EventsExportGetEventsAsCsvZipStatus]):
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attribute_category_combo=attribute_category_combo,
        attribute_category_options=attribute_category_options,
        attribute_cc=attribute_cc,
        attribute_cos=attribute_cos,
        enrollment_enrolled_after=enrollment_enrolled_after,
        enrollment_enrolled_before=enrollment_enrolled_before,
        enrollment_occurred_after=enrollment_occurred_after,
        enrollment_occurred_before=enrollment_occurred_before,
        enrollments=enrollments,
        event=event,
        events=events,
        fields=fields,
        filter_=filter_,
        filter_attributes=filter_attributes,
        follow_up=follow_up,
        include_deleted=include_deleted,
        occurred_after=occurred_after,
        occurred_before=occurred_before,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        program=program,
        program_stage=program_stage,
        program_status=program_status,
        scheduled_after=scheduled_after,
        scheduled_before=scheduled_before,
        skip_header=skip_header,
        skip_paging=skip_paging,
        status=status,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        updated_after=updated_after,
        updated_before=updated_before,
        updated_within=updated_within,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, list[str]] = UNSET,
    assigned_user_mode: Union[Unset, EventsExportGetEventsAsCsvZipAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute_category_combo: Union[Unset, str] = UNSET,
    attribute_category_options: Union[Unset, list[str]] = UNSET,
    attribute_cc: Union[Unset, str] = UNSET,
    attribute_cos: Union[Unset, list[str]] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollments: Union[Unset, list[str]] = UNSET,
    event: Union[Unset, list[str]] = UNSET,
    events: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    filter_attributes: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, str] = UNSET,
    org_unit_mode: Union[Unset, EventsExportGetEventsAsCsvZipOrgUnitMode] = UNSET,
    ou_mode: Union[Unset, EventsExportGetEventsAsCsvZipOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, EventsExportGetEventsAsCsvZipProgramStatus] = UNSET,
    scheduled_after: Union[Unset, "StartDateTime"] = UNSET,
    scheduled_before: Union[Unset, "EndDateTime"] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    status: Union[Unset, EventsExportGetEventsAsCsvZipStatus] = UNSET,
    total_pages: Union[Unset, bool] = False,
    tracked_entity: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_before: Union[Unset, "EndDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, list[str]]):
        assigned_user_mode (Union[Unset, EventsExportGetEventsAsCsvZipAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attribute_category_combo (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        attribute_category_options (Union[Unset, list[str]]):
        attribute_cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        attribute_cos (Union[Unset, list[str]]):
        enrollment_enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollments (Union[Unset, list[str]]):
        event (Union[Unset, list[str]]):
        events (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        filter_attributes (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_deleted (Union[Unset, bool]):  Default: False.
        occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        org_unit_mode (Union[Unset, EventsExportGetEventsAsCsvZipOrgUnitMode]):
        ou_mode (Union[Unset, EventsExportGetEventsAsCsvZipOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_stage (Union[Unset, str]): A UID for an ProgramStage object
            (Java name `org.hisp.dhis.program.ProgramStage`) Example: uf8uS7d0KE2.
        program_status (Union[Unset, EventsExportGetEventsAsCsvZipProgramStatus]):
        scheduled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        scheduled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        skip_header (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):  Default: False.
        status (Union[Unset, EventsExportGetEventsAsCsvZipStatus]):
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entity (Union[Unset, str]): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attribute_category_combo=attribute_category_combo,
        attribute_category_options=attribute_category_options,
        attribute_cc=attribute_cc,
        attribute_cos=attribute_cos,
        enrollment_enrolled_after=enrollment_enrolled_after,
        enrollment_enrolled_before=enrollment_enrolled_before,
        enrollment_occurred_after=enrollment_occurred_after,
        enrollment_occurred_before=enrollment_occurred_before,
        enrollments=enrollments,
        event=event,
        events=events,
        fields=fields,
        filter_=filter_,
        filter_attributes=filter_attributes,
        follow_up=follow_up,
        include_deleted=include_deleted,
        occurred_after=occurred_after,
        occurred_before=occurred_before,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        program=program,
        program_stage=program_stage,
        program_status=program_status,
        scheduled_after=scheduled_after,
        scheduled_before=scheduled_before,
        skip_header=skip_header,
        skip_paging=skip_paging,
        status=status,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        updated_after=updated_after,
        updated_before=updated_before,
        updated_within=updated_within,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
