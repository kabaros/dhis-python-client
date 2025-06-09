from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracked_entity_data_element_dimension_data_element import TrackedEntityDataElementDimensionDataElement
    from ..models.tracked_entity_data_element_dimension_legend_set import TrackedEntityDataElementDimensionLegendSet
    from ..models.tracked_entity_data_element_dimension_program_stage import (
        TrackedEntityDataElementDimensionProgramStage,
    )


T = TypeVar("T", bound="TrackedEntityDataElementDimension")


@_attrs_define
class TrackedEntityDataElementDimension:
    """
    Attributes:
        data_element (Union[Unset, TrackedEntityDataElementDimensionDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        filter_ (Union[Unset, str]):
        legend_set (Union[Unset, TrackedEntityDataElementDimensionLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        program_stage (Union[Unset, TrackedEntityDataElementDimensionProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
    """

    data_element: Union[Unset, "TrackedEntityDataElementDimensionDataElement"] = UNSET
    filter_: Union[Unset, str] = UNSET
    legend_set: Union[Unset, "TrackedEntityDataElementDimensionLegendSet"] = UNSET
    program_stage: Union[Unset, "TrackedEntityDataElementDimensionProgramStage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

        filter_ = self.filter_

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracked_entity_data_element_dimension_data_element import (
            TrackedEntityDataElementDimensionDataElement,
        )
        from ..models.tracked_entity_data_element_dimension_legend_set import TrackedEntityDataElementDimensionLegendSet
        from ..models.tracked_entity_data_element_dimension_program_stage import (
            TrackedEntityDataElementDimensionProgramStage,
        )

        d = src_dict.copy()
        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, TrackedEntityDataElementDimensionDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = TrackedEntityDataElementDimensionDataElement.from_dict(_data_element)

        filter_ = d.pop("filter", UNSET)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, TrackedEntityDataElementDimensionLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = TrackedEntityDataElementDimensionLegendSet.from_dict(_legend_set)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, TrackedEntityDataElementDimensionProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = TrackedEntityDataElementDimensionProgramStage.from_dict(_program_stage)

        tracked_entity_data_element_dimension = cls(
            data_element=data_element,
            filter_=filter_,
            legend_set=legend_set,
            program_stage=program_stage,
        )

        tracked_entity_data_element_dimension.additional_properties = d
        return tracked_entity_data_element_dimension

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
