from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.font_style import FontStyle


T = TypeVar("T", bound="VisualizationFontStyle")


@_attrs_define
class VisualizationFontStyle:
    """
    Attributes:
        base_line_label (Union[Unset, FontStyle]):
        category_axis_label (Union[Unset, FontStyle]):
        horizontal_axis_title (Union[Unset, FontStyle]):
        legend (Union[Unset, FontStyle]):
        series_axis_label (Union[Unset, FontStyle]):
        target_line_label (Union[Unset, FontStyle]):
        vertical_axis_title (Union[Unset, FontStyle]):
        visualization_subtitle (Union[Unset, FontStyle]):
        visualization_title (Union[Unset, FontStyle]):
    """

    base_line_label: Union[Unset, "FontStyle"] = UNSET
    category_axis_label: Union[Unset, "FontStyle"] = UNSET
    horizontal_axis_title: Union[Unset, "FontStyle"] = UNSET
    legend: Union[Unset, "FontStyle"] = UNSET
    series_axis_label: Union[Unset, "FontStyle"] = UNSET
    target_line_label: Union[Unset, "FontStyle"] = UNSET
    vertical_axis_title: Union[Unset, "FontStyle"] = UNSET
    visualization_subtitle: Union[Unset, "FontStyle"] = UNSET
    visualization_title: Union[Unset, "FontStyle"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_line_label: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.base_line_label, Unset):
            base_line_label = self.base_line_label.to_dict()

        category_axis_label: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_axis_label, Unset):
            category_axis_label = self.category_axis_label.to_dict()

        horizontal_axis_title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.horizontal_axis_title, Unset):
            horizontal_axis_title = self.horizontal_axis_title.to_dict()

        legend: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend, Unset):
            legend = self.legend.to_dict()

        series_axis_label: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.series_axis_label, Unset):
            series_axis_label = self.series_axis_label.to_dict()

        target_line_label: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target_line_label, Unset):
            target_line_label = self.target_line_label.to_dict()

        vertical_axis_title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vertical_axis_title, Unset):
            vertical_axis_title = self.vertical_axis_title.to_dict()

        visualization_subtitle: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visualization_subtitle, Unset):
            visualization_subtitle = self.visualization_subtitle.to_dict()

        visualization_title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visualization_title, Unset):
            visualization_title = self.visualization_title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_line_label is not UNSET:
            field_dict["baseLineLabel"] = base_line_label
        if category_axis_label is not UNSET:
            field_dict["categoryAxisLabel"] = category_axis_label
        if horizontal_axis_title is not UNSET:
            field_dict["horizontalAxisTitle"] = horizontal_axis_title
        if legend is not UNSET:
            field_dict["legend"] = legend
        if series_axis_label is not UNSET:
            field_dict["seriesAxisLabel"] = series_axis_label
        if target_line_label is not UNSET:
            field_dict["targetLineLabel"] = target_line_label
        if vertical_axis_title is not UNSET:
            field_dict["verticalAxisTitle"] = vertical_axis_title
        if visualization_subtitle is not UNSET:
            field_dict["visualizationSubtitle"] = visualization_subtitle
        if visualization_title is not UNSET:
            field_dict["visualizationTitle"] = visualization_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.font_style import FontStyle

        d = src_dict.copy()
        _base_line_label = d.pop("baseLineLabel", UNSET)
        base_line_label: Union[Unset, FontStyle]
        if isinstance(_base_line_label, Unset):
            base_line_label = UNSET
        else:
            base_line_label = FontStyle.from_dict(_base_line_label)

        _category_axis_label = d.pop("categoryAxisLabel", UNSET)
        category_axis_label: Union[Unset, FontStyle]
        if isinstance(_category_axis_label, Unset):
            category_axis_label = UNSET
        else:
            category_axis_label = FontStyle.from_dict(_category_axis_label)

        _horizontal_axis_title = d.pop("horizontalAxisTitle", UNSET)
        horizontal_axis_title: Union[Unset, FontStyle]
        if isinstance(_horizontal_axis_title, Unset):
            horizontal_axis_title = UNSET
        else:
            horizontal_axis_title = FontStyle.from_dict(_horizontal_axis_title)

        _legend = d.pop("legend", UNSET)
        legend: Union[Unset, FontStyle]
        if isinstance(_legend, Unset):
            legend = UNSET
        else:
            legend = FontStyle.from_dict(_legend)

        _series_axis_label = d.pop("seriesAxisLabel", UNSET)
        series_axis_label: Union[Unset, FontStyle]
        if isinstance(_series_axis_label, Unset):
            series_axis_label = UNSET
        else:
            series_axis_label = FontStyle.from_dict(_series_axis_label)

        _target_line_label = d.pop("targetLineLabel", UNSET)
        target_line_label: Union[Unset, FontStyle]
        if isinstance(_target_line_label, Unset):
            target_line_label = UNSET
        else:
            target_line_label = FontStyle.from_dict(_target_line_label)

        _vertical_axis_title = d.pop("verticalAxisTitle", UNSET)
        vertical_axis_title: Union[Unset, FontStyle]
        if isinstance(_vertical_axis_title, Unset):
            vertical_axis_title = UNSET
        else:
            vertical_axis_title = FontStyle.from_dict(_vertical_axis_title)

        _visualization_subtitle = d.pop("visualizationSubtitle", UNSET)
        visualization_subtitle: Union[Unset, FontStyle]
        if isinstance(_visualization_subtitle, Unset):
            visualization_subtitle = UNSET
        else:
            visualization_subtitle = FontStyle.from_dict(_visualization_subtitle)

        _visualization_title = d.pop("visualizationTitle", UNSET)
        visualization_title: Union[Unset, FontStyle]
        if isinstance(_visualization_title, Unset):
            visualization_title = UNSET
        else:
            visualization_title = FontStyle.from_dict(_visualization_title)

        visualization_font_style = cls(
            base_line_label=base_line_label,
            category_axis_label=category_axis_label,
            horizontal_axis_title=horizontal_axis_title,
            legend=legend,
            series_axis_label=series_axis_label,
            target_line_label=target_line_label,
            vertical_axis_title=vertical_axis_title,
            visualization_subtitle=visualization_subtitle,
            visualization_title=visualization_title,
        )

        visualization_font_style.additional_properties = d
        return visualization_font_style

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
