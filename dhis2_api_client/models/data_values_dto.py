from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_values_dto_lock_status import DataValuesDtoLockStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.complete_status_dto import CompleteStatusDto
    from ..models.data_value_dto import DataValueDto
    from ..models.min_max_value_dto import MinMaxValueDto


T = TypeVar("T", bound="DataValuesDto")


@_attrs_define
class DataValuesDto:
    """
    Attributes:
        lock_status (DataValuesDtoLockStatus):
        complete_status (Union[Unset, CompleteStatusDto]):
        data_values (Union[Unset, list['DataValueDto']]):
        min_max_values (Union[Unset, list['MinMaxValueDto']]):
    """

    lock_status: DataValuesDtoLockStatus
    complete_status: Union[Unset, "CompleteStatusDto"] = UNSET
    data_values: Union[Unset, list["DataValueDto"]] = UNSET
    min_max_values: Union[Unset, list["MinMaxValueDto"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lock_status = self.lock_status.value

        complete_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.complete_status, Unset):
            complete_status = self.complete_status.to_dict()

        data_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_values, Unset):
            data_values = []
            for data_values_item_data in self.data_values:
                data_values_item = data_values_item_data.to_dict()
                data_values.append(data_values_item)

        min_max_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.min_max_values, Unset):
            min_max_values = []
            for min_max_values_item_data in self.min_max_values:
                min_max_values_item = min_max_values_item_data.to_dict()
                min_max_values.append(min_max_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lockStatus": lock_status,
            }
        )
        if complete_status is not UNSET:
            field_dict["completeStatus"] = complete_status
        if data_values is not UNSET:
            field_dict["dataValues"] = data_values
        if min_max_values is not UNSET:
            field_dict["minMaxValues"] = min_max_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.complete_status_dto import CompleteStatusDto
        from ..models.data_value_dto import DataValueDto
        from ..models.min_max_value_dto import MinMaxValueDto

        d = src_dict.copy()
        lock_status = DataValuesDtoLockStatus(d.pop("lockStatus"))

        _complete_status = d.pop("completeStatus", UNSET)
        complete_status: Union[Unset, CompleteStatusDto]
        if isinstance(_complete_status, Unset):
            complete_status = UNSET
        else:
            complete_status = CompleteStatusDto.from_dict(_complete_status)

        data_values = []
        _data_values = d.pop("dataValues", UNSET)
        for data_values_item_data in _data_values or []:
            data_values_item = DataValueDto.from_dict(data_values_item_data)

            data_values.append(data_values_item)

        min_max_values = []
        _min_max_values = d.pop("minMaxValues", UNSET)
        for min_max_values_item_data in _min_max_values or []:
            min_max_values_item = MinMaxValueDto.from_dict(min_max_values_item_data)

            min_max_values.append(min_max_values_item)

        data_values_dto = cls(
            lock_status=lock_status,
            complete_status=complete_status,
            data_values=data_values,
            min_max_values=min_max_values,
        )

        data_values_dto.additional_properties = d
        return data_values_dto

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
