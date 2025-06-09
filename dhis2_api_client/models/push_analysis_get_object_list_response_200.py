from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager import Pager
    from ..models.push_analysis import PushAnalysis


T = TypeVar("T", bound="PushAnalysisGetObjectListResponse200")


@_attrs_define
class PushAnalysisGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        push_analysis (Union[Unset, list['PushAnalysis']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    push_analysis: Union[Unset, list["PushAnalysis"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        push_analysis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.push_analysis, Unset):
            push_analysis = []
            for push_analysis_item_data in self.push_analysis:
                push_analysis_item = push_analysis_item_data.to_dict()
                push_analysis.append(push_analysis_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if push_analysis is not UNSET:
            field_dict["pushAnalysis"] = push_analysis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pager import Pager
        from ..models.push_analysis import PushAnalysis

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        push_analysis = []
        _push_analysis = d.pop("pushAnalysis", UNSET)
        for push_analysis_item_data in _push_analysis or []:
            push_analysis_item = PushAnalysis.from_dict(push_analysis_item_data)

            push_analysis.append(push_analysis_item)

        push_analysis_get_object_list_response_200 = cls(
            pager=pager,
            push_analysis=push_analysis,
        )

        push_analysis_get_object_list_response_200.additional_properties = d
        return push_analysis_get_object_list_response_200

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
