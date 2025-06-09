from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_propose_params_change import MetadataProposeParamsChange


T = TypeVar("T", bound="MetadataProposeParams")


@_attrs_define
class MetadataProposeParams:
    """
    Attributes:
        change (Union[Unset, MetadataProposeParamsChange]):
        comment (Union[Unset, str]):
        target_id (Union[Unset, str]):
    """

    change: Union[Unset, "MetadataProposeParamsChange"] = UNSET
    comment: Union[Unset, str] = UNSET
    target_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.change, Unset):
            change = self.change.to_dict()

        comment = self.comment

        target_id = self.target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change is not UNSET:
            field_dict["change"] = change
        if comment is not UNSET:
            field_dict["comment"] = comment
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.metadata_propose_params_change import MetadataProposeParamsChange

        d = src_dict.copy()
        _change = d.pop("change", UNSET)
        change: Union[Unset, MetadataProposeParamsChange]
        if isinstance(_change, Unset):
            change = UNSET
        else:
            change = MetadataProposeParamsChange.from_dict(_change)

        comment = d.pop("comment", UNSET)

        target_id = d.pop("targetId", UNSET)

        metadata_propose_params = cls(
            change=change,
            comment=comment,
            target_id=target_id,
        )

        metadata_propose_params.additional_properties = d
        return metadata_propose_params

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
