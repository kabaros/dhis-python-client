from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_hook import EventHook
    from ..models.pager import Pager


T = TypeVar("T", bound="EventHookGetObjectListResponse200")


@_attrs_define
class EventHookGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        event_hooks (Union[Unset, list['EventHook']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    event_hooks: Union[Unset, list["EventHook"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        event_hooks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.event_hooks, Unset):
            event_hooks = []
            for event_hooks_item_data in self.event_hooks:
                event_hooks_item = event_hooks_item_data.to_dict()
                event_hooks.append(event_hooks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if event_hooks is not UNSET:
            field_dict["eventHooks"] = event_hooks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.event_hook import EventHook
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        event_hooks = []
        _event_hooks = d.pop("eventHooks", UNSET)
        for event_hooks_item_data in _event_hooks or []:
            event_hooks_item = EventHook.from_dict(event_hooks_item_data)

            event_hooks.append(event_hooks_item)

        event_hook_get_object_list_response_200 = cls(
            pager=pager,
            event_hooks=event_hooks,
        )

        event_hook_get_object_list_response_200.additional_properties = d
        return event_hook_get_object_list_response_200

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
