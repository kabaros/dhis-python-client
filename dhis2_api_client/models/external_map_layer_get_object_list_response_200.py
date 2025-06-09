from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_map_layer import ExternalMapLayer
    from ..models.pager import Pager


T = TypeVar("T", bound="ExternalMapLayerGetObjectListResponse200")


@_attrs_define
class ExternalMapLayerGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        external_map_layers (Union[Unset, list['ExternalMapLayer']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    external_map_layers: Union[Unset, list["ExternalMapLayer"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        external_map_layers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_map_layers, Unset):
            external_map_layers = []
            for external_map_layers_item_data in self.external_map_layers:
                external_map_layers_item = external_map_layers_item_data.to_dict()
                external_map_layers.append(external_map_layers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if external_map_layers is not UNSET:
            field_dict["externalMapLayers"] = external_map_layers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.external_map_layer import ExternalMapLayer
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        external_map_layers = []
        _external_map_layers = d.pop("externalMapLayers", UNSET)
        for external_map_layers_item_data in _external_map_layers or []:
            external_map_layers_item = ExternalMapLayer.from_dict(external_map_layers_item_data)

            external_map_layers.append(external_map_layers_item)

        external_map_layer_get_object_list_response_200 = cls(
            pager=pager,
            external_map_layers=external_map_layers,
        )

        external_map_layer_get_object_list_response_200.additional_properties = d
        return external_map_layer_get_object_list_response_200

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
