import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_attribute_option_combo_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlAttributeOptionComboIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_category_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_category_option_combo_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionComboIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_category_option_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_data_element_group_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementGroupIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_data_element_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_data_set_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataSetIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_org_unit_group_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitGroupIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_org_unit_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_program_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_program_stage_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_program_stage_instance_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageInstanceIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_tracked_entity_attribute_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityAttributeIdScheme,
)
from ...models.complete_data_set_registration_get_complete_registrations_jsonget_complete_registrations_xml_tracked_entity_id_scheme import (
    CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityIdScheme,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    attribute_option_combo_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlAttributeOptionComboIdScheme,
    ] = UNSET,
    category_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryIdScheme
    ] = UNSET,
    category_option_combo_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionComboIdScheme,
    ] = UNSET,
    category_option_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionIdScheme
    ] = UNSET,
    children: Union[Unset, bool] = False,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_duration: Union[Unset, str] = UNSET,
    data_element_group_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementGroupIdScheme,
    ] = UNSET,
    data_element_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementIdScheme
    ] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataSetIdScheme
    ] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlIdScheme
    ] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_group_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitGroupIdScheme
    ] = UNSET,
    org_unit_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitIdScheme
    ] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramIdScheme
    ] = UNSET,
    program_stage_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageIdScheme
    ] = UNSET,
    program_stage_instance_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageInstanceIdScheme,
    ] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityAttributeIdScheme,
    ] = UNSET,
    tracked_entity_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityIdScheme
    ] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_attribute_option_combo_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(attribute_option_combo_id_scheme, Unset):
        json_attribute_option_combo_id_scheme = attribute_option_combo_id_scheme.value

    params["attributeOptionComboIdScheme"] = json_attribute_option_combo_id_scheme

    json_category_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(category_id_scheme, Unset):
        json_category_id_scheme = category_id_scheme.value

    params["categoryIdScheme"] = json_category_id_scheme

    json_category_option_combo_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(category_option_combo_id_scheme, Unset):
        json_category_option_combo_id_scheme = category_option_combo_id_scheme.value

    params["categoryOptionComboIdScheme"] = json_category_option_combo_id_scheme

    json_category_option_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(category_option_id_scheme, Unset):
        json_category_option_id_scheme = category_option_id_scheme.value

    params["categoryOptionIdScheme"] = json_category_option_id_scheme

    params["children"] = children

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    params["createdDuration"] = created_duration

    json_data_element_group_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(data_element_group_id_scheme, Unset):
        json_data_element_group_id_scheme = data_element_group_id_scheme.value

    params["dataElementGroupIdScheme"] = json_data_element_group_id_scheme

    json_data_element_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(data_element_id_scheme, Unset):
        json_data_element_id_scheme = data_element_id_scheme.value

    params["dataElementIdScheme"] = json_data_element_id_scheme

    json_data_set: Union[Unset, list[str]] = UNSET
    if not isinstance(data_set, Unset):
        json_data_set = data_set

    params["dataSet"] = json_data_set

    json_data_set_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(data_set_id_scheme, Unset):
        json_data_set_id_scheme = data_set_id_scheme.value

    params["dataSetIdScheme"] = json_data_set_id_scheme

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(id_scheme, Unset):
        json_id_scheme = id_scheme.value

    params["idScheme"] = json_id_scheme

    params["limit"] = limit

    json_org_unit: Union[Unset, list[str]] = UNSET
    if not isinstance(org_unit, Unset):
        json_org_unit = org_unit

    params["orgUnit"] = json_org_unit

    json_org_unit_group: Union[Unset, list[str]] = UNSET
    if not isinstance(org_unit_group, Unset):
        json_org_unit_group = org_unit_group

    params["orgUnitGroup"] = json_org_unit_group

    json_org_unit_group_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(org_unit_group_id_scheme, Unset):
        json_org_unit_group_id_scheme = org_unit_group_id_scheme.value

    params["orgUnitGroupIdScheme"] = json_org_unit_group_id_scheme

    json_org_unit_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(org_unit_id_scheme, Unset):
        json_org_unit_id_scheme = org_unit_id_scheme.value

    params["orgUnitIdScheme"] = json_org_unit_id_scheme

    json_period: Union[Unset, list[str]] = UNSET
    if not isinstance(period, Unset):
        json_period = period

    params["period"] = json_period

    json_program_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(program_id_scheme, Unset):
        json_program_id_scheme = program_id_scheme.value

    params["programIdScheme"] = json_program_id_scheme

    json_program_stage_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(program_stage_id_scheme, Unset):
        json_program_stage_id_scheme = program_stage_id_scheme.value

    params["programStageIdScheme"] = json_program_stage_id_scheme

    json_program_stage_instance_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(program_stage_instance_id_scheme, Unset):
        json_program_stage_instance_id_scheme = program_stage_instance_id_scheme.value

    params["programStageInstanceIdScheme"] = json_program_stage_instance_id_scheme

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(tracked_entity_attribute_id_scheme, Unset):
        json_tracked_entity_attribute_id_scheme = tracked_entity_attribute_id_scheme.value

    params["trackedEntityAttributeIdScheme"] = json_tracked_entity_attribute_id_scheme

    json_tracked_entity_id_scheme: Union[Unset, str] = UNSET
    if not isinstance(tracked_entity_id_scheme, Unset):
        json_tracked_entity_id_scheme = tracked_entity_id_scheme.value

    params["trackedEntityIdScheme"] = json_tracked_entity_id_scheme

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/completeDataSetRegistrations/",
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
    attribute_option_combo_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlAttributeOptionComboIdScheme,
    ] = UNSET,
    category_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryIdScheme
    ] = UNSET,
    category_option_combo_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionComboIdScheme,
    ] = UNSET,
    category_option_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionIdScheme
    ] = UNSET,
    children: Union[Unset, bool] = False,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_duration: Union[Unset, str] = UNSET,
    data_element_group_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementGroupIdScheme,
    ] = UNSET,
    data_element_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementIdScheme
    ] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataSetIdScheme
    ] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlIdScheme
    ] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_group_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitGroupIdScheme
    ] = UNSET,
    org_unit_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitIdScheme
    ] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramIdScheme
    ] = UNSET,
    program_stage_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageIdScheme
    ] = UNSET,
    program_stage_instance_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageInstanceIdScheme,
    ] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityAttributeIdScheme,
    ] = UNSET,
    tracked_entity_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityIdScheme
    ] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        attribute_option_combo_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegis
            trationsJsongetCompleteRegistrationsXmlAttributeOptionComboIdScheme]):
        category_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonge
            tCompleteRegistrationsXmlCategoryIdScheme]):
        category_option_combo_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegist
            rationsJsongetCompleteRegistrationsXmlCategoryOptionComboIdScheme]):
        category_option_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistration
            sJsongetCompleteRegistrationsXmlCategoryOptionIdScheme]):
        children (Union[Unset, bool]):  Default: False.
        created (Union[Unset, datetime.datetime]):
        created_duration (Union[Unset, str]):
        data_element_group_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrat
            ionsJsongetCompleteRegistrationsXmlDataElementGroupIdScheme]):
        data_element_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJs
            ongetCompleteRegistrationsXmlDataElementIdScheme]):
        data_set (Union[Unset, list[str]]):
        data_set_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonge
            tCompleteRegistrationsXmlDataSetIdScheme]):
        end_date (Union[Unset, datetime.datetime]):
        id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetComplete
            RegistrationsXmlIdScheme]):
        limit (Union[Unset, int]):
        org_unit (Union[Unset, list[str]]):
        org_unit_group (Union[Unset, list[str]]):
        org_unit_group_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrations
            JsongetCompleteRegistrationsXmlOrgUnitGroupIdScheme]):
        org_unit_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonge
            tCompleteRegistrationsXmlOrgUnitIdScheme]):
        period (Union[Unset, list[str]]):
        program_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonget
            CompleteRegistrationsXmlProgramIdScheme]):
        program_stage_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJ
            songetCompleteRegistrationsXmlProgramStageIdScheme]):
        program_stage_instance_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegis
            trationsJsongetCompleteRegistrationsXmlProgramStageInstanceIdScheme]):
        start_date (Union[Unset, datetime.datetime]):
        tracked_entity_attribute_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteReg
            istrationsJsongetCompleteRegistrationsXmlTrackedEntityAttributeIdScheme]):
        tracked_entity_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrations
            JsongetCompleteRegistrationsXmlTrackedEntityIdScheme]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attribute_option_combo_id_scheme=attribute_option_combo_id_scheme,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        children=children,
        created=created,
        created_duration=created_duration,
        data_element_group_id_scheme=data_element_group_id_scheme,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        end_date=end_date,
        id_scheme=id_scheme,
        limit=limit,
        org_unit=org_unit,
        org_unit_group=org_unit_group,
        org_unit_group_id_scheme=org_unit_group_id_scheme,
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


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute_option_combo_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlAttributeOptionComboIdScheme,
    ] = UNSET,
    category_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryIdScheme
    ] = UNSET,
    category_option_combo_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionComboIdScheme,
    ] = UNSET,
    category_option_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlCategoryOptionIdScheme
    ] = UNSET,
    children: Union[Unset, bool] = False,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_duration: Union[Unset, str] = UNSET,
    data_element_group_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementGroupIdScheme,
    ] = UNSET,
    data_element_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataElementIdScheme
    ] = UNSET,
    data_set: Union[Unset, list[str]] = UNSET,
    data_set_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlDataSetIdScheme
    ] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlIdScheme
    ] = UNSET,
    limit: Union[Unset, int] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_group: Union[Unset, list[str]] = UNSET,
    org_unit_group_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitGroupIdScheme
    ] = UNSET,
    org_unit_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlOrgUnitIdScheme
    ] = UNSET,
    period: Union[Unset, list[str]] = UNSET,
    program_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramIdScheme
    ] = UNSET,
    program_stage_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageIdScheme
    ] = UNSET,
    program_stage_instance_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlProgramStageInstanceIdScheme,
    ] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tracked_entity_attribute_id_scheme: Union[
        Unset,
        CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityAttributeIdScheme,
    ] = UNSET,
    tracked_entity_id_scheme: Union[
        Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetCompleteRegistrationsXmlTrackedEntityIdScheme
    ] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        attribute_option_combo_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegis
            trationsJsongetCompleteRegistrationsXmlAttributeOptionComboIdScheme]):
        category_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonge
            tCompleteRegistrationsXmlCategoryIdScheme]):
        category_option_combo_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegist
            rationsJsongetCompleteRegistrationsXmlCategoryOptionComboIdScheme]):
        category_option_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistration
            sJsongetCompleteRegistrationsXmlCategoryOptionIdScheme]):
        children (Union[Unset, bool]):  Default: False.
        created (Union[Unset, datetime.datetime]):
        created_duration (Union[Unset, str]):
        data_element_group_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrat
            ionsJsongetCompleteRegistrationsXmlDataElementGroupIdScheme]):
        data_element_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJs
            ongetCompleteRegistrationsXmlDataElementIdScheme]):
        data_set (Union[Unset, list[str]]):
        data_set_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonge
            tCompleteRegistrationsXmlDataSetIdScheme]):
        end_date (Union[Unset, datetime.datetime]):
        id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsongetComplete
            RegistrationsXmlIdScheme]):
        limit (Union[Unset, int]):
        org_unit (Union[Unset, list[str]]):
        org_unit_group (Union[Unset, list[str]]):
        org_unit_group_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrations
            JsongetCompleteRegistrationsXmlOrgUnitGroupIdScheme]):
        org_unit_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonge
            tCompleteRegistrationsXmlOrgUnitIdScheme]):
        period (Union[Unset, list[str]]):
        program_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJsonget
            CompleteRegistrationsXmlProgramIdScheme]):
        program_stage_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrationsJ
            songetCompleteRegistrationsXmlProgramStageIdScheme]):
        program_stage_instance_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegis
            trationsJsongetCompleteRegistrationsXmlProgramStageInstanceIdScheme]):
        start_date (Union[Unset, datetime.datetime]):
        tracked_entity_attribute_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteReg
            istrationsJsongetCompleteRegistrationsXmlTrackedEntityAttributeIdScheme]):
        tracked_entity_id_scheme (Union[Unset, CompleteDataSetRegistrationGetCompleteRegistrations
            JsongetCompleteRegistrationsXmlTrackedEntityIdScheme]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attribute_option_combo_id_scheme=attribute_option_combo_id_scheme,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        children=children,
        created=created,
        created_duration=created_duration,
        data_element_group_id_scheme=data_element_group_id_scheme,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        end_date=end_date,
        id_scheme=id_scheme,
        limit=limit,
        org_unit=org_unit,
        org_unit_group=org_unit_group,
        org_unit_group_id_scheme=org_unit_group_id_scheme,
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
