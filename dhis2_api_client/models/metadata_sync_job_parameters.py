from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetadataSyncJobParameters")


@_attrs_define
class MetadataSyncJobParameters:
    """
    Attributes:
        data_values_page_size (int):
        event_program_page_size (int):
        tracker_program_page_size (int):
    """

    data_values_page_size: int
    event_program_page_size: int
    tracker_program_page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_values_page_size = self.data_values_page_size

        event_program_page_size = self.event_program_page_size

        tracker_program_page_size = self.tracker_program_page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataValuesPageSize": data_values_page_size,
                "eventProgramPageSize": event_program_page_size,
                "trackerProgramPageSize": tracker_program_page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        data_values_page_size = d.pop("dataValuesPageSize")

        event_program_page_size = d.pop("eventProgramPageSize")

        tracker_program_page_size = d.pop("trackerProgramPageSize")

        metadata_sync_job_parameters = cls(
            data_values_page_size=data_values_page_size,
            event_program_page_size=event_program_page_size,
            tracker_program_page_size=tracker_program_page_size,
        )

        metadata_sync_job_parameters.additional_properties = d
        return metadata_sync_job_parameters

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
