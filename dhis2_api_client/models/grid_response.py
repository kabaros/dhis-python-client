from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grid import Grid
    from ..models.pager import Pager


T = TypeVar("T", bound="GridResponse")


@_attrs_define
class GridResponse:
    """
    Attributes:
        list_grid (Union[Unset, Grid]):
        pager (Union[Unset, Pager]):
    """

    list_grid: Union[Unset, "Grid"] = UNSET
    pager: Union[Unset, "Pager"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_grid: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.list_grid, Unset):
            list_grid = self.list_grid.to_dict()

        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if list_grid is not UNSET:
            field_dict["listGrid"] = list_grid
        if pager is not UNSET:
            field_dict["pager"] = pager

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.grid import Grid
        from ..models.pager import Pager

        d = src_dict.copy()
        _list_grid = d.pop("listGrid", UNSET)
        list_grid: Union[Unset, Grid]
        if isinstance(_list_grid, Unset):
            list_grid = UNSET
        else:
            list_grid = Grid.from_dict(_list_grid)

        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        grid_response = cls(
            list_grid=list_grid,
            pager=pager,
        )

        grid_response.additional_properties = d
        return grid_response

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
