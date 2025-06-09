from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.axis_v2_type import AxisV2Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line import Line
    from ..models.styled_object import StyledObject


T = TypeVar("T", bound="AxisV2")


@_attrs_define
class AxisV2:
    """
    Attributes:
        type_ (AxisV2Type):
        base_line (Union[Unset, Line]):
        decimals (Union[Unset, int]):
        index (Union[Unset, int]):
        label (Union[Unset, StyledObject]):
        max_value (Union[Unset, float]):
        min_value (Union[Unset, float]):
        steps (Union[Unset, int]):
        target_line (Union[Unset, Line]):
        title (Union[Unset, StyledObject]):
    """

    type_: AxisV2Type
    base_line: Union[Unset, "Line"] = UNSET
    decimals: Union[Unset, int] = UNSET
    index: Union[Unset, int] = UNSET
    label: Union[Unset, "StyledObject"] = UNSET
    max_value: Union[Unset, float] = UNSET
    min_value: Union[Unset, float] = UNSET
    steps: Union[Unset, int] = UNSET
    target_line: Union[Unset, "Line"] = UNSET
    title: Union[Unset, "StyledObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        base_line: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_line, Unset):
            base_line = self.base_line.to_dict()

        decimals = self.decimals

        index = self.index

        label: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.to_dict()

        max_value = self.max_value

        min_value = self.min_value

        steps = self.steps

        target_line: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target_line, Unset):
            target_line = self.target_line.to_dict()

        title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if base_line is not UNSET:
            field_dict["baseLine"] = base_line
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if index is not UNSET:
            field_dict["index"] = index
        if label is not UNSET:
            field_dict["label"] = label
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if steps is not UNSET:
            field_dict["steps"] = steps
        if target_line is not UNSET:
            field_dict["targetLine"] = target_line
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.line import Line
        from ..models.styled_object import StyledObject

        d = src_dict.copy()
        type_ = AxisV2Type(d.pop("type"))

        _base_line = d.pop("baseLine", UNSET)
        base_line: Union[Unset, Line]
        if isinstance(_base_line, Unset):
            base_line = UNSET
        else:
            base_line = Line.from_dict(_base_line)

        decimals = d.pop("decimals", UNSET)

        index = d.pop("index", UNSET)

        _label = d.pop("label", UNSET)
        label: Union[Unset, StyledObject]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = StyledObject.from_dict(_label)

        max_value = d.pop("maxValue", UNSET)

        min_value = d.pop("minValue", UNSET)

        steps = d.pop("steps", UNSET)

        _target_line = d.pop("targetLine", UNSET)
        target_line: Union[Unset, Line]
        if isinstance(_target_line, Unset):
            target_line = UNSET
        else:
            target_line = Line.from_dict(_target_line)

        _title = d.pop("title", UNSET)
        title: Union[Unset, StyledObject]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = StyledObject.from_dict(_title)

        axis_v2 = cls(
            type_=type_,
            base_line=base_line,
            decimals=decimals,
            index=index,
            label=label,
            max_value=max_value,
            min_value=min_value,
            steps=steps,
            target_line=target_line,
            title=title,
        )

        axis_v2.additional_properties = d
        return axis_v2

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
