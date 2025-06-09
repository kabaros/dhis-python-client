import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_stage_feature_type import ProgramStageFeatureType
from ..models.program_stage_form_type import ProgramStageFormType
from ..models.program_stage_period_type import ProgramStagePeriodType
from ..models.program_stage_validation_strategy import ProgramStageValidationStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.object_style import ObjectStyle
    from ..models.program_stage_created_by import ProgramStageCreatedBy
    from ..models.program_stage_data_element import ProgramStageDataElement
    from ..models.program_stage_data_entry_form import ProgramStageDataEntryForm
    from ..models.program_stage_last_updated_by import ProgramStageLastUpdatedBy
    from ..models.program_stage_next_schedule_date import ProgramStageNextScheduleDate
    from ..models.program_stage_notification_templates_item import ProgramStageNotificationTemplatesItem
    from ..models.program_stage_program import ProgramStageProgram
    from ..models.program_stage_program_stage_sections_item import ProgramStageProgramStageSectionsItem
    from ..models.program_stage_user import ProgramStageUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramStage")


@_attrs_define
class ProgramStage:
    """
    Attributes:
        feature_type (ProgramStageFeatureType):
        form_type (ProgramStageFormType):
        min_days_from_start (int):
        validation_strategy (ProgramStageValidationStrategy):
        access (Union[Unset, Access]):
        allow_generate_next_visit (Union[Unset, bool]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        auto_generate_event (Union[Unset, bool]):
        block_entry_form (Union[Unset, bool]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramStageCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_entry_form (Union[Unset, ProgramStageDataEntryForm]): A UID reference to a DataEntryForm
            (Java name `org.hisp.dhis.dataentryform.DataEntryForm`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_due_date_label (Union[Unset, str]):
        display_event_label (Union[Unset, str]):
        display_execution_date_label (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_generate_event_box (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        display_program_stage_label (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        due_date_label (Union[Unset, str]):
        enable_user_assignment (Union[Unset, bool]):
        event_label (Union[Unset, str]):
        execution_date_label (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        generated_by_enrollment_date (Union[Unset, bool]):
        hide_due_date (Union[Unset, bool]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramStageLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        next_schedule_date (Union[Unset, ProgramStageNextScheduleDate]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        notification_templates (Union[Unset, list['ProgramStageNotificationTemplatesItem']]):
        open_after_enrollment (Union[Unset, bool]):
        period_type (Union[Unset, ProgramStagePeriodType]):
        pre_generate_uid (Union[Unset, bool]):
        program (Union[Unset, ProgramStageProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_stage_data_elements (Union[Unset, list['ProgramStageDataElement']]):
        program_stage_label (Union[Unset, str]):
        program_stage_sections (Union[Unset, list['ProgramStageProgramStageSectionsItem']]):
        referral (Union[Unset, bool]):
        remind_completed (Union[Unset, bool]):
        repeatable (Union[Unset, bool]):
        report_date_to_use (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        sort_order (Union[Unset, int]):
        standard_interval (Union[Unset, int]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramStageUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    feature_type: ProgramStageFeatureType
    form_type: ProgramStageFormType
    min_days_from_start: int
    validation_strategy: ProgramStageValidationStrategy
    access: Union[Unset, "Access"] = UNSET
    allow_generate_next_visit: Union[Unset, bool] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    auto_generate_event: Union[Unset, bool] = UNSET
    block_entry_form: Union[Unset, bool] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramStageCreatedBy"] = UNSET
    data_entry_form: Union[Unset, "ProgramStageDataEntryForm"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_due_date_label: Union[Unset, str] = UNSET
    display_event_label: Union[Unset, str] = UNSET
    display_execution_date_label: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_generate_event_box: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_program_stage_label: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    due_date_label: Union[Unset, str] = UNSET
    enable_user_assignment: Union[Unset, bool] = UNSET
    event_label: Union[Unset, str] = UNSET
    execution_date_label: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    generated_by_enrollment_date: Union[Unset, bool] = UNSET
    hide_due_date: Union[Unset, bool] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramStageLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    next_schedule_date: Union[Unset, "ProgramStageNextScheduleDate"] = UNSET
    notification_templates: Union[Unset, list["ProgramStageNotificationTemplatesItem"]] = UNSET
    open_after_enrollment: Union[Unset, bool] = UNSET
    period_type: Union[Unset, ProgramStagePeriodType] = UNSET
    pre_generate_uid: Union[Unset, bool] = UNSET
    program: Union[Unset, "ProgramStageProgram"] = UNSET
    program_stage_data_elements: Union[Unset, list["ProgramStageDataElement"]] = UNSET
    program_stage_label: Union[Unset, str] = UNSET
    program_stage_sections: Union[Unset, list["ProgramStageProgramStageSectionsItem"]] = UNSET
    referral: Union[Unset, bool] = UNSET
    remind_completed: Union[Unset, bool] = UNSET
    repeatable: Union[Unset, bool] = UNSET
    report_date_to_use: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    standard_interval: Union[Unset, int] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramStageUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_type = self.feature_type.value

        form_type = self.form_type.value

        min_days_from_start = self.min_days_from_start

        validation_strategy = self.validation_strategy.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        allow_generate_next_visit = self.allow_generate_next_visit

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        auto_generate_event = self.auto_generate_event

        block_entry_form = self.block_entry_form

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

        display_due_date_label = self.display_due_date_label

        display_event_label = self.display_event_label

        display_execution_date_label = self.display_execution_date_label

        display_form_name = self.display_form_name

        display_generate_event_box = self.display_generate_event_box

        display_name = self.display_name

        display_program_stage_label = self.display_program_stage_label

        display_short_name = self.display_short_name

        due_date_label = self.due_date_label

        enable_user_assignment = self.enable_user_assignment

        event_label = self.event_label

        execution_date_label = self.execution_date_label

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        generated_by_enrollment_date = self.generated_by_enrollment_date

        hide_due_date = self.hide_due_date

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        next_schedule_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_schedule_date, Unset):
            next_schedule_date = self.next_schedule_date.to_dict()

        notification_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_templates, Unset):
            notification_templates = []
            for notification_templates_item_data in self.notification_templates:
                notification_templates_item = notification_templates_item_data.to_dict()
                notification_templates.append(notification_templates_item)

        open_after_enrollment = self.open_after_enrollment

        period_type: Union[Unset, str] = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value

        pre_generate_uid = self.pre_generate_uid

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_stage_data_elements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_stage_data_elements, Unset):
            program_stage_data_elements = []
            for program_stage_data_elements_item_data in self.program_stage_data_elements:
                program_stage_data_elements_item = program_stage_data_elements_item_data.to_dict()
                program_stage_data_elements.append(program_stage_data_elements_item)

        program_stage_label = self.program_stage_label

        program_stage_sections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_stage_sections, Unset):
            program_stage_sections = []
            for program_stage_sections_item_data in self.program_stage_sections:
                program_stage_sections_item = program_stage_sections_item_data.to_dict()
                program_stage_sections.append(program_stage_sections_item)

        referral = self.referral

        remind_completed = self.remind_completed

        repeatable = self.repeatable

        report_date_to_use = self.report_date_to_use

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        sort_order = self.sort_order

        standard_interval = self.standard_interval

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "featureType": feature_type,
                "formType": form_type,
                "minDaysFromStart": min_days_from_start,
                "validationStrategy": validation_strategy,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if allow_generate_next_visit is not UNSET:
            field_dict["allowGenerateNextVisit"] = allow_generate_next_visit
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if auto_generate_event is not UNSET:
            field_dict["autoGenerateEvent"] = auto_generate_event
        if block_entry_form is not UNSET:
            field_dict["blockEntryForm"] = block_entry_form
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
        if display_due_date_label is not UNSET:
            field_dict["displayDueDateLabel"] = display_due_date_label
        if display_event_label is not UNSET:
            field_dict["displayEventLabel"] = display_event_label
        if display_execution_date_label is not UNSET:
            field_dict["displayExecutionDateLabel"] = display_execution_date_label
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_generate_event_box is not UNSET:
            field_dict["displayGenerateEventBox"] = display_generate_event_box
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_program_stage_label is not UNSET:
            field_dict["displayProgramStageLabel"] = display_program_stage_label
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if due_date_label is not UNSET:
            field_dict["dueDateLabel"] = due_date_label
        if enable_user_assignment is not UNSET:
            field_dict["enableUserAssignment"] = enable_user_assignment
        if event_label is not UNSET:
            field_dict["eventLabel"] = event_label
        if execution_date_label is not UNSET:
            field_dict["executionDateLabel"] = execution_date_label
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if generated_by_enrollment_date is not UNSET:
            field_dict["generatedByEnrollmentDate"] = generated_by_enrollment_date
        if hide_due_date is not UNSET:
            field_dict["hideDueDate"] = hide_due_date
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if name is not UNSET:
            field_dict["name"] = name
        if next_schedule_date is not UNSET:
            field_dict["nextScheduleDate"] = next_schedule_date
        if notification_templates is not UNSET:
            field_dict["notificationTemplates"] = notification_templates
        if open_after_enrollment is not UNSET:
            field_dict["openAfterEnrollment"] = open_after_enrollment
        if period_type is not UNSET:
            field_dict["periodType"] = period_type
        if pre_generate_uid is not UNSET:
            field_dict["preGenerateUID"] = pre_generate_uid
        if program is not UNSET:
            field_dict["program"] = program
        if program_stage_data_elements is not UNSET:
            field_dict["programStageDataElements"] = program_stage_data_elements
        if program_stage_label is not UNSET:
            field_dict["programStageLabel"] = program_stage_label
        if program_stage_sections is not UNSET:
            field_dict["programStageSections"] = program_stage_sections
        if referral is not UNSET:
            field_dict["referral"] = referral
        if remind_completed is not UNSET:
            field_dict["remindCompleted"] = remind_completed
        if repeatable is not UNSET:
            field_dict["repeatable"] = repeatable
        if report_date_to_use is not UNSET:
            field_dict["reportDateToUse"] = report_date_to_use
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if standard_interval is not UNSET:
            field_dict["standardInterval"] = standard_interval
        if style is not UNSET:
            field_dict["style"] = style
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.object_style import ObjectStyle
        from ..models.program_stage_created_by import ProgramStageCreatedBy
        from ..models.program_stage_data_element import ProgramStageDataElement
        from ..models.program_stage_data_entry_form import ProgramStageDataEntryForm
        from ..models.program_stage_last_updated_by import ProgramStageLastUpdatedBy
        from ..models.program_stage_next_schedule_date import ProgramStageNextScheduleDate
        from ..models.program_stage_notification_templates_item import ProgramStageNotificationTemplatesItem
        from ..models.program_stage_program import ProgramStageProgram
        from ..models.program_stage_program_stage_sections_item import ProgramStageProgramStageSectionsItem
        from ..models.program_stage_user import ProgramStageUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        feature_type = ProgramStageFeatureType(d.pop("featureType"))

        form_type = ProgramStageFormType(d.pop("formType"))

        min_days_from_start = d.pop("minDaysFromStart")

        validation_strategy = ProgramStageValidationStrategy(d.pop("validationStrategy"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        allow_generate_next_visit = d.pop("allowGenerateNextVisit", UNSET)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        auto_generate_event = d.pop("autoGenerateEvent", UNSET)

        block_entry_form = d.pop("blockEntryForm", UNSET)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ProgramStageCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramStageCreatedBy.from_dict(_created_by)

        _data_entry_form = d.pop("dataEntryForm", UNSET)
        data_entry_form: Union[Unset, ProgramStageDataEntryForm]
        if isinstance(_data_entry_form, Unset):
            data_entry_form = UNSET
        else:
            data_entry_form = ProgramStageDataEntryForm.from_dict(_data_entry_form)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_due_date_label = d.pop("displayDueDateLabel", UNSET)

        display_event_label = d.pop("displayEventLabel", UNSET)

        display_execution_date_label = d.pop("displayExecutionDateLabel", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_generate_event_box = d.pop("displayGenerateEventBox", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_program_stage_label = d.pop("displayProgramStageLabel", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        due_date_label = d.pop("dueDateLabel", UNSET)

        enable_user_assignment = d.pop("enableUserAssignment", UNSET)

        event_label = d.pop("eventLabel", UNSET)

        execution_date_label = d.pop("executionDateLabel", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        generated_by_enrollment_date = d.pop("generatedByEnrollmentDate", UNSET)

        hide_due_date = d.pop("hideDueDate", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ProgramStageLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramStageLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _next_schedule_date = d.pop("nextScheduleDate", UNSET)
        next_schedule_date: Union[Unset, ProgramStageNextScheduleDate]
        if isinstance(_next_schedule_date, Unset):
            next_schedule_date = UNSET
        else:
            next_schedule_date = ProgramStageNextScheduleDate.from_dict(_next_schedule_date)

        notification_templates = []
        _notification_templates = d.pop("notificationTemplates", UNSET)
        for notification_templates_item_data in _notification_templates or []:
            notification_templates_item = ProgramStageNotificationTemplatesItem.from_dict(
                notification_templates_item_data
            )

            notification_templates.append(notification_templates_item)

        open_after_enrollment = d.pop("openAfterEnrollment", UNSET)

        _period_type = d.pop("periodType", UNSET)
        period_type: Union[Unset, ProgramStagePeriodType]
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = ProgramStagePeriodType(_period_type)

        pre_generate_uid = d.pop("preGenerateUID", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, ProgramStageProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = ProgramStageProgram.from_dict(_program)

        program_stage_data_elements = []
        _program_stage_data_elements = d.pop("programStageDataElements", UNSET)
        for program_stage_data_elements_item_data in _program_stage_data_elements or []:
            program_stage_data_elements_item = ProgramStageDataElement.from_dict(program_stage_data_elements_item_data)

            program_stage_data_elements.append(program_stage_data_elements_item)

        program_stage_label = d.pop("programStageLabel", UNSET)

        program_stage_sections = []
        _program_stage_sections = d.pop("programStageSections", UNSET)
        for program_stage_sections_item_data in _program_stage_sections or []:
            program_stage_sections_item = ProgramStageProgramStageSectionsItem.from_dict(
                program_stage_sections_item_data
            )

            program_stage_sections.append(program_stage_sections_item)

        referral = d.pop("referral", UNSET)

        remind_completed = d.pop("remindCompleted", UNSET)

        repeatable = d.pop("repeatable", UNSET)

        report_date_to_use = d.pop("reportDateToUse", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        standard_interval = d.pop("standardInterval", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, ObjectStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ObjectStyle.from_dict(_style)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramStageUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramStageUser.from_dict(_user)

        program_stage = cls(
            feature_type=feature_type,
            form_type=form_type,
            min_days_from_start=min_days_from_start,
            validation_strategy=validation_strategy,
            access=access,
            allow_generate_next_visit=allow_generate_next_visit,
            attribute_values=attribute_values,
            auto_generate_event=auto_generate_event,
            block_entry_form=block_entry_form,
            code=code,
            created=created,
            created_by=created_by,
            data_entry_form=data_entry_form,
            description=description,
            display_description=display_description,
            display_due_date_label=display_due_date_label,
            display_event_label=display_event_label,
            display_execution_date_label=display_execution_date_label,
            display_form_name=display_form_name,
            display_generate_event_box=display_generate_event_box,
            display_name=display_name,
            display_program_stage_label=display_program_stage_label,
            display_short_name=display_short_name,
            due_date_label=due_date_label,
            enable_user_assignment=enable_user_assignment,
            event_label=event_label,
            execution_date_label=execution_date_label,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            generated_by_enrollment_date=generated_by_enrollment_date,
            hide_due_date=hide_due_date,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            next_schedule_date=next_schedule_date,
            notification_templates=notification_templates,
            open_after_enrollment=open_after_enrollment,
            period_type=period_type,
            pre_generate_uid=pre_generate_uid,
            program=program,
            program_stage_data_elements=program_stage_data_elements,
            program_stage_label=program_stage_label,
            program_stage_sections=program_stage_sections,
            referral=referral,
            remind_completed=remind_completed,
            repeatable=repeatable,
            report_date_to_use=report_date_to_use,
            sharing=sharing,
            short_name=short_name,
            sort_order=sort_order,
            standard_interval=standard_interval,
            style=style,
            translations=translations,
            user=user,
        )

        program_stage.additional_properties = d
        return program_stage

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
