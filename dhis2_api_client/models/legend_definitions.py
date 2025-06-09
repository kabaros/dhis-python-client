from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.legend_definitions_strategy import LegendDefinitionsStrategy
from ..models.legend_definitions_style import LegendDefinitionsStyle
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.legend_definitions_set import LegendDefinitionsSet


T = TypeVar("T", bound="LegendDefinitions")


@_attrs_define
class LegendDefinitions:
    """
    Attributes:
        strategy (LegendDefinitionsStrategy):
        style (LegendDefinitionsStyle):
        set_ (Union[Unset, LegendDefinitionsSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        show_key (Union[Unset, bool]):
    """

    strategy: LegendDefinitionsStrategy
    style: LegendDefinitionsStyle
    set_: Union[Unset, "LegendDefinitionsSet"] = UNSET
    show_key: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategy = self.strategy.value

        style = self.style.value

        set_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.set_, Unset):
            set_ = self.set_.to_dict()

        show_key = self.show_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategy": strategy,
                "style": style,
            }
        )
        if set_ is not UNSET:
            field_dict["set"] = set_
        if show_key is not UNSET:
            field_dict["showKey"] = show_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.legend_definitions_set import LegendDefinitionsSet

        d = src_dict.copy()
        strategy = LegendDefinitionsStrategy(d.pop("strategy"))

        style = LegendDefinitionsStyle(d.pop("style"))

        _set_ = d.pop("set", UNSET)
        set_: Union[Unset, LegendDefinitionsSet]
        if isinstance(_set_, Unset):
            set_ = UNSET
        else:
            set_ = LegendDefinitionsSet.from_dict(_set_)

        show_key = d.pop("showKey", UNSET)

        legend_definitions = cls(
            strategy=strategy,
            style=style,
            set_=set_,
            show_key=show_key,
        )

        legend_definitions.additional_properties = d
        return legend_definitions

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
