import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_category_combo_categories_item_category_options_item_organisation_units_item import (
        FormCategoryComboCategoriesItemCategoryOptionsItemOrganisationUnitsItem,
    )


T = TypeVar("T", bound="FormCategoryComboCategoriesItemCategoryOptionsItem")


@_attrs_define
class FormCategoryComboCategoriesItemCategoryOptionsItem:
    """
    Attributes:
        end_date (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        label (Union[Unset, str]):
        organisation_units (Union[Unset,
            list['FormCategoryComboCategoriesItemCategoryOptionsItemOrganisationUnitsItem']]):
        start_date (Union[Unset, datetime.datetime]):
    """

    end_date: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    organisation_units: Union[
        Unset, list["FormCategoryComboCategoriesItemCategoryOptionsItemOrganisationUnitsItem"]
    ] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        id = self.id

        label = self.label

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if start_date is not UNSET:
            field_dict["startDate"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.form_category_combo_categories_item_category_options_item_organisation_units_item import (
            FormCategoryComboCategoriesItemCategoryOptionsItemOrganisationUnitsItem,
        )

        d = src_dict.copy()
        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = FormCategoryComboCategoriesItemCategoryOptionsItemOrganisationUnitsItem.from_dict(
                organisation_units_item_data
            )

            organisation_units.append(organisation_units_item)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        form_category_combo_categories_item_category_options_item = cls(
            end_date=end_date,
            id=id,
            label=label,
            organisation_units=organisation_units,
            start_date=start_date,
        )

        form_category_combo_categories_item_category_options_item.additional_properties = d
        return form_category_combo_categories_item_category_options_item

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
