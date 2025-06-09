import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_category import NotificationCategory
from ..models.notification_data_type import NotificationDataType
from ..models.notification_level import NotificationLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_data import NotificationData


T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """
    Attributes:
        category (NotificationCategory):
        data_type (NotificationDataType):
        level (NotificationLevel):
        completed (Union[Unset, bool]):
        data (Union[Unset, NotificationData]):
        id (Union[Unset, str]):
        message (Union[Unset, str]):
        time (Union[Unset, datetime.datetime]):
        uid (Union[Unset, str]):
    """

    category: NotificationCategory
    data_type: NotificationDataType
    level: NotificationLevel
    completed: Union[Unset, bool] = UNSET
    data: Union[Unset, "NotificationData"] = UNSET
    id: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        data_type = self.data_type.value

        level = self.level.value

        completed = self.completed

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        id = self.id

        message = self.message

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "dataType": data_type,
                "level": level,
            }
        )
        if completed is not UNSET:
            field_dict["completed"] = completed
        if data is not UNSET:
            field_dict["data"] = data
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if time is not UNSET:
            field_dict["time"] = time
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.notification_data import NotificationData

        d = src_dict.copy()
        category = NotificationCategory(d.pop("category"))

        data_type = NotificationDataType(d.pop("dataType"))

        level = NotificationLevel(d.pop("level"))

        completed = d.pop("completed", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, NotificationData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = NotificationData.from_dict(_data)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        uid = d.pop("uid", UNSET)

        notification = cls(
            category=category,
            data_type=data_type,
            level=level,
            completed=completed,
            data=data,
            id=id,
            message=message,
            time=time,
            uid=uid,
        )

        notification.additional_properties = d
        return notification

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
