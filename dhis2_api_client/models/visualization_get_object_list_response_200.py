from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager import Pager
    from ..models.visualization import Visualization


T = TypeVar("T", bound="VisualizationGetObjectListResponse200")


@_attrs_define
class VisualizationGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        visualizations (Union[Unset, list['Visualization']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    visualizations: Union[Unset, list["Visualization"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        visualizations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.visualizations, Unset):
            visualizations = []
            for visualizations_item_data in self.visualizations:
                visualizations_item = visualizations_item_data.to_dict()
                visualizations.append(visualizations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if visualizations is not UNSET:
            field_dict["visualizations"] = visualizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pager import Pager
        from ..models.visualization import Visualization

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        visualizations = []
        _visualizations = d.pop("visualizations", UNSET)
        for visualizations_item_data in _visualizations or []:
            visualizations_item = Visualization.from_dict(visualizations_item_data)

            visualizations.append(visualizations_item)

        visualization_get_object_list_response_200 = cls(
            pager=pager,
            visualizations=visualizations,
        )

        visualization_get_object_list_response_200.additional_properties = d
        return visualization_get_object_list_response_200

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
