from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.lock_exception_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_lock_exceptions_item import (
        LockExceptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0LockExceptionsItem,
    )


T = TypeVar("T", bound="LockExceptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class LockExceptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        lock_exceptions (Union[Unset,
            list['LockExceptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0LockExceptionsItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    lock_exceptions: Union[
        Unset, list["LockExceptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0LockExceptionsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        lock_exceptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lock_exceptions, Unset):
            lock_exceptions = []
            for lock_exceptions_item_data in self.lock_exceptions:
                lock_exceptions_item = lock_exceptions_item_data.to_dict()
                lock_exceptions.append(lock_exceptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if lock_exceptions is not UNSET:
            field_dict["lockExceptions"] = lock_exceptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.lock_exception_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_lock_exceptions_item import (
            LockExceptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0LockExceptionsItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        lock_exceptions = []
        _lock_exceptions = d.pop("lockExceptions", UNSET)
        for lock_exceptions_item_data in _lock_exceptions or []:
            lock_exceptions_item = (
                LockExceptionGetObjectListGistgetObjectListGistAsCsvResponse200Type0LockExceptionsItem.from_dict(
                    lock_exceptions_item_data
                )
            )

            lock_exceptions.append(lock_exceptions_item)

        lock_exception_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            lock_exceptions=lock_exceptions,
        )

        lock_exception_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return lock_exception_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
