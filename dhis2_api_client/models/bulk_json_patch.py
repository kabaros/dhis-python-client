from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_json_patch_target_ids import BulkJsonPatchTargetIds
    from ..models.json_patch import JsonPatch


T = TypeVar("T", bound="BulkJsonPatch")


@_attrs_define
class BulkJsonPatch:
    """
    Attributes:
        patch (Union[Unset, JsonPatch]):
        target_ids (Union[Unset, BulkJsonPatchTargetIds]):
    """

    patch: Union[Unset, "JsonPatch"] = UNSET
    target_ids: Union[Unset, "BulkJsonPatchTargetIds"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        patch: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.patch, Unset):
            patch = self.patch.to_dict()

        target_ids: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target_ids, Unset):
            target_ids = self.target_ids.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if patch is not UNSET:
            field_dict["patch"] = patch
        if target_ids is not UNSET:
            field_dict["targetIds"] = target_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.bulk_json_patch_target_ids import BulkJsonPatchTargetIds
        from ..models.json_patch import JsonPatch

        d = src_dict.copy()
        _patch = d.pop("patch", UNSET)
        patch: Union[Unset, JsonPatch]
        if isinstance(_patch, Unset):
            patch = UNSET
        else:
            patch = JsonPatch.from_dict(_patch)

        _target_ids = d.pop("targetIds", UNSET)
        target_ids: Union[Unset, BulkJsonPatchTargetIds]
        if isinstance(_target_ids, Unset):
            target_ids = UNSET
        else:
            target_ids = BulkJsonPatchTargetIds.from_dict(_target_ids)

        bulk_json_patch = cls(
            patch=patch,
            target_ids=target_ids,
        )

        bulk_json_patch.additional_properties = d
        return bulk_json_patch

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
