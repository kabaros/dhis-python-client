import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.validation_rule_aggregation_type import ValidationRuleAggregationType
from ..models.validation_rule_dimension_item_type import ValidationRuleDimensionItemType
from ..models.validation_rule_importance import ValidationRuleImportance
from ..models.validation_rule_operator import ValidationRuleOperator
from ..models.validation_rule_period_type import ValidationRulePeriodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.expression import Expression
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.validation_rule_created_by import ValidationRuleCreatedBy
    from ..models.validation_rule_last_updated_by import ValidationRuleLastUpdatedBy
    from ..models.validation_rule_legend_set import ValidationRuleLegendSet
    from ..models.validation_rule_legend_sets_item import ValidationRuleLegendSetsItem
    from ..models.validation_rule_notification_templates_item import ValidationRuleNotificationTemplatesItem
    from ..models.validation_rule_user import ValidationRuleUser
    from ..models.validation_rule_validation_rule_groups_item import ValidationRuleValidationRuleGroupsItem


T = TypeVar("T", bound="ValidationRule")


@_attrs_define
class ValidationRule:
    """
    Attributes:
        aggregation_type (ValidationRuleAggregationType):
        dimension_item_type (ValidationRuleDimensionItemType):
        importance (ValidationRuleImportance):
        operator (ValidationRuleOperator):
        access (Union[Unset, Access]):
        aggregate_export_attribute_option_combo (Union[Unset, str]):
        aggregate_export_category_option_combo (Union[Unset, str]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ValidationRuleCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_instruction (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        instruction (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ValidationRuleLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        left_side (Union[Unset, Expression]):
        legend_set (Union[Unset, ValidationRuleLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['ValidationRuleLegendSetsItem']]):
        name (Union[Unset, str]):
        notification_templates (Union[Unset, list['ValidationRuleNotificationTemplatesItem']]):
        organisation_unit_levels (Union[Unset, list[int]]):
        period_type (Union[Unset, ValidationRulePeriodType]):
        query_mods (Union[Unset, QueryModifiers]):
        right_side (Union[Unset, Expression]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        skip_form_validation (Union[Unset, bool]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ValidationRuleUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        validation_rule_groups (Union[Unset, list['ValidationRuleValidationRuleGroupsItem']]):
    """

    aggregation_type: ValidationRuleAggregationType
    dimension_item_type: ValidationRuleDimensionItemType
    importance: ValidationRuleImportance
    operator: ValidationRuleOperator
    access: Union[Unset, "Access"] = UNSET
    aggregate_export_attribute_option_combo: Union[Unset, str] = UNSET
    aggregate_export_category_option_combo: Union[Unset, str] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ValidationRuleCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_instruction: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    instruction: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ValidationRuleLastUpdatedBy"] = UNSET
    left_side: Union[Unset, "Expression"] = UNSET
    legend_set: Union[Unset, "ValidationRuleLegendSet"] = UNSET
    legend_sets: Union[Unset, list["ValidationRuleLegendSetsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    notification_templates: Union[Unset, list["ValidationRuleNotificationTemplatesItem"]] = UNSET
    organisation_unit_levels: Union[Unset, list[int]] = UNSET
    period_type: Union[Unset, ValidationRulePeriodType] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    right_side: Union[Unset, "Expression"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    skip_form_validation: Union[Unset, bool] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ValidationRuleUser"] = UNSET
    validation_rule_groups: Union[Unset, list["ValidationRuleValidationRuleGroupsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        dimension_item_type = self.dimension_item_type.value

        importance = self.importance.value

        operator = self.operator.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        aggregate_export_attribute_option_combo = self.aggregate_export_attribute_option_combo

        aggregate_export_category_option_combo = self.aggregate_export_category_option_combo

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        dimension_item = self.dimension_item

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_instruction = self.display_instruction

        display_name = self.display_name

        display_short_name = self.display_short_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        href = self.href

        id = self.id

        instruction = self.instruction

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        left_side: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.left_side, Unset):
            left_side = self.left_side.to_dict()

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        legend_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legend_sets, Unset):
            legend_sets = []
            for legend_sets_item_data in self.legend_sets:
                legend_sets_item = legend_sets_item_data.to_dict()
                legend_sets.append(legend_sets_item)

        name = self.name

        notification_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_templates, Unset):
            notification_templates = []
            for notification_templates_item_data in self.notification_templates:
                notification_templates_item = notification_templates_item_data.to_dict()
                notification_templates.append(notification_templates_item)

        organisation_unit_levels: Union[Unset, list[int]] = UNSET
        if not isinstance(self.organisation_unit_levels, Unset):
            organisation_unit_levels = self.organisation_unit_levels

        period_type: Union[Unset, str] = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        right_side: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.right_side, Unset):
            right_side = self.right_side.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        skip_form_validation = self.skip_form_validation

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        validation_rule_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validation_rule_groups, Unset):
            validation_rule_groups = []
            for validation_rule_groups_item_data in self.validation_rule_groups:
                validation_rule_groups_item = validation_rule_groups_item_data.to_dict()
                validation_rule_groups.append(validation_rule_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "dimensionItemType": dimension_item_type,
                "importance": importance,
                "operator": operator,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if aggregate_export_attribute_option_combo is not UNSET:
            field_dict["aggregateExportAttributeOptionCombo"] = aggregate_export_attribute_option_combo
        if aggregate_export_category_option_combo is not UNSET:
            field_dict["aggregateExportCategoryOptionCombo"] = aggregate_export_category_option_combo
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_item is not UNSET:
            field_dict["dimensionItem"] = dimension_item
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_instruction is not UNSET:
            field_dict["displayInstruction"] = display_instruction
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
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
        if instruction is not UNSET:
            field_dict["instruction"] = instruction
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if left_side is not UNSET:
            field_dict["leftSide"] = left_side
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if name is not UNSET:
            field_dict["name"] = name
        if notification_templates is not UNSET:
            field_dict["notificationTemplates"] = notification_templates
        if organisation_unit_levels is not UNSET:
            field_dict["organisationUnitLevels"] = organisation_unit_levels
        if period_type is not UNSET:
            field_dict["periodType"] = period_type
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if right_side is not UNSET:
            field_dict["rightSide"] = right_side
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if skip_form_validation is not UNSET:
            field_dict["skipFormValidation"] = skip_form_validation
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if validation_rule_groups is not UNSET:
            field_dict["validationRuleGroups"] = validation_rule_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.expression import Expression
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.validation_rule_created_by import ValidationRuleCreatedBy
        from ..models.validation_rule_last_updated_by import ValidationRuleLastUpdatedBy
        from ..models.validation_rule_legend_set import ValidationRuleLegendSet
        from ..models.validation_rule_legend_sets_item import ValidationRuleLegendSetsItem
        from ..models.validation_rule_notification_templates_item import ValidationRuleNotificationTemplatesItem
        from ..models.validation_rule_user import ValidationRuleUser
        from ..models.validation_rule_validation_rule_groups_item import ValidationRuleValidationRuleGroupsItem

        d = src_dict.copy()
        aggregation_type = ValidationRuleAggregationType(d.pop("aggregationType"))

        dimension_item_type = ValidationRuleDimensionItemType(d.pop("dimensionItemType"))

        importance = ValidationRuleImportance(d.pop("importance"))

        operator = ValidationRuleOperator(d.pop("operator"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        aggregate_export_attribute_option_combo = d.pop("aggregateExportAttributeOptionCombo", UNSET)

        aggregate_export_category_option_combo = d.pop("aggregateExportCategoryOptionCombo", UNSET)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ValidationRuleCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ValidationRuleCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_instruction = d.pop("displayInstruction", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        instruction = d.pop("instruction", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ValidationRuleLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ValidationRuleLastUpdatedBy.from_dict(_last_updated_by)

        _left_side = d.pop("leftSide", UNSET)
        left_side: Union[Unset, Expression]
        if isinstance(_left_side, Unset):
            left_side = UNSET
        else:
            left_side = Expression.from_dict(_left_side)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, ValidationRuleLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = ValidationRuleLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = ValidationRuleLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        name = d.pop("name", UNSET)

        notification_templates = []
        _notification_templates = d.pop("notificationTemplates", UNSET)
        for notification_templates_item_data in _notification_templates or []:
            notification_templates_item = ValidationRuleNotificationTemplatesItem.from_dict(
                notification_templates_item_data
            )

            notification_templates.append(notification_templates_item)

        organisation_unit_levels = cast(list[int], d.pop("organisationUnitLevels", UNSET))

        _period_type = d.pop("periodType", UNSET)
        period_type: Union[Unset, ValidationRulePeriodType]
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = ValidationRulePeriodType(_period_type)

        _query_mods = d.pop("queryMods", UNSET)
        query_mods: Union[Unset, QueryModifiers]
        if isinstance(_query_mods, Unset):
            query_mods = UNSET
        else:
            query_mods = QueryModifiers.from_dict(_query_mods)

        _right_side = d.pop("rightSide", UNSET)
        right_side: Union[Unset, Expression]
        if isinstance(_right_side, Unset):
            right_side = UNSET
        else:
            right_side = Expression.from_dict(_right_side)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        skip_form_validation = d.pop("skipFormValidation", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ValidationRuleUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ValidationRuleUser.from_dict(_user)

        validation_rule_groups = []
        _validation_rule_groups = d.pop("validationRuleGroups", UNSET)
        for validation_rule_groups_item_data in _validation_rule_groups or []:
            validation_rule_groups_item = ValidationRuleValidationRuleGroupsItem.from_dict(
                validation_rule_groups_item_data
            )

            validation_rule_groups.append(validation_rule_groups_item)

        validation_rule = cls(
            aggregation_type=aggregation_type,
            dimension_item_type=dimension_item_type,
            importance=importance,
            operator=operator,
            access=access,
            aggregate_export_attribute_option_combo=aggregate_export_attribute_option_combo,
            aggregate_export_category_option_combo=aggregate_export_category_option_combo,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_instruction=display_instruction,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            instruction=instruction,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            left_side=left_side,
            legend_set=legend_set,
            legend_sets=legend_sets,
            name=name,
            notification_templates=notification_templates,
            organisation_unit_levels=organisation_unit_levels,
            period_type=period_type,
            query_mods=query_mods,
            right_side=right_side,
            sharing=sharing,
            short_name=short_name,
            skip_form_validation=skip_form_validation,
            translations=translations,
            user=user,
            validation_rule_groups=validation_rule_groups,
        )

        validation_rule.additional_properties = d
        return validation_rule

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
