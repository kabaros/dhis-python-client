from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_data import AccessData


T = TypeVar("T", bound="Access")


@_attrs_define
class Access:
    """
    Attributes:
        data (Union[Unset, AccessData]):
        delete (Union[Unset, bool]):
        externalize (Union[Unset, bool]):
        manage (Union[Unset, bool]):
        read (Union[Unset, bool]):
        update (Union[Unset, bool]):
        write (Union[Unset, bool]):
    """

    data: Union[Unset, "AccessData"] = UNSET
    delete: Union[Unset, bool] = UNSET
    externalize: Union[Unset, bool] = UNSET
    manage: Union[Unset, bool] = UNSET
    read: Union[Unset, bool] = UNSET
    update: Union[Unset, bool] = UNSET
    write: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        delete = self.delete

        externalize = self.externalize

        manage = self.manage

        read = self.read

        update = self.update

        write = self.write

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if delete is not UNSET:
            field_dict["delete"] = delete
        if externalize is not UNSET:
            field_dict["externalize"] = externalize
        if manage is not UNSET:
            field_dict["manage"] = manage
        if read is not UNSET:
            field_dict["read"] = read
        if update is not UNSET:
            field_dict["update"] = update
        if write is not UNSET:
            field_dict["write"] = write

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access_data import AccessData

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, AccessData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AccessData.from_dict(_data)

        delete = d.pop("delete", UNSET)

        externalize = d.pop("externalize", UNSET)

        manage = d.pop("manage", UNSET)

        read = d.pop("read", UNSET)

        update = d.pop("update", UNSET)

        write = d.pop("write", UNSET)

        access = cls(
            data=data,
            delete=delete,
            externalize=externalize,
            manage=manage,
            read=read,
            update=update,
            write=write,
        )

        access.additional_properties = d
        return access

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
