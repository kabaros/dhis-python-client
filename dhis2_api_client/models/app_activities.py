from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_dhis import AppDhis


T = TypeVar("T", bound="AppActivities")


@_attrs_define
class AppActivities:
    """
    Attributes:
        dhis (Union[Unset, AppDhis]):
    """

    dhis: Union[Unset, "AppDhis"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dhis: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dhis, Unset):
            dhis = self.dhis.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dhis is not UNSET:
            field_dict["dhis"] = dhis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.app_dhis import AppDhis

        d = src_dict.copy()
        _dhis = d.pop("dhis", UNSET)
        dhis: Union[Unset, AppDhis]
        if isinstance(_dhis, Unset):
            dhis = UNSET
        else:
            dhis = AppDhis.from_dict(_dhis)

        app_activities = cls(
            dhis=dhis,
        )

        app_activities.additional_properties = d
        return app_activities

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
