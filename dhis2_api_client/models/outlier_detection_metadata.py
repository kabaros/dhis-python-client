import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.outlier_detection_metadata_algorithm import OutlierDetectionMetadataAlgorithm
from ..models.outlier_detection_metadata_order_by import OutlierDetectionMetadataOrderBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutlierDetectionMetadata")


@_attrs_define
class OutlierDetectionMetadata:
    """
    Attributes:
        algorithm (OutlierDetectionMetadataAlgorithm):
        order_by (OutlierDetectionMetadataOrderBy):
        count (Union[Unset, int]):
        data_end_date (Union[Unset, datetime.datetime]):
        data_start_date (Union[Unset, datetime.datetime]):
        max_results (Union[Unset, int]):
        threshold (Union[Unset, float]):
    """

    algorithm: OutlierDetectionMetadataAlgorithm
    order_by: OutlierDetectionMetadataOrderBy
    count: Union[Unset, int] = UNSET
    data_end_date: Union[Unset, datetime.datetime] = UNSET
    data_start_date: Union[Unset, datetime.datetime] = UNSET
    max_results: Union[Unset, int] = UNSET
    threshold: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm.value

        order_by = self.order_by.value

        count = self.count

        data_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.data_end_date, Unset):
            data_end_date = self.data_end_date.isoformat()

        data_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.data_start_date, Unset):
            data_start_date = self.data_start_date.isoformat()

        max_results = self.max_results

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithm": algorithm,
                "orderBy": order_by,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if data_end_date is not UNSET:
            field_dict["dataEndDate"] = data_end_date
        if data_start_date is not UNSET:
            field_dict["dataStartDate"] = data_start_date
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        algorithm = OutlierDetectionMetadataAlgorithm(d.pop("algorithm"))

        order_by = OutlierDetectionMetadataOrderBy(d.pop("orderBy"))

        count = d.pop("count", UNSET)

        _data_end_date = d.pop("dataEndDate", UNSET)
        data_end_date: Union[Unset, datetime.datetime]
        if isinstance(_data_end_date, Unset):
            data_end_date = UNSET
        else:
            data_end_date = isoparse(_data_end_date)

        _data_start_date = d.pop("dataStartDate", UNSET)
        data_start_date: Union[Unset, datetime.datetime]
        if isinstance(_data_start_date, Unset):
            data_start_date = UNSET
        else:
            data_start_date = isoparse(_data_start_date)

        max_results = d.pop("maxResults", UNSET)

        threshold = d.pop("threshold", UNSET)

        outlier_detection_metadata = cls(
            algorithm=algorithm,
            order_by=order_by,
            count=count,
            data_end_date=data_end_date,
            data_start_date=data_start_date,
            max_results=max_results,
            threshold=threshold,
        )

        outlier_detection_metadata.additional_properties = d
        return outlier_detection_metadata

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
