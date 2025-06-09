import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.data_element_operand_attribute_option_combo import DataElementOperandAttributeOptionCombo
    from ..models.data_element_operand_category_option_combo import DataElementOperandCategoryOptionCombo
    from ..models.data_element_operand_created_by import DataElementOperandCreatedBy
    from ..models.data_element_operand_data_element import DataElementOperandDataElement
    from ..models.data_element_operand_last_updated_by import DataElementOperandLastUpdatedBy
    from ..models.data_element_operand_legend_set import DataElementOperandLegendSet
    from ..models.data_element_operand_legend_sets_item import DataElementOperandLegendSetsItem
    from ..models.data_element_operand_user import DataElementOperandUser
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="DataElementOperand")


@_attrs_define
class DataElementOperand:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_option_combo (Union[Unset, DataElementOperandAttributeOptionCombo]): A UID reference to a
            CategoryOptionCombo
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`)
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_option_combo (Union[Unset, DataElementOperandCategoryOptionCombo]): A UID reference to a
            CategoryOptionCombo
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`)
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, DataElementOperandCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_element (Union[Unset, DataElementOperandDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, DataElementOperandLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, DataElementOperandLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['DataElementOperandLegendSetsItem']]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, DataElementOperandUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_option_combo: Union[Unset, "DataElementOperandAttributeOptionCombo"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_option_combo: Union[Unset, "DataElementOperandCategoryOptionCombo"] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "DataElementOperandCreatedBy"] = UNSET
    data_element: Union[Unset, "DataElementOperandDataElement"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "DataElementOperandLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "DataElementOperandLegendSet"] = UNSET
    legend_sets: Union[Unset, list["DataElementOperandLegendSetsItem"]] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "DataElementOperandUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_option_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute_option_combo, Unset):
            attribute_option_combo = self.attribute_option_combo.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        category_option_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_option_combo, Unset):
            category_option_combo = self.category_option_combo.to_dict()

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

        description = self.description

        display_description = self.display_description

        display_form_name = self.display_form_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        href = self.href

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

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

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
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_option_combo is not UNSET:
            field_dict["categoryOptionCombo"] = category_option_combo
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if href is not UNSET:
            field_dict["href"] = href
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.data_element_operand_attribute_option_combo import DataElementOperandAttributeOptionCombo
        from ..models.data_element_operand_category_option_combo import DataElementOperandCategoryOptionCombo
        from ..models.data_element_operand_created_by import DataElementOperandCreatedBy
        from ..models.data_element_operand_data_element import DataElementOperandDataElement
        from ..models.data_element_operand_last_updated_by import DataElementOperandLastUpdatedBy
        from ..models.data_element_operand_legend_set import DataElementOperandLegendSet
        from ..models.data_element_operand_legend_sets_item import DataElementOperandLegendSetsItem
        from ..models.data_element_operand_user import DataElementOperandUser
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        _attribute_option_combo = d.pop("attributeOptionCombo", UNSET)
        attribute_option_combo: Union[Unset, DataElementOperandAttributeOptionCombo]
        if isinstance(_attribute_option_combo, Unset):
            attribute_option_combo = UNSET
        else:
            attribute_option_combo = DataElementOperandAttributeOptionCombo.from_dict(_attribute_option_combo)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        _category_option_combo = d.pop("categoryOptionCombo", UNSET)
        category_option_combo: Union[Unset, DataElementOperandCategoryOptionCombo]
        if isinstance(_category_option_combo, Unset):
            category_option_combo = UNSET
        else:
            category_option_combo = DataElementOperandCategoryOptionCombo.from_dict(_category_option_combo)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, DataElementOperandCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = DataElementOperandCreatedBy.from_dict(_created_by)

        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, DataElementOperandDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = DataElementOperandDataElement.from_dict(_data_element)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, DataElementOperandLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = DataElementOperandLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, DataElementOperandLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = DataElementOperandLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = DataElementOperandLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

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

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, DataElementOperandUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = DataElementOperandUser.from_dict(_user)

        data_element_operand = cls(
            access=access,
            attribute_option_combo=attribute_option_combo,
            attribute_values=attribute_values,
            category_option_combo=category_option_combo,
            code=code,
            created=created,
            created_by=created_by,
            data_element=data_element,
            description=description,
            display_description=display_description,
            display_form_name=display_form_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            legend_sets=legend_sets,
            query_mods=query_mods,
            sharing=sharing,
            translations=translations,
            user=user,
        )

        data_element_operand.additional_properties = d
        return data_element_operand

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
