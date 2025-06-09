from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_integrity_check_severity import DataIntegrityCheckSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataIntegrityCheck")


@_attrs_define
class DataIntegrityCheck:
    """
    Attributes:
        section_order (int):
        severity (DataIntegrityCheckSeverity):
        average_execution_time (Union[Unset, int]):
        code (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        introduction (Union[Unset, str]):
        is_programmatic (Union[Unset, bool]):
        is_slow (Union[Unset, bool]):
        issues_id_type (Union[Unset, str]):
        name (Union[Unset, str]):
        recommendation (Union[Unset, str]):
        section (Union[Unset, str]):
    """

    section_order: int
    severity: DataIntegrityCheckSeverity
    average_execution_time: Union[Unset, int] = UNSET
    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    introduction: Union[Unset, str] = UNSET
    is_programmatic: Union[Unset, bool] = UNSET
    is_slow: Union[Unset, bool] = UNSET
    issues_id_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    recommendation: Union[Unset, str] = UNSET
    section: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        section_order = self.section_order

        severity = self.severity.value

        average_execution_time = self.average_execution_time

        code = self.code

        description = self.description

        display_name = self.display_name

        introduction = self.introduction

        is_programmatic = self.is_programmatic

        is_slow = self.is_slow

        issues_id_type = self.issues_id_type

        name = self.name

        recommendation = self.recommendation

        section = self.section

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sectionOrder": section_order,
                "severity": severity,
            }
        )
        if average_execution_time is not UNSET:
            field_dict["averageExecutionTime"] = average_execution_time
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if introduction is not UNSET:
            field_dict["introduction"] = introduction
        if is_programmatic is not UNSET:
            field_dict["isProgrammatic"] = is_programmatic
        if is_slow is not UNSET:
            field_dict["isSlow"] = is_slow
        if issues_id_type is not UNSET:
            field_dict["issuesIdType"] = issues_id_type
        if name is not UNSET:
            field_dict["name"] = name
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if section is not UNSET:
            field_dict["section"] = section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        section_order = d.pop("sectionOrder")

        severity = DataIntegrityCheckSeverity(d.pop("severity"))

        average_execution_time = d.pop("averageExecutionTime", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        introduction = d.pop("introduction", UNSET)

        is_programmatic = d.pop("isProgrammatic", UNSET)

        is_slow = d.pop("isSlow", UNSET)

        issues_id_type = d.pop("issuesIdType", UNSET)

        name = d.pop("name", UNSET)

        recommendation = d.pop("recommendation", UNSET)

        section = d.pop("section", UNSET)

        data_integrity_check = cls(
            section_order=section_order,
            severity=severity,
            average_execution_time=average_execution_time,
            code=code,
            description=description,
            display_name=display_name,
            introduction=introduction,
            is_programmatic=is_programmatic,
            is_slow=is_slow,
            issues_id_type=issues_id_type,
            name=name,
            recommendation=recommendation,
            section=section,
        )

        data_integrity_check.additional_properties = d
        return data_integrity_check

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
