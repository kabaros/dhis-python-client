from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrackerStats")


@_attrs_define
class TrackerStats:
    """
    Attributes:
        created (int):
        deleted (int):
        ignored (int):
        total (int):
        updated (int):
    """

    created: int
    deleted: int
    ignored: int
    total: int
    updated: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        deleted = self.deleted

        ignored = self.ignored

        total = self.total

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "deleted": deleted,
                "ignored": ignored,
                "total": total,
                "updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created = d.pop("created")

        deleted = d.pop("deleted")

        ignored = d.pop("ignored")

        total = d.pop("total")

        updated = d.pop("updated")

        tracker_stats = cls(
            created=created,
            deleted=deleted,
            ignored=ignored,
            total=total,
            updated=updated,
        )

        tracker_stats.additional_properties = d
        return tracker_stats

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
