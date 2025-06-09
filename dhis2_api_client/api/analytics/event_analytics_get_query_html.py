import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_analytics_get_query_html_aggregation_type import EventAnalyticsGetQueryHtmlAggregationType
from ...models.event_analytics_get_query_html_data_id_scheme import EventAnalyticsGetQueryHtmlDataIdScheme
from ...models.event_analytics_get_query_html_display_property import EventAnalyticsGetQueryHtmlDisplayProperty
from ...models.event_analytics_get_query_html_endpoint_action import EventAnalyticsGetQueryHtmlEndpointAction
from ...models.event_analytics_get_query_html_endpoint_item import EventAnalyticsGetQueryHtmlEndpointItem
from ...models.event_analytics_get_query_html_event_status_item import EventAnalyticsGetQueryHtmlEventStatusItem
from ...models.event_analytics_get_query_html_ou_mode import EventAnalyticsGetQueryHtmlOuMode
from ...models.event_analytics_get_query_html_output_id_scheme import EventAnalyticsGetQueryHtmlOutputIdScheme
from ...models.event_analytics_get_query_html_output_type import EventAnalyticsGetQueryHtmlOutputType
from ...models.event_analytics_get_query_html_program_status_item import EventAnalyticsGetQueryHtmlProgramStatusItem
from ...models.event_analytics_get_query_html_sort_order import EventAnalyticsGetQueryHtmlSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    program: str,
    *,
    aggregate_data: Union[Unset, bool] = False,
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregation_type: Union[Unset, EventAnalyticsGetQueryHtmlAggregationType] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    collapse_data_dimensions: Union[Unset, bool] = False,
    columns: Union[Unset, str] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EventAnalyticsGetQueryHtmlDataIdScheme] = UNSET,
    default_coordinate_fallback: Union[Unset, bool] = False,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EventAnalyticsGetQueryHtmlDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EventAnalyticsGetQueryHtmlEndpointAction
    ] = EventAnalyticsGetQueryHtmlEndpointAction.OTHER,
    endpoint_item: Union[Unset, EventAnalyticsGetQueryHtmlEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    event_date: Union[Unset, str] = UNSET,
    event_status: Union[Unset, list[EventAnalyticsGetQueryHtmlEventStatusItem]] = UNSET,
    fallback_coordinate_field: Union[Unset, str] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit_field: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EventAnalyticsGetQueryHtmlOuMode] = EventAnalyticsGetQueryHtmlOuMode.DESCENDANTS,
    output_id_scheme: Union[Unset, EventAnalyticsGetQueryHtmlOutputIdScheme] = UNSET,
    output_type: Union[Unset, EventAnalyticsGetQueryHtmlOutputType] = EventAnalyticsGetQueryHtmlOutputType.EVENT,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EventAnalyticsGetQueryHtmlProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    rows: Union[Unset, str] = UNSET,
    scheduled_date: Union[Unset, str] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EventAnalyticsGetQueryHtmlSortOrder] = UNSET,
    stage: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = True,
    user_org_unit: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aggregateData"] = aggregate_data

    params["aggregateEndpoint"] = aggregate_endpoint

    json_aggregation_type: Union[Unset, str] = UNSET
    if not isinstance(aggregation_type, Unset):
        json_aggregation_type = aggregation_type.value

    params["aggregationType"] = json_aggregation_type

    json_asc: Union[Unset, list[str]] = UNSET
    if not isinstance(asc, Unset):
        json_asc = asc

    params["asc"] = json_asc

    params["collapseDataDimensions"] = collapse_data_dimensions

    params["columns"] = columns

    params["completedOnly"] = completed_only

    params["coordinateField"] = coordinate_field

    params["coordinatesOnly"] = coordinates_only

    json_data_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(data_id_scheme, Unset):
        json_data_id_scheme = data_id_scheme.value

    params["dataIdScheme"] = json_data_id_scheme

    params["defaultCoordinateFallback"] = default_coordinate_fallback

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

    params["eventDate"] = event_date

    json_event_status: Union[Unset, list[str]] = UNSET
    if not isinstance(event_status, Unset):
        json_event_status = []
        for event_status_item_data in event_status:
            event_status_item = event_status_item_data.value
            json_event_status.append(event_status_item)

    params["eventStatus"] = json_event_status

    params["fallbackCoordinateField"] = fallback_coordinate_field

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

    params["limit"] = limit

    params["orgUnitField"] = org_unit_field

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    json_output_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_id_scheme, Unset):
        json_output_id_scheme = output_id_scheme.value

    params["outputIdScheme"] = json_output_id_scheme

    json_output_type: Union[Unset, str] = UNSET
    if not isinstance(output_type, Unset):
        json_output_type = output_type.value

    params["outputType"] = json_output_type

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

    params["rows"] = rows

    params["scheduledDate"] = scheduled_date

    params["showHierarchy"] = show_hierarchy

    params["skipData"] = skip_data

    params["skipMeta"] = skip_meta

    params["skipRounding"] = skip_rounding

    json_sort_order: Union[Unset, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["stage"] = stage

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params["timeField"] = time_field

    params["totalPages"] = total_pages

    params["userOrgUnit"] = user_org_unit

    params["value"] = value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/analytics/events/query/{program}.html",
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
    program: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregate_data: Union[Unset, bool] = False,
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregation_type: Union[Unset, EventAnalyticsGetQueryHtmlAggregationType] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    collapse_data_dimensions: Union[Unset, bool] = False,
    columns: Union[Unset, str] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EventAnalyticsGetQueryHtmlDataIdScheme] = UNSET,
    default_coordinate_fallback: Union[Unset, bool] = False,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EventAnalyticsGetQueryHtmlDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EventAnalyticsGetQueryHtmlEndpointAction
    ] = EventAnalyticsGetQueryHtmlEndpointAction.OTHER,
    endpoint_item: Union[Unset, EventAnalyticsGetQueryHtmlEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    event_date: Union[Unset, str] = UNSET,
    event_status: Union[Unset, list[EventAnalyticsGetQueryHtmlEventStatusItem]] = UNSET,
    fallback_coordinate_field: Union[Unset, str] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit_field: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EventAnalyticsGetQueryHtmlOuMode] = EventAnalyticsGetQueryHtmlOuMode.DESCENDANTS,
    output_id_scheme: Union[Unset, EventAnalyticsGetQueryHtmlOutputIdScheme] = UNSET,
    output_type: Union[Unset, EventAnalyticsGetQueryHtmlOutputType] = EventAnalyticsGetQueryHtmlOutputType.EVENT,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EventAnalyticsGetQueryHtmlProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    rows: Union[Unset, str] = UNSET,
    scheduled_date: Union[Unset, str] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EventAnalyticsGetQueryHtmlSortOrder] = UNSET,
    stage: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = True,
    user_org_unit: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        program (str):
        aggregate_data (Union[Unset, bool]):  Default: False.
        aggregate_endpoint (Union[Unset, bool]):
        aggregation_type (Union[Unset, EventAnalyticsGetQueryHtmlAggregationType]):
        asc (Union[Unset, list[str]]):
        collapse_data_dimensions (Union[Unset, bool]):  Default: False.
        columns (Union[Unset, str]):
        completed_only (Union[Unset, bool]):  Default: False.
        coordinate_field (Union[Unset, str]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        data_id_scheme (Union[Unset, EventAnalyticsGetQueryHtmlDataIdScheme]):
        default_coordinate_fallback (Union[Unset, bool]):  Default: False.
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, EventAnalyticsGetQueryHtmlDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        endpoint_action (Union[Unset, EventAnalyticsGetQueryHtmlEndpointAction]):  Default:
            EventAnalyticsGetQueryHtmlEndpointAction.OTHER.
        endpoint_item (Union[Unset, EventAnalyticsGetQueryHtmlEndpointItem]):
        enhanced_conditions (Union[Unset, bool]):  Default: False.
        enrollment_date (Union[Unset, str]):
        enrollment_endpoint_item (Union[Unset, bool]):
        event_date (Union[Unset, str]):
        event_status (Union[Unset, list[EventAnalyticsGetQueryHtmlEventStatusItem]]):
        fallback_coordinate_field (Union[Unset, str]):
        filter_ (Union[Unset, list[str]]):
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, str]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, str]):
        limit (Union[Unset, int]):
        org_unit_field (Union[Unset, str]):
        ou_mode (Union[Unset, EventAnalyticsGetQueryHtmlOuMode]):  Default:
            EventAnalyticsGetQueryHtmlOuMode.DESCENDANTS.
        output_id_scheme (Union[Unset, EventAnalyticsGetQueryHtmlOutputIdScheme]):
        output_type (Union[Unset, EventAnalyticsGetQueryHtmlOutputType]):  Default:
            EventAnalyticsGetQueryHtmlOutputType.EVENT.
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program_status (Union[Unset, list[EventAnalyticsGetQueryHtmlProgramStatusItem]]):
        query_endpoint (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        row_context (Union[Unset, bool]):  Default: False.
        rows (Union[Unset, str]):
        scheduled_date (Union[Unset, str]):
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        sort_order (Union[Unset, EventAnalyticsGetQueryHtmlSortOrder]):
        stage (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        total_pages (Union[Unset, bool]):  Default: True.
        user_org_unit (Union[Unset, str]):
        value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        program=program,
        aggregate_data=aggregate_data,
        aggregate_endpoint=aggregate_endpoint,
        aggregation_type=aggregation_type,
        asc=asc,
        collapse_data_dimensions=collapse_data_dimensions,
        columns=columns,
        completed_only=completed_only,
        coordinate_field=coordinate_field,
        coordinates_only=coordinates_only,
        data_id_scheme=data_id_scheme,
        default_coordinate_fallback=default_coordinate_fallback,
        desc=desc,
        dimension=dimension,
        display_property=display_property,
        end_date=end_date,
        endpoint_action=endpoint_action,
        endpoint_item=endpoint_item,
        enhanced_conditions=enhanced_conditions,
        enrollment_date=enrollment_date,
        enrollment_endpoint_item=enrollment_endpoint_item,
        event_date=event_date,
        event_status=event_status,
        fallback_coordinate_field=fallback_coordinate_field,
        filter_=filter_,
        headers=headers,
        hierarchy_meta=hierarchy_meta,
        incident_date=incident_date,
        include_metadata_details=include_metadata_details,
        last_updated=last_updated,
        limit=limit,
        org_unit_field=org_unit_field,
        ou_mode=ou_mode,
        output_id_scheme=output_id_scheme,
        output_type=output_type,
        page=page,
        page_size=page_size,
        paging=paging,
        program_status=program_status,
        query_endpoint=query_endpoint,
        relative_period_date=relative_period_date,
        row_context=row_context,
        rows=rows,
        scheduled_date=scheduled_date,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        sort_order=sort_order,
        stage=stage,
        start_date=start_date,
        time_field=time_field,
        total_pages=total_pages,
        user_org_unit=user_org_unit,
        value=value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    program: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregate_data: Union[Unset, bool] = False,
    aggregate_endpoint: Union[Unset, bool] = UNSET,
    aggregation_type: Union[Unset, EventAnalyticsGetQueryHtmlAggregationType] = UNSET,
    asc: Union[Unset, list[str]] = UNSET,
    collapse_data_dimensions: Union[Unset, bool] = False,
    columns: Union[Unset, str] = UNSET,
    completed_only: Union[Unset, bool] = False,
    coordinate_field: Union[Unset, str] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    data_id_scheme: Union[Unset, EventAnalyticsGetQueryHtmlDataIdScheme] = UNSET,
    default_coordinate_fallback: Union[Unset, bool] = False,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, EventAnalyticsGetQueryHtmlDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    endpoint_action: Union[
        Unset, EventAnalyticsGetQueryHtmlEndpointAction
    ] = EventAnalyticsGetQueryHtmlEndpointAction.OTHER,
    endpoint_item: Union[Unset, EventAnalyticsGetQueryHtmlEndpointItem] = UNSET,
    enhanced_conditions: Union[Unset, bool] = False,
    enrollment_date: Union[Unset, str] = UNSET,
    enrollment_endpoint_item: Union[Unset, bool] = UNSET,
    event_date: Union[Unset, str] = UNSET,
    event_status: Union[Unset, list[EventAnalyticsGetQueryHtmlEventStatusItem]] = UNSET,
    fallback_coordinate_field: Union[Unset, str] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    incident_date: Union[Unset, str] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit_field: Union[Unset, str] = UNSET,
    ou_mode: Union[Unset, EventAnalyticsGetQueryHtmlOuMode] = EventAnalyticsGetQueryHtmlOuMode.DESCENDANTS,
    output_id_scheme: Union[Unset, EventAnalyticsGetQueryHtmlOutputIdScheme] = UNSET,
    output_type: Union[Unset, EventAnalyticsGetQueryHtmlOutputType] = EventAnalyticsGetQueryHtmlOutputType.EVENT,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program_status: Union[Unset, list[EventAnalyticsGetQueryHtmlProgramStatusItem]] = UNSET,
    query_endpoint: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    row_context: Union[Unset, bool] = False,
    rows: Union[Unset, str] = UNSET,
    scheduled_date: Union[Unset, str] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    sort_order: Union[Unset, EventAnalyticsGetQueryHtmlSortOrder] = UNSET,
    stage: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    total_pages: Union[Unset, bool] = True,
    user_org_unit: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        program (str):
        aggregate_data (Union[Unset, bool]):  Default: False.
        aggregate_endpoint (Union[Unset, bool]):
        aggregation_type (Union[Unset, EventAnalyticsGetQueryHtmlAggregationType]):
        asc (Union[Unset, list[str]]):
        collapse_data_dimensions (Union[Unset, bool]):  Default: False.
        columns (Union[Unset, str]):
        completed_only (Union[Unset, bool]):  Default: False.
        coordinate_field (Union[Unset, str]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        data_id_scheme (Union[Unset, EventAnalyticsGetQueryHtmlDataIdScheme]):
        default_coordinate_fallback (Union[Unset, bool]):  Default: False.
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, EventAnalyticsGetQueryHtmlDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        endpoint_action (Union[Unset, EventAnalyticsGetQueryHtmlEndpointAction]):  Default:
            EventAnalyticsGetQueryHtmlEndpointAction.OTHER.
        endpoint_item (Union[Unset, EventAnalyticsGetQueryHtmlEndpointItem]):
        enhanced_conditions (Union[Unset, bool]):  Default: False.
        enrollment_date (Union[Unset, str]):
        enrollment_endpoint_item (Union[Unset, bool]):
        event_date (Union[Unset, str]):
        event_status (Union[Unset, list[EventAnalyticsGetQueryHtmlEventStatusItem]]):
        fallback_coordinate_field (Union[Unset, str]):
        filter_ (Union[Unset, list[str]]):
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, str]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, str]):
        limit (Union[Unset, int]):
        org_unit_field (Union[Unset, str]):
        ou_mode (Union[Unset, EventAnalyticsGetQueryHtmlOuMode]):  Default:
            EventAnalyticsGetQueryHtmlOuMode.DESCENDANTS.
        output_id_scheme (Union[Unset, EventAnalyticsGetQueryHtmlOutputIdScheme]):
        output_type (Union[Unset, EventAnalyticsGetQueryHtmlOutputType]):  Default:
            EventAnalyticsGetQueryHtmlOutputType.EVENT.
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program_status (Union[Unset, list[EventAnalyticsGetQueryHtmlProgramStatusItem]]):
        query_endpoint (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        row_context (Union[Unset, bool]):  Default: False.
        rows (Union[Unset, str]):
        scheduled_date (Union[Unset, str]):
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        sort_order (Union[Unset, EventAnalyticsGetQueryHtmlSortOrder]):
        stage (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        total_pages (Union[Unset, bool]):  Default: True.
        user_org_unit (Union[Unset, str]):
        value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        program=program,
        aggregate_data=aggregate_data,
        aggregate_endpoint=aggregate_endpoint,
        aggregation_type=aggregation_type,
        asc=asc,
        collapse_data_dimensions=collapse_data_dimensions,
        columns=columns,
        completed_only=completed_only,
        coordinate_field=coordinate_field,
        coordinates_only=coordinates_only,
        data_id_scheme=data_id_scheme,
        default_coordinate_fallback=default_coordinate_fallback,
        desc=desc,
        dimension=dimension,
        display_property=display_property,
        end_date=end_date,
        endpoint_action=endpoint_action,
        endpoint_item=endpoint_item,
        enhanced_conditions=enhanced_conditions,
        enrollment_date=enrollment_date,
        enrollment_endpoint_item=enrollment_endpoint_item,
        event_date=event_date,
        event_status=event_status,
        fallback_coordinate_field=fallback_coordinate_field,
        filter_=filter_,
        headers=headers,
        hierarchy_meta=hierarchy_meta,
        incident_date=incident_date,
        include_metadata_details=include_metadata_details,
        last_updated=last_updated,
        limit=limit,
        org_unit_field=org_unit_field,
        ou_mode=ou_mode,
        output_id_scheme=output_id_scheme,
        output_type=output_type,
        page=page,
        page_size=page_size,
        paging=paging,
        program_status=program_status,
        query_endpoint=query_endpoint,
        relative_period_date=relative_period_date,
        row_context=row_context,
        rows=rows,
        scheduled_date=scheduled_date,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        sort_order=sort_order,
        stage=stage,
        start_date=start_date,
        time_field=time_field,
        total_pages=total_pages,
        user_org_unit=user_org_unit,
        value=value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
