import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_criteria import OrderCriteria
from ...models.tracked_entity_instance_get_tracked_entity_instances_assigned_user_mode import (
    TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode,
)
from ...models.tracked_entity_instance_get_tracked_entity_instances_event_status import (
    TrackedEntityInstanceGetTrackedEntityInstancesEventStatus,
)
from ...models.tracked_entity_instance_get_tracked_entity_instances_ou_mode import (
    TrackedEntityInstanceGetTrackedEntityInstancesOuMode,
)
from ...models.tracked_entity_instance_get_tracked_entity_instances_program_status import (
    TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus,
)
from ...models.tracked_entity_instance_get_tracked_entity_instances_response_200 import (
    TrackedEntityInstanceGetTrackedEntityInstancesResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assigned_user: Union[Unset, str] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attachment: Union[Unset, str] = UNSET,
    attribute: Union[Unset, list[str]] = UNSET,
    event_end_date: Union[Unset, datetime.datetime] = UNSET,
    event_start_date: Union[Unset, datetime.datetime] = UNSET,
    event_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, bool] = False,
    include_deleted: Union[Unset, bool] = False,
    last_updated_duration: Union[Unset, str] = UNSET,
    last_updated_end_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_start_date: Union[Unset, datetime.datetime] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_meta: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_instances: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assignedUser"] = assigned_user

    json_assigned_user_mode: Union[Unset, str] = UNSET
    if not isinstance(assigned_user_mode, Unset):
        json_assigned_user_mode = assigned_user_mode.value

    params["assignedUserMode"] = json_assigned_user_mode

    json_assigned_users: Union[Unset, list[str]] = UNSET
    if not isinstance(assigned_users, Unset):
        json_assigned_users = assigned_users

    params["assignedUsers"] = json_assigned_users

    params["attachment"] = attachment

    json_attribute: Union[Unset, list[str]] = UNSET
    if not isinstance(attribute, Unset):
        json_attribute = attribute

    params["attribute"] = json_attribute

    json_event_end_date: Union[Unset, str] = UNSET
    if not isinstance(event_end_date, Unset):
        json_event_end_date = event_end_date.isoformat()
    params["eventEndDate"] = json_event_end_date

    json_event_start_date: Union[Unset, str] = UNSET
    if not isinstance(event_start_date, Unset):
        json_event_start_date = event_start_date.isoformat()
    params["eventStartDate"] = json_event_start_date

    json_event_status: Union[Unset, str] = UNSET
    if not isinstance(event_status, Unset):
        json_event_status = event_status.value

    params["eventStatus"] = json_event_status

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    params["followUp"] = follow_up

    params["includeAllAttributes"] = include_all_attributes

    params["includeDeleted"] = include_deleted

    params["lastUpdatedDuration"] = last_updated_duration

    json_last_updated_end_date: Union[Unset, str] = UNSET
    if not isinstance(last_updated_end_date, Unset):
        json_last_updated_end_date = last_updated_end_date.isoformat()
    params["lastUpdatedEndDate"] = json_last_updated_end_date

    json_last_updated_start_date: Union[Unset, str] = UNSET
    if not isinstance(last_updated_start_date, Unset):
        json_last_updated_start_date = last_updated_start_date.isoformat()
    params["lastUpdatedStartDate"] = json_last_updated_start_date

    json_order: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["order"] = json_order

    json_org_units: Union[Unset, list[str]] = UNSET
    if not isinstance(org_units, Unset):
        json_org_units = org_units

    params["orgUnits"] = json_org_units

    params["ou"] = ou

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    params["page"] = page

    params["pageSize"] = page_size

    params["pageSizeWithDefault"] = page_size_with_default

    params["pageWithDefault"] = page_with_default

    params["potentialDuplicate"] = potential_duplicate

    params["program"] = program

    json_program_end_date: Union[Unset, str] = UNSET
    if not isinstance(program_end_date, Unset):
        json_program_end_date = program_end_date.isoformat()
    params["programEndDate"] = json_program_end_date

    json_program_enrollment_end_date: Union[Unset, str] = UNSET
    if not isinstance(program_enrollment_end_date, Unset):
        json_program_enrollment_end_date = program_enrollment_end_date.isoformat()
    params["programEnrollmentEndDate"] = json_program_enrollment_end_date

    json_program_enrollment_start_date: Union[Unset, str] = UNSET
    if not isinstance(program_enrollment_start_date, Unset):
        json_program_enrollment_start_date = program_enrollment_start_date.isoformat()
    params["programEnrollmentStartDate"] = json_program_enrollment_start_date

    json_program_incident_end_date: Union[Unset, str] = UNSET
    if not isinstance(program_incident_end_date, Unset):
        json_program_incident_end_date = program_incident_end_date.isoformat()
    params["programIncidentEndDate"] = json_program_incident_end_date

    json_program_incident_start_date: Union[Unset, str] = UNSET
    if not isinstance(program_incident_start_date, Unset):
        json_program_incident_start_date = program_incident_start_date.isoformat()
    params["programIncidentStartDate"] = json_program_incident_start_date

    params["programStage"] = program_stage

    json_program_start_date: Union[Unset, str] = UNSET
    if not isinstance(program_start_date, Unset):
        json_program_start_date = program_start_date.isoformat()
    params["programStartDate"] = json_program_start_date

    json_program_status: Union[Unset, str] = UNSET
    if not isinstance(program_status, Unset):
        json_program_status = program_status.value

    params["programStatus"] = json_program_status

    params["query"] = query

    params["skipMeta"] = skip_meta

    params["skipPaging"] = skip_paging

    params["totalPages"] = total_pages

    params["trackedEntity"] = tracked_entity

    params["trackedEntityInstance"] = tracked_entity_instance

    json_tracked_entity_instances: Union[Unset, list[str]] = UNSET
    if not isinstance(tracked_entity_instances, Unset):
        json_tracked_entity_instances = tracked_entity_instances

    params["trackedEntityInstances"] = json_tracked_entity_instances

    params["trackedEntityType"] = tracked_entity_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/trackedEntityInstances/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]:
    if response.status_code == 200:
        response_200 = TrackedEntityInstanceGetTrackedEntityInstancesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, str] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attachment: Union[Unset, str] = UNSET,
    attribute: Union[Unset, list[str]] = UNSET,
    event_end_date: Union[Unset, datetime.datetime] = UNSET,
    event_start_date: Union[Unset, datetime.datetime] = UNSET,
    event_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, bool] = False,
    include_deleted: Union[Unset, bool] = False,
    last_updated_duration: Union[Unset, str] = UNSET,
    last_updated_end_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_start_date: Union[Unset, datetime.datetime] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_meta: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_instances: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Response[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, str]):
        assigned_user_mode (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attachment (Union[Unset, str]):
        attribute (Union[Unset, list[str]]):
        event_end_date (Union[Unset, datetime.datetime]):
        event_start_date (Union[Unset, datetime.datetime]):
        event_status (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus]):
        filter_ (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, bool]):  Default: False.
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated_duration (Union[Unset, str]):
        last_updated_end_date (Union[Unset, datetime.datetime]):
        last_updated_start_date (Union[Unset, datetime.datetime]):
        order (Union[Unset, list['OrderCriteria']]):
        org_units (Union[Unset, list[str]]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_start_date (Union[Unset, datetime.datetime]):
        program_incident_end_date (Union[Unset, datetime.datetime]):
        program_incident_start_date (Union[Unset, datetime.datetime]):
        program_stage (Union[Unset, str]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus]):
        query (Union[Unset, str]):
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_instances (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]
    """

    kwargs = _get_kwargs(
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attachment=attachment,
        attribute=attribute,
        event_end_date=event_end_date,
        event_start_date=event_start_date,
        event_status=event_status,
        filter_=filter_,
        follow_up=follow_up,
        include_all_attributes=include_all_attributes,
        include_deleted=include_deleted,
        last_updated_duration=last_updated_duration,
        last_updated_end_date=last_updated_end_date,
        last_updated_start_date=last_updated_start_date,
        order=order,
        org_units=org_units,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        potential_duplicate=potential_duplicate,
        program=program,
        program_end_date=program_end_date,
        program_enrollment_end_date=program_enrollment_end_date,
        program_enrollment_start_date=program_enrollment_start_date,
        program_incident_end_date=program_incident_end_date,
        program_incident_start_date=program_incident_start_date,
        program_stage=program_stage,
        program_start_date=program_start_date,
        program_status=program_status,
        query=query,
        skip_meta=skip_meta,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        tracked_entity_instance=tracked_entity_instance,
        tracked_entity_instances=tracked_entity_instances,
        tracked_entity_type=tracked_entity_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, str] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attachment: Union[Unset, str] = UNSET,
    attribute: Union[Unset, list[str]] = UNSET,
    event_end_date: Union[Unset, datetime.datetime] = UNSET,
    event_start_date: Union[Unset, datetime.datetime] = UNSET,
    event_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, bool] = False,
    include_deleted: Union[Unset, bool] = False,
    last_updated_duration: Union[Unset, str] = UNSET,
    last_updated_end_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_start_date: Union[Unset, datetime.datetime] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_meta: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_instances: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Optional[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, str]):
        assigned_user_mode (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attachment (Union[Unset, str]):
        attribute (Union[Unset, list[str]]):
        event_end_date (Union[Unset, datetime.datetime]):
        event_start_date (Union[Unset, datetime.datetime]):
        event_status (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus]):
        filter_ (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, bool]):  Default: False.
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated_duration (Union[Unset, str]):
        last_updated_end_date (Union[Unset, datetime.datetime]):
        last_updated_start_date (Union[Unset, datetime.datetime]):
        order (Union[Unset, list['OrderCriteria']]):
        org_units (Union[Unset, list[str]]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_start_date (Union[Unset, datetime.datetime]):
        program_incident_end_date (Union[Unset, datetime.datetime]):
        program_incident_start_date (Union[Unset, datetime.datetime]):
        program_stage (Union[Unset, str]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus]):
        query (Union[Unset, str]):
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_instances (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackedEntityInstanceGetTrackedEntityInstancesResponse200
    """

    return sync_detailed(
        client=client,
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attachment=attachment,
        attribute=attribute,
        event_end_date=event_end_date,
        event_start_date=event_start_date,
        event_status=event_status,
        filter_=filter_,
        follow_up=follow_up,
        include_all_attributes=include_all_attributes,
        include_deleted=include_deleted,
        last_updated_duration=last_updated_duration,
        last_updated_end_date=last_updated_end_date,
        last_updated_start_date=last_updated_start_date,
        order=order,
        org_units=org_units,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        potential_duplicate=potential_duplicate,
        program=program,
        program_end_date=program_end_date,
        program_enrollment_end_date=program_enrollment_end_date,
        program_enrollment_start_date=program_enrollment_start_date,
        program_incident_end_date=program_incident_end_date,
        program_incident_start_date=program_incident_start_date,
        program_stage=program_stage,
        program_start_date=program_start_date,
        program_status=program_status,
        query=query,
        skip_meta=skip_meta,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        tracked_entity_instance=tracked_entity_instance,
        tracked_entity_instances=tracked_entity_instances,
        tracked_entity_type=tracked_entity_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, str] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attachment: Union[Unset, str] = UNSET,
    attribute: Union[Unset, list[str]] = UNSET,
    event_end_date: Union[Unset, datetime.datetime] = UNSET,
    event_start_date: Union[Unset, datetime.datetime] = UNSET,
    event_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, bool] = False,
    include_deleted: Union[Unset, bool] = False,
    last_updated_duration: Union[Unset, str] = UNSET,
    last_updated_end_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_start_date: Union[Unset, datetime.datetime] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_meta: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_instances: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Response[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, str]):
        assigned_user_mode (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attachment (Union[Unset, str]):
        attribute (Union[Unset, list[str]]):
        event_end_date (Union[Unset, datetime.datetime]):
        event_start_date (Union[Unset, datetime.datetime]):
        event_status (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus]):
        filter_ (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, bool]):  Default: False.
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated_duration (Union[Unset, str]):
        last_updated_end_date (Union[Unset, datetime.datetime]):
        last_updated_start_date (Union[Unset, datetime.datetime]):
        order (Union[Unset, list['OrderCriteria']]):
        org_units (Union[Unset, list[str]]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_start_date (Union[Unset, datetime.datetime]):
        program_incident_end_date (Union[Unset, datetime.datetime]):
        program_incident_start_date (Union[Unset, datetime.datetime]):
        program_stage (Union[Unset, str]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus]):
        query (Union[Unset, str]):
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_instances (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]
    """

    kwargs = _get_kwargs(
        assigned_user=assigned_user,
        assigned_user_mode=assigned_user_mode,
        assigned_users=assigned_users,
        attachment=attachment,
        attribute=attribute,
        event_end_date=event_end_date,
        event_start_date=event_start_date,
        event_status=event_status,
        filter_=filter_,
        follow_up=follow_up,
        include_all_attributes=include_all_attributes,
        include_deleted=include_deleted,
        last_updated_duration=last_updated_duration,
        last_updated_end_date=last_updated_end_date,
        last_updated_start_date=last_updated_start_date,
        order=order,
        org_units=org_units,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        page_size_with_default=page_size_with_default,
        page_with_default=page_with_default,
        potential_duplicate=potential_duplicate,
        program=program,
        program_end_date=program_end_date,
        program_enrollment_end_date=program_enrollment_end_date,
        program_enrollment_start_date=program_enrollment_start_date,
        program_incident_end_date=program_incident_end_date,
        program_incident_start_date=program_incident_start_date,
        program_stage=program_stage,
        program_start_date=program_start_date,
        program_status=program_status,
        query=query,
        skip_meta=skip_meta,
        skip_paging=skip_paging,
        total_pages=total_pages,
        tracked_entity=tracked_entity,
        tracked_entity_instance=tracked_entity_instance,
        tracked_entity_instances=tracked_entity_instances,
        tracked_entity_type=tracked_entity_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    assigned_user: Union[Unset, str] = UNSET,
    assigned_user_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode] = UNSET,
    assigned_users: Union[Unset, list[str]] = UNSET,
    attachment: Union[Unset, str] = UNSET,
    attribute: Union[Unset, list[str]] = UNSET,
    event_end_date: Union[Unset, datetime.datetime] = UNSET,
    event_start_date: Union[Unset, datetime.datetime] = UNSET,
    event_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    include_all_attributes: Union[Unset, bool] = False,
    include_deleted: Union[Unset, bool] = False,
    last_updated_duration: Union[Unset, str] = UNSET,
    last_updated_end_date: Union[Unset, datetime.datetime] = UNSET,
    last_updated_start_date: Union[Unset, datetime.datetime] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    org_units: Union[Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    page_size_with_default: Union[Unset, int] = UNSET,
    page_with_default: Union[Unset, int] = UNSET,
    potential_duplicate: Union[Unset, bool] = UNSET,
    program: Union[Unset, str] = UNSET,
    program_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_enrollment_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_end_date: Union[Unset, datetime.datetime] = UNSET,
    program_incident_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_stage: Union[Unset, str] = UNSET,
    program_start_date: Union[Unset, datetime.datetime] = UNSET,
    program_status: Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus] = UNSET,
    query: Union[Unset, str] = UNSET,
    skip_meta: Union[Unset, bool] = False,
    skip_paging: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    tracked_entity: Union[Unset, bool] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
    tracked_entity_instances: Union[Unset, list[str]] = UNSET,
    tracked_entity_type: Union[Unset, str] = UNSET,
) -> Optional[TrackedEntityInstanceGetTrackedEntityInstancesResponse200]:
    """[no description yet]

    Args:
        assigned_user (Union[Unset, str]):
        assigned_user_mode (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesAssignedUserMode]):
        assigned_users (Union[Unset, list[str]]):
        attachment (Union[Unset, str]):
        attribute (Union[Unset, list[str]]):
        event_end_date (Union[Unset, datetime.datetime]):
        event_start_date (Union[Unset, datetime.datetime]):
        event_status (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesEventStatus]):
        filter_ (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        include_all_attributes (Union[Unset, bool]):  Default: False.
        include_deleted (Union[Unset, bool]):  Default: False.
        last_updated_duration (Union[Unset, str]):
        last_updated_end_date (Union[Unset, datetime.datetime]):
        last_updated_start_date (Union[Unset, datetime.datetime]):
        order (Union[Unset, list['OrderCriteria']]):
        org_units (Union[Unset, list[str]]):
        ou (Union[Unset, str]):
        ou_mode (Union[Unset, TrackedEntityInstanceGetTrackedEntityInstancesOuMode]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        page_size_with_default (Union[Unset, int]):
        page_with_default (Union[Unset, int]):
        potential_duplicate (Union[Unset, bool]):
        program (Union[Unset, str]):
        program_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_end_date (Union[Unset, datetime.datetime]):
        program_enrollment_start_date (Union[Unset, datetime.datetime]):
        program_incident_end_date (Union[Unset, datetime.datetime]):
        program_incident_start_date (Union[Unset, datetime.datetime]):
        program_stage (Union[Unset, str]):
        program_start_date (Union[Unset, datetime.datetime]):
        program_status (Union[Unset,
            TrackedEntityInstanceGetTrackedEntityInstancesProgramStatus]):
        query (Union[Unset, str]):
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_paging (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        tracked_entity (Union[Unset, bool]):
        tracked_entity_instance (Union[Unset, str]):
        tracked_entity_instances (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackedEntityInstanceGetTrackedEntityInstancesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            assigned_user=assigned_user,
            assigned_user_mode=assigned_user_mode,
            assigned_users=assigned_users,
            attachment=attachment,
            attribute=attribute,
            event_end_date=event_end_date,
            event_start_date=event_start_date,
            event_status=event_status,
            filter_=filter_,
            follow_up=follow_up,
            include_all_attributes=include_all_attributes,
            include_deleted=include_deleted,
            last_updated_duration=last_updated_duration,
            last_updated_end_date=last_updated_end_date,
            last_updated_start_date=last_updated_start_date,
            order=order,
            org_units=org_units,
            ou=ou,
            ou_mode=ou_mode,
            page=page,
            page_size=page_size,
            page_size_with_default=page_size_with_default,
            page_with_default=page_with_default,
            potential_duplicate=potential_duplicate,
            program=program,
            program_end_date=program_end_date,
            program_enrollment_end_date=program_enrollment_end_date,
            program_enrollment_start_date=program_enrollment_start_date,
            program_incident_end_date=program_incident_end_date,
            program_incident_start_date=program_incident_start_date,
            program_stage=program_stage,
            program_start_date=program_start_date,
            program_status=program_status,
            query=query,
            skip_meta=skip_meta,
            skip_paging=skip_paging,
            total_pages=total_pages,
            tracked_entity=tracked_entity,
            tracked_entity_instance=tracked_entity_instance,
            tracked_entity_instances=tracked_entity_instances,
            tracked_entity_type=tracked_entity_type,
        )
    ).parsed
