from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expression_missing_value_strategy import ExpressionMissingValueStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.translation import Translation


T = TypeVar("T", bound="Expression")


@_attrs_define
class Expression:
    """
    Attributes:
        missing_value_strategy (ExpressionMissingValueStrategy):
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        expression (Union[Unset, str]):
        sliding_window (Union[Unset, bool]):
        translations (Union[Unset, list['Translation']]):
    """

    missing_value_strategy: ExpressionMissingValueStrategy
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    expression: Union[Unset, str] = UNSET
    sliding_window: Union[Unset, bool] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        missing_value_strategy = self.missing_value_strategy.value

        description = self.description

        display_description = self.display_description

        expression = self.expression

        sliding_window = self.sliding_window

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "missingValueStrategy": missing_value_strategy,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if expression is not UNSET:
            field_dict["expression"] = expression
        if sliding_window is not UNSET:
            field_dict["slidingWindow"] = sliding_window
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.translation import Translation

        d = src_dict.copy()
        missing_value_strategy = ExpressionMissingValueStrategy(d.pop("missingValueStrategy"))

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        expression = d.pop("expression", UNSET)

        sliding_window = d.pop("slidingWindow", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        expression = cls(
            missing_value_strategy=missing_value_strategy,
            description=description,
            display_description=display_description,
            expression=expression,
            sliding_window=sliding_window,
            translations=translations,
        )

        expression.additional_properties = d
        return expression

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
