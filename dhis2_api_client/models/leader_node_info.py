from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderNodeInfo")


@_attrs_define
class LeaderNodeInfo:
    """
    Attributes:
        current_node_id (Union[Unset, str]):
        current_node_uuid (Union[Unset, str]):
        leader (Union[Unset, bool]):
        leader_node_id (Union[Unset, str]):
        leader_node_uuid (Union[Unset, str]):
    """

    current_node_id: Union[Unset, str] = UNSET
    current_node_uuid: Union[Unset, str] = UNSET
    leader: Union[Unset, bool] = UNSET
    leader_node_id: Union[Unset, str] = UNSET
    leader_node_uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_node_id = self.current_node_id

        current_node_uuid = self.current_node_uuid

        leader = self.leader

        leader_node_id = self.leader_node_id

        leader_node_uuid = self.leader_node_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_node_id is not UNSET:
            field_dict["currentNodeId"] = current_node_id
        if current_node_uuid is not UNSET:
            field_dict["currentNodeUuid"] = current_node_uuid
        if leader is not UNSET:
            field_dict["leader"] = leader
        if leader_node_id is not UNSET:
            field_dict["leaderNodeId"] = leader_node_id
        if leader_node_uuid is not UNSET:
            field_dict["leaderNodeUuid"] = leader_node_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        current_node_id = d.pop("currentNodeId", UNSET)

        current_node_uuid = d.pop("currentNodeUuid", UNSET)

        leader = d.pop("leader", UNSET)

        leader_node_id = d.pop("leaderNodeId", UNSET)

        leader_node_uuid = d.pop("leaderNodeUuid", UNSET)

        leader_node_info = cls(
            current_node_id=current_node_id,
            current_node_uuid=current_node_uuid,
            leader=leader,
            leader_node_id=leader_node_id,
            leader_node_uuid=leader_node_uuid,
        )

        leader_node_info.additional_properties = d
        return leader_node_info

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
