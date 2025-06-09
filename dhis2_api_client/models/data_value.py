from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataValue")


@_attrs_define
class DataValue:
    """
    Attributes:
        attribute_option_combo (Union[Unset, str]):
        category_option_combo (Union[Unset, str]):
        comment (Union[Unset, str]):
        created (Union[Unset, str]):
        data_element (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        followup (Union[Unset, bool]):
        last_updated (Union[Unset, str]):
        org_unit (Union[Unset, str]):
        period (Union[Unset, str]):
        stored_by (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    attribute_option_combo: Union[Unset, str] = UNSET
    category_option_combo: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    data_element: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    followup: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, str] = UNSET
    org_unit: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    stored_by: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_option_combo = self.attribute_option_combo

        category_option_combo = self.category_option_combo

        comment = self.comment

        created = self.created

        data_element = self.data_element

        deleted = self.deleted

        followup = self.followup

        last_updated = self.last_updated

        org_unit = self.org_unit

        period = self.period

        stored_by = self.stored_by

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if category_option_combo is not UNSET:
            field_dict["categoryOptionCombo"] = category_option_combo
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if followup is not UNSET:
            field_dict["followup"] = followup
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if period is not UNSET:
            field_dict["period"] = period
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_option_combo = d.pop("attributeOptionCombo", UNSET)

        category_option_combo = d.pop("categoryOptionCombo", UNSET)

        comment = d.pop("comment", UNSET)

        created = d.pop("created", UNSET)

        data_element = d.pop("dataElement", UNSET)

        deleted = d.pop("deleted", UNSET)

        followup = d.pop("followup", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        period = d.pop("period", UNSET)

        stored_by = d.pop("storedBy", UNSET)

        value = d.pop("value", UNSET)

        data_value = cls(
            attribute_option_combo=attribute_option_combo,
            category_option_combo=category_option_combo,
            comment=comment,
            created=created,
            data_element=data_element,
            deleted=deleted,
            followup=followup,
            last_updated=last_updated,
            org_unit=org_unit,
            period=period,
            stored_by=stored_by,
            value=value,
        )

        data_value.additional_properties = d
        return data_value

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
