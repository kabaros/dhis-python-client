from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracked_entity_attribute_dimension_attribute import TrackedEntityAttributeDimensionAttribute
    from ..models.tracked_entity_attribute_dimension_legend_set import TrackedEntityAttributeDimensionLegendSet


T = TypeVar("T", bound="TrackedEntityAttributeDimension")


@_attrs_define
class TrackedEntityAttributeDimension:
    """
    Attributes:
        attribute (Union[Unset, TrackedEntityAttributeDimensionAttribute]): A UID reference to a TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        filter_ (Union[Unset, str]):
        legend_set (Union[Unset, TrackedEntityAttributeDimensionLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
    """

    attribute: Union[Unset, "TrackedEntityAttributeDimensionAttribute"] = UNSET
    filter_: Union[Unset, str] = UNSET
    legend_set: Union[Unset, "TrackedEntityAttributeDimensionLegendSet"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

        filter_ = self.filter_

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tracked_entity_attribute_dimension_attribute import TrackedEntityAttributeDimensionAttribute
        from ..models.tracked_entity_attribute_dimension_legend_set import TrackedEntityAttributeDimensionLegendSet

        d = src_dict.copy()
        _attribute = d.pop("attribute", UNSET)
        attribute: Union[Unset, TrackedEntityAttributeDimensionAttribute]
        if isinstance(_attribute, Unset):
            attribute = UNSET
        else:
            attribute = TrackedEntityAttributeDimensionAttribute.from_dict(_attribute)

        filter_ = d.pop("filter", UNSET)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, TrackedEntityAttributeDimensionLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = TrackedEntityAttributeDimensionLegendSet.from_dict(_legend_set)

        tracked_entity_attribute_dimension = cls(
            attribute=attribute,
            filter_=filter_,
            legend_set=legend_set,
        )

        tracked_entity_attribute_dimension.additional_properties = d
        return tracked_entity_attribute_dimension

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
