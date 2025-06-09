from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportConflicts")


@_attrs_define
class ImportConflicts:
    """
    Attributes:
        conflict_count (int):
        total_conflict_occurrence_count (int):
        conflicts (Union[Unset, bool]):
        conflicts_description (Union[Unset, str]):
    """

    conflict_count: int
    total_conflict_occurrence_count: int
    conflicts: Union[Unset, bool] = UNSET
    conflicts_description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflict_count = self.conflict_count

        total_conflict_occurrence_count = self.total_conflict_occurrence_count

        conflicts = self.conflicts

        conflicts_description = self.conflicts_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conflictCount": conflict_count,
                "totalConflictOccurrenceCount": total_conflict_occurrence_count,
            }
        )
        if conflicts is not UNSET:
            field_dict["conflicts"] = conflicts
        if conflicts_description is not UNSET:
            field_dict["conflictsDescription"] = conflicts_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        conflict_count = d.pop("conflictCount")

        total_conflict_occurrence_count = d.pop("totalConflictOccurrenceCount")

        conflicts = d.pop("conflicts", UNSET)

        conflicts_description = d.pop("conflictsDescription", UNSET)

        import_conflicts = cls(
            conflict_count=conflict_count,
            total_conflict_occurrence_count=total_conflict_occurrence_count,
            conflicts=conflicts,
            conflicts_description=conflicts_description,
        )

        import_conflicts.additional_properties = d
        return import_conflicts

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
