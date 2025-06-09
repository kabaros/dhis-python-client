from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.predictor_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_predictor_groups_item import (
        PredictorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorGroupsItem,
    )


T = TypeVar("T", bound="PredictorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class PredictorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        predictor_groups (Union[Unset,
            list['PredictorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorGroupsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    predictor_groups: Union[
        Unset, list["PredictorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorGroupsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        predictor_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.predictor_groups, Unset):
            predictor_groups = []
            for predictor_groups_item_data in self.predictor_groups:
                predictor_groups_item = predictor_groups_item_data.to_dict()
                predictor_groups.append(predictor_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if predictor_groups is not UNSET:
            field_dict["predictorGroups"] = predictor_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.predictor_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_predictor_groups_item import (
            PredictorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorGroupsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        predictor_groups = []
        _predictor_groups = d.pop("predictorGroups", UNSET)
        for predictor_groups_item_data in _predictor_groups or []:
            predictor_groups_item = (
                PredictorGroupGetObjectListGistgetObjectListGistAsCsvResponse200Type0PredictorGroupsItem.from_dict(
                    predictor_groups_item_data
                )
            )

            predictor_groups.append(predictor_groups_item)

        predictor_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            predictor_groups=predictor_groups,
        )

        predictor_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return predictor_group_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
