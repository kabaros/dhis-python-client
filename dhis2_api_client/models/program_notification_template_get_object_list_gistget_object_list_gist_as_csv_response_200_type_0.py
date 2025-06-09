from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_pager import GistPager
    from ..models.program_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_notification_templates_item import (
        ProgramNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramNotificationTemplatesItem,
    )


T = TypeVar("T", bound="ProgramNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0")


@_attrs_define
class ProgramNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0:
    """
    Attributes:
        pager (Union[Unset, GistPager]):
        program_notification_templates (Union[Unset, list['ProgramNotificationTemplateGetObjectListGistgetObjectListGist
            AsCsvResponse200Type0ProgramNotificationTemplatesItem']]):
    """

    pager: Union[Unset, "GistPager"] = UNSET
    program_notification_templates: Union[
        Unset,
        list[
            "ProgramNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramNotificationTemplatesItem"
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        program_notification_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_notification_templates, Unset):
            program_notification_templates = []
            for program_notification_templates_item_data in self.program_notification_templates:
                program_notification_templates_item = program_notification_templates_item_data.to_dict()
                program_notification_templates.append(program_notification_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if program_notification_templates is not UNSET:
            field_dict["programNotificationTemplates"] = program_notification_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_pager import GistPager
        from ..models.program_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0_program_notification_templates_item import (
            ProgramNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramNotificationTemplatesItem,
        )

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, GistPager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = GistPager.from_dict(_pager)

        program_notification_templates = []
        _program_notification_templates = d.pop("programNotificationTemplates", UNSET)
        for program_notification_templates_item_data in _program_notification_templates or []:
            program_notification_templates_item = ProgramNotificationTemplateGetObjectListGistgetObjectListGistAsCsvResponse200Type0ProgramNotificationTemplatesItem.from_dict(
                program_notification_templates_item_data
            )

            program_notification_templates.append(program_notification_templates_item)

        program_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 = cls(
            pager=pager,
            program_notification_templates=program_notification_templates,
        )

        program_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0.additional_properties = d
        return program_notification_template_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0

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
