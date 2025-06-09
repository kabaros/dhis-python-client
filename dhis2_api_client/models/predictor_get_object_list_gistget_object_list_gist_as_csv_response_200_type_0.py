from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.predictor_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_predictors_item import (
        PredictorGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorsItem,
    )


T = TypeVar("T", bound="PredictorGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class PredictorGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        predictors (Union[Unset,
            list['PredictorGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    predictors: Union[Unset, list["PredictorGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorsItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        predictors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.predictors, Unset):
            predictors = []
            for predictors_item_data in self.predictors:
                predictors_item = predictors_item_data.to_dict()
                predictors.append(predictors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if predictors is not UNSET:
            field_dict["predictors"] = predictors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.predictor_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_predictors_item import (
            PredictorGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        predictors = []
        _predictors = d.pop("predictors", UNSET)
        for predictors_item_data in _predictors or []:
            predictors_item = PredictorGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorsItem.from_dict(
                predictors_item_data
            )

            predictors.append(predictors_item)

        predictor_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            predictors=predictors,
        )

        predictor_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return predictor_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
