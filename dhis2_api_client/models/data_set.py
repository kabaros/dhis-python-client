import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_set_aggregation_type import DataSetAggregationType
from ..models.data_set_form_type import DataSetFormType
from ..models.data_set_period_type import DataSetPeriodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.data_element_operand import DataElementOperand
    from ..models.data_input_period import DataInputPeriod
    from ..models.data_set_category_combo import DataSetCategoryCombo
    from ..models.data_set_created_by import DataSetCreatedBy
    from ..models.data_set_data_entry_form import DataSetDataEntryForm
    from ..models.data_set_element import DataSetElement
    from ..models.data_set_indicators_item import DataSetIndicatorsItem
    from ..models.data_set_interpretations_item import DataSetInterpretationsItem
    from ..models.data_set_last_updated_by import DataSetLastUpdatedBy
    from ..models.data_set_legend_set import DataSetLegendSet
    from ..models.data_set_legend_sets_item import DataSetLegendSetsItem
    from ..models.data_set_notification_recipients import DataSetNotificationRecipients
    from ..models.data_set_organisation_units_item import DataSetOrganisationUnitsItem
    from ..models.data_set_sections_item import DataSetSectionsItem
    from ..models.data_set_user import DataSetUser
    from ..models.data_set_workflow import DataSetWorkflow
    from ..models.object_style import ObjectStyle
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="DataSet")


@_attrs_define
class DataSet:
    """
    Attributes:
        aggregation_type (DataSetAggregationType):
        expiry_days (int):
        form_type (DataSetFormType):
        open_future_periods (int):
        open_periods_after_co_end_date (int):
        timely_days (float):
        version (int):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_combo (Union[Unset, DataSetCategoryCombo]): A UID reference to a CategoryCombo
            (Java name `org.hisp.dhis.category.CategoryCombo`)
        code (Union[Unset, str]):
        compulsory_data_element_operands (Union[Unset, list['DataElementOperand']]):
        compulsory_fields_complete_only (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, DataSetCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_element_decoration (Union[Unset, bool]):
        data_entry_form (Union[Unset, DataSetDataEntryForm]): A UID reference to a DataEntryForm
            (Java name `org.hisp.dhis.dataentryform.DataEntryForm`)
        data_input_periods (Union[Unset, list['DataInputPeriod']]):
        data_set_elements (Union[Unset, list['DataSetElement']]):
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        field_combination_required (Union[Unset, bool]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        indicators (Union[Unset, list['DataSetIndicatorsItem']]):
        interpretations (Union[Unset, list['DataSetInterpretationsItem']]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, DataSetLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, DataSetLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['DataSetLegendSetsItem']]):
        mobile (Union[Unset, bool]):
        name (Union[Unset, str]):
        no_value_requires_comment (Union[Unset, bool]):
        notification_recipients (Union[Unset, DataSetNotificationRecipients]): A UID reference to a UserGroup
            (Java name `org.hisp.dhis.user.UserGroup`)
        notify_completing_user (Union[Unset, bool]):
        organisation_units (Union[Unset, list['DataSetOrganisationUnitsItem']]):
        period_type (Union[Unset, DataSetPeriodType]):
        query_mods (Union[Unset, QueryModifiers]):
        render_as_tabs (Union[Unset, bool]):
        render_horizontally (Union[Unset, bool]):
        sections (Union[Unset, list['DataSetSectionsItem']]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        skip_offline (Union[Unset, bool]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, DataSetUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        valid_complete_only (Union[Unset, bool]):
        workflow (Union[Unset, DataSetWorkflow]): A UID reference to a DataApprovalWorkflow
            (Java name `org.hisp.dhis.dataapproval.DataApprovalWorkflow`)
    """

    aggregation_type: DataSetAggregationType
    expiry_days: int
    form_type: DataSetFormType
    open_future_periods: int
    open_periods_after_co_end_date: int
    timely_days: float
    version: int
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_combo: Union[Unset, "DataSetCategoryCombo"] = UNSET
    code: Union[Unset, str] = UNSET
    compulsory_data_element_operands: Union[Unset, list["DataElementOperand"]] = UNSET
    compulsory_fields_complete_only: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "DataSetCreatedBy"] = UNSET
    data_element_decoration: Union[Unset, bool] = UNSET
    data_entry_form: Union[Unset, "DataSetDataEntryForm"] = UNSET
    data_input_periods: Union[Unset, list["DataInputPeriod"]] = UNSET
    data_set_elements: Union[Unset, list["DataSetElement"]] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    field_combination_required: Union[Unset, bool] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    indicators: Union[Unset, list["DataSetIndicatorsItem"]] = UNSET
    interpretations: Union[Unset, list["DataSetInterpretationsItem"]] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "DataSetLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "DataSetLegendSet"] = UNSET
    legend_sets: Union[Unset, list["DataSetLegendSetsItem"]] = UNSET
    mobile: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    no_value_requires_comment: Union[Unset, bool] = UNSET
    notification_recipients: Union[Unset, "DataSetNotificationRecipients"] = UNSET
    notify_completing_user: Union[Unset, bool] = UNSET
    organisation_units: Union[Unset, list["DataSetOrganisationUnitsItem"]] = UNSET
    period_type: Union[Unset, DataSetPeriodType] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    render_as_tabs: Union[Unset, bool] = UNSET
    render_horizontally: Union[Unset, bool] = UNSET
    sections: Union[Unset, list["DataSetSectionsItem"]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    skip_offline: Union[Unset, bool] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "DataSetUser"] = UNSET
    valid_complete_only: Union[Unset, bool] = UNSET
    workflow: Union[Unset, "DataSetWorkflow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        expiry_days = self.expiry_days

        form_type = self.form_type.value

        open_future_periods = self.open_future_periods

        open_periods_after_co_end_date = self.open_periods_after_co_end_date

        timely_days = self.timely_days

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

        compulsory_data_element_operands: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.compulsory_data_element_operands, Unset):
            compulsory_data_element_operands = []
            for compulsory_data_element_operands_item_data in self.compulsory_data_element_operands:
                compulsory_data_element_operands_item = compulsory_data_element_operands_item_data.to_dict()
                compulsory_data_element_operands.append(compulsory_data_element_operands_item)

        compulsory_fields_complete_only = self.compulsory_fields_complete_only

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_element_decoration = self.data_element_decoration

        data_entry_form: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_entry_form, Unset):
            data_entry_form = self.data_entry_form.to_dict()

        data_input_periods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_input_periods, Unset):
            data_input_periods = []
            for data_input_periods_item_data in self.data_input_periods:
                data_input_periods_item = data_input_periods_item_data.to_dict()
                data_input_periods.append(data_input_periods_item)

        data_set_elements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_set_elements, Unset):
            data_set_elements = []
            for data_set_elements_item_data in self.data_set_elements:
                data_set_elements_item = data_set_elements_item_data.to_dict()
                data_set_elements.append(data_set_elements_item)

        description = self.description

        dimension_item = self.dimension_item

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        field_combination_required = self.field_combination_required

        form_name = self.form_name

        href = self.href

        id = self.id

        indicators: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicators, Unset):
            indicators = []
            for indicators_item_data in self.indicators:
                indicators_item = indicators_item_data.to_dict()
                indicators.append(indicators_item)

        interpretations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interpretations, Unset):
            interpretations = []
            for interpretations_item_data in self.interpretations:
                interpretations_item = interpretations_item_data.to_dict()
                interpretations.append(interpretations_item)

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        legend_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legend_sets, Unset):
            legend_sets = []
            for legend_sets_item_data in self.legend_sets:
                legend_sets_item = legend_sets_item_data.to_dict()
                legend_sets.append(legend_sets_item)

        mobile = self.mobile

        name = self.name

        no_value_requires_comment = self.no_value_requires_comment

        notification_recipients: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.notification_recipients, Unset):
            notification_recipients = self.notification_recipients.to_dict()

        notify_completing_user = self.notify_completing_user

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        period_type: Union[Unset, str] = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        render_as_tabs = self.render_as_tabs

        render_horizontally = self.render_horizontally

        sections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        skip_offline = self.skip_offline

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

        valid_complete_only = self.valid_complete_only

        workflow: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "expiryDays": expiry_days,
                "formType": form_type,
                "openFuturePeriods": open_future_periods,
                "openPeriodsAfterCoEndDate": open_periods_after_co_end_date,
                "timelyDays": timely_days,
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
        if compulsory_data_element_operands is not UNSET:
            field_dict["compulsoryDataElementOperands"] = compulsory_data_element_operands
        if compulsory_fields_complete_only is not UNSET:
            field_dict["compulsoryFieldsCompleteOnly"] = compulsory_fields_complete_only
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_element_decoration is not UNSET:
            field_dict["dataElementDecoration"] = data_element_decoration
        if data_entry_form is not UNSET:
            field_dict["dataEntryForm"] = data_entry_form
        if data_input_periods is not UNSET:
            field_dict["dataInputPeriods"] = data_input_periods
        if data_set_elements is not UNSET:
            field_dict["dataSetElements"] = data_set_elements
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_item is not UNSET:
            field_dict["dimensionItem"] = dimension_item
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if field_combination_required is not UNSET:
            field_dict["fieldCombinationRequired"] = field_combination_required
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if indicators is not UNSET:
            field_dict["indicators"] = indicators
        if interpretations is not UNSET:
            field_dict["interpretations"] = interpretations
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if name is not UNSET:
            field_dict["name"] = name
        if no_value_requires_comment is not UNSET:
            field_dict["noValueRequiresComment"] = no_value_requires_comment
        if notification_recipients is not UNSET:
            field_dict["notificationRecipients"] = notification_recipients
        if notify_completing_user is not UNSET:
            field_dict["notifyCompletingUser"] = notify_completing_user
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if period_type is not UNSET:
            field_dict["periodType"] = period_type
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if render_as_tabs is not UNSET:
            field_dict["renderAsTabs"] = render_as_tabs
        if render_horizontally is not UNSET:
            field_dict["renderHorizontally"] = render_horizontally
        if sections is not UNSET:
            field_dict["sections"] = sections
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if skip_offline is not UNSET:
            field_dict["skipOffline"] = skip_offline
        if style is not UNSET:
            field_dict["style"] = style
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if valid_complete_only is not UNSET:
            field_dict["validCompleteOnly"] = valid_complete_only
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.data_element_operand import DataElementOperand
        from ..models.data_input_period import DataInputPeriod
        from ..models.data_set_category_combo import DataSetCategoryCombo
        from ..models.data_set_created_by import DataSetCreatedBy
        from ..models.data_set_data_entry_form import DataSetDataEntryForm
        from ..models.data_set_element import DataSetElement
        from ..models.data_set_indicators_item import DataSetIndicatorsItem
        from ..models.data_set_interpretations_item import DataSetInterpretationsItem
        from ..models.data_set_last_updated_by import DataSetLastUpdatedBy
        from ..models.data_set_legend_set import DataSetLegendSet
        from ..models.data_set_legend_sets_item import DataSetLegendSetsItem
        from ..models.data_set_notification_recipients import DataSetNotificationRecipients
        from ..models.data_set_organisation_units_item import DataSetOrganisationUnitsItem
        from ..models.data_set_sections_item import DataSetSectionsItem
        from ..models.data_set_user import DataSetUser
        from ..models.data_set_workflow import DataSetWorkflow
        from ..models.object_style import ObjectStyle
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = DataSetAggregationType(d.pop("aggregationType"))

        expiry_days = d.pop("expiryDays")

        form_type = DataSetFormType(d.pop("formType"))

        open_future_periods = d.pop("openFuturePeriods")

        open_periods_after_co_end_date = d.pop("openPeriodsAfterCoEndDate")

        timely_days = d.pop("timelyDays")

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
        category_combo: Union[Unset, DataSetCategoryCombo]
        if isinstance(_category_combo, Unset):
            category_combo = UNSET
        else:
            category_combo = DataSetCategoryCombo.from_dict(_category_combo)

        code = d.pop("code", UNSET)

        compulsory_data_element_operands = []
        _compulsory_data_element_operands = d.pop("compulsoryDataElementOperands", UNSET)
        for compulsory_data_element_operands_item_data in _compulsory_data_element_operands or []:
            compulsory_data_element_operands_item = DataElementOperand.from_dict(
                compulsory_data_element_operands_item_data
            )

            compulsory_data_element_operands.append(compulsory_data_element_operands_item)

        compulsory_fields_complete_only = d.pop("compulsoryFieldsCompleteOnly", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, DataSetCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = DataSetCreatedBy.from_dict(_created_by)

        data_element_decoration = d.pop("dataElementDecoration", UNSET)

        _data_entry_form = d.pop("dataEntryForm", UNSET)
        data_entry_form: Union[Unset, DataSetDataEntryForm]
        if isinstance(_data_entry_form, Unset):
            data_entry_form = UNSET
        else:
            data_entry_form = DataSetDataEntryForm.from_dict(_data_entry_form)

        data_input_periods = []
        _data_input_periods = d.pop("dataInputPeriods", UNSET)
        for data_input_periods_item_data in _data_input_periods or []:
            data_input_periods_item = DataInputPeriod.from_dict(data_input_periods_item_data)

            data_input_periods.append(data_input_periods_item)

        data_set_elements = []
        _data_set_elements = d.pop("dataSetElements", UNSET)
        for data_set_elements_item_data in _data_set_elements or []:
            data_set_elements_item = DataSetElement.from_dict(data_set_elements_item_data)

            data_set_elements.append(data_set_elements_item)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        field_combination_required = d.pop("fieldCombinationRequired", UNSET)

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        indicators = []
        _indicators = d.pop("indicators", UNSET)
        for indicators_item_data in _indicators or []:
            indicators_item = DataSetIndicatorsItem.from_dict(indicators_item_data)

            indicators.append(indicators_item)

        interpretations = []
        _interpretations = d.pop("interpretations", UNSET)
        for interpretations_item_data in _interpretations or []:
            interpretations_item = DataSetInterpretationsItem.from_dict(interpretations_item_data)

            interpretations.append(interpretations_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, DataSetLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = DataSetLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, DataSetLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = DataSetLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = DataSetLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        mobile = d.pop("mobile", UNSET)

        name = d.pop("name", UNSET)

        no_value_requires_comment = d.pop("noValueRequiresComment", UNSET)

        _notification_recipients = d.pop("notificationRecipients", UNSET)
        notification_recipients: Union[Unset, DataSetNotificationRecipients]
        if isinstance(_notification_recipients, Unset):
            notification_recipients = UNSET
        else:
            notification_recipients = DataSetNotificationRecipients.from_dict(_notification_recipients)

        notify_completing_user = d.pop("notifyCompletingUser", UNSET)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = DataSetOrganisationUnitsItem.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

        _period_type = d.pop("periodType", UNSET)
        period_type: Union[Unset, DataSetPeriodType]
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = DataSetPeriodType(_period_type)

        _query_mods = d.pop("queryMods", UNSET)
        query_mods: Union[Unset, QueryModifiers]
        if isinstance(_query_mods, Unset):
            query_mods = UNSET
        else:
            query_mods = QueryModifiers.from_dict(_query_mods)

        render_as_tabs = d.pop("renderAsTabs", UNSET)

        render_horizontally = d.pop("renderHorizontally", UNSET)

        sections = []
        _sections = d.pop("sections", UNSET)
        for sections_item_data in _sections or []:
            sections_item = DataSetSectionsItem.from_dict(sections_item_data)

            sections.append(sections_item)

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

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, DataSetUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = DataSetUser.from_dict(_user)

        valid_complete_only = d.pop("validCompleteOnly", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, DataSetWorkflow]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = DataSetWorkflow.from_dict(_workflow)

        data_set = cls(
            aggregation_type=aggregation_type,
            expiry_days=expiry_days,
            form_type=form_type,
            open_future_periods=open_future_periods,
            open_periods_after_co_end_date=open_periods_after_co_end_date,
            timely_days=timely_days,
            version=version,
            access=access,
            attribute_values=attribute_values,
            category_combo=category_combo,
            code=code,
            compulsory_data_element_operands=compulsory_data_element_operands,
            compulsory_fields_complete_only=compulsory_fields_complete_only,
            created=created,
            created_by=created_by,
            data_element_decoration=data_element_decoration,
            data_entry_form=data_entry_form,
            data_input_periods=data_input_periods,
            data_set_elements=data_set_elements,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            field_combination_required=field_combination_required,
            form_name=form_name,
            href=href,
            id=id,
            indicators=indicators,
            interpretations=interpretations,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            mobile=mobile,
            name=name,
            no_value_requires_comment=no_value_requires_comment,
            notification_recipients=notification_recipients,
            notify_completing_user=notify_completing_user,
            organisation_units=organisation_units,
            period_type=period_type,
            query_mods=query_mods,
            render_as_tabs=render_as_tabs,
            render_horizontally=render_horizontally,
            sections=sections,
            sharing=sharing,
            short_name=short_name,
            skip_offline=skip_offline,
            style=style,
            translations=translations,
            user=user,
            valid_complete_only=valid_complete_only,
            workflow=workflow,
        )

        data_set.additional_properties = d
        return data_set

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
