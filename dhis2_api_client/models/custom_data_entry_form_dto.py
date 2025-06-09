from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_data_entry_form_dto_display_density import CustomDataEntryFormDtoDisplayDensity
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDataEntryFormDto")


@_attrs_define
class CustomDataEntryFormDto:
    """
    Attributes:
        display_density (CustomDataEntryFormDtoDisplayDensity):
        data_set_id (Union[Unset, str]):
        form (Union[Unset, str]):
        id (Union[Unset, str]):
        version (Union[Unset, int]):
    """

    display_density: CustomDataEntryFormDtoDisplayDensity
    data_set_id: Union[Unset, str] = UNSET
    form: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_density = self.display_density.value

        data_set_id = self.data_set_id

        form = self.form

        id = self.id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayDensity": display_density,
            }
        )
        if data_set_id is not UNSET:
            field_dict["dataSetId"] = data_set_id
        if form is not UNSET:
            field_dict["form"] = form
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        display_density = CustomDataEntryFormDtoDisplayDensity(d.pop("displayDensity"))

        data_set_id = d.pop("dataSetId", UNSET)

        form = d.pop("form", UNSET)

        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        custom_data_entry_form_dto = cls(
            display_density=display_density,
            data_set_id=data_set_id,
            form=form,
            id=id,
            version=version,
        )

        custom_data_entry_form_dto.additional_properties = d
        return custom_data_entry_form_dto

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
