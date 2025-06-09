from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_category_combo import FormCategoryCombo
    from ..models.form_options import FormOptions
    from ..models.group import Group


T = TypeVar("T", bound="Form")


@_attrs_define
class Form:
    """
    Attributes:
        category_combo (Union[Unset, FormCategoryCombo]):
        groups (Union[Unset, list['Group']]):
        label (Union[Unset, str]):
        options (Union[Unset, FormOptions]):
        subtitle (Union[Unset, str]):
    """

    category_combo: Union[Unset, "FormCategoryCombo"] = UNSET
    groups: Union[Unset, list["Group"]] = UNSET
    label: Union[Unset, str] = UNSET
    options: Union[Unset, "FormOptions"] = UNSET
    subtitle: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_combo, Unset):
            category_combo = self.category_combo.to_dict()

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        label = self.label

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        subtitle = self.subtitle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_combo is not UNSET:
            field_dict["categoryCombo"] = category_combo
        if groups is not UNSET:
            field_dict["groups"] = groups
        if label is not UNSET:
            field_dict["label"] = label
        if options is not UNSET:
            field_dict["options"] = options
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.form_category_combo import FormCategoryCombo
        from ..models.form_options import FormOptions
        from ..models.group import Group

        d = src_dict.copy()
        _category_combo = d.pop("categoryCombo", UNSET)
        category_combo: Union[Unset, FormCategoryCombo]
        if isinstance(_category_combo, Unset):
            category_combo = UNSET
        else:
            category_combo = FormCategoryCombo.from_dict(_category_combo)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = Group.from_dict(groups_item_data)

            groups.append(groups_item)

        label = d.pop("label", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, FormOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FormOptions.from_dict(_options)

        subtitle = d.pop("subtitle", UNSET)

        form = cls(
            category_combo=category_combo,
            groups=groups,
            label=label,
            options=options,
            subtitle=subtitle,
        )

        form.additional_properties = d
        return form

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
