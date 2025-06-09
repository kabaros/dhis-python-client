from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_resource_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_file_resources_item import (
        FileResourceGetObjectListGistgetObjectListGistAsCsvResponse200Type0FileResourcesItem,
    )
    from ..models.gist_pager import GistPager


T = TypeVar("T", bound="FileResourceGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class FileResourceGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        file_resources (Union[Unset,
            list['FileResourceGetObjectListGistgetObjectListGistAsCsvResponse200Type0FileResourcesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    file_resources: Union[
        Unset, list["FileResourceGetObjectListGistgetObjectListGistAsCsvResponse200Type0FileResourcesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        file_resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.file_resources, Unset):
            file_resources = []
            for file_resources_item_data in self.file_resources:
                file_resources_item = file_resources_item_data.to_dict()
                file_resources.append(file_resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if file_resources is not UNSET:
            field_dict["fileResources"] = file_resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file_resource_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_file_resources_item import (
            FileResourceGetObjectListGistgetObjectListGistAsCsvResponse200Type0FileResourcesItem,
        )
        from ..models.gist_pager import GistPager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        file_resources = []
        _file_resources = d.pop("fileResources", UNSET)
        for file_resources_item_data in _file_resources or []:
            file_resources_item = (
                FileResourceGetObjectListGistgetObjectListGistAsCsvResponse200Type0FileResourcesItem.from_dict(
                    file_resources_item_data
                )
            )

            file_resources.append(file_resources_item)

        file_resource_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            file_resources=file_resources,
        )

        file_resource_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return file_resource_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
