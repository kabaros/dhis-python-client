from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lock_exception_dto import LockExceptionDto


T = TypeVar("T", bound="LockExceptionsDto")


@_attrs_define
class LockExceptionsDto:
    """
    Attributes:
        lock_exceptions (Union[Unset, list['LockExceptionDto']]):
    """

    lock_exceptions: Union[Unset, list["LockExceptionDto"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lock_exceptions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lock_exceptions, Unset):
            lock_exceptions = []
            for lock_exceptions_item_data in self.lock_exceptions:
                lock_exceptions_item = lock_exceptions_item_data.to_dict()
                lock_exceptions.append(lock_exceptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_exceptions is not UNSET:
            field_dict["lockExceptions"] = lock_exceptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.lock_exception_dto import LockExceptionDto

        d = src_dict.copy()
        lock_exceptions = []
        _lock_exceptions = d.pop("lockExceptions", UNSET)
        for lock_exceptions_item_data in _lock_exceptions or []:
            lock_exceptions_item = LockExceptionDto.from_dict(lock_exceptions_item_data)

            lock_exceptions.append(lock_exceptions_item)

        lock_exceptions_dto = cls(
            lock_exceptions=lock_exceptions,
        )

        lock_exceptions_dto.additional_properties = d
        return lock_exceptions_dto

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
