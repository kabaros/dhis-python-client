from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.styled_object import StyledObject


T = TypeVar("T", bound="SeriesKey")


@_attrs_define
class SeriesKey:
    """
    Attributes:
        hidden (Union[Unset, bool]):
        label (Union[Unset, StyledObject]):
    """

    hidden: Union[Unset, bool] = UNSET
    label: Union[Unset, "StyledObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hidden = self.hidden

        label: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.styled_object import StyledObject

        d = src_dict.copy()
        hidden = d.pop("hidden", UNSET)

        _label = d.pop("label", UNSET)
        label: Union[Unset, StyledObject]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = StyledObject.from_dict(_label)

        series_key = cls(
            hidden=hidden,
            label=label,
        )

        series_key.additional_properties = d
        return series_key

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
