from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field
    from ..models.group_meta_data import GroupMetaData


T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """
    Attributes:
        data_element_count (int):
        description (Union[Unset, str]):
        fields (Union[Unset, list['Field']]):
        label (Union[Unset, str]):
        meta_data (Union[Unset, GroupMetaData]): keys are class java.lang.Object
    """

    data_element_count: int
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, list["Field"]] = UNSET
    label: Union[Unset, str] = UNSET
    meta_data: Union[Unset, "GroupMetaData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_element_count = self.data_element_count

        description = self.description

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        label = self.label

        meta_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataElementCount": data_element_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if label is not UNSET:
            field_dict["label"] = label
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.field import Field
        from ..models.group_meta_data import GroupMetaData

        d = src_dict.copy()
        data_element_count = d.pop("dataElementCount")

        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = Field.from_dict(fields_item_data)

            fields.append(fields_item)

        label = d.pop("label", UNSET)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: Union[Unset, GroupMetaData]
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = GroupMetaData.from_dict(_meta_data)

        group = cls(
            data_element_count=data_element_count,
            description=description,
            fields=fields,
            label=label,
            meta_data=meta_data,
        )

        group.additional_properties = d
        return group

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
