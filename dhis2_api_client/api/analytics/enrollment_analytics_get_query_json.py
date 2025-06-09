import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enrollment_analytics_get_query_json_data_id_scheme import EnrollmentAnalyticsGetQueryJsonDataIdScheme
from ...models.enrollment_analytics_get_query_json_display_property import (
    EnrollmentAnalyticsGetQueryJsonDisplayProperty,
)
from ...models.enrollment_analytics_get_query_json_endpoint_action import EnrollmentAnalyticsGetQueryJsonEndpointAction
from ...models.enrollment_analytics_get_query_json_endpoint_item import EnrollmentAnalyticsGetQueryJsonEndpointItem
from ...models.enrollment_analytics_get_query_json_ou_mode import EnrollmentAnalyticsGetQueryJsonOuMode
from ...models.enrollment_analytics_get_query_json_output_id_scheme import EnrollmentAnalyticsGetQueryJsonOutputIdScheme
from ...models.enrollment_analytics_get_query_json_program_status_item import (
    EnrollmentAnalyticsGetQueryJsonProgramStatusItem,
)
from ...models.enrollment_analytics_get_query_json_sort_order import EnrollmentAnalyticsGetQueryJsonSortOrder
from ...models.grid import Grid
from ...types import UNSET, Response, Unset


def _get_kwargs(
    program: str,
    *,
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregated_enrollments: Union[Unset, bool] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction
    ] = EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER,
    endpoint_item: Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode] = UNSET,
    output_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aggregateEndpoint"] = aggregate_endpoint

    params["aggregatedEnrollments"] = aggregated_enrollments

    json_asc: Union[Unset, list[str]] = UNSET
    if not isinstance(asc, Unset):
        json_asc = asc

    params["asc"] = json_asc

    params["completedOnly"] = completed_only

    params["coordinateField"] = coordinate_field

    params["coordinatesOnly"] = coordinates_only

    json_data_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(data_id_scheme, Unset):
        json_data_id_scheme = data_id_scheme.value

    params["dataIdScheme"] = json_data_id_scheme

    json_desc: Union[Unset, list[str]] = UNSET
    if not isinstance(desc, Unset):
        json_desc = desc

    params["desc"] = json_desc

    json_dimension: Union[Unset, list[str]] = UNSET
    if not isinstance(dimension, Unset):
        json_dimension = dimension

    params["dimension"] = json_dimension

    json_display_property: Union[Unset, str] = UNSET
    if not isinstance(display_property, Unset):
        json_display_property = display_property.value

    params["displayProperty"] = json_display_property

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_endpoint_action: Union[Unset, str] = UNSET
    if not isinstance(endpoint_action, Unset):
        json_endpoint_action = endpoint_action.value

    params["endpointAction"] = json_endpoint_action

    json_endpoint_item: Union[Unset, str] = UNSET
    if not isinstance(endpoint_item, Unset):
        json_endpoint_item = endpoint_item.value

    params["endpointItem"] = json_endpoint_item

    params["enhancedConditions"] = enhanced_conditions

    params["enrollmentDate"] = enrollment_date

    params["enrollmentEndpointItem"] = enrollment_endpoint_item

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    json_headers: Union[Unset, list[str]] = UNSET
    if not isinstance(headers, Unset):
        json_headers = headers

    params["headers"] = json_headers

    params["hierarchyMeta"] = hierarchy_meta

    params["incidentDate"] = incident_date

    params["includeMetadataDetails"] = include_metadata_details

    params["lastUpdated"] = last_updated

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    json_output_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_id_scheme, Unset):
        json_output_id_scheme = output_id_scheme.value

    params["outputIdScheme"] = json_output_id_scheme

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_program_status: Union[Unset, list[str]] = UNSET
    if not isinstance(program_status, Unset):
        json_program_status = []
        for program_status_item_data in program_status:
            program_status_item = program_status_item_data.value
            json_program_status.append(program_status_item)

    params["programStatus"] = json_program_status

    params["queryEndpoint"] = query_endpoint

    json_relative_period_date: Union[Unset, str] = UNSET
    if not isinstance(relative_period_date, Unset):
        json_relative_period_date = relative_period_date.isoformat()
    params["relativePeriodDate"] = json_relative_period_date

    params["rowContext"] = row_context

    params["showHierarchy"] = show_hierarchy

    params["skipData"] = skip_data

    params["skipMeta"] = skip_meta

    params["skipRounding"] = skip_rounding

    json_sort_order: Union[Unset, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params["timeField"] = time_field

    params["totalPages"] = total_pages

    params["userOrgUnit"] = user_org_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/analytics/enrollments/query/{program}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Grid]:
    if response.status_code == 200:
        response_200 = Grid.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Grid]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    program: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregated_enrollments: Union[Unset, bool] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction
    ] = EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER,
    endpoint_item: Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode] = UNSET,
    output_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Response[Grid]:
    """[no description yet]

    Args:
        program (str):
        aggregate_endpoint (Union[Unset, bool]):
        aggregated_enrollments (Union[Unset, bool]):
        asc (Union[Unset, list[str]]):
        completed_only (Union[Unset, bool]):  Default: False.
        coordinate_field (Union[Unset, str]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        data_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme]):
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        endpoint_action (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction]):  Default:
            EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER.
        endpoint_item (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem]):
        enhanced_conditions (Union[Unset, bool]):  Default: False.
        enrollment_date (Union[Unset, str]):
        enrollment_endpoint_item (Union[Unset, bool]):
        filter_ (Union[Unset, list[str]]):
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, str]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode]):
        output_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program_status (Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]]):
        query_endpoint (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        row_context (Union[Unset, bool]):  Default: False.
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        sort_order (Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder]):
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        total_pages (Union[Unset, bool]):  Default: False.
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Grid]
    """

    kwargs = _get_kwargs(
        program=program,
        aggregate_endpoint=aggregate_endpoint,
        aggregated_enrollments=aggregated_enrollments,
        asc=asc,
        completed_only=completed_only,
        coordinate_field=coordinate_field,
        coordinates_only=coordinates_only,
        data_id_scheme=data_id_scheme,
        desc=desc,
        dimension=dimension,
        display_property=display_property,
        end_date=end_date,
        endpoint_action=endpoint_action,
        endpoint_item=endpoint_item,
        enhanced_conditions=enhanced_conditions,
        enrollment_date=enrollment_date,
        enrollment_endpoint_item=enrollment_endpoint_item,
        filter_=filter_,
        headers=headers,
        hierarchy_meta=hierarchy_meta,
        incident_date=incident_date,
        include_metadata_details=include_metadata_details,
        last_updated=last_updated,
        ou_mode=ou_mode,
        output_id_scheme=output_id_scheme,
        page=page,
        page_size=page_size,
        paging=paging,
        program_status=program_status,
        query_endpoint=query_endpoint,
        relative_period_date=relative_period_date,
        row_context=row_context,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        sort_order=sort_order,
        start_date=start_date,
        time_field=time_field,
        total_pages=total_pages,
        user_org_unit=user_org_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    program: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregated_enrollments: Union[Unset, bool] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction
    ] = EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER,
    endpoint_item: Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode] = UNSET,
    output_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Optional[Grid]:
    """[no description yet]

    Args:
        program (str):
        aggregate_endpoint (Union[Unset, bool]):
        aggregated_enrollments (Union[Unset, bool]):
        asc (Union[Unset, list[str]]):
        completed_only (Union[Unset, bool]):  Default: False.
        coordinate_field (Union[Unset, str]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        data_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme]):
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        endpoint_action (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction]):  Default:
            EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER.
        endpoint_item (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem]):
        enhanced_conditions (Union[Unset, bool]):  Default: False.
        enrollment_date (Union[Unset, str]):
        enrollment_endpoint_item (Union[Unset, bool]):
        filter_ (Union[Unset, list[str]]):
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, str]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode]):
        output_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program_status (Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]]):
        query_endpoint (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        row_context (Union[Unset, bool]):  Default: False.
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        sort_order (Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder]):
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        total_pages (Union[Unset, bool]):  Default: False.
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Grid
    """

    return sync_detailed(
        program=program,
        client=client,
        aggregate_endpoint=aggregate_endpoint,
        aggregated_enrollments=aggregated_enrollments,
        asc=asc,
        completed_only=completed_only,
        coordinate_field=coordinate_field,
        coordinates_only=coordinates_only,
        data_id_scheme=data_id_scheme,
        desc=desc,
        dimension=dimension,
        display_property=display_property,
        end_date=end_date,
        endpoint_action=endpoint_action,
        endpoint_item=endpoint_item,
        enhanced_conditions=enhanced_conditions,
        enrollment_date=enrollment_date,
        enrollment_endpoint_item=enrollment_endpoint_item,
        filter_=filter_,
        headers=headers,
        hierarchy_meta=hierarchy_meta,
        incident_date=incident_date,
        include_metadata_details=include_metadata_details,
        last_updated=last_updated,
        ou_mode=ou_mode,
        output_id_scheme=output_id_scheme,
        page=page,
        page_size=page_size,
        paging=paging,
        program_status=program_status,
        query_endpoint=query_endpoint,
        relative_period_date=relative_period_date,
        row_context=row_context,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        sort_order=sort_order,
        start_date=start_date,
        time_field=time_field,
        total_pages=total_pages,
        user_org_unit=user_org_unit,
    ).parsed


async def asyncio_detailed(
    program: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregated_enrollments: Union[Unset, bool] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction
    ] = EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER,
    endpoint_item: Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode] = UNSET,
    output_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Response[Grid]:
    """[no description yet]

    Args:
        program (str):
        aggregate_endpoint (Union[Unset, bool]):
        aggregated_enrollments (Union[Unset, bool]):
        asc (Union[Unset, list[str]]):
        completed_only (Union[Unset, bool]):  Default: False.
        coordinate_field (Union[Unset, str]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        data_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme]):
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        endpoint_action (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction]):  Default:
            EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER.
        endpoint_item (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem]):
        enhanced_conditions (Union[Unset, bool]):  Default: False.
        enrollment_date (Union[Unset, str]):
        enrollment_endpoint_item (Union[Unset, bool]):
        filter_ (Union[Unset, list[str]]):
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, str]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode]):
        output_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program_status (Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]]):
        query_endpoint (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        row_context (Union[Unset, bool]):  Default: False.
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        sort_order (Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder]):
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        total_pages (Union[Unset, bool]):  Default: False.
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Grid]
    """

    kwargs = _get_kwargs(
        program=program,
        aggregate_endpoint=aggregate_endpoint,
        aggregated_enrollments=aggregated_enrollments,
        asc=asc,
        completed_only=completed_only,
        coordinate_field=coordinate_field,
        coordinates_only=coordinates_only,
        data_id_scheme=data_id_scheme,
        desc=desc,
        dimension=dimension,
        display_property=display_property,
        end_date=end_date,
        endpoint_action=endpoint_action,
        endpoint_item=endpoint_item,
        enhanced_conditions=enhanced_conditions,
        enrollment_date=enrollment_date,
        enrollment_endpoint_item=enrollment_endpoint_item,
        filter_=filter_,
        headers=headers,
        hierarchy_meta=hierarchy_meta,
        incident_date=incident_date,
        include_metadata_details=include_metadata_details,
        last_updated=last_updated,
        ou_mode=ou_mode,
        output_id_scheme=output_id_scheme,
        page=page,
        page_size=page_size,
        paging=paging,
        program_status=program_status,
        query_endpoint=query_endpoint,
        relative_period_date=relative_period_date,
        row_context=row_context,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        sort_order=sort_order,
        start_date=start_date,
        time_field=time_field,
        total_pages=total_pages,
        user_org_unit=user_org_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    program: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregated_enrollments: Union[Unset, bool] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction
    ] = EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER,
    endpoint_item: Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode] = UNSET,
    output_id_scheme: Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Optional[Grid]:
    """[no description yet]

    Args:
        program (str):
        aggregate_endpoint (Union[Unset, bool]):
        aggregated_enrollments (Union[Unset, bool]):
        asc (Union[Unset, list[str]]):
        completed_only (Union[Unset, bool]):  Default: False.
        coordinate_field (Union[Unset, str]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        data_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonDataIdScheme]):
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, EnrollmentAnalyticsGetQueryJsonDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        endpoint_action (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointAction]):  Default:
            EnrollmentAnalyticsGetQueryJsonEndpointAction.OTHER.
        endpoint_item (Union[Unset, EnrollmentAnalyticsGetQueryJsonEndpointItem]):
        enhanced_conditions (Union[Unset, bool]):  Default: False.
        enrollment_date (Union[Unset, str]):
        enrollment_endpoint_item (Union[Unset, bool]):
        filter_ (Union[Unset, list[str]]):
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, str]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, str]):
        ou_mode (Union[Unset, EnrollmentAnalyticsGetQueryJsonOuMode]):
        output_id_scheme (Union[Unset, EnrollmentAnalyticsGetQueryJsonOutputIdScheme]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program_status (Union[Unset, list[EnrollmentAnalyticsGetQueryJsonProgramStatusItem]]):
        query_endpoint (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        row_context (Union[Unset, bool]):  Default: False.
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        sort_order (Union[Unset, EnrollmentAnalyticsGetQueryJsonSortOrder]):
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        total_pages (Union[Unset, bool]):  Default: False.
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Grid
    """

    return (
        await asyncio_detailed(
            program=program,
            client=client,
            aggregate_endpoint=aggregate_endpoint,
            aggregated_enrollments=aggregated_enrollments,
            asc=asc,
            completed_only=completed_only,
            coordinate_field=coordinate_field,
            coordinates_only=coordinates_only,
            data_id_scheme=data_id_scheme,
            desc=desc,
            dimension=dimension,
            display_property=display_property,
            end_date=end_date,
            endpoint_action=endpoint_action,
            endpoint_item=endpoint_item,
            enhanced_conditions=enhanced_conditions,
            enrollment_date=enrollment_date,
            enrollment_endpoint_item=enrollment_endpoint_item,
            filter_=filter_,
            headers=headers,
            hierarchy_meta=hierarchy_meta,
            incident_date=incident_date,
            include_metadata_details=include_metadata_details,
            last_updated=last_updated,
            ou_mode=ou_mode,
            output_id_scheme=output_id_scheme,
            page=page,
            page_size=page_size,
            paging=paging,
            program_status=program_status,
            query_endpoint=query_endpoint,
            relative_period_date=relative_period_date,
            row_context=row_context,
            show_hierarchy=show_hierarchy,
            skip_data=skip_data,
            skip_meta=skip_meta,
            skip_rounding=skip_rounding,
            sort_order=sort_order,
            start_date=start_date,
            time_field=time_field,
            total_pages=total_pages,
            user_org_unit=user_org_unit,
        )
    ).parsed
