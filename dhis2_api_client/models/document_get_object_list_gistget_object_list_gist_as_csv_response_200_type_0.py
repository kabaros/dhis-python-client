from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_documents_item import (
        DocumentGetObjectListGistgetObjectListGistAsCsvResponse200Type0DocumentsItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="DocumentGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class DocumentGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        documents (Union[Unset, list['DocumentGetObjectListGistgetObjectListGistAsCsvResponse200Type0DocumentsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    documents: Union[Unset, list["DocumentGetObjectListGistgetObjectListGistAsCsvResponse200Type0DocumentsItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.document_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_documents_item import (
            DocumentGetObjectListGistgetObjectListGistAsCsvResponse200Type0DocumentsItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = DocumentGetObjectListGistgetObjectListGistAsCsvResponse200Type0DocumentsItem.from_dict(
                documents_item_data
            )

            documents.append(documents_item)

        document_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            documents=documents,
        )

        document_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return document_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
