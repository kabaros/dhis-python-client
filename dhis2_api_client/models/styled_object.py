from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.styled_object_text_mode import StyledObjectTextMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.font_style import FontStyle


T = TypeVar("T", bound="StyledObject")


@_attrs_define
class StyledObject:
    """
    Attributes:
        text_mode (StyledObjectTextMode):
        font_style (Union[Unset, FontStyle]):
        text (Union[Unset, str]):
    """

    text_mode: StyledObjectTextMode
    font_style: Union[Unset, "FontStyle"] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_mode = self.text_mode.value

        font_style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.font_style, Unset):
            font_style = self.font_style.to_dict()

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "textMode": text_mode,
            }
        )
        if font_style is not UNSET:
            field_dict["fontStyle"] = font_style
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.font_style import FontStyle

        d = src_dict.copy()
        text_mode = StyledObjectTextMode(d.pop("textMode"))

        _font_style = d.pop("fontStyle", UNSET)
        font_style: Union[Unset, FontStyle]
        if isinstance(_font_style, Unset):
            font_style = UNSET
        else:
            font_style = FontStyle.from_dict(_font_style)

        text = d.pop("text", UNSET)

        styled_object = cls(
            text_mode=text_mode,
            font_style=font_style,
            text=text,
        )

        styled_object.additional_properties = d
        return styled_object

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
