import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_get_jrxml_aggregation_type import AnalyticsGetJrxmlAggregationType
from ...models.analytics_get_jrxml_display_property import AnalyticsGetJrxmlDisplayProperty
from ...models.analytics_get_jrxml_input_id_scheme import AnalyticsGetJrxmlInputIdScheme
from ...models.analytics_get_jrxml_order import AnalyticsGetJrxmlOrder
from ...models.analytics_get_jrxml_output_data_element_id_scheme import AnalyticsGetJrxmlOutputDataElementIdScheme
from ...models.analytics_get_jrxml_output_data_item_id_scheme import AnalyticsGetJrxmlOutputDataItemIdScheme
from ...models.analytics_get_jrxml_output_id_scheme import AnalyticsGetJrxmlOutputIdScheme
from ...models.analytics_get_jrxml_output_org_unit_id_scheme import AnalyticsGetJrxmlOutputOrgUnitIdScheme
from ...models.analytics_get_jrxml_user_org_unit_type import AnalyticsGetJrxmlUserOrgUnitType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aggregation_type: Union[Unset, AnalyticsGetJrxmlAggregationType] = UNSET,
    approval_level: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    completed_only: Union[Unset, bool] = False,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, AnalyticsGetJrxmlDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    hide_empty_columns: Union[Unset, bool] = False,
    hide_empty_rows: Union[Unset, bool] = False,
    hierarchy_meta: Union[Unset, bool] = False,
    ignore_limit: Union[Unset, bool] = False,
    include_metadata_details: Union[Unset, bool] = False,
    include_num_den: Union[Unset, bool] = False,
    input_id_scheme: Union[Unset, AnalyticsGetJrxmlInputIdScheme] = UNSET,
    measure_criteria: Union[Unset, str] = UNSET,
    order: Union[Unset, AnalyticsGetJrxmlOrder] = UNSET,
    org_unit_field: Union[Unset, str] = UNSET,
    output_data_element_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputDataElementIdScheme] = UNSET,
    output_data_item_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputDataItemIdScheme] = UNSET,
    output_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputIdScheme] = UNSET,
    output_org_unit_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputOrgUnitIdScheme] = UNSET,
    pre_aggregation_measure_criteria: Union[Unset, str] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    rows: Union[Unset, str] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    user_org_unit: Union[Unset, str] = UNSET,
    user_org_unit_type: Union[Unset, AnalyticsGetJrxmlUserOrgUnitType] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_aggregation_type: Union[Unset, str] = UNSET
    if not isinstance(aggregation_type, Unset):
        json_aggregation_type = aggregation_type.value

    params["aggregationType"] = json_aggregation_type

    params["approvalLevel"] = approval_level

    params["columns"] = columns

    params["completedOnly"] = completed_only

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

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    params["hideEmptyColumns"] = hide_empty_columns

    params["hideEmptyRows"] = hide_empty_rows

    params["hierarchyMeta"] = hierarchy_meta

    params["ignoreLimit"] = ignore_limit

    params["includeMetadataDetails"] = include_metadata_details

    params["includeNumDen"] = include_num_den

    json_input_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(input_id_scheme, Unset):
        json_input_id_scheme = input_id_scheme.value

    params["inputIdScheme"] = json_input_id_scheme

    params["measureCriteria"] = measure_criteria

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["orgUnitField"] = org_unit_field

    json_output_data_element_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_data_element_id_scheme, Unset):
        json_output_data_element_id_scheme = output_data_element_id_scheme.value

    params["outputDataElementIdScheme"] = json_output_data_element_id_scheme

    json_output_data_item_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_data_item_id_scheme, Unset):
        json_output_data_item_id_scheme = output_data_item_id_scheme.value

    params["outputDataItemIdScheme"] = json_output_data_item_id_scheme

    json_output_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_id_scheme, Unset):
        json_output_id_scheme = output_id_scheme.value

    params["outputIdScheme"] = json_output_id_scheme

    json_output_org_unit_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(output_org_unit_id_scheme, Unset):
        json_output_org_unit_id_scheme = output_org_unit_id_scheme.value

    params["outputOrgUnitIdScheme"] = json_output_org_unit_id_scheme

    params["preAggregationMeasureCriteria"] = pre_aggregation_measure_criteria

    json_relative_period_date: Union[Unset, str] = UNSET
    if not isinstance(relative_period_date, Unset):
        json_relative_period_date = relative_period_date.isoformat()
    params["relativePeriodDate"] = json_relative_period_date

    params["rows"] = rows

    params["showHierarchy"] = show_hierarchy

    params["skipData"] = skip_data

    params["skipMeta"] = skip_meta

    params["skipRounding"] = skip_rounding

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params["timeField"] = time_field

    params["userOrgUnit"] = user_org_unit

    json_user_org_unit_type: Union[Unset, str] = UNSET
    if not isinstance(user_org_unit_type, Unset):
        json_user_org_unit_type = user_org_unit_type.value

    params["userOrgUnitType"] = json_user_org_unit_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics.jrxml",
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
    aggregation_type: Union[Unset, AnalyticsGetJrxmlAggregationType] = UNSET,
    approval_level: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    completed_only: Union[Unset, bool] = False,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, AnalyticsGetJrxmlDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    hide_empty_columns: Union[Unset, bool] = False,
    hide_empty_rows: Union[Unset, bool] = False,
    hierarchy_meta: Union[Unset, bool] = False,
    ignore_limit: Union[Unset, bool] = False,
    include_metadata_details: Union[Unset, bool] = False,
    include_num_den: Union[Unset, bool] = False,
    input_id_scheme: Union[Unset, AnalyticsGetJrxmlInputIdScheme] = UNSET,
    measure_criteria: Union[Unset, str] = UNSET,
    order: Union[Unset, AnalyticsGetJrxmlOrder] = UNSET,
    org_unit_field: Union[Unset, str] = UNSET,
    output_data_element_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputDataElementIdScheme] = UNSET,
    output_data_item_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputDataItemIdScheme] = UNSET,
    output_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputIdScheme] = UNSET,
    output_org_unit_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputOrgUnitIdScheme] = UNSET,
    pre_aggregation_measure_criteria: Union[Unset, str] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    rows: Union[Unset, str] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    user_org_unit: Union[Unset, str] = UNSET,
    user_org_unit_type: Union[Unset, AnalyticsGetJrxmlUserOrgUnitType] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        aggregation_type (Union[Unset, AnalyticsGetJrxmlAggregationType]):
        approval_level (Union[Unset, str]):
        columns (Union[Unset, str]):
        completed_only (Union[Unset, bool]):  Default: False.
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, AnalyticsGetJrxmlDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        filter_ (Union[Unset, list[str]]):
        hide_empty_columns (Union[Unset, bool]):  Default: False.
        hide_empty_rows (Union[Unset, bool]):  Default: False.
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        ignore_limit (Union[Unset, bool]):  Default: False.
        include_metadata_details (Union[Unset, bool]):  Default: False.
        include_num_den (Union[Unset, bool]):  Default: False.
        input_id_scheme (Union[Unset, AnalyticsGetJrxmlInputIdScheme]):
        measure_criteria (Union[Unset, str]):
        order (Union[Unset, AnalyticsGetJrxmlOrder]):
        org_unit_field (Union[Unset, str]):
        output_data_element_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputDataElementIdScheme]):
        output_data_item_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputDataItemIdScheme]):
        output_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputIdScheme]):
        output_org_unit_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputOrgUnitIdScheme]):
        pre_aggregation_measure_criteria (Union[Unset, str]):
        relative_period_date (Union[Unset, datetime.datetime]):
        rows (Union[Unset, str]):
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        user_org_unit (Union[Unset, str]):
        user_org_unit_type (Union[Unset, AnalyticsGetJrxmlUserOrgUnitType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        aggregation_type=aggregation_type,
        approval_level=approval_level,
        columns=columns,
        completed_only=completed_only,
        dimension=dimension,
        display_property=display_property,
        end_date=end_date,
        filter_=filter_,
        hide_empty_columns=hide_empty_columns,
        hide_empty_rows=hide_empty_rows,
        hierarchy_meta=hierarchy_meta,
        ignore_limit=ignore_limit,
        include_metadata_details=include_metadata_details,
        include_num_den=include_num_den,
        input_id_scheme=input_id_scheme,
        measure_criteria=measure_criteria,
        order=order,
        org_unit_field=org_unit_field,
        output_data_element_id_scheme=output_data_element_id_scheme,
        output_data_item_id_scheme=output_data_item_id_scheme,
        output_id_scheme=output_id_scheme,
        output_org_unit_id_scheme=output_org_unit_id_scheme,
        pre_aggregation_measure_criteria=pre_aggregation_measure_criteria,
        relative_period_date=relative_period_date,
        rows=rows,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        start_date=start_date,
        time_field=time_field,
        user_org_unit=user_org_unit,
        user_org_unit_type=user_org_unit_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aggregation_type: Union[Unset, AnalyticsGetJrxmlAggregationType] = UNSET,
    approval_level: Union[Unset, str] = UNSET,
    columns: Union[Unset, str] = UNSET,
    completed_only: Union[Unset, bool] = False,
    dimension: Union[Unset, list[str]] = UNSET,
    display_property: Union[Unset, AnalyticsGetJrxmlDisplayProperty] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    hide_empty_columns: Union[Unset, bool] = False,
    hide_empty_rows: Union[Unset, bool] = False,
    hierarchy_meta: Union[Unset, bool] = False,
    ignore_limit: Union[Unset, bool] = False,
    include_metadata_details: Union[Unset, bool] = False,
    include_num_den: Union[Unset, bool] = False,
    input_id_scheme: Union[Unset, AnalyticsGetJrxmlInputIdScheme] = UNSET,
    measure_criteria: Union[Unset, str] = UNSET,
    order: Union[Unset, AnalyticsGetJrxmlOrder] = UNSET,
    org_unit_field: Union[Unset, str] = UNSET,
    output_data_element_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputDataElementIdScheme] = UNSET,
    output_data_item_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputDataItemIdScheme] = UNSET,
    output_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputIdScheme] = UNSET,
    output_org_unit_id_scheme: Union[Unset, AnalyticsGetJrxmlOutputOrgUnitIdScheme] = UNSET,
    pre_aggregation_measure_criteria: Union[Unset, str] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    rows: Union[Unset, str] = UNSET,
    show_hierarchy: Union[Unset, bool] = False,
    skip_data: Union[Unset, bool] = False,
    skip_meta: Union[Unset, bool] = False,
    skip_rounding: Union[Unset, bool] = False,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    time_field: Union[Unset, str] = UNSET,
    user_org_unit: Union[Unset, str] = UNSET,
    user_org_unit_type: Union[Unset, AnalyticsGetJrxmlUserOrgUnitType] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        aggregation_type (Union[Unset, AnalyticsGetJrxmlAggregationType]):
        approval_level (Union[Unset, str]):
        columns (Union[Unset, str]):
        completed_only (Union[Unset, bool]):  Default: False.
        dimension (Union[Unset, list[str]]):
        display_property (Union[Unset, AnalyticsGetJrxmlDisplayProperty]):
        end_date (Union[Unset, datetime.datetime]):
        filter_ (Union[Unset, list[str]]):
        hide_empty_columns (Union[Unset, bool]):  Default: False.
        hide_empty_rows (Union[Unset, bool]):  Default: False.
        hierarchy_meta (Union[Unset, bool]):  Default: False.
        ignore_limit (Union[Unset, bool]):  Default: False.
        include_metadata_details (Union[Unset, bool]):  Default: False.
        include_num_den (Union[Unset, bool]):  Default: False.
        input_id_scheme (Union[Unset, AnalyticsGetJrxmlInputIdScheme]):
        measure_criteria (Union[Unset, str]):
        order (Union[Unset, AnalyticsGetJrxmlOrder]):
        org_unit_field (Union[Unset, str]):
        output_data_element_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputDataElementIdScheme]):
        output_data_item_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputDataItemIdScheme]):
        output_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputIdScheme]):
        output_org_unit_id_scheme (Union[Unset, AnalyticsGetJrxmlOutputOrgUnitIdScheme]):
        pre_aggregation_measure_criteria (Union[Unset, str]):
        relative_period_date (Union[Unset, datetime.datetime]):
        rows (Union[Unset, str]):
        show_hierarchy (Union[Unset, bool]):  Default: False.
        skip_data (Union[Unset, bool]):  Default: False.
        skip_meta (Union[Unset, bool]):  Default: False.
        skip_rounding (Union[Unset, bool]):  Default: False.
        start_date (Union[Unset, datetime.datetime]):
        time_field (Union[Unset, str]):
        user_org_unit (Union[Unset, str]):
        user_org_unit_type (Union[Unset, AnalyticsGetJrxmlUserOrgUnitType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        aggregation_type=aggregation_type,
        approval_level=approval_level,
        columns=columns,
        completed_only=completed_only,
        dimension=dimension,
        display_property=display_property,
        end_date=end_date,
        filter_=filter_,
        hide_empty_columns=hide_empty_columns,
        hide_empty_rows=hide_empty_rows,
        hierarchy_meta=hierarchy_meta,
        ignore_limit=ignore_limit,
        include_metadata_details=include_metadata_details,
        include_num_den=include_num_den,
        input_id_scheme=input_id_scheme,
        measure_criteria=measure_criteria,
        order=order,
        org_unit_field=org_unit_field,
        output_data_element_id_scheme=output_data_element_id_scheme,
        output_data_item_id_scheme=output_data_item_id_scheme,
        output_id_scheme=output_id_scheme,
        output_org_unit_id_scheme=output_org_unit_id_scheme,
        pre_aggregation_measure_criteria=pre_aggregation_measure_criteria,
        relative_period_date=relative_period_date,
        rows=rows,
        show_hierarchy=show_hierarchy,
        skip_data=skip_data,
        skip_meta=skip_meta,
        skip_rounding=skip_rounding,
        start_date=start_date,
        time_field=time_field,
        user_org_unit=user_org_unit,
        user_org_unit_type=user_org_unit_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
