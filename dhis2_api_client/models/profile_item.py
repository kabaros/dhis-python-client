from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_item_value import ProfileItemValue


T = TypeVar("T", bound="ProfileItem")


@_attrs_define
class ProfileItem:
    """
    Attributes:
        id (Union[Unset, str]):
        label (Union[Unset, str]):
        value (Union[Unset, ProfileItemValue]): The actual type is unknown.
            (Java type was: `class java.lang.Object`)
    """

    id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    value: Union[Unset, "ProfileItemValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.profile_item_value import ProfileItemValue

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, ProfileItemValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ProfileItemValue.from_dict(_value)

        profile_item = cls(
            id=id,
            label=label,
            value=value,
        )

        profile_item.additional_properties = d
        return profile_item

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
