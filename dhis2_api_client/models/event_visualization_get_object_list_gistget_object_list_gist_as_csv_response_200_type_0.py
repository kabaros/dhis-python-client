from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_visualization_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_event_visualizations_item import (
        EventVisualizationGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventVisualizationsItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="EventVisualizationGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class EventVisualizationGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        event_visualizations (Union[Unset,
            list['EventVisualizationGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventVisualizationsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    event_visualizations: Union[
        Unset, list["EventVisualizationGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventVisualizationsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        event_visualizations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_visualizations, Unset):
            event_visualizations = []
            for event_visualizations_item_data in self.event_visualizations:
                event_visualizations_item = event_visualizations_item_data.to_dict()
                event_visualizations.append(event_visualizations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if event_visualizations is not UNSET:
            field_dict["eventVisualizations"] = event_visualizations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.event_visualization_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_event_visualizations_item import (
            EventVisualizationGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventVisualizationsItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        event_visualizations = []
        _event_visualizations = d.pop("eventVisualizations", UNSET)
        for event_visualizations_item_data in _event_visualizations or []:
            event_visualizations_item = EventVisualizationGetObjectListGistgetObjectListGistAsCsvResponse200Type0EventVisualizationsItem.from_dict(
                event_visualizations_item_data
            )

            event_visualizations.append(event_visualizations_item)

        event_visualization_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            event_visualizations=event_visualizations,
        )

        event_visualization_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return event_visualization_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
