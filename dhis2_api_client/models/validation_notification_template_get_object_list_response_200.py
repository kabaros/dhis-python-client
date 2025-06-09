from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pager import Pager
    from ..models.validation_notification_template import ValidationNotificationTemplate


T = TypeVar("T", bound="ValidationNotificationTemplateGetObjectListResponse200")


@_attrs_define
class ValidationNotificationTemplateGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        validation_notification_templates (Union[Unset, list['ValidationNotificationTemplate']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    validation_notification_templates: Union[Unset, list["ValidationNotificationTemplate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        validation_notification_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validation_notification_templates, Unset):
            validation_notification_templates = []
            for validation_notification_templates_item_data in self.validation_notification_templates:
                validation_notification_templates_item = validation_notification_templates_item_data.to_dict()
                validation_notification_templates.append(validation_notification_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if validation_notification_templates is not UNSET:
            field_dict["validationNotificationTemplates"] = validation_notification_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pager import Pager
        from ..models.validation_notification_template import ValidationNotificationTemplate

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        validation_notification_templates = []
        _validation_notification_templates = d.pop("validationNotificationTemplates", UNSET)
        for validation_notification_templates_item_data in _validation_notification_templates or []:
            validation_notification_templates_item = ValidationNotificationTemplate.from_dict(
                validation_notification_templates_item_data
            )

            validation_notification_templates.append(validation_notification_templates_item)

        validation_notification_template_get_object_list_response_200 = cls(
            pager=pager,
            validation_notification_templates=validation_notification_templates,
        )

        validation_notification_template_get_object_list_response_200.additional_properties = d
        return validation_notification_template_get_object_list_response_200

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
