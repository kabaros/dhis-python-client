from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_data_set_registration_post_complete_registrations_xmlpost_complete_registrations_json_import_strategy import (
    CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy,
)
from ...models.complete_data_set_registration_post_complete_registrations_xmlpost_complete_registrations_json_merge_mode import (
    CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode,
)
from ...models.complete_data_set_registration_post_complete_registrations_xmlpost_complete_registrations_json_notification_level import (
    CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonNotificationLevel,
)
from ...models.complete_data_set_registration_post_complete_registrations_xmlpost_complete_registrations_json_report_mode import (
    CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    async_: Union[Unset, bool] = False,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, str] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    dataset_allows_periods: Union[Unset, bool] = False,
    dry_run: Union[Unset, bool] = False,
    event_id_scheme: Union[Unset, str] = UNSET,
    filename: Union[Unset, str] = UNSET,
    first_row_is_header: Union[Unset, bool] = True,
    force: Union[Unset, bool] = False,
    id_scheme: Union[Unset, str] = UNSET,
    ignore_empty_collection: Union[Unset, bool] = False,
    import_strategy: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE,
    merge_data_values: Union[Unset, bool] = False,
    merge_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE,
    notification_level: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonNotificationLevel
    ] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    preheat_cache: Union[Unset, bool] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    report_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode.FULL,
    require_attribute_option_combo: Union[Unset, bool] = False,
    require_category_option_combo: Union[Unset, bool] = False,
    sharing: Union[Unset, bool] = False,
    skip_audit: Union[Unset, bool] = False,
    skip_cache: Union[Unset, bool] = False,
    skip_existing_check: Union[Unset, bool] = False,
    skip_last_updated: Union[Unset, bool] = False,
    skip_notifications: Union[Unset, bool] = False,
    skip_pattern_validation: Union[Unset, bool] = False,
    strict_attribute_option_combos: Union[Unset, bool] = False,
    strict_category_option_combos: Union[Unset, bool] = False,
    strict_data_elements: Union[Unset, bool] = False,
    strict_data_set_approval: Union[Unset, bool] = False,
    strict_data_set_input_periods: Union[Unset, bool] = False,
    strict_data_set_locking: Union[Unset, bool] = False,
    strict_organisation_units: Union[Unset, bool] = False,
    strict_periods: Union[Unset, bool] = False,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["async"] = async_

    params["categoryIdScheme"] = category_id_scheme

    params["categoryOptionComboIdScheme"] = category_option_combo_id_scheme

    params["categoryOptionIdScheme"] = category_option_id_scheme

    params["dataElementIdScheme"] = data_element_id_scheme

    params["dataSet"] = data_set

    params["dataSetIdScheme"] = data_set_id_scheme

    params["datasetAllowsPeriods"] = dataset_allows_periods

    params["dryRun"] = dry_run

    params["eventIdScheme"] = event_id_scheme

    params["filename"] = filename

    params["firstRowIsHeader"] = first_row_is_header

    params["force"] = force

    params["idScheme"] = id_scheme

    params["ignoreEmptyCollection"] = ignore_empty_collection

    json_import_strategy: Union[Unset, str] = UNSET
    if not isinstance(import_strategy, Unset):
        json_import_strategy = import_strategy.value

    params["importStrategy"] = json_import_strategy

    params["mergeDataValues"] = merge_data_values

    json_merge_mode: Union[Unset, str] = UNSET
    if not isinstance(merge_mode, Unset):
        json_merge_mode = merge_mode.value

    params["mergeMode"] = json_merge_mode

    json_notification_level: Union[Unset, str] = UNSET
    if not isinstance(notification_level, Unset):
        json_notification_level = notification_level.value

    params["notificationLevel"] = json_notification_level

    params["orgUnitIdScheme"] = org_unit_id_scheme

    params["preheatCache"] = preheat_cache

    params["programIdScheme"] = program_id_scheme

    params["programStageIdScheme"] = program_stage_id_scheme

    json_report_mode: Union[Unset, str] = UNSET
    if not isinstance(report_mode, Unset):
        json_report_mode = report_mode.value

    params["reportMode"] = json_report_mode

    params["requireAttributeOptionCombo"] = require_attribute_option_combo

    params["requireCategoryOptionCombo"] = require_category_option_combo

    params["sharing"] = sharing

    params["skipAudit"] = skip_audit

    params["skipCache"] = skip_cache

    params["skipExistingCheck"] = skip_existing_check

    params["skipLastUpdated"] = skip_last_updated

    params["skipNotifications"] = skip_notifications

    params["skipPatternValidation"] = skip_pattern_validation

    params["strictAttributeOptionCombos"] = strict_attribute_option_combos

    params["strictCategoryOptionCombos"] = strict_category_option_combos

    params["strictDataElements"] = strict_data_elements

    params["strictDataSetApproval"] = strict_data_set_approval

    params["strictDataSetInputPeriods"] = strict_data_set_input_periods

    params["strictDataSetLocking"] = strict_data_set_locking

    params["strictOrganisationUnits"] = strict_organisation_units

    params["strictPeriods"] = strict_periods

    params["trackedEntityAttributeIdScheme"] = tracked_entity_attribute_id_scheme

    params["trackedEntityIdScheme"] = tracked_entity_id_scheme

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/completeDataSetRegistrations/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, str] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    dataset_allows_periods: Union[Unset, bool] = False,
    dry_run: Union[Unset, bool] = False,
    event_id_scheme: Union[Unset, str] = UNSET,
    filename: Union[Unset, str] = UNSET,
    first_row_is_header: Union[Unset, bool] = True,
    force: Union[Unset, bool] = False,
    id_scheme: Union[Unset, str] = UNSET,
    ignore_empty_collection: Union[Unset, bool] = False,
    import_strategy: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE,
    merge_data_values: Union[Unset, bool] = False,
    merge_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE,
    notification_level: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonNotificationLevel
    ] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    preheat_cache: Union[Unset, bool] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    report_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode.FULL,
    require_attribute_option_combo: Union[Unset, bool] = False,
    require_category_option_combo: Union[Unset, bool] = False,
    sharing: Union[Unset, bool] = False,
    skip_audit: Union[Unset, bool] = False,
    skip_cache: Union[Unset, bool] = False,
    skip_existing_check: Union[Unset, bool] = False,
    skip_last_updated: Union[Unset, bool] = False,
    skip_notifications: Union[Unset, bool] = False,
    skip_pattern_validation: Union[Unset, bool] = False,
    strict_attribute_option_combos: Union[Unset, bool] = False,
    strict_category_option_combos: Union[Unset, bool] = False,
    strict_data_elements: Union[Unset, bool] = False,
    strict_data_set_approval: Union[Unset, bool] = False,
    strict_data_set_input_periods: Union[Unset, bool] = False,
    strict_data_set_locking: Union[Unset, bool] = False,
    strict_organisation_units: Union[Unset, bool] = False,
    strict_periods: Union[Unset, bool] = False,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, str]):
        data_set_id_scheme (Union[Unset, str]):
        dataset_allows_periods (Union[Unset, bool]):  Default: False.
        dry_run (Union[Unset, bool]):  Default: False.
        event_id_scheme (Union[Unset, str]):
        filename (Union[Unset, str]):
        first_row_is_header (Union[Unset, bool]):  Default: True.
        force (Union[Unset, bool]):  Default: False.
        id_scheme (Union[Unset, str]):
        ignore_empty_collection (Union[Unset, bool]):  Default: False.
        import_strategy (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostC
            ompleteRegistrationsJsonImportStrategy]):  Default: CompleteDataSetRegistrationPostComplet
            eRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE.
        merge_data_values (Union[Unset, bool]):  Default: False.
        merge_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostComple
            teRegistrationsJsonMergeMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistrat
            ionsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE.
        notification_level (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpo
            stCompleteRegistrationsJsonNotificationLevel]):
        org_unit_id_scheme (Union[Unset, str]):
        preheat_cache (Union[Unset, bool]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        report_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompl
            eteRegistrationsJsonReportMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistr
            ationsXmlpostCompleteRegistrationsJsonReportMode.FULL.
        require_attribute_option_combo (Union[Unset, bool]):  Default: False.
        require_category_option_combo (Union[Unset, bool]):  Default: False.
        sharing (Union[Unset, bool]):  Default: False.
        skip_audit (Union[Unset, bool]):  Default: False.
        skip_cache (Union[Unset, bool]):  Default: False.
        skip_existing_check (Union[Unset, bool]):  Default: False.
        skip_last_updated (Union[Unset, bool]):  Default: False.
        skip_notifications (Union[Unset, bool]):  Default: False.
        skip_pattern_validation (Union[Unset, bool]):  Default: False.
        strict_attribute_option_combos (Union[Unset, bool]):  Default: False.
        strict_category_option_combos (Union[Unset, bool]):  Default: False.
        strict_data_elements (Union[Unset, bool]):  Default: False.
        strict_data_set_approval (Union[Unset, bool]):  Default: False.
        strict_data_set_input_periods (Union[Unset, bool]):  Default: False.
        strict_data_set_locking (Union[Unset, bool]):  Default: False.
        strict_organisation_units (Union[Unset, bool]):  Default: False.
        strict_periods (Union[Unset, bool]):  Default: False.
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        async_=async_,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        dataset_allows_periods=dataset_allows_periods,
        dry_run=dry_run,
        event_id_scheme=event_id_scheme,
        filename=filename,
        first_row_is_header=first_row_is_header,
        force=force,
        id_scheme=id_scheme,
        ignore_empty_collection=ignore_empty_collection,
        import_strategy=import_strategy,
        merge_data_values=merge_data_values,
        merge_mode=merge_mode,
        notification_level=notification_level,
        org_unit_id_scheme=org_unit_id_scheme,
        preheat_cache=preheat_cache,
        program_id_scheme=program_id_scheme,
        program_stage_id_scheme=program_stage_id_scheme,
        report_mode=report_mode,
        require_attribute_option_combo=require_attribute_option_combo,
        require_category_option_combo=require_category_option_combo,
        sharing=sharing,
        skip_audit=skip_audit,
        skip_cache=skip_cache,
        skip_existing_check=skip_existing_check,
        skip_last_updated=skip_last_updated,
        skip_notifications=skip_notifications,
        skip_pattern_validation=skip_pattern_validation,
        strict_attribute_option_combos=strict_attribute_option_combos,
        strict_category_option_combos=strict_category_option_combos,
        strict_data_elements=strict_data_elements,
        strict_data_set_approval=strict_data_set_approval,
        strict_data_set_input_periods=strict_data_set_input_periods,
        strict_data_set_locking=strict_data_set_locking,
        strict_organisation_units=strict_organisation_units,
        strict_periods=strict_periods,
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
    async_: Union[Unset, bool] = False,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, str] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    dataset_allows_periods: Union[Unset, bool] = False,
    dry_run: Union[Unset, bool] = False,
    event_id_scheme: Union[Unset, str] = UNSET,
    filename: Union[Unset, str] = UNSET,
    first_row_is_header: Union[Unset, bool] = True,
    force: Union[Unset, bool] = False,
    id_scheme: Union[Unset, str] = UNSET,
    ignore_empty_collection: Union[Unset, bool] = False,
    import_strategy: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE,
    merge_data_values: Union[Unset, bool] = False,
    merge_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE,
    notification_level: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonNotificationLevel
    ] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    preheat_cache: Union[Unset, bool] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    report_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode.FULL,
    require_attribute_option_combo: Union[Unset, bool] = False,
    require_category_option_combo: Union[Unset, bool] = False,
    sharing: Union[Unset, bool] = False,
    skip_audit: Union[Unset, bool] = False,
    skip_cache: Union[Unset, bool] = False,
    skip_existing_check: Union[Unset, bool] = False,
    skip_last_updated: Union[Unset, bool] = False,
    skip_notifications: Union[Unset, bool] = False,
    skip_pattern_validation: Union[Unset, bool] = False,
    strict_attribute_option_combos: Union[Unset, bool] = False,
    strict_category_option_combos: Union[Unset, bool] = False,
    strict_data_elements: Union[Unset, bool] = False,
    strict_data_set_approval: Union[Unset, bool] = False,
    strict_data_set_input_periods: Union[Unset, bool] = False,
    strict_data_set_locking: Union[Unset, bool] = False,
    strict_organisation_units: Union[Unset, bool] = False,
    strict_periods: Union[Unset, bool] = False,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, str]):
        data_set_id_scheme (Union[Unset, str]):
        dataset_allows_periods (Union[Unset, bool]):  Default: False.
        dry_run (Union[Unset, bool]):  Default: False.
        event_id_scheme (Union[Unset, str]):
        filename (Union[Unset, str]):
        first_row_is_header (Union[Unset, bool]):  Default: True.
        force (Union[Unset, bool]):  Default: False.
        id_scheme (Union[Unset, str]):
        ignore_empty_collection (Union[Unset, bool]):  Default: False.
        import_strategy (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostC
            ompleteRegistrationsJsonImportStrategy]):  Default: CompleteDataSetRegistrationPostComplet
            eRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE.
        merge_data_values (Union[Unset, bool]):  Default: False.
        merge_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostComple
            teRegistrationsJsonMergeMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistrat
            ionsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE.
        notification_level (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpo
            stCompleteRegistrationsJsonNotificationLevel]):
        org_unit_id_scheme (Union[Unset, str]):
        preheat_cache (Union[Unset, bool]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        report_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompl
            eteRegistrationsJsonReportMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistr
            ationsXmlpostCompleteRegistrationsJsonReportMode.FULL.
        require_attribute_option_combo (Union[Unset, bool]):  Default: False.
        require_category_option_combo (Union[Unset, bool]):  Default: False.
        sharing (Union[Unset, bool]):  Default: False.
        skip_audit (Union[Unset, bool]):  Default: False.
        skip_cache (Union[Unset, bool]):  Default: False.
        skip_existing_check (Union[Unset, bool]):  Default: False.
        skip_last_updated (Union[Unset, bool]):  Default: False.
        skip_notifications (Union[Unset, bool]):  Default: False.
        skip_pattern_validation (Union[Unset, bool]):  Default: False.
        strict_attribute_option_combos (Union[Unset, bool]):  Default: False.
        strict_category_option_combos (Union[Unset, bool]):  Default: False.
        strict_data_elements (Union[Unset, bool]):  Default: False.
        strict_data_set_approval (Union[Unset, bool]):  Default: False.
        strict_data_set_input_periods (Union[Unset, bool]):  Default: False.
        strict_data_set_locking (Union[Unset, bool]):  Default: False.
        strict_organisation_units (Union[Unset, bool]):  Default: False.
        strict_periods (Union[Unset, bool]):  Default: False.
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        async_=async_,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        dataset_allows_periods=dataset_allows_periods,
        dry_run=dry_run,
        event_id_scheme=event_id_scheme,
        filename=filename,
        first_row_is_header=first_row_is_header,
        force=force,
        id_scheme=id_scheme,
        ignore_empty_collection=ignore_empty_collection,
        import_strategy=import_strategy,
        merge_data_values=merge_data_values,
        merge_mode=merge_mode,
        notification_level=notification_level,
        org_unit_id_scheme=org_unit_id_scheme,
        preheat_cache=preheat_cache,
        program_id_scheme=program_id_scheme,
        program_stage_id_scheme=program_stage_id_scheme,
        report_mode=report_mode,
        require_attribute_option_combo=require_attribute_option_combo,
        require_category_option_combo=require_category_option_combo,
        sharing=sharing,
        skip_audit=skip_audit,
        skip_cache=skip_cache,
        skip_existing_check=skip_existing_check,
        skip_last_updated=skip_last_updated,
        skip_notifications=skip_notifications,
        skip_pattern_validation=skip_pattern_validation,
        strict_attribute_option_combos=strict_attribute_option_combos,
        strict_category_option_combos=strict_category_option_combos,
        strict_data_elements=strict_data_elements,
        strict_data_set_approval=strict_data_set_approval,
        strict_data_set_input_periods=strict_data_set_input_periods,
        strict_data_set_locking=strict_data_set_locking,
        strict_organisation_units=strict_organisation_units,
        strict_periods=strict_periods,
        tracked_entity_attribute_id_scheme=tracked_entity_attribute_id_scheme,
        tracked_entity_id_scheme=tracked_entity_id_scheme,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, str] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    dataset_allows_periods: Union[Unset, bool] = False,
    dry_run: Union[Unset, bool] = False,
    event_id_scheme: Union[Unset, str] = UNSET,
    filename: Union[Unset, str] = UNSET,
    first_row_is_header: Union[Unset, bool] = True,
    force: Union[Unset, bool] = False,
    id_scheme: Union[Unset, str] = UNSET,
    ignore_empty_collection: Union[Unset, bool] = False,
    import_strategy: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE,
    merge_data_values: Union[Unset, bool] = False,
    merge_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE,
    notification_level: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonNotificationLevel
    ] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    preheat_cache: Union[Unset, bool] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    report_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode.FULL,
    require_attribute_option_combo: Union[Unset, bool] = False,
    require_category_option_combo: Union[Unset, bool] = False,
    sharing: Union[Unset, bool] = False,
    skip_audit: Union[Unset, bool] = False,
    skip_cache: Union[Unset, bool] = False,
    skip_existing_check: Union[Unset, bool] = False,
    skip_last_updated: Union[Unset, bool] = False,
    skip_notifications: Union[Unset, bool] = False,
    skip_pattern_validation: Union[Unset, bool] = False,
    strict_attribute_option_combos: Union[Unset, bool] = False,
    strict_category_option_combos: Union[Unset, bool] = False,
    strict_data_elements: Union[Unset, bool] = False,
    strict_data_set_approval: Union[Unset, bool] = False,
    strict_data_set_input_periods: Union[Unset, bool] = False,
    strict_data_set_locking: Union[Unset, bool] = False,
    strict_organisation_units: Union[Unset, bool] = False,
    strict_periods: Union[Unset, bool] = False,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, str]):
        data_set_id_scheme (Union[Unset, str]):
        dataset_allows_periods (Union[Unset, bool]):  Default: False.
        dry_run (Union[Unset, bool]):  Default: False.
        event_id_scheme (Union[Unset, str]):
        filename (Union[Unset, str]):
        first_row_is_header (Union[Unset, bool]):  Default: True.
        force (Union[Unset, bool]):  Default: False.
        id_scheme (Union[Unset, str]):
        ignore_empty_collection (Union[Unset, bool]):  Default: False.
        import_strategy (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostC
            ompleteRegistrationsJsonImportStrategy]):  Default: CompleteDataSetRegistrationPostComplet
            eRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE.
        merge_data_values (Union[Unset, bool]):  Default: False.
        merge_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostComple
            teRegistrationsJsonMergeMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistrat
            ionsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE.
        notification_level (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpo
            stCompleteRegistrationsJsonNotificationLevel]):
        org_unit_id_scheme (Union[Unset, str]):
        preheat_cache (Union[Unset, bool]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        report_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompl
            eteRegistrationsJsonReportMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistr
            ationsXmlpostCompleteRegistrationsJsonReportMode.FULL.
        require_attribute_option_combo (Union[Unset, bool]):  Default: False.
        require_category_option_combo (Union[Unset, bool]):  Default: False.
        sharing (Union[Unset, bool]):  Default: False.
        skip_audit (Union[Unset, bool]):  Default: False.
        skip_cache (Union[Unset, bool]):  Default: False.
        skip_existing_check (Union[Unset, bool]):  Default: False.
        skip_last_updated (Union[Unset, bool]):  Default: False.
        skip_notifications (Union[Unset, bool]):  Default: False.
        skip_pattern_validation (Union[Unset, bool]):  Default: False.
        strict_attribute_option_combos (Union[Unset, bool]):  Default: False.
        strict_category_option_combos (Union[Unset, bool]):  Default: False.
        strict_data_elements (Union[Unset, bool]):  Default: False.
        strict_data_set_approval (Union[Unset, bool]):  Default: False.
        strict_data_set_input_periods (Union[Unset, bool]):  Default: False.
        strict_data_set_locking (Union[Unset, bool]):  Default: False.
        strict_organisation_units (Union[Unset, bool]):  Default: False.
        strict_periods (Union[Unset, bool]):  Default: False.
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        async_=async_,
        category_id_scheme=category_id_scheme,
        category_option_combo_id_scheme=category_option_combo_id_scheme,
        category_option_id_scheme=category_option_id_scheme,
        data_element_id_scheme=data_element_id_scheme,
        data_set=data_set,
        data_set_id_scheme=data_set_id_scheme,
        dataset_allows_periods=dataset_allows_periods,
        dry_run=dry_run,
        event_id_scheme=event_id_scheme,
        filename=filename,
        first_row_is_header=first_row_is_header,
        force=force,
        id_scheme=id_scheme,
        ignore_empty_collection=ignore_empty_collection,
        import_strategy=import_strategy,
        merge_data_values=merge_data_values,
        merge_mode=merge_mode,
        notification_level=notification_level,
        org_unit_id_scheme=org_unit_id_scheme,
        preheat_cache=preheat_cache,
        program_id_scheme=program_id_scheme,
        program_stage_id_scheme=program_stage_id_scheme,
        report_mode=report_mode,
        require_attribute_option_combo=require_attribute_option_combo,
        require_category_option_combo=require_category_option_combo,
        sharing=sharing,
        skip_audit=skip_audit,
        skip_cache=skip_cache,
        skip_existing_check=skip_existing_check,
        skip_last_updated=skip_last_updated,
        skip_notifications=skip_notifications,
        skip_pattern_validation=skip_pattern_validation,
        strict_attribute_option_combos=strict_attribute_option_combos,
        strict_category_option_combos=strict_category_option_combos,
        strict_data_elements=strict_data_elements,
        strict_data_set_approval=strict_data_set_approval,
        strict_data_set_input_periods=strict_data_set_input_periods,
        strict_data_set_locking=strict_data_set_locking,
        strict_organisation_units=strict_organisation_units,
        strict_periods=strict_periods,
        tracked_entity_attribute_id_scheme=tracked_entity_attribute_id_scheme,
        tracked_entity_id_scheme=tracked_entity_id_scheme,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    category_id_scheme: Union[Unset, str] = UNSET,
    category_option_combo_id_scheme: Union[Unset, str] = UNSET,
    category_option_id_scheme: Union[Unset, str] = UNSET,
    data_element_id_scheme: Union[Unset, str] = UNSET,
    data_set: Union[Unset, str] = UNSET,
    data_set_id_scheme: Union[Unset, str] = UNSET,
    dataset_allows_periods: Union[Unset, bool] = False,
    dry_run: Union[Unset, bool] = False,
    event_id_scheme: Union[Unset, str] = UNSET,
    filename: Union[Unset, str] = UNSET,
    first_row_is_header: Union[Unset, bool] = True,
    force: Union[Unset, bool] = False,
    id_scheme: Union[Unset, str] = UNSET,
    ignore_empty_collection: Union[Unset, bool] = False,
    import_strategy: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE,
    merge_data_values: Union[Unset, bool] = False,
    merge_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE,
    notification_level: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonNotificationLevel
    ] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = UNSET,
    preheat_cache: Union[Unset, bool] = UNSET,
    program_id_scheme: Union[Unset, str] = UNSET,
    program_stage_id_scheme: Union[Unset, str] = UNSET,
    report_mode: Union[
        Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode
    ] = CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompleteRegistrationsJsonReportMode.FULL,
    require_attribute_option_combo: Union[Unset, bool] = False,
    require_category_option_combo: Union[Unset, bool] = False,
    sharing: Union[Unset, bool] = False,
    skip_audit: Union[Unset, bool] = False,
    skip_cache: Union[Unset, bool] = False,
    skip_existing_check: Union[Unset, bool] = False,
    skip_last_updated: Union[Unset, bool] = False,
    skip_notifications: Union[Unset, bool] = False,
    skip_pattern_validation: Union[Unset, bool] = False,
    strict_attribute_option_combos: Union[Unset, bool] = False,
    strict_category_option_combos: Union[Unset, bool] = False,
    strict_data_elements: Union[Unset, bool] = False,
    strict_data_set_approval: Union[Unset, bool] = False,
    strict_data_set_input_periods: Union[Unset, bool] = False,
    strict_data_set_locking: Union[Unset, bool] = False,
    strict_organisation_units: Union[Unset, bool] = False,
    strict_periods: Union[Unset, bool] = False,
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET,
    tracked_entity_id_scheme: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, str]):
        data_set_id_scheme (Union[Unset, str]):
        dataset_allows_periods (Union[Unset, bool]):  Default: False.
        dry_run (Union[Unset, bool]):  Default: False.
        event_id_scheme (Union[Unset, str]):
        filename (Union[Unset, str]):
        first_row_is_header (Union[Unset, bool]):  Default: True.
        force (Union[Unset, bool]):  Default: False.
        id_scheme (Union[Unset, str]):
        ignore_empty_collection (Union[Unset, bool]):  Default: False.
        import_strategy (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostC
            ompleteRegistrationsJsonImportStrategy]):  Default: CompleteDataSetRegistrationPostComplet
            eRegistrationsXmlpostCompleteRegistrationsJsonImportStrategy.CREATE_AND_UPDATE.
        merge_data_values (Union[Unset, bool]):  Default: False.
        merge_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostComple
            teRegistrationsJsonMergeMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistrat
            ionsXmlpostCompleteRegistrationsJsonMergeMode.REPLACE.
        notification_level (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpo
            stCompleteRegistrationsJsonNotificationLevel]):
        org_unit_id_scheme (Union[Unset, str]):
        preheat_cache (Union[Unset, bool]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        report_mode (Union[Unset, CompleteDataSetRegistrationPostCompleteRegistrationsXmlpostCompl
            eteRegistrationsJsonReportMode]):  Default: CompleteDataSetRegistrationPostCompleteRegistr
            ationsXmlpostCompleteRegistrationsJsonReportMode.FULL.
        require_attribute_option_combo (Union[Unset, bool]):  Default: False.
        require_category_option_combo (Union[Unset, bool]):  Default: False.
        sharing (Union[Unset, bool]):  Default: False.
        skip_audit (Union[Unset, bool]):  Default: False.
        skip_cache (Union[Unset, bool]):  Default: False.
        skip_existing_check (Union[Unset, bool]):  Default: False.
        skip_last_updated (Union[Unset, bool]):  Default: False.
        skip_notifications (Union[Unset, bool]):  Default: False.
        skip_pattern_validation (Union[Unset, bool]):  Default: False.
        strict_attribute_option_combos (Union[Unset, bool]):  Default: False.
        strict_category_option_combos (Union[Unset, bool]):  Default: False.
        strict_data_elements (Union[Unset, bool]):  Default: False.
        strict_data_set_approval (Union[Unset, bool]):  Default: False.
        strict_data_set_input_periods (Union[Unset, bool]):  Default: False.
        strict_data_set_locking (Union[Unset, bool]):  Default: False.
        strict_organisation_units (Union[Unset, bool]):  Default: False.
        strict_periods (Union[Unset, bool]):  Default: False.
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            async_=async_,
            category_id_scheme=category_id_scheme,
            category_option_combo_id_scheme=category_option_combo_id_scheme,
            category_option_id_scheme=category_option_id_scheme,
            data_element_id_scheme=data_element_id_scheme,
            data_set=data_set,
            data_set_id_scheme=data_set_id_scheme,
            dataset_allows_periods=dataset_allows_periods,
            dry_run=dry_run,
            event_id_scheme=event_id_scheme,
            filename=filename,
            first_row_is_header=first_row_is_header,
            force=force,
            id_scheme=id_scheme,
            ignore_empty_collection=ignore_empty_collection,
            import_strategy=import_strategy,
            merge_data_values=merge_data_values,
            merge_mode=merge_mode,
            notification_level=notification_level,
            org_unit_id_scheme=org_unit_id_scheme,
            preheat_cache=preheat_cache,
            program_id_scheme=program_id_scheme,
            program_stage_id_scheme=program_stage_id_scheme,
            report_mode=report_mode,
            require_attribute_option_combo=require_attribute_option_combo,
            require_category_option_combo=require_category_option_combo,
            sharing=sharing,
            skip_audit=skip_audit,
            skip_cache=skip_cache,
            skip_existing_check=skip_existing_check,
            skip_last_updated=skip_last_updated,
            skip_notifications=skip_notifications,
            skip_pattern_validation=skip_pattern_validation,
            strict_attribute_option_combos=strict_attribute_option_combos,
            strict_category_option_combos=strict_category_option_combos,
            strict_data_elements=strict_data_elements,
            strict_data_set_approval=strict_data_set_approval,
            strict_data_set_input_periods=strict_data_set_input_periods,
            strict_data_set_locking=strict_data_set_locking,
            strict_organisation_units=strict_organisation_units,
            strict_periods=strict_periods,
            tracked_entity_attribute_id_scheme=tracked_entity_attribute_id_scheme,
            tracked_entity_id_scheme=tracked_entity_id_scheme,
        )
    ).parsed
