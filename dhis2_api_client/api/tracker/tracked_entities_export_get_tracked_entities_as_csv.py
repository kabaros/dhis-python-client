from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.end_date_time import EndDateTime
from ...models.order_criteria import OrderCriteria
from ...models.start_date_time import StartDateTime
from ...models.tracked_entities_export_get_tracked_entities_as_csv_assigned_user_mode import (
    TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode,
)
from ...models.tracked_entities_export_get_tracked_entities_as_csv_event_status import (
    TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus,
)
from ...models.tracked_entities_export_get_tracked_entities_as_csv_org_unit_mode import (
    TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode,
)
from ...models.tracked_entities_export_get_tracked_entities_as_csv_ou_mode import (
    TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode,
)
from ...models.tracked_entities_export_get_tracked_entities_as_csv_program_status import (
    TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assigned_user: Union[Unset, list[str]] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute: Union[Unset, str] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    event_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entities: Union[Unset, list[str]] = UNSET,
    tracked_entity: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
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

    params["attribute"] = attribute

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

    json_event_occurred_after: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(event_occurred_after, Unset):
        json_event_occurred_after = event_occurred_after.to_dict()
    if not isinstance(json_event_occurred_after, Unset):
        params.update(json_event_occurred_after)

    json_event_occurred_before: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(event_occurred_before, Unset):
        json_event_occurred_before = event_occurred_before.to_dict()
    if not isinstance(json_event_occurred_before, Unset):
        params.update(json_event_occurred_before)

    json_event_status: Union[Unset, str] = UNSET
    if not isinstance(event_status, Unset):
        json_event_status = event_status.value

    params["eventStatus"] = json_event_status

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["filter"] = filter_

    params["followUp"] = follow_up

    params["includeAllAttributes"] = include_all_attributes

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

    params["potentialDuplicate"] = potential_duplicate

    params["program"] = program

    params["programStage"] = program_stage

    json_program_status: Union[Unset, str] = UNSET
    if not isinstance(program_status, Unset):
        json_program_status = program_status.value

    params["programStatus"] = json_program_status

    params["query"] = query

    params["skipHeader"] = skip_header

    params["skipPaging"] = skip_paging

    params["totalPages"] = total_pages

    json_tracked_entities: Union[Unset, list[str]] = UNSET
    if not isinstance(tracked_entities, Unset):
        json_tracked_entities = tracked_entities

    params["trackedEntities"] = json_tracked_entities

    json_tracked_entity: Union[Unset, list[str]] = UNSET
    if not isinstance(tracked_entity, Unset):
        json_tracked_entity = tracked_entity

    params["trackedEntity"] = json_tracked_entity

    params["trackedEntityType"] = tracked_entity_type

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
        "url": "/tracker/trackedEntities/#getTrackedEntitiesAsCsv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WebMessage]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.text)

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.text)

        return response_403
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.text)

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, WebMessage]]:
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
    assigned_user_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute: Union[Unset, str] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    event_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entities: Union[Unset, list[str]] = UNSET,
    tracked_entity: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_before: Union[Unset, "EndDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, list[str]]):
        assigned_user_mode (Union[Unset,
            TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attribute (Union[Unset, str]):
        enrollment_enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        event_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus]):
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_stage (Union[Unset, str]): A UID for an ProgramStage object
            (Java name `org.hisp.dhis.program.ProgramStage`) Example: uf8uS7d0KE2.
        program_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus]):
        query (Union[Unset, str]):
        skip_header (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entities (Union[Unset, list[str]]):
        tracked_entity (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attribute=attribute,
        enrollment_enrolled_after=enrollment_enrolled_after,
        enrollment_enrolled_before=enrollment_enrolled_before,
        enrollment_occurred_after=enrollment_occurred_after,
        enrollment_occurred_before=enrollment_occurred_before,
        event_occurred_after=event_occurred_after,
        event_occurred_before=event_occurred_before,
        event_status=event_status,
        fields=fields,
        filter_=filter_,
        follow_up=follow_up,
        include_all_attributes=include_all_attributes,
        include_deleted=include_deleted,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        org_units=org_units,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        potential_duplicate=potential_duplicate,
        program=program,
        program_stage=program_stage,
        program_status=program_status,
        query=query,
        skip_header=skip_header,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entities=tracked_entities,
        tracked_entity=tracked_entity,
        tracked_entity_type=tracked_entity_type,
        updated_after=updated_after,
        updated_before=updated_before,
        updated_within=updated_within,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, list[str]] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute: Union[Unset, str] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    event_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entities: Union[Unset, list[str]] = UNSET,
    tracked_entity: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_before: Union[Unset, "EndDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, list[str]]):
        assigned_user_mode (Union[Unset,
            TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attribute (Union[Unset, str]):
        enrollment_enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        event_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus]):
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_stage (Union[Unset, str]): A UID for an ProgramStage object
            (Java name `org.hisp.dhis.program.ProgramStage`) Example: uf8uS7d0KE2.
        program_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus]):
        query (Union[Unset, str]):
        skip_header (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entities (Union[Unset, list[str]]):
        tracked_entity (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return sync_detailed(
        client=client,
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attribute=attribute,
        enrollment_enrolled_after=enrollment_enrolled_after,
        enrollment_enrolled_before=enrollment_enrolled_before,
        enrollment_occurred_after=enrollment_occurred_after,
        enrollment_occurred_before=enrollment_occurred_before,
        event_occurred_after=event_occurred_after,
        event_occurred_before=event_occurred_before,
        event_status=event_status,
        fields=fields,
        filter_=filter_,
        follow_up=follow_up,
        include_all_attributes=include_all_attributes,
        include_deleted=include_deleted,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        org_units=org_units,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        potential_duplicate=potential_duplicate,
        program=program,
        program_stage=program_stage,
        program_status=program_status,
        query=query,
        skip_header=skip_header,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entities=tracked_entities,
        tracked_entity=tracked_entity,
        tracked_entity_type=tracked_entity_type,
        updated_after=updated_after,
        updated_before=updated_before,
        updated_within=updated_within,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, list[str]] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute: Union[Unset, str] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    event_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entities: Union[Unset, list[str]] = UNSET,
    tracked_entity: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_before: Union[Unset, "EndDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, list[str]]):
        assigned_user_mode (Union[Unset,
            TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attribute (Union[Unset, str]):
        enrollment_enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        event_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus]):
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_stage (Union[Unset, str]): A UID for an ProgramStage object
            (Java name `org.hisp.dhis.program.ProgramStage`) Example: uf8uS7d0KE2.
        program_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus]):
        query (Union[Unset, str]):
        skip_header (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entities (Union[Unset, list[str]]):
        tracked_entity (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attribute=attribute,
        enrollment_enrolled_after=enrollment_enrolled_after,
        enrollment_enrolled_before=enrollment_enrolled_before,
        enrollment_occurred_after=enrollment_occurred_after,
        enrollment_occurred_before=enrollment_occurred_before,
        event_occurred_after=event_occurred_after,
        event_occurred_before=event_occurred_before,
        event_status=event_status,
        fields=fields,
        filter_=filter_,
        follow_up=follow_up,
        include_all_attributes=include_all_attributes,
        include_deleted=include_deleted,
        order=order,
        org_unit=org_unit,
        org_unit_mode=org_unit_mode,
        org_units=org_units,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        potential_duplicate=potential_duplicate,
        program=program,
        program_stage=program_stage,
        program_status=program_status,
        query=query,
        skip_header=skip_header,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entities=tracked_entities,
        tracked_entity=tracked_entity,
        tracked_entity_type=tracked_entity_type,
        updated_after=updated_after,
        updated_before=updated_before,
        updated_within=updated_within,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, list[str]] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attribute: Union[Unset, str] = UNSET,
    enrollment_enrolled_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_enrolled_before: Union[Unset, "EndDateTime"] = UNSET,
    enrollment_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    enrollment_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_occurred_after: Union[Unset, "StartDateTime"] = UNSET,
    event_occurred_before: Union[Unset, "EndDateTime"] = UNSET,
    event_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_status: Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_header: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    tracked_entities: Union[Unset, list[str]] = UNSET,
    tracked_entity: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, "StartDateTime"] = UNSET,
    updated_before: Union[Unset, "EndDateTime"] = UNSET,
    updated_within: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, list[str]]):
        assigned_user_mode (Union[Unset,
            TrackedEntitiesExportGetTrackedEntitiesAsCsvAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attribute (Union[Unset, str]):
        enrollment_enrolled_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_enrolled_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        enrollment_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        enrollment_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_occurred_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        event_occurred_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        event_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvEventStatus]):
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        order (Union[Unset, list['OrderCriteria']]):
        org_unit (Union[Unset, list[str]]):
        org_unit_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOrgUnitMode]):
        org_units (Union[Unset, list[str]]):
        ou_mode (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.
        program_stage (Union[Unset, str]): A UID for an ProgramStage object
            (Java name `org.hisp.dhis.program.ProgramStage`) Example: uf8uS7d0KE2.
        program_status (Union[Unset, TrackedEntitiesExportGetTrackedEntitiesAsCsvProgramStatus]):
        query (Union[Unset, str]):
        skip_header (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        tracked_entities (Union[Unset, list[str]]):
        tracked_entity (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]): A UID for an TrackedEntityType object
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`) Example: Dk3vQ29RJ44.
        updated_after (Union[Unset, StartDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.StartDateTime`)
        updated_before (Union[Unset, EndDateTime]): The actual type is unknown.
            (Java type was: `class org.hisp.dhis.webapi.webdomain.EndDateTime`)
        updated_within (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            assigned_user=assigned_user,
            assigned_user_mode=assigned_user_mode,
            assigned_users=assigned_users,
            attribute=attribute,
            enrollment_enrolled_after=enrollment_enrolled_after,
            enrollment_enrolled_before=enrollment_enrolled_before,
            enrollment_occurred_after=enrollment_occurred_after,
            enrollment_occurred_before=enrollment_occurred_before,
            event_occurred_after=event_occurred_after,
            event_occurred_before=event_occurred_before,
            event_status=event_status,
            fields=fields,
            filter_=filter_,
            follow_up=follow_up,
            include_all_attributes=include_all_attributes,
            include_deleted=include_deleted,
            order=order,
            org_unit=org_unit,
            org_unit_mode=org_unit_mode,
            org_units=org_units,
            ou_mode=ou_mode,
            page=page,
            page_size=page_size,
            paging=paging,
            potential_duplicate=potential_duplicate,
            program=program,
            program_stage=program_stage,
            program_status=program_status,
            query=query,
            skip_header=skip_header,
            skip_paging=skip_paging,
            total_pages=total_pages,
            tracked_entities=tracked_entities,
            tracked_entity=tracked_entity,
            tracked_entity_type=tracked_entity_type,
            updated_after=updated_after,
            updated_before=updated_before,
            updated_within=updated_within,
        )
    ).parsed
