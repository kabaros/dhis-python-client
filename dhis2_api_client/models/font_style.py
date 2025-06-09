from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.font_style_font import FontStyleFont
from ..models.font_style_text_align import FontStyleTextAlign
from ..types import UNSET, Unset

T = TypeVar("T", bound="FontStyle")


@_attrs_define
class FontStyle:
    """
    Attributes:
        font (FontStyleFont):
        text_align (FontStyleTextAlign):
        bold (Union[Unset, bool]):
        font_size (Union[Unset, int]):
        italic (Union[Unset, bool]):
        text_color (Union[Unset, str]):
        underline (Union[Unset, bool]):
    """

    font: FontStyleFont
    text_align: FontStyleTextAlign
    bold: Union[Unset, bool] = UNSET
    font_size: Union[Unset, int] = UNSET
    italic: Union[Unset, bool] = UNSET
    text_color: Union[Unset, str] = UNSET
    underline: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        font = self.font.value

        text_align = self.text_align.value

        bold = self.bold

        font_size = self.font_size

        italic = self.italic

        text_color = self.text_color

        underline = self.underline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "font": font,
                "textAlign": text_align,
            }
        )
        if bold is not UNSET:
            field_dict["bold"] = bold
        if font_size is not UNSET:
            field_dict["fontSize"] = font_size
        if italic is not UNSET:
            field_dict["italic"] = italic
        if text_color is not UNSET:
            field_dict["textColor"] = text_color
        if underline is not UNSET:
            field_dict["underline"] = underline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        font = FontStyleFont(d.pop("font"))

        text_align = FontStyleTextAlign(d.pop("textAlign"))

        bold = d.pop("bold", UNSET)

        font_size = d.pop("fontSize", UNSET)

        italic = d.pop("italic", UNSET)

        text_color = d.pop("textColor", UNSET)

        underline = d.pop("underline", UNSET)

        font_style = cls(
            font=font,
            text_align=text_align,
            bold=bold,
            font_size=font_size,
            italic=italic,
            text_color=text_color,
            underline=underline,
        )

        font_style.additional_properties = d
        return font_style

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
