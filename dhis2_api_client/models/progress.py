from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process import Process
    from ..models.progress_errors import ProgressErrors


T = TypeVar("T", bound="Progress")


@_attrs_define
class Progress:
    """
    Attributes:
        errors (Union[Unset, ProgressErrors]):
        sequence (Union[Unset, list['Process']]):
    """

    errors: Union[Unset, "ProgressErrors"] = UNSET
    sequence: Union[Unset, list["Process"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        sequence: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sequence, Unset):
            sequence = []
            for sequence_item_data in self.sequence:
                sequence_item = sequence_item_data.to_dict()
                sequence.append(sequence_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.process import Process
        from ..models.progress_errors import ProgressErrors

        d = src_dict.copy()
        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, ProgressErrors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ProgressErrors.from_dict(_errors)

        sequence = []
        _sequence = d.pop("sequence", UNSET)
        for sequence_item_data in _sequence or []:
            sequence_item = Process.from_dict(sequence_item_data)

            sequence.append(sequence_item)

        progress = cls(
            errors=errors,
            sequence=sequence,
        )

        progress.additional_properties = d
        return progress

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
