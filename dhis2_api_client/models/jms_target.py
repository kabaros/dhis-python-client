from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JmsTarget")


@_attrs_define
class JmsTarget:
    """
    Attributes:
        address (str):
        broker_url (str):
        client_id (str):
        group_id (str):
        password (Union[Unset, str]):
        type_ (Union[Unset, str]):
        use_queue (Union[Unset, bool]):
        username (Union[Unset, str]):
    """

    address: str
    broker_url: str
    client_id: str
    group_id: str
    password: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    use_queue: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        broker_url = self.broker_url

        client_id = self.client_id

        group_id = self.group_id

        password = self.password

        type_ = self.type_

        use_queue = self.use_queue

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "brokerUrl": broker_url,
                "clientId": client_id,
                "groupId": group_id,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if type_ is not UNSET:
            field_dict["type"] = type_
        if use_queue is not UNSET:
            field_dict["useQueue"] = use_queue
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address")

        broker_url = d.pop("brokerUrl")

        client_id = d.pop("clientId")

        group_id = d.pop("groupId")

        password = d.pop("password", UNSET)

        type_ = d.pop("type", UNSET)

        use_queue = d.pop("useQueue", UNSET)

        username = d.pop("username", UNSET)

        jms_target = cls(
            address=address,
            broker_url=broker_url,
            client_id=client_id,
            group_id=group_id,
            password=password,
            type_=type_,
            use_queue=use_queue,
            username=username,
        )

        jms_target.additional_properties = d
        return jms_target

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
