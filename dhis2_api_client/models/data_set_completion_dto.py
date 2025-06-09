from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_value_category_dto import DataValueCategoryDto


T = TypeVar("T", bound="DataSetCompletionDto")


@_attrs_define
class DataSetCompletionDto:
    """
    Attributes:
        attribute (Union[Unset, DataValueCategoryDto]):
        completed (Union[Unset, bool]):
        data_set (Union[Unset, str]):
        org_unit (Union[Unset, str]):
        period (Union[Unset, str]):
    """

    attribute: Union[Unset, "DataValueCategoryDto"] = UNSET
    completed: Union[Unset, bool] = UNSET
    data_set: Union[Unset, str] = UNSET
    org_unit: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

        completed = self.completed

        data_set = self.data_set

        org_unit = self.org_unit

        period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if completed is not UNSET:
            field_dict["completed"] = completed
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_value_category_dto import DataValueCategoryDto

        d = src_dict.copy()
        _attribute = d.pop("attribute", UNSET)
        attribute: Union[Unset, DataValueCategoryDto]
        if isinstance(_attribute, Unset):
            attribute = UNSET
        else:
            attribute = DataValueCategoryDto.from_dict(_attribute)

        completed = d.pop("completed", UNSET)

        data_set = d.pop("dataSet", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        period = d.pop("period", UNSET)

        data_set_completion_dto = cls(
            attribute=attribute,
            completed=completed,
            data_set=data_set,
            org_unit=org_unit,
            period=period,
        )

        data_set_completion_dto.additional_properties = d
        return data_set_completion_dto

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
