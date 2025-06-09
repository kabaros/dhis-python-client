from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.persistence_report_type_report_map import PersistenceReportTypeReportMap


T = TypeVar("T", bound="PersistenceReport")


@_attrs_define
class PersistenceReport:
    """
    Attributes:
        type_report_map (Union[Unset, PersistenceReportTypeReportMap]): keys are class org.hisp.dhis.tracker.TrackerType
    """

    type_report_map: Union[Unset, "PersistenceReportTypeReportMap"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_report_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_report_map, Unset):
            type_report_map = self.type_report_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_report_map is not UNSET:
            field_dict["typeReportMap"] = type_report_map

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.persistence_report_type_report_map import PersistenceReportTypeReportMap

        d = src_dict.copy()
        _type_report_map = d.pop("typeReportMap", UNSET)
        type_report_map: Union[Unset, PersistenceReportTypeReportMap]
        if isinstance(_type_report_map, Unset):
            type_report_map = UNSET
        else:
            type_report_map = PersistenceReportTypeReportMap.from_dict(_type_report_map)

        persistence_report = cls(
            type_report_map=type_report_map,
        )

        persistence_report.additional_properties = d
        return persistence_report

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
