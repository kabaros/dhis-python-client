from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.form_options_additional_property import FormOptionsAdditionalProperty


T = TypeVar("T", bound="FormOptions")


@_attrs_define
class FormOptions:
    """ """

    additional_properties: dict[str, "FormOptionsAdditionalProperty"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.form_options_additional_property import FormOptionsAdditionalProperty

        d = src_dict.copy()
        form_options = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FormOptionsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        form_options.additional_properties = additional_properties
        return form_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "FormOptionsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "FormOptionsAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
