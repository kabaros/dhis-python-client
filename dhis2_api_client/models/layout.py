from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column import Column
    from ..models.spacing import Spacing


T = TypeVar("T", bound="Layout")


@_attrs_define
class Layout:
    """
    Attributes:
        columns (Union[Unset, list['Column']]):
        spacing (Union[Unset, Spacing]):
    """

    columns: Union[Unset, list["Column"]] = UNSET
    spacing: Union[Unset, "Spacing"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        spacing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spacing, Unset):
            spacing = self.spacing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if spacing is not UNSET:
            field_dict["spacing"] = spacing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.column import Column
        from ..models.spacing import Spacing

        d = src_dict.copy()
        columns = []
        _columns = d.pop("columns", UNSET)
        for columns_item_data in _columns or []:
            columns_item = Column.from_dict(columns_item_data)

            columns.append(columns_item)

        _spacing = d.pop("spacing", UNSET)
        spacing: Union[Unset, Spacing]
        if isinstance(_spacing, Unset):
            spacing = UNSET
        else:
            spacing = Spacing.from_dict(_spacing)

        layout = cls(
            columns=columns,
            spacing=spacing,
        )

        layout.additional_properties = d
        return layout

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
