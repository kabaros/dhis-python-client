from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebModule")


@_attrs_define
class WebModule:
    """
    Attributes:
        default_action (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        icon (Union[Unset, str]):
        name (Union[Unset, str]):
        namespace (Union[Unset, str]):
    """

    default_action: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_action = self.default_action

        description = self.description

        display_name = self.display_name

        icon = self.icon

        name = self.name

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_action is not UNSET:
            field_dict["defaultAction"] = default_action
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        default_action = d.pop("defaultAction", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        icon = d.pop("icon", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        web_module = cls(
            default_action=default_action,
            description=description,
            display_name=display_name,
            icon=icon,
            name=name,
            namespace=namespace,
        )

        web_module.additional_properties = d
        return web_module

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
