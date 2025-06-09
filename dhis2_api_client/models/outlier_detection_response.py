from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outlier_detection_metadata import OutlierDetectionMetadata
    from ..models.outlier_value import OutlierValue


T = TypeVar("T", bound="OutlierDetectionResponse")


@_attrs_define
class OutlierDetectionResponse:
    """
    Attributes:
        metadata (Union[Unset, OutlierDetectionMetadata]):
        outlier_values (Union[Unset, list['OutlierValue']]):
    """

    metadata: Union[Unset, "OutlierDetectionMetadata"] = UNSET
    outlier_values: Union[Unset, list["OutlierValue"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        outlier_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.outlier_values, Unset):
            outlier_values = []
            for outlier_values_item_data in self.outlier_values:
                outlier_values_item = outlier_values_item_data.to_dict()
                outlier_values.append(outlier_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if outlier_values is not UNSET:
            field_dict["outlierValues"] = outlier_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.outlier_detection_metadata import OutlierDetectionMetadata
        from ..models.outlier_value import OutlierValue

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OutlierDetectionMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OutlierDetectionMetadata.from_dict(_metadata)

        outlier_values = []
        _outlier_values = d.pop("outlierValues", UNSET)
        for outlier_values_item_data in _outlier_values or []:
            outlier_values_item = OutlierValue.from_dict(outlier_values_item_data)

            outlier_values.append(outlier_values_item)

        outlier_detection_response = cls(
            metadata=metadata,
            outlier_values=outlier_values,
        )

        outlier_detection_response.additional_properties = d
        return outlier_detection_response

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
