from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interpretation import Interpretation
    from ..models.pager import Pager


T = TypeVar("T", bound="InterpretationGetObjectListResponse200")


@_attrs_define
class InterpretationGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        interpretations (Union[Unset, list['Interpretation']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    interpretations: Union[Unset, list["Interpretation"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        interpretations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interpretations, Unset):
            interpretations = []
            for interpretations_item_data in self.interpretations:
                interpretations_item = interpretations_item_data.to_dict()
                interpretations.append(interpretations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if interpretations is not UNSET:
            field_dict["interpretations"] = interpretations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.interpretation import Interpretation
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        interpretations = []
        _interpretations = d.pop("interpretations", UNSET)
        for interpretations_item_data in _interpretations or []:
            interpretations_item = Interpretation.from_dict(interpretations_item_data)

            interpretations.append(interpretations_item)

        interpretation_get_object_list_response_200 = cls(
            pager=pager,
            interpretations=interpretations,
        )

        interpretation_get_object_list_response_200.additional_properties = d
        return interpretation_get_object_list_response_200

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
