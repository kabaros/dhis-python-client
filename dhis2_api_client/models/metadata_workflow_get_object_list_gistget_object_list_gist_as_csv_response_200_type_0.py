from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.metadata_workflow_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_metadataproposals_item import (
        MetadataWorkflowGetObjectListGistgetObjectListGistAsCsvResponse200Type0MetadataproposalsItem,
    )


T = TypeVar("T", bound="MetadataWorkflowGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class MetadataWorkflowGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        metadataproposals (Union[Unset,
            list['MetadataWorkflowGetObjectListGistgetObjectListGistAsCsvResponse200Type0MetadataproposalsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    metadataproposals: Union[
        Unset, list["MetadataWorkflowGetObjectListGistgetObjectListGistAsCsvResponse200Type0MetadataproposalsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        metadataproposals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metadataproposals, Unset):
            metadataproposals = []
            for metadataproposals_item_data in self.metadataproposals:
                metadataproposals_item = metadataproposals_item_data.to_dict()
                metadataproposals.append(metadataproposals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if metadataproposals is not UNSET:
            field_dict["metadataproposals"] = metadataproposals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.metadata_workflow_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_metadataproposals_item import (
            MetadataWorkflowGetObjectListGistgetObjectListGistAsCsvResponse200Type0MetadataproposalsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        metadataproposals = []
        _metadataproposals = d.pop("metadataproposals", UNSET)
        for metadataproposals_item_data in _metadataproposals or []:
            metadataproposals_item = (
                MetadataWorkflowGetObjectListGistgetObjectListGistAsCsvResponse200Type0MetadataproposalsItem.from_dict(
                    metadataproposals_item_data
                )
            )

            metadataproposals.append(metadataproposals_item)

        metadata_workflow_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            metadataproposals=metadataproposals,
        )

        metadata_workflow_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return metadata_workflow_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
