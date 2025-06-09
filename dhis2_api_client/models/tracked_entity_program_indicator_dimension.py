from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracked_entity_program_indicator_dimension_legend_set import (
        TrackedEntityProgramIndicatorDimensionLegendSet,
    )
    from ..models.tracked_entity_program_indicator_dimension_program_indicator import (
        TrackedEntityProgramIndicatorDimensionProgramIndicator,
    )


T = TypeVar("T", bound="TrackedEntityProgramIndicatorDimension")


@_attrs_define
class TrackedEntityProgramIndicatorDimension:
    """
    Attributes:
        filter_ (Union[Unset, str]):
        legend_set (Union[Unset, TrackedEntityProgramIndicatorDimensionLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        program_indicator (Union[Unset, TrackedEntityProgramIndicatorDimensionProgramIndicator]): A UID reference to a
            ProgramIndicator
            (Java name `org.hisp.dhis.program.ProgramIndicator`)
    """

    filter_: Union[Unset, str] = UNSET
    legend_set: Union[Unset, "TrackedEntityProgramIndicatorDimensionLegendSet"] = UNSET
    program_indicator: Union[Unset, "TrackedEntityProgramIndicatorDimensionProgramIndicator"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        program_indicator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_indicator, Unset):
            program_indicator = self.program_indicator.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if program_indicator is not UNSET:
            field_dict["programIndicator"] = program_indicator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracked_entity_program_indicator_dimension_legend_set import (
            TrackedEntityProgramIndicatorDimensionLegendSet,
        )
        from ..models.tracked_entity_program_indicator_dimension_program_indicator import (
            TrackedEntityProgramIndicatorDimensionProgramIndicator,
        )

        d = src_dict.copy()
        filter_ = d.pop("filter", UNSET)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, TrackedEntityProgramIndicatorDimensionLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = TrackedEntityProgramIndicatorDimensionLegendSet.from_dict(_legend_set)

        _program_indicator = d.pop("programIndicator", UNSET)
        program_indicator: Union[Unset, TrackedEntityProgramIndicatorDimensionProgramIndicator]
        if isinstance(_program_indicator, Unset):
            program_indicator = UNSET
        else:
            program_indicator = TrackedEntityProgramIndicatorDimensionProgramIndicator.from_dict(_program_indicator)

        tracked_entity_program_indicator_dimension = cls(
            filter_=filter_,
            legend_set=legend_set,
            program_indicator=program_indicator,
        )

        tracked_entity_program_indicator_dimension.additional_properties = d
        return tracked_entity_program_indicator_dimension

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
