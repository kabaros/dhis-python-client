import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.data_element_operand import DataElementOperand
    from ..models.section_category_combos_item import SectionCategoryCombosItem
    from ..models.section_created_by import SectionCreatedBy
    from ..models.section_data_elements_item import SectionDataElementsItem
    from ..models.section_data_set import SectionDataSet
    from ..models.section_indicators_item import SectionIndicatorsItem
    from ..models.section_last_updated_by import SectionLastUpdatedBy
    from ..models.section_user import SectionUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Section")


@_attrs_define
class Section:
    """
    Attributes:
        sort_order (int):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_combos (Union[Unset, list['SectionCategoryCombosItem']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, SectionCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_elements (Union[Unset, list['SectionDataElementsItem']]):
        data_set (Union[Unset, SectionDataSet]): A UID reference to a DataSet
            (Java name `org.hisp.dhis.dataset.DataSet`)
        description (Union[Unset, str]):
        disable_data_element_auto_group (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        display_options (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        greyed_fields (Union[Unset, list['DataElementOperand']]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        indicators (Union[Unset, list['SectionIndicatorsItem']]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, SectionLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        show_column_totals (Union[Unset, bool]):
        show_row_totals (Union[Unset, bool]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, SectionUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    sort_order: int
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_combos: Union[Unset, list["SectionCategoryCombosItem"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "SectionCreatedBy"] = UNSET
    data_elements: Union[Unset, list["SectionDataElementsItem"]] = UNSET
    data_set: Union[Unset, "SectionDataSet"] = UNSET
    description: Union[Unset, str] = UNSET
    disable_data_element_auto_group: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_options: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    greyed_fields: Union[Unset, list["DataElementOperand"]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    indicators: Union[Unset, list["SectionIndicatorsItem"]] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "SectionLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    show_column_totals: Union[Unset, bool] = UNSET
    show_row_totals: Union[Unset, bool] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "SectionUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sort_order = self.sort_order

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        category_combos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_combos, Unset):
            category_combos = []
            for category_combos_item_data in self.category_combos:
                category_combos_item = category_combos_item_data.to_dict()
                category_combos.append(category_combos_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_elements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_elements, Unset):
            data_elements = []
            for data_elements_item_data in self.data_elements:
                data_elements_item = data_elements_item_data.to_dict()
                data_elements.append(data_elements_item)

        data_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_set, Unset):
            data_set = self.data_set.to_dict()

        description = self.description

        disable_data_element_auto_group = self.disable_data_element_auto_group

        display_name = self.display_name

        display_options = self.display_options

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        greyed_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.greyed_fields, Unset):
            greyed_fields = []
            for greyed_fields_item_data in self.greyed_fields:
                greyed_fields_item = greyed_fields_item_data.to_dict()
                greyed_fields.append(greyed_fields_item)

        href = self.href

        id = self.id

        indicators: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicators, Unset):
            indicators = []
            for indicators_item_data in self.indicators:
                indicators_item = indicators_item_data.to_dict()
                indicators.append(indicators_item)

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        show_column_totals = self.show_column_totals

        show_row_totals = self.show_row_totals

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
                "sortOrder": sort_order,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_combos is not UNSET:
            field_dict["categoryCombos"] = category_combos
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_elements is not UNSET:
            field_dict["dataElements"] = data_elements
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
        if description is not UNSET:
            field_dict["description"] = description
        if disable_data_element_auto_group is not UNSET:
            field_dict["disableDataElementAutoGroup"] = disable_data_element_auto_group
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_options is not UNSET:
            field_dict["displayOptions"] = display_options
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if greyed_fields is not UNSET:
            field_dict["greyedFields"] = greyed_fields
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if indicators is not UNSET:
            field_dict["indicators"] = indicators
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if name is not UNSET:
            field_dict["name"] = name
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if show_column_totals is not UNSET:
            field_dict["showColumnTotals"] = show_column_totals
        if show_row_totals is not UNSET:
            field_dict["showRowTotals"] = show_row_totals
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.data_element_operand import DataElementOperand
        from ..models.section_category_combos_item import SectionCategoryCombosItem
        from ..models.section_created_by import SectionCreatedBy
        from ..models.section_data_elements_item import SectionDataElementsItem
        from ..models.section_data_set import SectionDataSet
        from ..models.section_indicators_item import SectionIndicatorsItem
        from ..models.section_last_updated_by import SectionLastUpdatedBy
        from ..models.section_user import SectionUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        sort_order = d.pop("sortOrder")

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

        category_combos = []
        _category_combos = d.pop("categoryCombos", UNSET)
        for category_combos_item_data in _category_combos or []:
            category_combos_item = SectionCategoryCombosItem.from_dict(category_combos_item_data)

            category_combos.append(category_combos_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, SectionCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = SectionCreatedBy.from_dict(_created_by)

        data_elements = []
        _data_elements = d.pop("dataElements", UNSET)
        for data_elements_item_data in _data_elements or []:
            data_elements_item = SectionDataElementsItem.from_dict(data_elements_item_data)

            data_elements.append(data_elements_item)

        _data_set = d.pop("dataSet", UNSET)
        data_set: Union[Unset, SectionDataSet]
        if isinstance(_data_set, Unset):
            data_set = UNSET
        else:
            data_set = SectionDataSet.from_dict(_data_set)

        description = d.pop("description", UNSET)

        disable_data_element_auto_group = d.pop("disableDataElementAutoGroup", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_options = d.pop("displayOptions", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        greyed_fields = []
        _greyed_fields = d.pop("greyedFields", UNSET)
        for greyed_fields_item_data in _greyed_fields or []:
            greyed_fields_item = DataElementOperand.from_dict(greyed_fields_item_data)

            greyed_fields.append(greyed_fields_item)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        indicators = []
        _indicators = d.pop("indicators", UNSET)
        for indicators_item_data in _indicators or []:
            indicators_item = SectionIndicatorsItem.from_dict(indicators_item_data)

            indicators.append(indicators_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, SectionLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = SectionLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        show_column_totals = d.pop("showColumnTotals", UNSET)

        show_row_totals = d.pop("showRowTotals", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, SectionUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = SectionUser.from_dict(_user)

        section = cls(
            sort_order=sort_order,
            access=access,
            attribute_values=attribute_values,
            category_combos=category_combos,
            code=code,
            created=created,
            created_by=created_by,
            data_elements=data_elements,
            data_set=data_set,
            description=description,
            disable_data_element_auto_group=disable_data_element_auto_group,
            display_name=display_name,
            display_options=display_options,
            favorite=favorite,
            favorites=favorites,
            greyed_fields=greyed_fields,
            href=href,
            id=id,
            indicators=indicators,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            sharing=sharing,
            show_column_totals=show_column_totals,
            show_row_totals=show_row_totals,
            translations=translations,
            user=user,
        )

        section.additional_properties = d
        return section

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
