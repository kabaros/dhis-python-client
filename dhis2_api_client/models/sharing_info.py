from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta import Meta
    from ..models.sharing_object import SharingObject


T = TypeVar("T", bound="SharingInfo")


@_attrs_define
class SharingInfo:
    """
    Attributes:
        meta (Union[Unset, Meta]):
        object_ (Union[Unset, SharingObject]):
    """

    meta: Union[Unset, "Meta"] = UNSET
    object_: Union[Unset, "SharingObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        object_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.meta import Meta
        from ..models.sharing_object import SharingObject

        d = src_dict.copy()
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = Meta.from_dict(_meta)

        _object_ = d.pop("object", UNSET)
        object_: Union[Unset, SharingObject]
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = SharingObject.from_dict(_object_)

        sharing_info = cls(
            meta=meta,
            object_=object_,
        )

        sharing_info.additional_properties = d
        return sharing_info

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
