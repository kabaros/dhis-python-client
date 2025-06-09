import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attribute_value_type import AttributeValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_created_by import AttributeCreatedBy
    from ..models.attribute_last_updated_by import AttributeLastUpdatedBy
    from ..models.attribute_option_set import AttributeOptionSet
    from ..models.attribute_user import AttributeUser
    from ..models.attribute_value import AttributeValue
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Attribute")


@_attrs_define
class Attribute:
    """
    Attributes:
        value_type (AttributeValueType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_attribute (Union[Unset, bool]):
        category_option_attribute (Union[Unset, bool]):
        category_option_combo_attribute (Union[Unset, bool]):
        category_option_group_attribute (Union[Unset, bool]):
        category_option_group_set_attribute (Union[Unset, bool]):
        code (Union[Unset, str]):
        constant_attribute (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, AttributeCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_element_attribute (Union[Unset, bool]):
        data_element_group_attribute (Union[Unset, bool]):
        data_element_group_set_attribute (Union[Unset, bool]):
        data_set_attribute (Union[Unset, bool]):
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        document_attribute (Union[Unset, bool]):
        event_chart_attribute (Union[Unset, bool]):
        event_report_attribute (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        indicator_attribute (Union[Unset, bool]):
        indicator_group_attribute (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, AttributeLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set_attribute (Union[Unset, bool]):
        mandatory (Union[Unset, bool]):
        map_attribute (Union[Unset, bool]):
        name (Union[Unset, str]):
        object_types (Union[Unset, list[str]]):
        option_attribute (Union[Unset, bool]):
        option_set (Union[Unset, AttributeOptionSet]): A UID reference to a OptionSet
            (Java name `org.hisp.dhis.option.OptionSet`)
        option_set_attribute (Union[Unset, bool]):
        organisation_unit_attribute (Union[Unset, bool]):
        organisation_unit_group_attribute (Union[Unset, bool]):
        organisation_unit_group_set_attribute (Union[Unset, bool]):
        program_attribute (Union[Unset, bool]):
        program_indicator_attribute (Union[Unset, bool]):
        program_stage_attribute (Union[Unset, bool]):
        relationship_type_attribute (Union[Unset, bool]):
        section_attribute (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        sort_order (Union[Unset, int]):
        sql_view_attribute (Union[Unset, bool]):
        tracked_entity_attribute_attribute (Union[Unset, bool]):
        tracked_entity_type_attribute (Union[Unset, bool]):
        translations (Union[Unset, list['Translation']]):
        unique (Union[Unset, bool]):
        user (Union[Unset, AttributeUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_attribute (Union[Unset, bool]):
        user_group_attribute (Union[Unset, bool]):
        validation_rule_attribute (Union[Unset, bool]):
        validation_rule_group_attribute (Union[Unset, bool]):
        visualization_attribute (Union[Unset, bool]):
    """

    value_type: AttributeValueType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_attribute: Union[Unset, bool] = UNSET
    category_option_attribute: Union[Unset, bool] = UNSET
    category_option_combo_attribute: Union[Unset, bool] = UNSET
    category_option_group_attribute: Union[Unset, bool] = UNSET
    category_option_group_set_attribute: Union[Unset, bool] = UNSET
    code: Union[Unset, str] = UNSET
    constant_attribute: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "AttributeCreatedBy"] = UNSET
    data_element_attribute: Union[Unset, bool] = UNSET
    data_element_group_attribute: Union[Unset, bool] = UNSET
    data_element_group_set_attribute: Union[Unset, bool] = UNSET
    data_set_attribute: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    document_attribute: Union[Unset, bool] = UNSET
    event_chart_attribute: Union[Unset, bool] = UNSET
    event_report_attribute: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    indicator_attribute: Union[Unset, bool] = UNSET
    indicator_group_attribute: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "AttributeLastUpdatedBy"] = UNSET
    legend_set_attribute: Union[Unset, bool] = UNSET
    mandatory: Union[Unset, bool] = UNSET
    map_attribute: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    object_types: Union[Unset, list[str]] = UNSET
    option_attribute: Union[Unset, bool] = UNSET
    option_set: Union[Unset, "AttributeOptionSet"] = UNSET
    option_set_attribute: Union[Unset, bool] = UNSET
    organisation_unit_attribute: Union[Unset, bool] = UNSET
    organisation_unit_group_attribute: Union[Unset, bool] = UNSET
    organisation_unit_group_set_attribute: Union[Unset, bool] = UNSET
    program_attribute: Union[Unset, bool] = UNSET
    program_indicator_attribute: Union[Unset, bool] = UNSET
    program_stage_attribute: Union[Unset, bool] = UNSET
    relationship_type_attribute: Union[Unset, bool] = UNSET
    section_attribute: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    sort_order: Union[Unset, int] = UNSET
    sql_view_attribute: Union[Unset, bool] = UNSET
    tracked_entity_attribute_attribute: Union[Unset, bool] = UNSET
    tracked_entity_type_attribute: Union[Unset, bool] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    unique: Union[Unset, bool] = UNSET
    user: Union[Unset, "AttributeUser"] = UNSET
    user_attribute: Union[Unset, bool] = UNSET
    user_group_attribute: Union[Unset, bool] = UNSET
    validation_rule_attribute: Union[Unset, bool] = UNSET
    validation_rule_group_attribute: Union[Unset, bool] = UNSET
    visualization_attribute: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        category_attribute = self.category_attribute

        category_option_attribute = self.category_option_attribute

        category_option_combo_attribute = self.category_option_combo_attribute

        category_option_group_attribute = self.category_option_group_attribute

        category_option_group_set_attribute = self.category_option_group_set_attribute

        code = self.code

        constant_attribute = self.constant_attribute

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_element_attribute = self.data_element_attribute

        data_element_group_attribute = self.data_element_group_attribute

        data_element_group_set_attribute = self.data_element_group_set_attribute

        data_set_attribute = self.data_set_attribute

        description = self.description

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        document_attribute = self.document_attribute

        event_chart_attribute = self.event_chart_attribute

        event_report_attribute = self.event_report_attribute

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        href = self.href

        id = self.id

        indicator_attribute = self.indicator_attribute

        indicator_group_attribute = self.indicator_group_attribute

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        legend_set_attribute = self.legend_set_attribute

        mandatory = self.mandatory

        map_attribute = self.map_attribute

        name = self.name

        object_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.object_types, Unset):
            object_types = self.object_types

        option_attribute = self.option_attribute

        option_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.option_set, Unset):
            option_set = self.option_set.to_dict()

        option_set_attribute = self.option_set_attribute

        organisation_unit_attribute = self.organisation_unit_attribute

        organisation_unit_group_attribute = self.organisation_unit_group_attribute

        organisation_unit_group_set_attribute = self.organisation_unit_group_set_attribute

        program_attribute = self.program_attribute

        program_indicator_attribute = self.program_indicator_attribute

        program_stage_attribute = self.program_stage_attribute

        relationship_type_attribute = self.relationship_type_attribute

        section_attribute = self.section_attribute

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        sort_order = self.sort_order

        sql_view_attribute = self.sql_view_attribute

        tracked_entity_attribute_attribute = self.tracked_entity_attribute_attribute

        tracked_entity_type_attribute = self.tracked_entity_type_attribute

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        unique = self.unique

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_attribute = self.user_attribute

        user_group_attribute = self.user_group_attribute

        validation_rule_attribute = self.validation_rule_attribute

        validation_rule_group_attribute = self.validation_rule_group_attribute

        visualization_attribute = self.visualization_attribute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valueType": value_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_attribute is not UNSET:
            field_dict["categoryAttribute"] = category_attribute
        if category_option_attribute is not UNSET:
            field_dict["categoryOptionAttribute"] = category_option_attribute
        if category_option_combo_attribute is not UNSET:
            field_dict["categoryOptionComboAttribute"] = category_option_combo_attribute
        if category_option_group_attribute is not UNSET:
            field_dict["categoryOptionGroupAttribute"] = category_option_group_attribute
        if category_option_group_set_attribute is not UNSET:
            field_dict["categoryOptionGroupSetAttribute"] = category_option_group_set_attribute
        if code is not UNSET:
            field_dict["code"] = code
        if constant_attribute is not UNSET:
            field_dict["constantAttribute"] = constant_attribute
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_element_attribute is not UNSET:
            field_dict["dataElementAttribute"] = data_element_attribute
        if data_element_group_attribute is not UNSET:
            field_dict["dataElementGroupAttribute"] = data_element_group_attribute
        if data_element_group_set_attribute is not UNSET:
            field_dict["dataElementGroupSetAttribute"] = data_element_group_set_attribute
        if data_set_attribute is not UNSET:
            field_dict["dataSetAttribute"] = data_set_attribute
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if document_attribute is not UNSET:
            field_dict["documentAttribute"] = document_attribute
        if event_chart_attribute is not UNSET:
            field_dict["eventChartAttribute"] = event_chart_attribute
        if event_report_attribute is not UNSET:
            field_dict["eventReportAttribute"] = event_report_attribute
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if indicator_attribute is not UNSET:
            field_dict["indicatorAttribute"] = indicator_attribute
        if indicator_group_attribute is not UNSET:
            field_dict["indicatorGroupAttribute"] = indicator_group_attribute
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set_attribute is not UNSET:
            field_dict["legendSetAttribute"] = legend_set_attribute
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if map_attribute is not UNSET:
            field_dict["mapAttribute"] = map_attribute
        if name is not UNSET:
            field_dict["name"] = name
        if object_types is not UNSET:
            field_dict["objectTypes"] = object_types
        if option_attribute is not UNSET:
            field_dict["optionAttribute"] = option_attribute
        if option_set is not UNSET:
            field_dict["optionSet"] = option_set
        if option_set_attribute is not UNSET:
            field_dict["optionSetAttribute"] = option_set_attribute
        if organisation_unit_attribute is not UNSET:
            field_dict["organisationUnitAttribute"] = organisation_unit_attribute
        if organisation_unit_group_attribute is not UNSET:
            field_dict["organisationUnitGroupAttribute"] = organisation_unit_group_attribute
        if organisation_unit_group_set_attribute is not UNSET:
            field_dict["organisationUnitGroupSetAttribute"] = organisation_unit_group_set_attribute
        if program_attribute is not UNSET:
            field_dict["programAttribute"] = program_attribute
        if program_indicator_attribute is not UNSET:
            field_dict["programIndicatorAttribute"] = program_indicator_attribute
        if program_stage_attribute is not UNSET:
            field_dict["programStageAttribute"] = program_stage_attribute
        if relationship_type_attribute is not UNSET:
            field_dict["relationshipTypeAttribute"] = relationship_type_attribute
        if section_attribute is not UNSET:
            field_dict["sectionAttribute"] = section_attribute
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if sql_view_attribute is not UNSET:
            field_dict["sqlViewAttribute"] = sql_view_attribute
        if tracked_entity_attribute_attribute is not UNSET:
            field_dict["trackedEntityAttributeAttribute"] = tracked_entity_attribute_attribute
        if tracked_entity_type_attribute is not UNSET:
            field_dict["trackedEntityTypeAttribute"] = tracked_entity_type_attribute
        if translations is not UNSET:
            field_dict["translations"] = translations
        if unique is not UNSET:
            field_dict["unique"] = unique
        if user is not UNSET:
            field_dict["user"] = user
        if user_attribute is not UNSET:
            field_dict["userAttribute"] = user_attribute
        if user_group_attribute is not UNSET:
            field_dict["userGroupAttribute"] = user_group_attribute
        if validation_rule_attribute is not UNSET:
            field_dict["validationRuleAttribute"] = validation_rule_attribute
        if validation_rule_group_attribute is not UNSET:
            field_dict["validationRuleGroupAttribute"] = validation_rule_group_attribute
        if visualization_attribute is not UNSET:
            field_dict["visualizationAttribute"] = visualization_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_created_by import AttributeCreatedBy
        from ..models.attribute_last_updated_by import AttributeLastUpdatedBy
        from ..models.attribute_option_set import AttributeOptionSet
        from ..models.attribute_user import AttributeUser
        from ..models.attribute_value import AttributeValue
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        value_type = AttributeValueType(d.pop("valueType"))

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

        category_attribute = d.pop("categoryAttribute", UNSET)

        category_option_attribute = d.pop("categoryOptionAttribute", UNSET)

        category_option_combo_attribute = d.pop("categoryOptionComboAttribute", UNSET)

        category_option_group_attribute = d.pop("categoryOptionGroupAttribute", UNSET)

        category_option_group_set_attribute = d.pop("categoryOptionGroupSetAttribute", UNSET)

        code = d.pop("code", UNSET)

        constant_attribute = d.pop("constantAttribute", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, AttributeCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = AttributeCreatedBy.from_dict(_created_by)

        data_element_attribute = d.pop("dataElementAttribute", UNSET)

        data_element_group_attribute = d.pop("dataElementGroupAttribute", UNSET)

        data_element_group_set_attribute = d.pop("dataElementGroupSetAttribute", UNSET)

        data_set_attribute = d.pop("dataSetAttribute", UNSET)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        document_attribute = d.pop("documentAttribute", UNSET)

        event_chart_attribute = d.pop("eventChartAttribute", UNSET)

        event_report_attribute = d.pop("eventReportAttribute", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        indicator_attribute = d.pop("indicatorAttribute", UNSET)

        indicator_group_attribute = d.pop("indicatorGroupAttribute", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, AttributeLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = AttributeLastUpdatedBy.from_dict(_last_updated_by)

        legend_set_attribute = d.pop("legendSetAttribute", UNSET)

        mandatory = d.pop("mandatory", UNSET)

        map_attribute = d.pop("mapAttribute", UNSET)

        name = d.pop("name", UNSET)

        object_types = cast(list[str], d.pop("objectTypes", UNSET))

        option_attribute = d.pop("optionAttribute", UNSET)

        _option_set = d.pop("optionSet", UNSET)
        option_set: Union[Unset, AttributeOptionSet]
        if isinstance(_option_set, Unset):
            option_set = UNSET
        else:
            option_set = AttributeOptionSet.from_dict(_option_set)

        option_set_attribute = d.pop("optionSetAttribute", UNSET)

        organisation_unit_attribute = d.pop("organisationUnitAttribute", UNSET)

        organisation_unit_group_attribute = d.pop("organisationUnitGroupAttribute", UNSET)

        organisation_unit_group_set_attribute = d.pop("organisationUnitGroupSetAttribute", UNSET)

        program_attribute = d.pop("programAttribute", UNSET)

        program_indicator_attribute = d.pop("programIndicatorAttribute", UNSET)

        program_stage_attribute = d.pop("programStageAttribute", UNSET)

        relationship_type_attribute = d.pop("relationshipTypeAttribute", UNSET)

        section_attribute = d.pop("sectionAttribute", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        sql_view_attribute = d.pop("sqlViewAttribute", UNSET)

        tracked_entity_attribute_attribute = d.pop("trackedEntityAttributeAttribute", UNSET)

        tracked_entity_type_attribute = d.pop("trackedEntityTypeAttribute", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        unique = d.pop("unique", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, AttributeUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = AttributeUser.from_dict(_user)

        user_attribute = d.pop("userAttribute", UNSET)

        user_group_attribute = d.pop("userGroupAttribute", UNSET)

        validation_rule_attribute = d.pop("validationRuleAttribute", UNSET)

        validation_rule_group_attribute = d.pop("validationRuleGroupAttribute", UNSET)

        visualization_attribute = d.pop("visualizationAttribute", UNSET)

        attribute = cls(
            value_type=value_type,
            access=access,
            attribute_values=attribute_values,
            category_attribute=category_attribute,
            category_option_attribute=category_option_attribute,
            category_option_combo_attribute=category_option_combo_attribute,
            category_option_group_attribute=category_option_group_attribute,
            category_option_group_set_attribute=category_option_group_set_attribute,
            code=code,
            constant_attribute=constant_attribute,
            created=created,
            created_by=created_by,
            data_element_attribute=data_element_attribute,
            data_element_group_attribute=data_element_group_attribute,
            data_element_group_set_attribute=data_element_group_set_attribute,
            data_set_attribute=data_set_attribute,
            description=description,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            document_attribute=document_attribute,
            event_chart_attribute=event_chart_attribute,
            event_report_attribute=event_report_attribute,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            indicator_attribute=indicator_attribute,
            indicator_group_attribute=indicator_group_attribute,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set_attribute=legend_set_attribute,
            mandatory=mandatory,
            map_attribute=map_attribute,
            name=name,
            object_types=object_types,
            option_attribute=option_attribute,
            option_set=option_set,
            option_set_attribute=option_set_attribute,
            organisation_unit_attribute=organisation_unit_attribute,
            organisation_unit_group_attribute=organisation_unit_group_attribute,
            organisation_unit_group_set_attribute=organisation_unit_group_set_attribute,
            program_attribute=program_attribute,
            program_indicator_attribute=program_indicator_attribute,
            program_stage_attribute=program_stage_attribute,
            relationship_type_attribute=relationship_type_attribute,
            section_attribute=section_attribute,
            sharing=sharing,
            short_name=short_name,
            sort_order=sort_order,
            sql_view_attribute=sql_view_attribute,
            tracked_entity_attribute_attribute=tracked_entity_attribute_attribute,
            tracked_entity_type_attribute=tracked_entity_type_attribute,
            translations=translations,
            unique=unique,
            user=user,
            user_attribute=user_attribute,
            user_group_attribute=user_group_attribute,
            validation_rule_attribute=validation_rule_attribute,
            validation_rule_group_attribute=validation_rule_group_attribute,
            visualization_attribute=visualization_attribute,
        )

        attribute.additional_properties = d
        return attribute

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
