from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_path_transformer import FieldPathTransformer
    from ..models.property_ import Property


T = TypeVar("T", bound="FieldPath")


@_attrs_define
class FieldPath:
    """
    Attributes:
        exclude (Union[Unset, bool]):
        full_path (Union[Unset, str]):
        name (Union[Unset, str]):
        path (Union[Unset, list[str]]):
        preset (Union[Unset, bool]):
        property_ (Union[Unset, Property]):
        root (Union[Unset, bool]):
        transformer (Union[Unset, bool]):
        transformers (Union[Unset, list['FieldPathTransformer']]):
    """

    exclude: Union[Unset, bool] = UNSET
    full_path: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    path: Union[Unset, list[str]] = UNSET
    preset: Union[Unset, bool] = UNSET
    property_: Union[Unset, "Property"] = UNSET
    root: Union[Unset, bool] = UNSET
    transformer: Union[Unset, bool] = UNSET
    transformers: Union[Unset, list["FieldPathTransformer"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude = self.exclude

        full_path = self.full_path

        name = self.name

        path: Union[Unset, list[str]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        preset = self.preset

        property_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.to_dict()

        root = self.root

        transformer = self.transformer

        transformers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transformers, Unset):
            transformers = []
            for transformers_item_data in self.transformers:
                transformers_item = transformers_item_data.to_dict()
                transformers.append(transformers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if full_path is not UNSET:
            field_dict["fullPath"] = full_path
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if preset is not UNSET:
            field_dict["preset"] = preset
        if property_ is not UNSET:
            field_dict["property"] = property_
        if root is not UNSET:
            field_dict["root"] = root
        if transformer is not UNSET:
            field_dict["transformer"] = transformer
        if transformers is not UNSET:
            field_dict["transformers"] = transformers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.field_path_transformer import FieldPathTransformer
        from ..models.property_ import Property

        d = src_dict.copy()
        exclude = d.pop("exclude", UNSET)

        full_path = d.pop("fullPath", UNSET)

        name = d.pop("name", UNSET)

        path = cast(list[str], d.pop("path", UNSET))

        preset = d.pop("preset", UNSET)

        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, Property]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = Property.from_dict(_property_)

        root = d.pop("root", UNSET)

        transformer = d.pop("transformer", UNSET)

        transformers = []
        _transformers = d.pop("transformers", UNSET)
        for transformers_item_data in _transformers or []:
            transformers_item = FieldPathTransformer.from_dict(transformers_item_data)

            transformers.append(transformers_item)

        field_path = cls(
            exclude=exclude,
            full_path=full_path,
            name=name,
            path=path,
            preset=preset,
            property_=property_,
            root=root,
            transformer=transformer,
            transformers=transformers,
        )

        field_path.additional_properties = d
        return field_path

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
