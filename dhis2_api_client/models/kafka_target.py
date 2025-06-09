from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KafkaTarget")


@_attrs_define
class KafkaTarget:
    """
    Attributes:
        bootstrap_servers (str):
        client_id (str):
        topic (str):
        password (Union[Unset, str]):
        type_ (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    bootstrap_servers: str
    client_id: str
    topic: str
    password: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bootstrap_servers = self.bootstrap_servers

        client_id = self.client_id

        topic = self.topic

        password = self.password

        type_ = self.type_

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bootstrapServers": bootstrap_servers,
                "clientId": client_id,
                "topic": topic,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if type_ is not UNSET:
            field_dict["type"] = type_
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bootstrap_servers = d.pop("bootstrapServers")

        client_id = d.pop("clientId")

        topic = d.pop("topic")

        password = d.pop("password", UNSET)

        type_ = d.pop("type", UNSET)

        username = d.pop("username", UNSET)

        kafka_target = cls(
            bootstrap_servers=bootstrap_servers,
            client_id=client_id,
            topic=topic,
            password=password,
            type_=type_,
            username=username,
        )

        kafka_target.additional_properties = d
        return kafka_target

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
