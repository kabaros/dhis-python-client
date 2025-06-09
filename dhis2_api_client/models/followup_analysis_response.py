from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.followup_analysis_metadata import FollowupAnalysisMetadata
    from ..models.followup_value import FollowupValue


T = TypeVar("T", bound="FollowupAnalysisResponse")


@_attrs_define
class FollowupAnalysisResponse:
    """
    Attributes:
        followup_values (Union[Unset, list['FollowupValue']]):
        metadata (Union[Unset, FollowupAnalysisMetadata]):
    """

    followup_values: Union[Unset, list["FollowupValue"]] = UNSET
    metadata: Union[Unset, "FollowupAnalysisMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        followup_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.followup_values, Unset):
            followup_values = []
            for followup_values_item_data in self.followup_values:
                followup_values_item = followup_values_item_data.to_dict()
                followup_values.append(followup_values_item)

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if followup_values is not UNSET:
            field_dict["followupValues"] = followup_values
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.followup_analysis_metadata import FollowupAnalysisMetadata
        from ..models.followup_value import FollowupValue

        d = src_dict.copy()
        followup_values = []
        _followup_values = d.pop("followupValues", UNSET)
        for followup_values_item_data in _followup_values or []:
            followup_values_item = FollowupValue.from_dict(followup_values_item_data)

            followup_values.append(followup_values_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, FollowupAnalysisMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = FollowupAnalysisMetadata.from_dict(_metadata)

        followup_analysis_response = cls(
            followup_values=followup_values,
            metadata=metadata,
        )

        followup_analysis_response.additional_properties = d
        return followup_analysis_response

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
