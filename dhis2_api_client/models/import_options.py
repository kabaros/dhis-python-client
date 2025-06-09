from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_options_import_strategy import ImportOptionsImportStrategy
from ..models.import_options_merge_mode import ImportOptionsMergeMode
from ..models.import_options_notification_level import ImportOptionsNotificationLevel
from ..models.import_options_report_mode import ImportOptionsReportMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportOptions")


@_attrs_define
class ImportOptions:
    """
    Attributes:
        import_strategy (ImportOptionsImportStrategy):
        merge_mode (ImportOptionsMergeMode):
        notification_level (ImportOptionsNotificationLevel):
        report_mode (ImportOptionsReportMode):
        async_ (Union[Unset, bool]):
        category_id_scheme (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        category_option_id_scheme (Union[Unset, str]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, str]):
        data_set_id_scheme (Union[Unset, str]):
        dataset_allows_periods (Union[Unset, bool]):
        dry_run (Union[Unset, bool]):
        event_id_scheme (Union[Unset, str]):
        filename (Union[Unset, str]):
        first_row_is_header (Union[Unset, bool]):
        force (Union[Unset, bool]):
        id_scheme (Union[Unset, str]):
        ignore_empty_collection (Union[Unset, bool]):
        merge_data_values (Union[Unset, bool]):
        org_unit_id_scheme (Union[Unset, str]):
        preheat_cache (Union[Unset, bool]):
        program_id_scheme (Union[Unset, str]):
        program_stage_id_scheme (Union[Unset, str]):
        require_attribute_option_combo (Union[Unset, bool]):
        require_category_option_combo (Union[Unset, bool]):
        sharing (Union[Unset, bool]):
        skip_audit (Union[Unset, bool]):
        skip_cache (Union[Unset, bool]):
        skip_existing_check (Union[Unset, bool]):
        skip_last_updated (Union[Unset, bool]):
        skip_notifications (Union[Unset, bool]):
        skip_pattern_validation (Union[Unset, bool]):
        strict_attribute_option_combos (Union[Unset, bool]):
        strict_category_option_combos (Union[Unset, bool]):
        strict_data_elements (Union[Unset, bool]):
        strict_data_set_approval (Union[Unset, bool]):
        strict_data_set_input_periods (Union[Unset, bool]):
        strict_data_set_locking (Union[Unset, bool]):
        strict_organisation_units (Union[Unset, bool]):
        strict_periods (Union[Unset, bool]):
        tracked_entity_attribute_id_scheme (Union[Unset, str]):
        tracked_entity_id_scheme (Union[Unset, str]):
    """

    import_strategy: ImportOptionsImportStrategy
    merge_mode: ImportOptionsMergeMode
    notification_level: ImportOptionsNotificationLevel
    report_mode: ImportOptionsReportMode
    async_: Union[Unset, bool] = UNSET
    category_id_scheme: Union[Unset, str] = UNSET
    category_option_combo_id_scheme: Union[Unset, str] = UNSET
    category_option_id_scheme: Union[Unset, str] = UNSET
    data_element_id_scheme: Union[Unset, str] = UNSET
    data_set: Union[Unset, str] = UNSET
    data_set_id_scheme: Union[Unset, str] = UNSET
    dataset_allows_periods: Union[Unset, bool] = UNSET
    dry_run: Union[Unset, bool] = UNSET
    event_id_scheme: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    first_row_is_header: Union[Unset, bool] = UNSET
    force: Union[Unset, bool] = UNSET
    id_scheme: Union[Unset, str] = UNSET
    ignore_empty_collection: Union[Unset, bool] = UNSET
    merge_data_values: Union[Unset, bool] = UNSET
    org_unit_id_scheme: Union[Unset, str] = UNSET
    preheat_cache: Union[Unset, bool] = UNSET
    program_id_scheme: Union[Unset, str] = UNSET
    program_stage_id_scheme: Union[Unset, str] = UNSET
    require_attribute_option_combo: Union[Unset, bool] = UNSET
    require_category_option_combo: Union[Unset, bool] = UNSET
    sharing: Union[Unset, bool] = UNSET
    skip_audit: Union[Unset, bool] = UNSET
    skip_cache: Union[Unset, bool] = UNSET
    skip_existing_check: Union[Unset, bool] = UNSET
    skip_last_updated: Union[Unset, bool] = UNSET
    skip_notifications: Union[Unset, bool] = UNSET
    skip_pattern_validation: Union[Unset, bool] = UNSET
    strict_attribute_option_combos: Union[Unset, bool] = UNSET
    strict_category_option_combos: Union[Unset, bool] = UNSET
    strict_data_elements: Union[Unset, bool] = UNSET
    strict_data_set_approval: Union[Unset, bool] = UNSET
    strict_data_set_input_periods: Union[Unset, bool] = UNSET
    strict_data_set_locking: Union[Unset, bool] = UNSET
    strict_organisation_units: Union[Unset, bool] = UNSET
    strict_periods: Union[Unset, bool] = UNSET
    tracked_entity_attribute_id_scheme: Union[Unset, str] = UNSET
    tracked_entity_id_scheme: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_strategy = self.import_strategy.value

        merge_mode = self.merge_mode.value

        notification_level = self.notification_level.value

        report_mode = self.report_mode.value

        async_ = self.async_

        category_id_scheme = self.category_id_scheme

        category_option_combo_id_scheme = self.category_option_combo_id_scheme

        category_option_id_scheme = self.category_option_id_scheme

        data_element_id_scheme = self.data_element_id_scheme

        data_set = self.data_set

        data_set_id_scheme = self.data_set_id_scheme

        dataset_allows_periods = self.dataset_allows_periods

        dry_run = self.dry_run

        event_id_scheme = self.event_id_scheme

        filename = self.filename

        first_row_is_header = self.first_row_is_header

        force = self.force

        id_scheme = self.id_scheme

        ignore_empty_collection = self.ignore_empty_collection

        merge_data_values = self.merge_data_values

        org_unit_id_scheme = self.org_unit_id_scheme

        preheat_cache = self.preheat_cache

        program_id_scheme = self.program_id_scheme

        program_stage_id_scheme = self.program_stage_id_scheme

        require_attribute_option_combo = self.require_attribute_option_combo

        require_category_option_combo = self.require_category_option_combo

        sharing = self.sharing

        skip_audit = self.skip_audit

        skip_cache = self.skip_cache

        skip_existing_check = self.skip_existing_check

        skip_last_updated = self.skip_last_updated

        skip_notifications = self.skip_notifications

        skip_pattern_validation = self.skip_pattern_validation

        strict_attribute_option_combos = self.strict_attribute_option_combos

        strict_category_option_combos = self.strict_category_option_combos

        strict_data_elements = self.strict_data_elements

        strict_data_set_approval = self.strict_data_set_approval

        strict_data_set_input_periods = self.strict_data_set_input_periods

        strict_data_set_locking = self.strict_data_set_locking

        strict_organisation_units = self.strict_organisation_units

        strict_periods = self.strict_periods

        tracked_entity_attribute_id_scheme = self.tracked_entity_attribute_id_scheme

        tracked_entity_id_scheme = self.tracked_entity_id_scheme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "importStrategy": import_strategy,
                "mergeMode": merge_mode,
                "notificationLevel": notification_level,
                "reportMode": report_mode,
            }
        )
        if async_ is not UNSET:
            field_dict["async"] = async_
        if category_id_scheme is not UNSET:
            field_dict["categoryIdScheme"] = category_id_scheme
        if category_option_combo_id_scheme is not UNSET:
            field_dict["categoryOptionComboIdScheme"] = category_option_combo_id_scheme
        if category_option_id_scheme is not UNSET:
            field_dict["categoryOptionIdScheme"] = category_option_id_scheme
        if data_element_id_scheme is not UNSET:
            field_dict["dataElementIdScheme"] = data_element_id_scheme
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
        if data_set_id_scheme is not UNSET:
            field_dict["dataSetIdScheme"] = data_set_id_scheme
        if dataset_allows_periods is not UNSET:
            field_dict["datasetAllowsPeriods"] = dataset_allows_periods
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if event_id_scheme is not UNSET:
            field_dict["eventIdScheme"] = event_id_scheme
        if filename is not UNSET:
            field_dict["filename"] = filename
        if first_row_is_header is not UNSET:
            field_dict["firstRowIsHeader"] = first_row_is_header
        if force is not UNSET:
            field_dict["force"] = force
        if id_scheme is not UNSET:
            field_dict["idScheme"] = id_scheme
        if ignore_empty_collection is not UNSET:
            field_dict["ignoreEmptyCollection"] = ignore_empty_collection
        if merge_data_values is not UNSET:
            field_dict["mergeDataValues"] = merge_data_values
        if org_unit_id_scheme is not UNSET:
            field_dict["orgUnitIdScheme"] = org_unit_id_scheme
        if preheat_cache is not UNSET:
            field_dict["preheatCache"] = preheat_cache
        if program_id_scheme is not UNSET:
            field_dict["programIdScheme"] = program_id_scheme
        if program_stage_id_scheme is not UNSET:
            field_dict["programStageIdScheme"] = program_stage_id_scheme
        if require_attribute_option_combo is not UNSET:
            field_dict["requireAttributeOptionCombo"] = require_attribute_option_combo
        if require_category_option_combo is not UNSET:
            field_dict["requireCategoryOptionCombo"] = require_category_option_combo
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if skip_audit is not UNSET:
            field_dict["skipAudit"] = skip_audit
        if skip_cache is not UNSET:
            field_dict["skipCache"] = skip_cache
        if skip_existing_check is not UNSET:
            field_dict["skipExistingCheck"] = skip_existing_check
        if skip_last_updated is not UNSET:
            field_dict["skipLastUpdated"] = skip_last_updated
        if skip_notifications is not UNSET:
            field_dict["skipNotifications"] = skip_notifications
        if skip_pattern_validation is not UNSET:
            field_dict["skipPatternValidation"] = skip_pattern_validation
        if strict_attribute_option_combos is not UNSET:
            field_dict["strictAttributeOptionCombos"] = strict_attribute_option_combos
        if strict_category_option_combos is not UNSET:
            field_dict["strictCategoryOptionCombos"] = strict_category_option_combos
        if strict_data_elements is not UNSET:
            field_dict["strictDataElements"] = strict_data_elements
        if strict_data_set_approval is not UNSET:
            field_dict["strictDataSetApproval"] = strict_data_set_approval
        if strict_data_set_input_periods is not UNSET:
            field_dict["strictDataSetInputPeriods"] = strict_data_set_input_periods
        if strict_data_set_locking is not UNSET:
            field_dict["strictDataSetLocking"] = strict_data_set_locking
        if strict_organisation_units is not UNSET:
            field_dict["strictOrganisationUnits"] = strict_organisation_units
        if strict_periods is not UNSET:
            field_dict["strictPeriods"] = strict_periods
        if tracked_entity_attribute_id_scheme is not UNSET:
            field_dict["trackedEntityAttributeIdScheme"] = tracked_entity_attribute_id_scheme
        if tracked_entity_id_scheme is not UNSET:
            field_dict["trackedEntityIdScheme"] = tracked_entity_id_scheme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        import_strategy = ImportOptionsImportStrategy(d.pop("importStrategy"))

        merge_mode = ImportOptionsMergeMode(d.pop("mergeMode"))

        notification_level = ImportOptionsNotificationLevel(d.pop("notificationLevel"))

        report_mode = ImportOptionsReportMode(d.pop("reportMode"))

        async_ = d.pop("async", UNSET)

        category_id_scheme = d.pop("categoryIdScheme", UNSET)

        category_option_combo_id_scheme = d.pop("categoryOptionComboIdScheme", UNSET)

        category_option_id_scheme = d.pop("categoryOptionIdScheme", UNSET)

        data_element_id_scheme = d.pop("dataElementIdScheme", UNSET)

        data_set = d.pop("dataSet", UNSET)

        data_set_id_scheme = d.pop("dataSetIdScheme", UNSET)

        dataset_allows_periods = d.pop("datasetAllowsPeriods", UNSET)

        dry_run = d.pop("dryRun", UNSET)

        event_id_scheme = d.pop("eventIdScheme", UNSET)

        filename = d.pop("filename", UNSET)

        first_row_is_header = d.pop("firstRowIsHeader", UNSET)

        force = d.pop("force", UNSET)

        id_scheme = d.pop("idScheme", UNSET)

        ignore_empty_collection = d.pop("ignoreEmptyCollection", UNSET)

        merge_data_values = d.pop("mergeDataValues", UNSET)

        org_unit_id_scheme = d.pop("orgUnitIdScheme", UNSET)

        preheat_cache = d.pop("preheatCache", UNSET)

        program_id_scheme = d.pop("programIdScheme", UNSET)

        program_stage_id_scheme = d.pop("programStageIdScheme", UNSET)

        require_attribute_option_combo = d.pop("requireAttributeOptionCombo", UNSET)

        require_category_option_combo = d.pop("requireCategoryOptionCombo", UNSET)

        sharing = d.pop("sharing", UNSET)

        skip_audit = d.pop("skipAudit", UNSET)

        skip_cache = d.pop("skipCache", UNSET)

        skip_existing_check = d.pop("skipExistingCheck", UNSET)

        skip_last_updated = d.pop("skipLastUpdated", UNSET)

        skip_notifications = d.pop("skipNotifications", UNSET)

        skip_pattern_validation = d.pop("skipPatternValidation", UNSET)

        strict_attribute_option_combos = d.pop("strictAttributeOptionCombos", UNSET)

        strict_category_option_combos = d.pop("strictCategoryOptionCombos", UNSET)

        strict_data_elements = d.pop("strictDataElements", UNSET)

        strict_data_set_approval = d.pop("strictDataSetApproval", UNSET)

        strict_data_set_input_periods = d.pop("strictDataSetInputPeriods", UNSET)

        strict_data_set_locking = d.pop("strictDataSetLocking", UNSET)

        strict_organisation_units = d.pop("strictOrganisationUnits", UNSET)

        strict_periods = d.pop("strictPeriods", UNSET)

        tracked_entity_attribute_id_scheme = d.pop("trackedEntityAttributeIdScheme", UNSET)

        tracked_entity_id_scheme = d.pop("trackedEntityIdScheme", UNSET)

        import_options = cls(
            import_strategy=import_strategy,
            merge_mode=merge_mode,
            notification_level=notification_level,
            report_mode=report_mode,
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
            merge_data_values=merge_data_values,
            org_unit_id_scheme=org_unit_id_scheme,
            preheat_cache=preheat_cache,
            program_id_scheme=program_id_scheme,
            program_stage_id_scheme=program_stage_id_scheme,
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

        import_options.additional_properties = d
        return import_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
