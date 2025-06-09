from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.validation_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_validation_notification_templates_item import (
        ValidationNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ValidationNotificationTemplatesItem,
    )


T = TypeVar("T", bound="ValidationNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class ValidationNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        validation_notification_templates (Union[Unset, list['ValidationNotificationTemplateGetObjectListGistgetObjectLi
            stGistAsCsvResponse200Type0ValidationNotificationTemplatesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    validation_notification_templates: Union[
        Unset,
        list[
            "ValidationNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ValidationNotificationTemplatesItem"
        ],
    ] = UNSET
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
        from ..models.gist_pager import GistPager
        from ..models.validation_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_validation_notification_templates_item import (
            ValidationNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ValidationNotificationTemplatesItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        validation_notification_templates = []
        _validation_notification_templates = d.pop("validationNotificationTemplates", UNSET)
        for validation_notification_templates_item_data in _validation_notification_templates or []:
            validation_notification_templates_item = ValidationNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ValidationNotificationTemplatesItem.from_dict(
                validation_notification_templates_item_data
            )

            validation_notification_templates.append(validation_notification_templates_item)

        validation_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            validation_notification_templates=validation_notification_templates,
        )

        validation_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return validation_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
