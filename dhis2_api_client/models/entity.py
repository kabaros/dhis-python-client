from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_tracker_type import EntityTrackerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracker_import_error import TrackerImportError


T = TypeVar("T", bound="Entity")


@_attrs_define
class Entity:
    """
    Attributes:
        tracker_type (EntityTrackerType):
        error_reports (Union[Unset, list['TrackerImportError']]):
        uid (Union[Unset, str]):
    """

    tracker_type: EntityTrackerType
    error_reports: Union[Unset, list["TrackerImportError"]] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracker_type = self.tracker_type.value

        error_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.error_reports, Unset):
            error_reports = []
            for error_reports_item_data in self.error_reports:
                error_reports_item = error_reports_item_data.to_dict()
                error_reports.append(error_reports_item)

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trackerType": tracker_type,
            }
        )
        if error_reports is not UNSET:
            field_dict["errorReports"] = error_reports
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracker_import_error import TrackerImportError

        d = src_dict.copy()
        tracker_type = EntityTrackerType(d.pop("trackerType"))

        error_reports = []
        _error_reports = d.pop("errorReports", UNSET)
        for error_reports_item_data in _error_reports or []:
            error_reports_item = TrackerImportError.from_dict(error_reports_item_data)

            error_reports.append(error_reports_item)

        uid = d.pop("uid", UNSET)

        entity = cls(
            tracker_type=tracker_type,
            error_reports=error_reports,
            uid=uid,
        )

        entity.additional_properties = d
        return entity

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
