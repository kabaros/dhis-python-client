import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_element_aggregation_type import DataElementAggregationType
from ..models.data_element_domain_type import DataElementDomainType
from ..models.data_element_value_type import DataElementValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.data_element_category_combo import DataElementCategoryCombo
    from ..models.data_element_comment_option_set import DataElementCommentOptionSet
    from ..models.data_element_created_by import DataElementCreatedBy
    from ..models.data_element_data_element_groups_item import DataElementDataElementGroupsItem
    from ..models.data_element_last_updated_by import DataElementLastUpdatedBy
    from ..models.data_element_legend_set import DataElementLegendSet
    from ..models.data_element_legend_sets_item import DataElementLegendSetsItem
    from ..models.data_element_option_set import DataElementOptionSet
    from ..models.data_element_user import DataElementUser
    from ..models.data_set_element import DataSetElement
    from ..models.file_type_value_options import FileTypeValueOptions
    from ..models.object_style import ObjectStyle
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="DataElement")


@_attrs_define
class DataElement:
    """
    Attributes:
        aggregation_type (DataElementAggregationType):
        domain_type (DataElementDomainType):
        value_type (DataElementValueType):
        access (Union[Unset, Access]):
        aggregation_levels (Union[Unset, list[int]]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_combo (Union[Unset, DataElementCategoryCombo]): A UID reference to a CategoryCombo
            (Java name `org.hisp.dhis.category.CategoryCombo`)
        code (Union[Unset, str]):
        comment_option_set (Union[Unset, DataElementCommentOptionSet]): A UID reference to a OptionSet
            (Java name `org.hisp.dhis.option.OptionSet`)
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, DataElementCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_element_groups (Union[Unset, list['DataElementDataElementGroupsItem']]):
        data_set_elements (Union[Unset, list['DataSetElement']]):
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        field_mask (Union[Unset, str]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, DataElementLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, DataElementLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['DataElementLegendSetsItem']]):
        name (Union[Unset, str]):
        option_set (Union[Unset, DataElementOptionSet]): A UID reference to a OptionSet
            (Java name `org.hisp.dhis.option.OptionSet`)
        option_set_value (Union[Unset, bool]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        style (Union[Unset, ObjectStyle]):
        translations (Union[Unset, list['Translation']]):
        url (Union[Unset, str]):
        user (Union[Unset, DataElementUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        value_type_options (Union[Unset, FileTypeValueOptions]):
        zero_is_significant (Union[Unset, bool]):
    """

    # aggregation_type: DataElementAggregationType
    # domain_type: DataElementDomainType
    # value_type: DataElementValueType
    access: Union[Unset, "Access"] = UNSET
    aggregation_levels: Union[Unset, list[int]] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_combo: Union[Unset, "DataElementCategoryCombo"] = UNSET
    code: Union[Unset, str] = UNSET
    comment_option_set: Union[Unset, "DataElementCommentOptionSet"] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "DataElementCreatedBy"] = UNSET
    data_element_groups: Union[Unset, list["DataElementDataElementGroupsItem"]] = UNSET
    data_set_elements: Union[Unset, list["DataSetElement"]] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    field_mask: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "DataElementLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "DataElementLegendSet"] = UNSET
    legend_sets: Union[Unset, list["DataElementLegendSetsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    option_set: Union[Unset, "DataElementOptionSet"] = UNSET
    option_set_value: Union[Unset, bool] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, "DataElementUser"] = UNSET
    value_type_options: Union[Unset, "FileTypeValueOptions"] = UNSET
    zero_is_significant: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        # aggregation_type = self.aggregation_type.value

        # domain_type = self.domain_type.value

        # value_type = self.value_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        aggregation_levels: Union[Unset, list[int]] = UNSET
        if not isinstance(self.aggregation_levels, Unset):
            aggregation_levels = self.aggregation_levels

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

        comment_option_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.comment_option_set, Unset):
            comment_option_set = self.comment_option_set.to_dict()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_element_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_element_groups, Unset):
            data_element_groups = []
            for data_element_groups_item_data in self.data_element_groups:
                data_element_groups_item = data_element_groups_item_data.to_dict()
                data_element_groups.append(data_element_groups_item)

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

        field_mask = self.field_mask

        form_name = self.form_name

        href = self.href

        id = self.id

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

        name = self.name

        option_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.option_set, Unset):
            option_set = self.option_set.to_dict()

        option_set_value = self.option_set_value

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        url = self.url

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        value_type_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value_type_options, Unset):
            value_type_options = self.value_type_options.to_dict()

        zero_is_significant = self.zero_is_significant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        # field_dict.update(
        #     {
        #         "aggregationType": aggregation_type,
        #         "domainType": domain_type,
        #         "valueType": value_type,
        #     }
        # )
        if access is not UNSET:
            field_dict["access"] = access
        if aggregation_levels is not UNSET:
            field_dict["aggregationLevels"] = aggregation_levels
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_combo is not UNSET:
            field_dict["categoryCombo"] = category_combo
        if code is not UNSET:
            field_dict["code"] = code
        if comment_option_set is not UNSET:
            field_dict["commentOptionSet"] = comment_option_set
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_element_groups is not UNSET:
            field_dict["dataElementGroups"] = data_element_groups
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
        if field_mask is not UNSET:
            field_dict["fieldMask"] = field_mask
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if name is not UNSET:
            field_dict["name"] = name
        if option_set is not UNSET:
            field_dict["optionSet"] = option_set
        if option_set_value is not UNSET:
            field_dict["optionSetValue"] = option_set_value
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if style is not UNSET:
            field_dict["style"] = style
        if translations is not UNSET:
            field_dict["translations"] = translations
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user
        if value_type_options is not UNSET:
            field_dict["valueTypeOptions"] = value_type_options
        if zero_is_significant is not UNSET:
            field_dict["zeroIsSignificant"] = zero_is_significant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.data_element_category_combo import DataElementCategoryCombo
        from ..models.data_element_comment_option_set import DataElementCommentOptionSet
        from ..models.data_element_created_by import DataElementCreatedBy
        from ..models.data_element_data_element_groups_item import DataElementDataElementGroupsItem
        from ..models.data_element_last_updated_by import DataElementLastUpdatedBy
        from ..models.data_element_legend_set import DataElementLegendSet
        from ..models.data_element_legend_sets_item import DataElementLegendSetsItem
        from ..models.data_element_option_set import DataElementOptionSet
        from ..models.data_element_user import DataElementUser
        from ..models.data_set_element import DataSetElement
        from ..models.file_type_value_options import FileTypeValueOptions
        from ..models.object_style import ObjectStyle
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        # aggregation_type = DataElementAggregationType(d.pop("aggregationType"))

        # domain_type = DataElementDomainType(d.pop("domainType"))

        # value_type = DataElementValueType(d.pop("valueType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        aggregation_levels = cast(list[int], d.pop("aggregationLevels", UNSET))

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        _category_combo = d.pop("categoryCombo", UNSET)
        category_combo: Union[Unset, DataElementCategoryCombo]
        if isinstance(_category_combo, Unset):
            category_combo = UNSET
        else:
            category_combo = DataElementCategoryCombo.from_dict(_category_combo)

        code = d.pop("code", UNSET)

        _comment_option_set = d.pop("commentOptionSet", UNSET)
        comment_option_set: Union[Unset, DataElementCommentOptionSet]
        if isinstance(_comment_option_set, Unset):
            comment_option_set = UNSET
        else:
            comment_option_set = DataElementCommentOptionSet.from_dict(_comment_option_set)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, DataElementCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = DataElementCreatedBy.from_dict(_created_by)

        data_element_groups = []
        _data_element_groups = d.pop("dataElementGroups", UNSET)
        for data_element_groups_item_data in _data_element_groups or []:
            data_element_groups_item = DataElementDataElementGroupsItem.from_dict(data_element_groups_item_data)

            data_element_groups.append(data_element_groups_item)

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

        field_mask = d.pop("fieldMask", UNSET)

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, DataElementLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = DataElementLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, DataElementLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = DataElementLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = DataElementLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        name = d.pop("name", UNSET)

        _option_set = d.pop("optionSet", UNSET)
        option_set: Union[Unset, DataElementOptionSet]
        if isinstance(_option_set, Unset):
            option_set = UNSET
        else:
            option_set = DataElementOptionSet.from_dict(_option_set)

        option_set_value = d.pop("optionSetValue", UNSET)

        _query_mods = d.pop("queryMods", UNSET)
        query_mods: Union[Unset, QueryModifiers]
        if isinstance(_query_mods, Unset):
            query_mods = UNSET
        else:
            query_mods = QueryModifiers.from_dict(_query_mods)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

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

        url = d.pop("url", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, DataElementUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = DataElementUser.from_dict(_user)

        _value_type_options = d.pop("valueTypeOptions", UNSET)
        value_type_options: Union[Unset, FileTypeValueOptions]
        if isinstance(_value_type_options, Unset):
            value_type_options = UNSET
        else:
            value_type_options = FileTypeValueOptions.from_dict(_value_type_options)

        zero_is_significant = d.pop("zeroIsSignificant", UNSET)

        data_element = cls(
            # aggregation_type=aggregation_type,
            # domain_type=domain_type,
            # value_type=value_type,
            access=access,
            aggregation_levels=aggregation_levels,
            attribute_values=attribute_values,
            category_combo=category_combo,
            code=code,
            comment_option_set=comment_option_set,
            created=created,
            created_by=created_by,
            data_element_groups=data_element_groups,
            data_set_elements=data_set_elements,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            field_mask=field_mask,
            form_name=form_name,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            name=name,
            option_set=option_set,
            option_set_value=option_set_value,
            query_mods=query_mods,
            sharing=sharing,
            short_name=short_name,
            style=style,
            translations=translations,
            url=url,
            user=user,
            value_type_options=value_type_options,
            zero_is_significant=zero_is_significant,
        )

        data_element.additional_properties = d
        return data_element

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
