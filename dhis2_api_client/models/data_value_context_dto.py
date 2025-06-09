from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_value_audit_dto import DataValueAuditDto
    from ..models.data_value_dto import DataValueDto


T = TypeVar("T", bound="DataValueContextDto")


@_attrs_define
class DataValueContextDto:
    """
    Attributes:
        audits (Union[Unset, list['DataValueAuditDto']]):
        history (Union[Unset, list['DataValueDto']]):
    """

    audits: Union[Unset, list["DataValueAuditDto"]] = UNSET
    history: Union[Unset, list["DataValueDto"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audits: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.audits, Unset):
            audits = []
            for audits_item_data in self.audits:
                audits_item = audits_item_data.to_dict()
                audits.append(audits_item)

        history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audits is not UNSET:
            field_dict["audits"] = audits
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_value_audit_dto import DataValueAuditDto
        from ..models.data_value_dto import DataValueDto

        d = src_dict.copy()
        audits = []
        _audits = d.pop("audits", UNSET)
        for audits_item_data in _audits or []:
            audits_item = DataValueAuditDto.from_dict(audits_item_data)

            audits.append(audits_item)

        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = DataValueDto.from_dict(history_item_data)

            history.append(history_item)

        data_value_context_dto = cls(
            audits=audits,
            history=history,
        )

        data_value_context_dto.additional_properties = d
        return data_value_context_dto

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
