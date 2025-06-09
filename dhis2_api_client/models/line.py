from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.styled_object import StyledObject


T = TypeVar("T", bound="Line")


@_attrs_define
class Line:
    """
    Attributes:
        title (Union[Unset, StyledObject]):
        value (Union[Unset, float]):
    """

    title: Union[Unset, "StyledObject"] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.styled_object import StyledObject

        d = src_dict.copy()
        _title = d.pop("title", UNSET)
        title: Union[Unset, StyledObject]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = StyledObject.from_dict(_title)

        value = d.pop("value", UNSET)

        line = cls(
            title=title,
            value=value,
        )

        line.additional_properties = d
        return line

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
