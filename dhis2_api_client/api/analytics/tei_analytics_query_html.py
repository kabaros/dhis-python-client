import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tei_analytics_query_html_data_id_scheme import TeiAnalyticsQueryHtmlDataIdScheme
from ...models.tei_analytics_query_html_display_property import TeiAnalyticsQueryHtmlDisplayProperty
from ...models.tei_analytics_query_html_ou_mode import TeiAnalyticsQueryHtmlOuMode
from ...models.tei_analytics_query_html_output_data_element_id_scheme import (
    TeiAnalyticsQueryHtmlOutputDataElementIdScheme,
)
from ...models.tei_analytics_query_html_output_id_scheme import TeiAnalyticsQueryHtmlOutputIdScheme
from ...models.tei_analytics_query_html_output_org_unit_id_scheme import TeiAnalyticsQueryHtmlOutputOrgUnitIdScheme
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tracked_entity_type: str,
    *,
    asc: Union[Unset, list[str]] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    created: Union[Unset, list[str]] = UNSET,
    data_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, TeiAnalyticsQueryHtmlDisplayProperty] = UNSET,
    enrollment_date: Union[Unset, list[str]] = UNSET,
    enrollment_status: Union[Unset, bool] = False,
    event_date: Union[Unset, list[str]] = UNSET,
    event_status: Union[Unset, bool] = False,
    filter_: Union[Unset, list[str]] = UNSET,
    geometry_only: Union[Unset, bool] = False,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    ignore_limit: Union[Unset, bool] = False,
    incident_date: Union[Unset, list[str]] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TeiAnalyticsQueryHtmlOuMode] = TeiAnalyticsQueryHtmlOuMode.DESCENDANTS,
    output_data_element_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputDataElementIdScheme] = UNSET,
    output_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputIdScheme] = UNSET,
    output_org_unit_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputOrgUnitIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, list[str]] = UNSET,
    program_status: Union[Unset, bool] = False,
    programs: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    scheduled_date: Union[Unset, list[str]] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_headers: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_asc: Union[Unset, list[str]] = UNSET
    if not isinstance(asc, Unset):
        json_asc = asc

    params["asc"] = json_asc

    params["coordinatesOnly"] = coordinates_only

    json_created: Union[Unset, list[str]] = UNSET
    if not isinstance(created, Unset):
        json_created = created

    params["created"] = json_created

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

    json_enrollment_date: Union[Unset, list[str]] = UNSET
    if not isinstance(enrollment_date, Unset):
        json_enrollment_date = enrollment_date

    params["enrollmentDate"] = json_enrollment_date

    params["enrollmentStatus"] = enrollment_status

    json_event_date: Union[Unset, list[str]] = UNSET
    if not isinstance(event_date, Unset):
        json_event_date = event_date

    params["eventDate"] = json_event_date

    params["eventStatus"] = event_status

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    params["geometryOnly"] = geometry_only

    json_headers: Union[Unset, list[str]] = UNSET
    if not isinstance(headers, Unset):
        json_headers = headers

    params["headers"] = json_headers

    params["hierarchyMeta"] = hierarchy_meta

    params["ignoreLimit"] = ignore_limit

    json_incident_date: Union[Unset, list[str]] = UNSET
    if not isinstance(incident_date, Unset):
        json_incident_date = incident_date

    params["incidentDate"] = json_incident_date

    params["includeMetadataDetails"] = include_metadata_details

    json_last_updated: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated, Unset):
        json_last_updated = last_updated

    params["lastUpdated"] = json_last_updated

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    json_output_data_element_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_data_element_id_scheme, Unset):
        json_output_data_element_id_scheme = output_data_element_id_scheme.value

    params["outputDataElementIdScheme"] = json_output_data_element_id_scheme

    json_output_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_id_scheme, Unset):
        json_output_id_scheme = output_id_scheme.value

    params["outputIdScheme"] = json_output_id_scheme

    json_output_org_unit_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_org_unit_id_scheme, Unset):
        json_output_org_unit_id_scheme = output_org_unit_id_scheme.value

    params["outputOrgUnitIdScheme"] = json_output_org_unit_id_scheme

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_program: Union[Unset, list[str]] = UNSET
    if not isinstance(program, Unset):
        json_program = program

    params["program"] = json_program

    params["programStatus"] = program_status

    params["programs"] = programs

    json_relative_period_date: Union[Unset, str] = UNSET
    if not isinstance(relative_period_date, Unset):
        json_relative_period_date = relative_period_date.isoformat()
    params["relativePeriodDate"] = json_relative_period_date

    json_scheduled_date: Union[Unset, list[str]] = UNSET
    if not isinstance(scheduled_date, Unset):
        json_scheduled_date = scheduled_date

    params["scheduledDate"] = json_scheduled_date

    params["showHierarchy"] = show_hierarchy

    params["skipData"] = skip_data

    params["skipHeaders"] = skip_headers

    params["skipMeta"] = skip_meta

    params["skipRounding"] = skip_rounding

    params["totalPages"] = total_pages

    params["userOrgUnit"] = user_org_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/analytics/trackedEntities/query/{tracked_entity_type}.html",
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
    tracked_entity_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asc: Union[Unset, list[str]] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    created: Union[Unset, list[str]] = UNSET,
    data_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, TeiAnalyticsQueryHtmlDisplayProperty] = UNSET,
    enrollment_date: Union[Unset, list[str]] = UNSET,
    enrollment_status: Union[Unset, bool] = False,
    event_date: Union[Unset, list[str]] = UNSET,
    event_status: Union[Unset, bool] = False,
    filter_: Union[Unset, list[str]] = UNSET,
    geometry_only: Union[Unset, bool] = False,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    ignore_limit: Union[Unset, bool] = False,
    incident_date: Union[Unset, list[str]] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TeiAnalyticsQueryHtmlOuMode] = TeiAnalyticsQueryHtmlOuMode.DESCENDANTS,
    output_data_element_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputDataElementIdScheme] = UNSET,
    output_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputIdScheme] = UNSET,
    output_org_unit_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputOrgUnitIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, list[str]] = UNSET,
    program_status: Union[Unset, bool] = False,
    programs: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    scheduled_date: Union[Unset, list[str]] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_headers: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        tracked_entity_type (str):
        asc (Union[Unset, list[str]]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        created (Union[Unset, list[str]]):
        data_id_scheme (Union[Unset, TeiAnalyticsQueryHtmlDataIdScheme]):
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, TeiAnalyticsQueryHtmlDisplayProperty]):
        enrollment_date (Union[Unset, list[str]]):
        enrollment_status (Union[Unset, bool]):  Default: False.
        event_date (Union[Unset, list[str]]):
        event_status (Union[Unset, bool]):  Default: False.
        filter_ (Union[Unset, list[str]]):
        geometry_only (Union[Unset, bool]):  Default: False.
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        ignore_limit (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, list[str]]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, list[str]]):
        ou_mode (Union[Unset, TeiAnalyticsQueryHtmlOuMode]):  Default:
            TeiAnalyticsQueryHtmlOuMode.DESCENDANTS.
        output_data_element_id_scheme (Union[Unset,
            TeiAnalyticsQueryHtmlOutputDataElementIdScheme]):
        output_id_scheme (Union[Unset, TeiAnalyticsQueryHtmlOutputIdScheme]):
        output_org_unit_id_scheme (Union[Unset, TeiAnalyticsQueryHtmlOutputOrgUnitIdScheme]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, list[str]]):
        program_status (Union[Unset, bool]):  Default: False.
        programs (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        scheduled_date (Union[Unset, list[str]]):
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_headers (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tracked_entity_type=tracked_entity_type,
        asc=asc,
        coordinates_only=coordinates_only,
        created=created,
        data_id_scheme=data_id_scheme,
        desc=desc,
        dimension=dimension,
        display_property=display_property,
        enrollment_date=enrollment_date,
        enrollment_status=enrollment_status,
        event_date=event_date,
        event_status=event_status,
        filter_=filter_,
        geometry_only=geometry_only,
        headers=headers,
        hierarchy_meta=hierarchy_meta,
        ignore_limit=ignore_limit,
        incident_date=incident_date,
        include_metadata_details=include_metadata_details,
        last_updated=last_updated,
        ou_mode=ou_mode,
        output_data_element_id_scheme=output_data_element_id_scheme,
        output_id_scheme=output_id_scheme,
        output_org_unit_id_scheme=output_org_unit_id_scheme,
        page=page,
        page_size=page_size,
        paging=paging,
        program=program,
        program_status=program_status,
        programs=programs,
        relative_period_date=relative_period_date,
        scheduled_date=scheduled_date,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_headers=skip_headers,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        total_pages=total_pages,
        user_org_unit=user_org_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    tracked_entity_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
    asc: Union[Unset, list[str]] = UNSET,
    coordinates_only: Union[Unset, bool] = False,
    created: Union[Unset, list[str]] = UNSET,
    data_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlDataIdScheme] = UNSET,
    desc: Union[Unset, list[str]] = UNSET,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, TeiAnalyticsQueryHtmlDisplayProperty] = UNSET,
    enrollment_date: Union[Unset, list[str]] = UNSET,
    enrollment_status: Union[Unset, bool] = False,
    event_date: Union[Unset, list[str]] = UNSET,
    event_status: Union[Unset, bool] = False,
    filter_: Union[Unset, list[str]] = UNSET,
    geometry_only: Union[Unset, bool] = False,
    headers: Union[Unset, list[str]] = UNSET,
    hierarchy_meta: Union[Unset, bool] = False,
    ignore_limit: Union[Unset, bool] = False,
    incident_date: Union[Unset, list[str]] = UNSET,
    include_metadata_details: Union[Unset, bool] = False,
    last_updated: Union[Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, TeiAnalyticsQueryHtmlOuMode] = TeiAnalyticsQueryHtmlOuMode.DESCENDANTS,
    output_data_element_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputDataElementIdScheme] = UNSET,
    output_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputIdScheme] = UNSET,
    output_org_unit_id_scheme: Union[Unset, TeiAnalyticsQueryHtmlOutputOrgUnitIdScheme] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    program: Union[Unset, list[str]] = UNSET,
    program_status: Union[Unset, bool] = False,
    programs: Union[Unset, bool] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    scheduled_date: Union[Unset, list[str]] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_headers: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    total_pages: Union[Unset, bool] = False,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        tracked_entity_type (str):
        asc (Union[Unset, list[str]]):
        coordinates_only (Union[Unset, bool]):  Default: False.
        created (Union[Unset, list[str]]):
        data_id_scheme (Union[Unset, TeiAnalyticsQueryHtmlDataIdScheme]):
        desc (Union[Unset, list[str]]):
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, TeiAnalyticsQueryHtmlDisplayProperty]):
        enrollment_date (Union[Unset, list[str]]):
        enrollment_status (Union[Unset, bool]):  Default: False.
        event_date (Union[Unset, list[str]]):
        event_status (Union[Unset, bool]):  Default: False.
        filter_ (Union[Unset, list[str]]):
        geometry_only (Union[Unset, bool]):  Default: False.
        headers (Union[Unset, list[str]]):
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        ignore_limit (Union[Unset, bool]):  Default: False.
        incident_date (Union[Unset, list[str]]):
        include_metadata_details (Union[Unset, bool]):  Default: False.
        last_updated (Union[Unset, list[str]]):
        ou_mode (Union[Unset, TeiAnalyticsQueryHtmlOuMode]):  Default:
            TeiAnalyticsQueryHtmlOuMode.DESCENDANTS.
        output_data_element_id_scheme (Union[Unset,
            TeiAnalyticsQueryHtmlOutputDataElementIdScheme]):
        output_id_scheme (Union[Unset, TeiAnalyticsQueryHtmlOutputIdScheme]):
        output_org_unit_id_scheme (Union[Unset, TeiAnalyticsQueryHtmlOutputOrgUnitIdScheme]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        program (Union[Unset, list[str]]):
        program_status (Union[Unset, bool]):  Default: False.
        programs (Union[Unset, bool]):
        relative_period_date (Union[Unset, datetime.datetime]):
        scheduled_date (Union[Unset, list[str]]):
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_headers (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        total_pages (Union[Unset, bool]):  Default: False.
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tracked_entity_type=tracked_entity_type,
        asc=asc,
        coordinates_only=coordinates_only,
        created=created,
        data_id_scheme=data_id_scheme,
        desc=desc,
        dimension=dimension,
        display_property=display_property,
        enrollment_date=enrollment_date,
        enrollment_status=enrollment_status,
        event_date=event_date,
        event_status=event_status,
        filter_=filter_,
        geometry_only=geometry_only,
        headers=headers,
        hierarchy_meta=hierarchy_meta,
        ignore_limit=ignore_limit,
        incident_date=incident_date,
        include_metadata_details=include_metadata_details,
        last_updated=last_updated,
        ou_mode=ou_mode,
        output_data_element_id_scheme=output_data_element_id_scheme,
        output_id_scheme=output_id_scheme,
        output_org_unit_id_scheme=output_org_unit_id_scheme,
        page=page,
        page_size=page_size,
        paging=paging,
        program=program,
        program_status=program_status,
        programs=programs,
        relative_period_date=relative_period_date,
        scheduled_date=scheduled_date,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_headers=skip_headers,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        total_pages=total_pages,
        user_org_unit=user_org_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
