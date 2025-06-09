from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_image_resource_images import SimpleImageResourceImages


T = TypeVar("T", bound="SimpleImageResource")


@_attrs_define
class SimpleImageResource:
    """
    Attributes:
        images (Union[Unset, SimpleImageResourceImages]):
    """

    images: Union[Unset, "SimpleImageResourceImages"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        images: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.simple_image_resource_images import SimpleImageResourceImages

        d = src_dict.copy()
        _images = d.pop("images", UNSET)
        images: Union[Unset, SimpleImageResourceImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = SimpleImageResourceImages.from_dict(_images)

        simple_image_resource = cls(
            images=images,
        )

        simple_image_resource.additional_properties = d
        return simple_image_resource

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
