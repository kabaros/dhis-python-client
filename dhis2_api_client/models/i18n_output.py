from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i18n_output_translations import I18NOutputTranslations


T = TypeVar("T", bound="I18NOutput")


@_attrs_define
class I18NOutput:
    """
    Attributes:
        translations (Union[Unset, I18NOutputTranslations]):
    """

    translations: Union[Unset, "I18NOutputTranslations"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        translations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = self.translations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.i18n_output_translations import I18NOutputTranslations

        d = src_dict.copy()
        _translations = d.pop("translations", UNSET)
        translations: Union[Unset, I18NOutputTranslations]
        if isinstance(_translations, Unset):
            translations = UNSET
        else:
            translations = I18NOutputTranslations.from_dict(_translations)

        i18n_output = cls(
            translations=translations,
        )

        i18n_output.additional_properties = d
        return i18n_output

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
