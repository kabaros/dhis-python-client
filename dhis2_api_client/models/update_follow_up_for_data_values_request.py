from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.followup_params import FollowupParams


T = TypeVar("T", bound="UpdateFollowUpForDataValuesRequest")


@_attrs_define
class UpdateFollowUpForDataValuesRequest:
    """
    Attributes:
        followups (Union[Unset, list['FollowupParams']]):
    """

    followups: Union[Unset, list["FollowupParams"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.followups, Unset):
            followups = []
            for followups_item_data in self.followups:
                followups_item = followups_item_data.to_dict()
                followups.append(followups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if followups is not UNSET:
            field_dict["followups"] = followups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.followup_params import FollowupParams

        d = src_dict.copy()
        followups = []
        _followups = d.pop("followups", UNSET)
        for followups_item_data in _followups or []:
            followups_item = FollowupParams.from_dict(followups_item_data)

            followups.append(followups_item)

        update_follow_up_for_data_values_request = cls(
            followups=followups,
        )

        update_follow_up_for_data_values_request.additional_properties = d
        return update_follow_up_for_data_values_request

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
