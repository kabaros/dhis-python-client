from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outlier_analysis_normalization_method import OutlierAnalysisNormalizationMethod
from ..models.outlier_analysis_outlier_method import OutlierAnalysisOutlierMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outlier_line import OutlierLine


T = TypeVar("T", bound="OutlierAnalysis")


@_attrs_define
class OutlierAnalysis:
    """
    Attributes:
        normalization_method (OutlierAnalysisNormalizationMethod):
        outlier_method (OutlierAnalysisOutlierMethod):
        enabled (Union[Unset, bool]):
        extreme_lines (Union[Unset, OutlierLine]):
        max_results (Union[Unset, int]):
        threshold_factor (Union[Unset, float]):
    """

    normalization_method: OutlierAnalysisNormalizationMethod
    outlier_method: OutlierAnalysisOutlierMethod
    enabled: Union[Unset, bool] = UNSET
    extreme_lines: Union[Unset, "OutlierLine"] = UNSET
    max_results: Union[Unset, int] = UNSET
    threshold_factor: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        normalization_method = self.normalization_method.value

        outlier_method = self.outlier_method.value

        enabled = self.enabled

        extreme_lines: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.extreme_lines, Unset):
            extreme_lines = self.extreme_lines.to_dict()

        max_results = self.max_results

        threshold_factor = self.threshold_factor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "normalizationMethod": normalization_method,
                "outlierMethod": outlier_method,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if extreme_lines is not UNSET:
            field_dict["extremeLines"] = extreme_lines
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if threshold_factor is not UNSET:
            field_dict["thresholdFactor"] = threshold_factor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.outlier_line import OutlierLine

        d = src_dict.copy()
        normalization_method = OutlierAnalysisNormalizationMethod(d.pop("normalizationMethod"))

        outlier_method = OutlierAnalysisOutlierMethod(d.pop("outlierMethod"))

        enabled = d.pop("enabled", UNSET)

        _extreme_lines = d.pop("extremeLines", UNSET)
        extreme_lines: Union[Unset, OutlierLine]
        if isinstance(_extreme_lines, Unset):
            extreme_lines = UNSET
        else:
            extreme_lines = OutlierLine.from_dict(_extreme_lines)

        max_results = d.pop("maxResults", UNSET)

        threshold_factor = d.pop("thresholdFactor", UNSET)

        outlier_analysis = cls(
            normalization_method=normalization_method,
            outlier_method=outlier_method,
            enabled=enabled,
            extreme_lines=extreme_lines,
            max_results=max_results,
            threshold_factor=threshold_factor,
        )

        outlier_analysis.additional_properties = d
        return outlier_analysis

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
