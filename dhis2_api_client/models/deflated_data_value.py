from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeflatedDataValue")


@_attrs_define
class DeflatedDataValue:
    """
    Attributes:
        attribute_option_combo_id (int):
        category_option_combo_id (int):
        data_element_id (int):
        max_ (int):
        min_ (int):
        period_id (int):
        source_id (int):
        category_option_combo_name (Union[Unset, str]):
        comment (Union[Unset, str]):
        data_element_name (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        followup (Union[Unset, bool]):
        period (Union[Unset, str]):
        source_name (Union[Unset, str]):
        source_path (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    attribute_option_combo_id: int
    category_option_combo_id: int
    data_element_id: int
    max_: int
    min_: int
    period_id: int
    source_id: int
    category_option_combo_name: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    data_element_name: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    followup: Union[Unset, bool] = UNSET
    period: Union[Unset, str] = UNSET
    source_name: Union[Unset, str] = UNSET
    source_path: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_option_combo_id = self.attribute_option_combo_id

        category_option_combo_id = self.category_option_combo_id

        data_element_id = self.data_element_id

        max_ = self.max_

        min_ = self.min_

        period_id = self.period_id

        source_id = self.source_id

        category_option_combo_name = self.category_option_combo_name

        comment = self.comment

        data_element_name = self.data_element_name

        deleted = self.deleted

        followup = self.followup

        period = self.period

        source_name = self.source_name

        source_path = self.source_path

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributeOptionComboId": attribute_option_combo_id,
                "categoryOptionComboId": category_option_combo_id,
                "dataElementId": data_element_id,
                "max": max_,
                "min": min_,
                "periodId": period_id,
                "sourceId": source_id,
            }
        )
        if category_option_combo_name is not UNSET:
            field_dict["categoryOptionComboName"] = category_option_combo_name
        if comment is not UNSET:
            field_dict["comment"] = comment
        if data_element_name is not UNSET:
            field_dict["dataElementName"] = data_element_name
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if followup is not UNSET:
            field_dict["followup"] = followup
        if period is not UNSET:
            field_dict["period"] = period
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if source_path is not UNSET:
            field_dict["sourcePath"] = source_path
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_option_combo_id = d.pop("attributeOptionComboId")

        category_option_combo_id = d.pop("categoryOptionComboId")

        data_element_id = d.pop("dataElementId")

        max_ = d.pop("max")

        min_ = d.pop("min")

        period_id = d.pop("periodId")

        source_id = d.pop("sourceId")

        category_option_combo_name = d.pop("categoryOptionComboName", UNSET)

        comment = d.pop("comment", UNSET)

        data_element_name = d.pop("dataElementName", UNSET)

        deleted = d.pop("deleted", UNSET)

        followup = d.pop("followup", UNSET)

        period = d.pop("period", UNSET)

        source_name = d.pop("sourceName", UNSET)

        source_path = d.pop("sourcePath", UNSET)

        value = d.pop("value", UNSET)

        deflated_data_value = cls(
            attribute_option_combo_id=attribute_option_combo_id,
            category_option_combo_id=category_option_combo_id,
            data_element_id=data_element_id,
            max_=max_,
            min_=min_,
            period_id=period_id,
            source_id=source_id,
            category_option_combo_name=category_option_combo_name,
            comment=comment,
            data_element_name=data_element_name,
            deleted=deleted,
            followup=followup,
            period=period,
            source_name=source_name,
            source_path=source_path,
            value=value,
        )

        deflated_data_value.additional_properties = d
        return deflated_data_value

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
