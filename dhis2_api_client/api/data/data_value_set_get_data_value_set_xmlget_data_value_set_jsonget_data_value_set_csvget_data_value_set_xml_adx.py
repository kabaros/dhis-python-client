import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_value_set import DataValueSet
from ...models.data_value_set_get_data_value_set_xmlget_data_value_set_jsonget_data_value_set_csvget_data_value_set_xml_adx_input_data_element_group_id_scheme import (
    DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme,
)
from ...models.data_value_set_get_data_value_set_xmlget_data_value_set_jsonget_data_value_set_csvget_data_value_set_xml_adx_input_data_element_id_scheme import (
    DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme,
)
from ...models.data_value_set_get_data_value_set_xmlget_data_value_set_jsonget_data_value_set_csvget_data_value_set_xml_adx_input_data_set_id_scheme import (
    DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme,
)
from ...models.data_value_set_get_data_value_set_xmlget_data_value_set_jsonget_data_value_set_csvget_data_value_set_xml_adx_input_id_scheme import (
    DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputIdScheme,
)
from ...models.data_value_set_get_data_value_set_xmlget_data_value_set_jsonget_data_value_set_csvget_data_value_set_xml_adx_input_org_unit_id_scheme import (
    DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    attachment: Union[Unset, str] = UNSET,
    attribute_combo: Union[Unset, str] = UNSET,
    attribute_option_combo: Union[Unset, list[str]] = UNSET,
    attribute_option_combo_id_scheme: Union[Unset, str] = UNSET,
    attribute_options: Union[Unset, list[str]] = UNSET,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    children: Union[Unset, bool] = False,
    compression: Union[Unset, str] = UNSET,
    data_element: Union[Unset, list[str]] = UNSET,
    data_element_group: Union[Unset, list[str]] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    input_data_element_group_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme,
    ] = UNSET,
    input_data_element_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme,
    ] = UNSET,
    input_data_set_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme,
    ] = UNSET,
    input_id_scheme: Union[
        Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputIdScheme
    ] = UNSET,
    input_org_unit_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme,
    ] = UNSET,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    program_stage_instance_id_scheme: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["attachment"] = attachment

    params["attributeCombo"] = attribute_combo

    json_attribute_option_combo: Union[Unset, list[str]] = UNSET
    if not isinstance(attribute_option_combo, Unset):
        json_attribute_option_combo = attribute_option_combo

    params["attributeOptionCombo"] = json_attribute_option_combo

    params["attributeOptionComboIdScheme"] = attribute_option_combo_id_scheme

    json_attribute_options: Union[Unset, list[str]] = UNSET
    if not isinstance(attribute_options, Unset):
        json_attribute_options = attribute_options

    params["attributeOptions"] = json_attribute_options

    params["categoryIdScheme"] = category_id_scheme

    params["categoryOptionComboIdScheme"] = category_option_combo_id_scheme

    params["categoryOptionIdScheme"] = category_option_id_scheme

    params["children"] = children

    params["compression"] = compression

    json_data_element: Union[Unset, list[str]] = UNSET
    if not isinstance(data_element, Unset):
        json_data_element = data_element

    params["dataElement"] = json_data_element

    json_data_element_group: Union[Unset, list[str]] = UNSET
    if not isinstance(data_element_group, Unset):
        json_data_element_group = data_element_group

    params["dataElementGroup"] = json_data_element_group

    params["dataElementIdScheme"] = data_element_id_scheme

    json_data_set: Union[Unset, list[str]] = UNSET
    if not isinstance(data_set, Unset):
        json_data_set = data_set

    params["dataSet"] = json_data_set

    params["dataSetIdScheme"] = data_set_id_scheme

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["idScheme"] = id_scheme

    params["includeDeleted"] = include_deleted

    json_input_data_element_group_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(input_data_element_group_id_scheme, Unset):
        json_input_data_element_group_id_scheme = input_data_element_group_id_scheme.value

    params["inputDataElementGroupIdScheme"] = json_input_data_element_group_id_scheme

    json_input_data_element_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(input_data_element_id_scheme, Unset):
        json_input_data_element_id_scheme = input_data_element_id_scheme.value

    params["inputDataElementIdScheme"] = json_input_data_element_id_scheme

    json_input_data_set_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(input_data_set_id_scheme, Unset):
        json_input_data_set_id_scheme = input_data_set_id_scheme.value

    params["inputDataSetIdScheme"] = json_input_data_set_id_scheme

    json_input_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(input_id_scheme, Unset):
        json_input_id_scheme = input_id_scheme.value

    params["inputIdScheme"] = json_input_id_scheme

    json_input_org_unit_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(input_org_unit_id_scheme, Unset):
        json_input_org_unit_id_scheme = input_org_unit_id_scheme.value

    params["inputOrgUnitIdScheme"] = json_input_org_unit_id_scheme

    json_last_updated: Union[Unset, str] = UNSET
    if not isinstance(last_updated, Unset):
        json_last_updated = last_updated.isoformat()
    params["lastUpdated"] = json_last_updated

    params["lastUpdatedDuration"] = last_updated_duration

    params["limit"] = limit

    json_org_unit: Union[Unset, list[str]] = UNSET
    if not isinstance(org_unit, Unset):
        json_org_unit = org_unit

    params["orgUnit"] = json_org_unit

    json_org_unit_group: Union[Unset, list[str]] = UNSET
    if not isinstance(org_unit_group, Unset):
        json_org_unit_group = org_unit_group

    params["orgUnitGroup"] = json_org_unit_group

    params["orgUnitIdScheme"] = org_unit_id_scheme

    json_period: Union[Unset, list[str]] = UNSET
    if not isinstance(period, Unset):
        json_period = period

    params["period"] = json_period

    params["programIdScheme"] = program_id_scheme

    params["programStageIdScheme"] = program_stage_id_scheme

    params["programStageInstanceIdScheme"] = program_stage_instance_id_scheme

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params["trackedEntityAttributeIdScheme"] = tracked_entity_attribute_id_scheme

    params["trackedEntityIdScheme"] = tracked_entity_id_scheme

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataValueSets/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[DataValueSet]:
    if response.status_code == 200:
        response_200 = DataValueSet.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[DataValueSet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attachment: Union[Unset, str] = UNSET,
    attribute_combo: Union[Unset, str] = UNSET,
    attribute_option_combo: Union[Unset, list[str]] = UNSET,
    attribute_option_combo_id_scheme: Union[Unset, str] = UNSET,
    attribute_options: Union[Unset, list[str]] = UNSET,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    children: Union[Unset, bool] = False,
    compression: Union[Unset, str] = UNSET,
    data_element: Union[Unset, list[str]] = UNSET,
    data_element_group: Union[Unset, list[str]] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    input_data_element_group_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme,
    ] = UNSET,
    input_data_element_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme,
    ] = UNSET,
    input_data_set_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme,
    ] = UNSET,
    input_id_scheme: Union[
        Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputIdScheme
    ] = UNSET,
    input_org_unit_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme,
    ] = UNSET,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    program_stage_instance_id_scheme: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Response[DataValueSet]:
    """[no description yet]

    Args:
        attachment (Union[Unset, str]):
        attribute_combo (Union[Unset, str]):
        attribute_option_combo (Union[Unset, list[str]]):
        attribute_option_combo_id_scheme (Union[Unset, str]):
        attribute_options (Union[Unset, list[str]]):
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        children (Union[Unset, bool]):  Default: False.
        compression (Union[Unset, str]):
        data_element (Union[Unset, list[str]]):
        data_element_group (Union[Unset, list[str]]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, list[str]]):
        data_set_id_scheme (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        id_scheme (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        input_data_element_group_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValu
            eSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme]):
        input_data_element_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJs
            ongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme]):
        input_data_set_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme]):
        input_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValu
            eSetCsvgetDataValueSetXmlAdxInputIdScheme]):
        input_org_unit_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        limit (Union[Unset, int]):
        org_unit (Union[Unset, list[str]]):
        org_unit_group (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):
        period (Union[Unset, list[str]]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        program_stage_instance_id_scheme (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataValueSet]
    """

    kwargs = _get_kwargs(
        attachment=attachment,
        attribute_combo=attribute_combo,
        attribute_option_combo=attribute_option_combo,
        attribute_option_combo_id_scheme=attribute_option_combo_id_scheme,
        attribute_options=attribute_options,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        children=children,
        compression=compression,
        data_element=data_element,
        data_element_group=data_element_group,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        end_date=end_date,
        id_scheme=id_scheme,
        include_deleted=include_deleted,
        input_data_element_group_id_scheme=input_data_element_group_id_scheme,
        input_data_element_id_scheme=input_data_element_id_scheme,
        input_data_set_id_scheme=input_data_set_id_scheme,
        input_id_scheme=input_id_scheme,
        input_org_unit_id_scheme=input_org_unit_id_scheme,
        last_updated=last_updated,
        last_updated_duration=last_updated_duration,
        limit=limit,
        org_unit=org_unit,
        org_unit_group=org_unit_group,
        org_unit_id_scheme=org_unit_id_scheme,
        period=period,
        program_id_scheme=program_id_scheme,
        program_stage_id_scheme=program_stage_id_scheme,
        program_stage_instance_id_scheme=program_stage_instance_id_scheme,
        start_date=start_date,
        tracked_entity_attribute_id_scheme=tracked_entity_attribute_id_scheme,
        tracked_entity_id_scheme=tracked_entity_id_scheme,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    attachment: Union[Unset, str] = UNSET,
    attribute_combo: Union[Unset, str] = UNSET,
    attribute_option_combo: Union[Unset, list[str]] = UNSET,
    attribute_option_combo_id_scheme: Union[Unset, str] = UNSET,
    attribute_options: Union[Unset, list[str]] = UNSET,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    children: Union[Unset, bool] = False,
    compression: Union[Unset, str] = UNSET,
    data_element: Union[Unset, list[str]] = UNSET,
    data_element_group: Union[Unset, list[str]] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    input_data_element_group_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme,
    ] = UNSET,
    input_data_element_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme,
    ] = UNSET,
    input_data_set_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme,
    ] = UNSET,
    input_id_scheme: Union[
        Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputIdScheme
    ] = UNSET,
    input_org_unit_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme,
    ] = UNSET,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    program_stage_instance_id_scheme: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Optional[DataValueSet]:
    """[no description yet]

    Args:
        attachment (Union[Unset, str]):
        attribute_combo (Union[Unset, str]):
        attribute_option_combo (Union[Unset, list[str]]):
        attribute_option_combo_id_scheme (Union[Unset, str]):
        attribute_options (Union[Unset, list[str]]):
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        children (Union[Unset, bool]):  Default: False.
        compression (Union[Unset, str]):
        data_element (Union[Unset, list[str]]):
        data_element_group (Union[Unset, list[str]]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, list[str]]):
        data_set_id_scheme (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        id_scheme (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        input_data_element_group_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValu
            eSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme]):
        input_data_element_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJs
            ongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme]):
        input_data_set_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme]):
        input_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValu
            eSetCsvgetDataValueSetXmlAdxInputIdScheme]):
        input_org_unit_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        limit (Union[Unset, int]):
        org_unit (Union[Unset, list[str]]):
        org_unit_group (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):
        period (Union[Unset, list[str]]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        program_stage_instance_id_scheme (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataValueSet
    """

    return sync_detailed(
        client=client,
        attachment=attachment,
        attribute_combo=attribute_combo,
        attribute_option_combo=attribute_option_combo,
        attribute_option_combo_id_scheme=attribute_option_combo_id_scheme,
        attribute_options=attribute_options,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        children=children,
        compression=compression,
        data_element=data_element,
        data_element_group=data_element_group,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        end_date=end_date,
        id_scheme=id_scheme,
        include_deleted=include_deleted,
        input_data_element_group_id_scheme=input_data_element_group_id_scheme,
        input_data_element_id_scheme=input_data_element_id_scheme,
        input_data_set_id_scheme=input_data_set_id_scheme,
        input_id_scheme=input_id_scheme,
        input_org_unit_id_scheme=input_org_unit_id_scheme,
        last_updated=last_updated,
        last_updated_duration=last_updated_duration,
        limit=limit,
        org_unit=org_unit,
        org_unit_group=org_unit_group,
        org_unit_id_scheme=org_unit_id_scheme,
        period=period,
        program_id_scheme=program_id_scheme,
        program_stage_id_scheme=program_stage_id_scheme,
        program_stage_instance_id_scheme=program_stage_instance_id_scheme,
        start_date=start_date,
        tracked_entity_attribute_id_scheme=tracked_entity_attribute_id_scheme,
        tracked_entity_id_scheme=tracked_entity_id_scheme,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attachment: Union[Unset, str] = UNSET,
    attribute_combo: Union[Unset, str] = UNSET,
    attribute_option_combo: Union[Unset, list[str]] = UNSET,
    attribute_option_combo_id_scheme: Union[Unset, str] = UNSET,
    attribute_options: Union[Unset, list[str]] = UNSET,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    children: Union[Unset, bool] = False,
    compression: Union[Unset, str] = UNSET,
    data_element: Union[Unset, list[str]] = UNSET,
    data_element_group: Union[Unset, list[str]] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    input_data_element_group_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme,
    ] = UNSET,
    input_data_element_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme,
    ] = UNSET,
    input_data_set_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme,
    ] = UNSET,
    input_id_scheme: Union[
        Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputIdScheme
    ] = UNSET,
    input_org_unit_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme,
    ] = UNSET,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    program_stage_instance_id_scheme: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Response[DataValueSet]:
    """[no description yet]

    Args:
        attachment (Union[Unset, str]):
        attribute_combo (Union[Unset, str]):
        attribute_option_combo (Union[Unset, list[str]]):
        attribute_option_combo_id_scheme (Union[Unset, str]):
        attribute_options (Union[Unset, list[str]]):
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        children (Union[Unset, bool]):  Default: False.
        compression (Union[Unset, str]):
        data_element (Union[Unset, list[str]]):
        data_element_group (Union[Unset, list[str]]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, list[str]]):
        data_set_id_scheme (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        id_scheme (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        input_data_element_group_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValu
            eSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme]):
        input_data_element_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJs
            ongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme]):
        input_data_set_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme]):
        input_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValu
            eSetCsvgetDataValueSetXmlAdxInputIdScheme]):
        input_org_unit_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        limit (Union[Unset, int]):
        org_unit (Union[Unset, list[str]]):
        org_unit_group (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):
        period (Union[Unset, list[str]]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        program_stage_instance_id_scheme (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataValueSet]
    """

    kwargs = _get_kwargs(
        attachment=attachment,
        attribute_combo=attribute_combo,
        attribute_option_combo=attribute_option_combo,
        attribute_option_combo_id_scheme=attribute_option_combo_id_scheme,
        attribute_options=attribute_options,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        children=children,
        compression=compression,
        data_element=data_element,
        data_element_group=data_element_group,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        end_date=end_date,
        id_scheme=id_scheme,
        include_deleted=include_deleted,
        input_data_element_group_id_scheme=input_data_element_group_id_scheme,
        input_data_element_id_scheme=input_data_element_id_scheme,
        input_data_set_id_scheme=input_data_set_id_scheme,
        input_id_scheme=input_id_scheme,
        input_org_unit_id_scheme=input_org_unit_id_scheme,
        last_updated=last_updated,
        last_updated_duration=last_updated_duration,
        limit=limit,
        org_unit=org_unit,
        org_unit_group=org_unit_group,
        org_unit_id_scheme=org_unit_id_scheme,
        period=period,
        program_id_scheme=program_id_scheme,
        program_stage_id_scheme=program_stage_id_scheme,
        program_stage_instance_id_scheme=program_stage_instance_id_scheme,
        start_date=start_date,
        tracked_entity_attribute_id_scheme=tracked_entity_attribute_id_scheme,
        tracked_entity_id_scheme=tracked_entity_id_scheme,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    attachment: Union[Unset, str] = UNSET,
    attribute_combo: Union[Unset, str] = UNSET,
    attribute_option_combo: Union[Unset, list[str]] = UNSET,
    attribute_option_combo_id_scheme: Union[Unset, str] = UNSET,
    attribute_options: Union[Unset, list[str]] = UNSET,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    children: Union[Unset, bool] = False,
    compression: Union[Unset, str] = UNSET,
    data_element: Union[Unset, list[str]] = UNSET,
    data_element_group: Union[Unset, list[str]] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[Unset, str] = UNSET,
    include_deleted: Union[Unset, bool] = False,
    input_data_element_group_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme,
    ] = UNSET,
    input_data_element_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme,
    ] = UNSET,
    input_data_set_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme,
    ] = UNSET,
    input_id_scheme: Union[
        Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputIdScheme
    ] = UNSET,
    input_org_unit_id_scheme: Union[
        Unset,
        DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme,
    ] = UNSET,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
    last_updated_duration: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    program_stage_instance_id_scheme: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Optional[DataValueSet]:
    """[no description yet]

    Args:
        attachment (Union[Unset, str]):
        attribute_combo (Union[Unset, str]):
        attribute_option_combo (Union[Unset, list[str]]):
        attribute_option_combo_id_scheme (Union[Unset, str]):
        attribute_options (Union[Unset, list[str]]):
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        children (Union[Unset, bool]):  Default: False.
        compression (Union[Unset, str]):
        data_element (Union[Unset, list[str]]):
        data_element_group (Union[Unset, list[str]]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, list[str]]):
        data_set_id_scheme (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        id_scheme (Union[Unset, str]):
        include_deleted (Union[Unset, bool]):  Default: False.
        input_data_element_group_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValu
            eSetJsongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementGroupIdScheme]):
        input_data_element_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJs
            ongetDataValueSetCsvgetDataValueSetXmlAdxInputDataElementIdScheme]):
        input_data_set_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputDataSetIdScheme]):
        input_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsongetDataValu
            eSetCsvgetDataValueSetXmlAdxInputIdScheme]):
        input_org_unit_id_scheme (Union[Unset, DataValueSetGetDataValueSetXmlgetDataValueSetJsonge
            tDataValueSetCsvgetDataValueSetXmlAdxInputOrgUnitIdScheme]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_duration (Union[Unset, str]):
        limit (Union[Unset, int]):
        org_unit (Union[Unset, list[str]]):
        org_unit_group (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):
        period (Union[Unset, list[str]]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        program_stage_instance_id_scheme (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataValueSet
    """

    return (
        await asyncio_detailed(
            client=client,
            attachment=attachment,
            attribute_combo=attribute_combo,
            attribute_option_combo=attribute_option_combo,
            attribute_option_combo_id_scheme=attribute_option_combo_id_scheme,
            attribute_options=attribute_options,
            category_id_scheme=category_id_scheme,
            category_option_combo_id_scheme=category_option_combo_id_scheme,
            category_option_id_scheme=category_option_id_scheme,
            children=children,
            compression=compression,
            data_element=data_element,
            data_element_group=data_element_group,
            data_element_id_scheme=data_element_id_scheme,
            data_set=data_set,
            data_set_id_scheme=data_set_id_scheme,
            end_date=end_date,
            id_scheme=id_scheme,
            include_deleted=include_deleted,
            input_data_element_group_id_scheme=input_data_element_group_id_scheme,
            input_data_element_id_scheme=input_data_element_id_scheme,
            input_data_set_id_scheme=input_data_set_id_scheme,
            input_id_scheme=input_id_scheme,
            input_org_unit_id_scheme=input_org_unit_id_scheme,
            last_updated=last_updated,
            last_updated_duration=last_updated_duration,
            limit=limit,
            org_unit=org_unit,
            org_unit_group=org_unit_group,
            org_unit_id_scheme=org_unit_id_scheme,
            period=period,
            program_id_scheme=program_id_scheme,
            program_stage_id_scheme=program_stage_id_scheme,
            program_stage_instance_id_scheme=program_stage_instance_id_scheme,
            start_date=start_date,
            tracked_entity_attribute_id_scheme=tracked_entity_attribute_id_scheme,
            tracked_entity_id_scheme=tracked_entity_id_scheme,
        )
    ).parsed
