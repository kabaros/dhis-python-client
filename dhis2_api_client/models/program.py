import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_access_level import ProgramAccessLevel
from ..models.program_expiry_period_type import ProgramExpiryPeriodType
from ..models.program_feature_type import ProgramFeatureType
from ..models.program_program_type import ProgramProgramType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.object_style import ObjectStyle
    from ..models.program_category_combo import ProgramCategoryCombo
    from ..models.program_created_by import ProgramCreatedBy
    from ..models.program_data_entry_form import ProgramDataEntryForm
    from ..models.program_last_updated_by import ProgramLastUpdatedBy
    from ..models.program_notification_templates_item import ProgramNotificationTemplatesItem
    from ..models.program_organisation_units_item import ProgramOrganisationUnitsItem
    from ..models.program_program_indicators_item import ProgramProgramIndicatorsItem
    from ..models.program_program_rule_variables_item import ProgramProgramRuleVariablesItem
    from ..models.program_program_sections_item import ProgramProgramSectionsItem
    from ..models.program_program_stages_item import ProgramProgramStagesItem
    from ..models.program_related_program import ProgramRelatedProgram
    from ..models.program_tracked_entity_attribute import ProgramTrackedEntityAttribute
    from ..models.program_tracked_entity_type import ProgramTrackedEntityType
    from ..models.program_user import ProgramUser
    from ..models.program_user_roles_item import ProgramUserRolesItem
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Program")


@_attrs_define
class Program:
    """
    Attributes:
        access_level (ProgramAccessLevel):
        complete_events_expiry_days (int):
        expiry_days (int):
        feature_type (ProgramFeatureType):
        max_tei_count_to_return (int):
        min_attributes_required_to_search (int):
        open_days_after_co_end_date (int):
        program_type (ProgramProgramType):
        version (int):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_combo (Union[Unset, ProgramCategoryCombo]): A UID reference to a CategoryCombo
            (Java name `org.hisp.dhis.category.CategoryCombo`)
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_entry_form (Union[Unset, ProgramDataEntryForm]): A UID reference to a DataEntryForm
            (Java name `org.hisp.dhis.dataentryform.DataEntryForm`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_enrollment_date_label (Union[Unset, str]):
        display_enrollment_label (Union[Unset, str]):
        display_event_label (Union[Unset, str]):
        display_follow_up_label (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_front_page_list (Union[Unset, bool]):
        display_incident_date (Union[Unset, bool]):
        display_incident_date_label (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_note_label (Union[Unset, str]):
        display_org_unit_label (Union[Unset, str]):
        display_program_stage_label (Union[Unset, str]):
        display_relationship_label (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        display_tracked_entity_attribute_label (Union[Unset, str]):
        enrollment_date_label (Union[Unset, str]):
        enrollment_label (Union[Unset, str]):
        event_label (Union[Unset, str]):
        expiry_period_type (Union[Unset, ProgramExpiryPeriodType]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        follow_up_label (Union[Unset, str]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        ignore_overdue_events (Union[Unset, bool]):
        incident_date_label (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        note_label (Union[Unset, str]):
        notification_templates (Union[Unset, list['ProgramNotificationTemplatesItem']]):
        only_enroll_once (Union[Unset, bool]):
        org_unit_label (Union[Unset, str]):
        organisation_units (Union[Unset, list['ProgramOrganisationUnitsItem']]):
        program_indicators (Union[Unset, list['ProgramProgramIndicatorsItem']]):
        program_rule_variables (Union[Unset, list['ProgramProgramRuleVariablesItem']]):
        program_sections (Union[Unset, list['ProgramProgramSectionsItem']]):
        program_stage_label (Union[Unset, str]):
        program_stages (Union[Unset, list['ProgramProgramStagesItem']]):
        program_tracked_entity_attributes (Union[Unset, list['ProgramTrackedEntityAttribute']]):
        registration (Union[Unset, bool]):
        related_program (Union[Unset, ProgramRelatedProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        relationship_label (Union[Unset, str]):
        select_enrollment_dates_in_future (Union[Unset, bool]):
        select_incident_dates_in_future (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        skip_offline (Union[Unset, bool]):
        style (Union[Unset, ObjectStyle]):
        tracked_entity_attribute_label (Union[Unset, str]):
        tracked_entity_type (Union[Unset, ProgramTrackedEntityType]): A UID reference to a TrackedEntityType
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`)
        translations (Union[Unset, list['Translation']]):
        use_first_stage_during_registration (Union[Unset, bool]):
        user (Union[Unset, ProgramUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_roles (Union[Unset, list['ProgramUserRolesItem']]):
        without_registration (Union[Unset, bool]):
    """

    access_level: ProgramAccessLevel
    complete_events_expiry_days: int
    expiry_days: int
    feature_type: ProgramFeatureType
    max_tei_count_to_return: int
    min_attributes_required_to_search: int
    open_days_after_co_end_date: int
    program_type: ProgramProgramType
    version: int
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_combo: Union[Unset, "ProgramCategoryCombo"] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramCreatedBy"] = UNSET
    data_entry_form: Union[Unset, "ProgramDataEntryForm"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_enrollment_date_label: Union[Unset, str] = UNSET
    display_enrollment_label: Union[Unset, str] = UNSET
    display_event_label: Union[Unset, str] = UNSET
    display_follow_up_label: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_front_page_list: Union[Unset, bool] = UNSET
    display_incident_date: Union[Unset, bool] = UNSET
    display_incident_date_label: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_note_label: Union[Unset, str] = UNSET
    display_org_unit_label: Union[Unset, str] = UNSET
    display_program_stage_label: Union[Unset, str] = UNSET
    display_relationship_label: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    display_tracked_entity_attribute_label: Union[Unset, str] = UNSET
    enrollment_date_label: Union[Unset, str] = UNSET
    enrollment_label: Union[Unset, str] = UNSET
    event_label: Union[Unset, str] = UNSET
    expiry_period_type: Union[Unset, ProgramExpiryPeriodType] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    follow_up_label: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ignore_overdue_events: Union[Unset, bool] = UNSET
    incident_date_label: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    note_label: Union[Unset, str] = UNSET
    notification_templates: Union[Unset, list["ProgramNotificationTemplatesItem"]] = UNSET
    only_enroll_once: Union[Unset, bool] = UNSET
    org_unit_label: Union[Unset, str] = UNSET
    organisation_units: Union[Unset, list["ProgramOrganisationUnitsItem"]] = UNSET
    program_indicators: Union[Unset, list["ProgramProgramIndicatorsItem"]] = UNSET
    program_rule_variables: Union[Unset, list["ProgramProgramRuleVariablesItem"]] = UNSET
    program_sections: Union[Unset, list["ProgramProgramSectionsItem"]] = UNSET
    program_stage_label: Union[Unset, str] = UNSET
    program_stages: Union[Unset, list["ProgramProgramStagesItem"]] = UNSET
    program_tracked_entity_attributes: Union[Unset, list["ProgramTrackedEntityAttribute"]] = UNSET
    registration: Union[Unset, bool] = UNSET
    related_program: Union[Unset, "ProgramRelatedProgram"] = UNSET
    relationship_label: Union[Unset, str] = UNSET
    select_enrollment_dates_in_future: Union[Unset, bool] = UNSET
    select_incident_dates_in_future: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    skip_offline: Union[Unset, bool] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    tracked_entity_attribute_label: Union[Unset, str] = UNSET
    tracked_entity_type: Union[Unset, "ProgramTrackedEntityType"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    use_first_stage_during_registration: Union[Unset, bool] = UNSET
    user: Union[Unset, "ProgramUser"] = UNSET
    user_roles: Union[Unset, list["ProgramUserRolesItem"]] = UNSET
    without_registration: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_level = self.access_level.value

        complete_events_expiry_days = self.complete_events_expiry_days

        expiry_days = self.expiry_days

        feature_type = self.feature_type.value

        max_tei_count_to_return = self.max_tei_count_to_return

        min_attributes_required_to_search = self.min_attributes_required_to_search

        open_days_after_co_end_date = self.open_days_after_co_end_date

        program_type = self.program_type.value

        version = self.version

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        category_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_combo, Unset):
            category_combo = self.category_combo.to_dict()

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_entry_form: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_entry_form, Unset):
            data_entry_form = self.data_entry_form.to_dict()

        description = self.description

        display_description = self.display_description

        display_enrollment_date_label = self.display_enrollment_date_label

        display_enrollment_label = self.display_enrollment_label

        display_event_label = self.display_event_label

        display_follow_up_label = self.display_follow_up_label

        display_form_name = self.display_form_name

        display_front_page_list = self.display_front_page_list

        display_incident_date = self.display_incident_date

        display_incident_date_label = self.display_incident_date_label

        display_name = self.display_name

        display_note_label = self.display_note_label

        display_org_unit_label = self.display_org_unit_label

        display_program_stage_label = self.display_program_stage_label

        display_relationship_label = self.display_relationship_label

        display_short_name = self.display_short_name

        display_tracked_entity_attribute_label = self.display_tracked_entity_attribute_label

        enrollment_date_label = self.enrollment_date_label

        enrollment_label = self.enrollment_label

        event_label = self.event_label

        expiry_period_type: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_period_type, Unset):
            expiry_period_type = self.expiry_period_type.value

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        follow_up_label = self.follow_up_label

        form_name = self.form_name

        href = self.href

        id = self.id

        ignore_overdue_events = self.ignore_overdue_events

        incident_date_label = self.incident_date_label

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        note_label = self.note_label

        notification_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_templates, Unset):
            notification_templates = []
            for notification_templates_item_data in self.notification_templates:
                notification_templates_item = notification_templates_item_data.to_dict()
                notification_templates.append(notification_templates_item)

        only_enroll_once = self.only_enroll_once

        org_unit_label = self.org_unit_label

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        program_indicators: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_indicators, Unset):
            program_indicators = []
            for program_indicators_item_data in self.program_indicators:
                program_indicators_item = program_indicators_item_data.to_dict()
                program_indicators.append(program_indicators_item)

        program_rule_variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_rule_variables, Unset):
            program_rule_variables = []
            for program_rule_variables_item_data in self.program_rule_variables:
                program_rule_variables_item = program_rule_variables_item_data.to_dict()
                program_rule_variables.append(program_rule_variables_item)

        program_sections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_sections, Unset):
            program_sections = []
            for program_sections_item_data in self.program_sections:
                program_sections_item = program_sections_item_data.to_dict()
                program_sections.append(program_sections_item)

        program_stage_label = self.program_stage_label

        program_stages: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_stages, Unset):
            program_stages = []
            for program_stages_item_data in self.program_stages:
                program_stages_item = program_stages_item_data.to_dict()
                program_stages.append(program_stages_item)

        program_tracked_entity_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_tracked_entity_attributes, Unset):
            program_tracked_entity_attributes = []
            for program_tracked_entity_attributes_item_data in self.program_tracked_entity_attributes:
                program_tracked_entity_attributes_item = program_tracked_entity_attributes_item_data.to_dict()
                program_tracked_entity_attributes.append(program_tracked_entity_attributes_item)

        registration = self.registration

        related_program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.related_program, Unset):
            related_program = self.related_program.to_dict()

        relationship_label = self.relationship_label

        select_enrollment_dates_in_future = self.select_enrollment_dates_in_future

        select_incident_dates_in_future = self.select_incident_dates_in_future

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        skip_offline = self.skip_offline

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        tracked_entity_attribute_label = self.tracked_entity_attribute_label

        tracked_entity_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_type, Unset):
            tracked_entity_type = self.tracked_entity_type.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        use_first_stage_during_registration = self.use_first_stage_during_registration

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_roles, Unset):
            user_roles = []
            for user_roles_item_data in self.user_roles:
                user_roles_item = user_roles_item_data.to_dict()
                user_roles.append(user_roles_item)

        without_registration = self.without_registration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessLevel": access_level,
                "completeEventsExpiryDays": complete_events_expiry_days,
                "expiryDays": expiry_days,
                "featureType": feature_type,
                "maxTeiCountToReturn": max_tei_count_to_return,
                "minAttributesRequiredToSearch": min_attributes_required_to_search,
                "openDaysAfterCoEndDate": open_days_after_co_end_date,
                "programType": program_type,
                "version": version,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_combo is not UNSET:
            field_dict["categoryCombo"] = category_combo
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_entry_form is not UNSET:
            field_dict["dataEntryForm"] = data_entry_form
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_enrollment_date_label is not UNSET:
            field_dict["displayEnrollmentDateLabel"] = display_enrollment_date_label
        if display_enrollment_label is not UNSET:
            field_dict["displayEnrollmentLabel"] = display_enrollment_label
        if display_event_label is not UNSET:
            field_dict["displayEventLabel"] = display_event_label
        if display_follow_up_label is not UNSET:
            field_dict["displayFollowUpLabel"] = display_follow_up_label
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_front_page_list is not UNSET:
            field_dict["displayFrontPageList"] = display_front_page_list
        if display_incident_date is not UNSET:
            field_dict["displayIncidentDate"] = display_incident_date
        if display_incident_date_label is not UNSET:
            field_dict["displayIncidentDateLabel"] = display_incident_date_label
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_note_label is not UNSET:
            field_dict["displayNoteLabel"] = display_note_label
        if display_org_unit_label is not UNSET:
            field_dict["displayOrgUnitLabel"] = display_org_unit_label
        if display_program_stage_label is not UNSET:
            field_dict["displayProgramStageLabel"] = display_program_stage_label
        if display_relationship_label is not UNSET:
            field_dict["displayRelationshipLabel"] = display_relationship_label
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if display_tracked_entity_attribute_label is not UNSET:
            field_dict["displayTrackedEntityAttributeLabel"] = display_tracked_entity_attribute_label
        if enrollment_date_label is not UNSET:
            field_dict["enrollmentDateLabel"] = enrollment_date_label
        if enrollment_label is not UNSET:
            field_dict["enrollmentLabel"] = enrollment_label
        if event_label is not UNSET:
            field_dict["eventLabel"] = event_label
        if expiry_period_type is not UNSET:
            field_dict["expiryPeriodType"] = expiry_period_type
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if follow_up_label is not UNSET:
            field_dict["followUpLabel"] = follow_up_label
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if ignore_overdue_events is not UNSET:
            field_dict["ignoreOverdueEvents"] = ignore_overdue_events
        if incident_date_label is not UNSET:
            field_dict["incidentDateLabel"] = incident_date_label
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if name is not UNSET:
            field_dict["name"] = name
        if note_label is not UNSET:
            field_dict["noteLabel"] = note_label
        if notification_templates is not UNSET:
            field_dict["notificationTemplates"] = notification_templates
        if only_enroll_once is not UNSET:
            field_dict["onlyEnrollOnce"] = only_enroll_once
        if org_unit_label is not UNSET:
            field_dict["orgUnitLabel"] = org_unit_label
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if program_indicators is not UNSET:
            field_dict["programIndicators"] = program_indicators
        if program_rule_variables is not UNSET:
            field_dict["programRuleVariables"] = program_rule_variables
        if program_sections is not UNSET:
            field_dict["programSections"] = program_sections
        if program_stage_label is not UNSET:
            field_dict["programStageLabel"] = program_stage_label
        if program_stages is not UNSET:
            field_dict["programStages"] = program_stages
        if program_tracked_entity_attributes is not UNSET:
            field_dict["programTrackedEntityAttributes"] = program_tracked_entity_attributes
        if registration is not UNSET:
            field_dict["registration"] = registration
        if related_program is not UNSET:
            field_dict["relatedProgram"] = related_program
        if relationship_label is not UNSET:
            field_dict["relationshipLabel"] = relationship_label
        if select_enrollment_dates_in_future is not UNSET:
            field_dict["selectEnrollmentDatesInFuture"] = select_enrollment_dates_in_future
        if select_incident_dates_in_future is not UNSET:
            field_dict["selectIncidentDatesInFuture"] = select_incident_dates_in_future
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if skip_offline is not UNSET:
            field_dict["skipOffline"] = skip_offline
        if style is not UNSET:
            field_dict["style"] = style
        if tracked_entity_attribute_label is not UNSET:
            field_dict["trackedEntityAttributeLabel"] = tracked_entity_attribute_label
        if tracked_entity_type is not UNSET:
            field_dict["trackedEntityType"] = tracked_entity_type
        if translations is not UNSET:
            field_dict["translations"] = translations
        if use_first_stage_during_registration is not UNSET:
            field_dict["useFirstStageDuringRegistration"] = use_first_stage_during_registration
        if user is not UNSET:
            field_dict["user"] = user
        if user_roles is not UNSET:
            field_dict["userRoles"] = user_roles
        if without_registration is not UNSET:
            field_dict["withoutRegistration"] = without_registration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.object_style import ObjectStyle
        from ..models.program_category_combo import ProgramCategoryCombo
        from ..models.program_created_by import ProgramCreatedBy
        from ..models.program_data_entry_form import ProgramDataEntryForm
        from ..models.program_last_updated_by import ProgramLastUpdatedBy
        from ..models.program_notification_templates_item import ProgramNotificationTemplatesItem
        from ..models.program_organisation_units_item import ProgramOrganisationUnitsItem
        from ..models.program_program_indicators_item import ProgramProgramIndicatorsItem
        from ..models.program_program_rule_variables_item import ProgramProgramRuleVariablesItem
        from ..models.program_program_sections_item import ProgramProgramSectionsItem
        from ..models.program_program_stages_item import ProgramProgramStagesItem
        from ..models.program_related_program import ProgramRelatedProgram
        from ..models.program_tracked_entity_attribute import ProgramTrackedEntityAttribute
        from ..models.program_tracked_entity_type import ProgramTrackedEntityType
        from ..models.program_user import ProgramUser
        from ..models.program_user_roles_item import ProgramUserRolesItem
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        access_level = ProgramAccessLevel(d.pop("accessLevel"))

        complete_events_expiry_days = d.pop("completeEventsExpiryDays")

        expiry_days = d.pop("expiryDays")

        feature_type = ProgramFeatureType(d.pop("featureType"))

        max_tei_count_to_return = d.pop("maxTeiCountToReturn")

        min_attributes_required_to_search = d.pop("minAttributesRequiredToSearch")

        open_days_after_co_end_date = d.pop("openDaysAfterCoEndDate")

        program_type = ProgramProgramType(d.pop("programType"))

        version = d.pop("version")

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        _category_combo = d.pop("categoryCombo", UNSET)
        category_combo: Union[Unset, ProgramCategoryCombo]
        if isinstance(_category_combo, Unset):
            category_combo = UNSET
        else:
            category_combo = ProgramCategoryCombo.from_dict(_category_combo)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ProgramCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramCreatedBy.from_dict(_created_by)

        _data_entry_form = d.pop("dataEntryForm", UNSET)
        data_entry_form: Union[Unset, ProgramDataEntryForm]
        if isinstance(_data_entry_form, Unset):
            data_entry_form = UNSET
        else:
            data_entry_form = ProgramDataEntryForm.from_dict(_data_entry_form)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_enrollment_date_label = d.pop("displayEnrollmentDateLabel", UNSET)

        display_enrollment_label = d.pop("displayEnrollmentLabel", UNSET)

        display_event_label = d.pop("displayEventLabel", UNSET)

        display_follow_up_label = d.pop("displayFollowUpLabel", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_front_page_list = d.pop("displayFrontPageList", UNSET)

        display_incident_date = d.pop("displayIncidentDate", UNSET)

        display_incident_date_label = d.pop("displayIncidentDateLabel", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_note_label = d.pop("displayNoteLabel", UNSET)

        display_org_unit_label = d.pop("displayOrgUnitLabel", UNSET)

        display_program_stage_label = d.pop("displayProgramStageLabel", UNSET)

        display_relationship_label = d.pop("displayRelationshipLabel", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        display_tracked_entity_attribute_label = d.pop("displayTrackedEntityAttributeLabel", UNSET)

        enrollment_date_label = d.pop("enrollmentDateLabel", UNSET)

        enrollment_label = d.pop("enrollmentLabel", UNSET)

        event_label = d.pop("eventLabel", UNSET)

        _expiry_period_type = d.pop("expiryPeriodType", UNSET)
        expiry_period_type: Union[Unset, ProgramExpiryPeriodType]
        if isinstance(_expiry_period_type, Unset):
            expiry_period_type = UNSET
        else:
            expiry_period_type = ProgramExpiryPeriodType(_expiry_period_type)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        follow_up_label = d.pop("followUpLabel", UNSET)

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        ignore_overdue_events = d.pop("ignoreOverdueEvents", UNSET)

        incident_date_label = d.pop("incidentDateLabel", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ProgramLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        note_label = d.pop("noteLabel", UNSET)

        notification_templates = []
        _notification_templates = d.pop("notificationTemplates", UNSET)
        for notification_templates_item_data in _notification_templates or []:
            notification_templates_item = ProgramNotificationTemplatesItem.from_dict(notification_templates_item_data)

            notification_templates.append(notification_templates_item)

        only_enroll_once = d.pop("onlyEnrollOnce", UNSET)

        org_unit_label = d.pop("orgUnitLabel", UNSET)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = ProgramOrganisationUnitsItem.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

        program_indicators = []
        _program_indicators = d.pop("programIndicators", UNSET)
        for program_indicators_item_data in _program_indicators or []:
            program_indicators_item = ProgramProgramIndicatorsItem.from_dict(program_indicators_item_data)

            program_indicators.append(program_indicators_item)

        program_rule_variables = []
        _program_rule_variables = d.pop("programRuleVariables", UNSET)
        for program_rule_variables_item_data in _program_rule_variables or []:
            program_rule_variables_item = ProgramProgramRuleVariablesItem.from_dict(program_rule_variables_item_data)

            program_rule_variables.append(program_rule_variables_item)

        program_sections = []
        _program_sections = d.pop("programSections", UNSET)
        for program_sections_item_data in _program_sections or []:
            program_sections_item = ProgramProgramSectionsItem.from_dict(program_sections_item_data)

            program_sections.append(program_sections_item)

        program_stage_label = d.pop("programStageLabel", UNSET)

        program_stages = []
        _program_stages = d.pop("programStages", UNSET)
        for program_stages_item_data in _program_stages or []:
            program_stages_item = ProgramProgramStagesItem.from_dict(program_stages_item_data)

            program_stages.append(program_stages_item)

        program_tracked_entity_attributes = []
        _program_tracked_entity_attributes = d.pop("programTrackedEntityAttributes", UNSET)
        for program_tracked_entity_attributes_item_data in _program_tracked_entity_attributes or []:
            program_tracked_entity_attributes_item = ProgramTrackedEntityAttribute.from_dict(
                program_tracked_entity_attributes_item_data
            )

            program_tracked_entity_attributes.append(program_tracked_entity_attributes_item)

        registration = d.pop("registration", UNSET)

        _related_program = d.pop("relatedProgram", UNSET)
        related_program: Union[Unset, ProgramRelatedProgram]
        if isinstance(_related_program, Unset):
            related_program = UNSET
        else:
            related_program = ProgramRelatedProgram.from_dict(_related_program)

        relationship_label = d.pop("relationshipLabel", UNSET)

        select_enrollment_dates_in_future = d.pop("selectEnrollmentDatesInFuture", UNSET)

        select_incident_dates_in_future = d.pop("selectIncidentDatesInFuture", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        skip_offline = d.pop("skipOffline", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, ObjectStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ObjectStyle.from_dict(_style)

        tracked_entity_attribute_label = d.pop("trackedEntityAttributeLabel", UNSET)

        _tracked_entity_type = d.pop("trackedEntityType", UNSET)
        tracked_entity_type: Union[Unset, ProgramTrackedEntityType]
        if isinstance(_tracked_entity_type, Unset):
            tracked_entity_type = UNSET
        else:
            tracked_entity_type = ProgramTrackedEntityType.from_dict(_tracked_entity_type)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        use_first_stage_during_registration = d.pop("useFirstStageDuringRegistration", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramUser.from_dict(_user)

        user_roles = []
        _user_roles = d.pop("userRoles", UNSET)
        for user_roles_item_data in _user_roles or []:
            user_roles_item = ProgramUserRolesItem.from_dict(user_roles_item_data)

            user_roles.append(user_roles_item)

        without_registration = d.pop("withoutRegistration", UNSET)

        program = cls(
            access_level=access_level,
            complete_events_expiry_days=complete_events_expiry_days,
            expiry_days=expiry_days,
            feature_type=feature_type,
            max_tei_count_to_return=max_tei_count_to_return,
            min_attributes_required_to_search=min_attributes_required_to_search,
            open_days_after_co_end_date=open_days_after_co_end_date,
            program_type=program_type,
            version=version,
            access=access,
            attribute_values=attribute_values,
            category_combo=category_combo,
            code=code,
            created=created,
            created_by=created_by,
            data_entry_form=data_entry_form,
            description=description,
            display_description=display_description,
            display_enrollment_date_label=display_enrollment_date_label,
            display_enrollment_label=display_enrollment_label,
            display_event_label=display_event_label,
            display_follow_up_label=display_follow_up_label,
            display_form_name=display_form_name,
            display_front_page_list=display_front_page_list,
            display_incident_date=display_incident_date,
            display_incident_date_label=display_incident_date_label,
            display_name=display_name,
            display_note_label=display_note_label,
            display_org_unit_label=display_org_unit_label,
            display_program_stage_label=display_program_stage_label,
            display_relationship_label=display_relationship_label,
            display_short_name=display_short_name,
            display_tracked_entity_attribute_label=display_tracked_entity_attribute_label,
            enrollment_date_label=enrollment_date_label,
            enrollment_label=enrollment_label,
            event_label=event_label,
            expiry_period_type=expiry_period_type,
            favorite=favorite,
            favorites=favorites,
            follow_up_label=follow_up_label,
            form_name=form_name,
            href=href,
            id=id,
            ignore_overdue_events=ignore_overdue_events,
            incident_date_label=incident_date_label,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            note_label=note_label,
            notification_templates=notification_templates,
            only_enroll_once=only_enroll_once,
            org_unit_label=org_unit_label,
            organisation_units=organisation_units,
            program_indicators=program_indicators,
            program_rule_variables=program_rule_variables,
            program_sections=program_sections,
            program_stage_label=program_stage_label,
            program_stages=program_stages,
            program_tracked_entity_attributes=program_tracked_entity_attributes,
            registration=registration,
            related_program=related_program,
            relationship_label=relationship_label,
            select_enrollment_dates_in_future=select_enrollment_dates_in_future,
            select_incident_dates_in_future=select_incident_dates_in_future,
            sharing=sharing,
            short_name=short_name,
            skip_offline=skip_offline,
            style=style,
            tracked_entity_attribute_label=tracked_entity_attribute_label,
            tracked_entity_type=tracked_entity_type,
            translations=translations,
            use_first_stage_during_registration=use_first_stage_during_registration,
            user=user,
            user_roles=user_roles,
            without_registration=without_registration,
        )

        program.additional_properties = d
        return program

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
