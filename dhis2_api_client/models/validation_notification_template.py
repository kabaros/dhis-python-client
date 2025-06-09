import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.validation_notification_template_send_strategy import ValidationNotificationTemplateSendStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.validation_notification_template_created_by import ValidationNotificationTemplateCreatedBy
    from ..models.validation_notification_template_last_updated_by import ValidationNotificationTemplateLastUpdatedBy
    from ..models.validation_notification_template_recipient_user_groups_item import (
        ValidationNotificationTemplateRecipientUserGroupsItem,
    )
    from ..models.validation_notification_template_user import ValidationNotificationTemplateUser
    from ..models.validation_notification_template_validation_rules_item import (
        ValidationNotificationTemplateValidationRulesItem,
    )


T = TypeVar("T", bound="ValidationNotificationTemplate")


@_attrs_define
class ValidationNotificationTemplate:
    """
    Attributes:
        send_strategy (ValidationNotificationTemplateSendStrategy):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ValidationNotificationTemplateCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        display_message_template (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_subject_template (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ValidationNotificationTemplateLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        message_template (Union[Unset, str]):
        name (Union[Unset, str]):
        notify_parent_organisation_unit_only (Union[Unset, bool]):
        notify_users_in_hierarchy_only (Union[Unset, bool]):
        recipient_user_groups (Union[Unset, list['ValidationNotificationTemplateRecipientUserGroupsItem']]):
        sharing (Union[Unset, Sharing]):
        subject_template (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ValidationNotificationTemplateUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        validation_rules (Union[Unset, list['ValidationNotificationTemplateValidationRulesItem']]):
    """

    send_strategy: ValidationNotificationTemplateSendStrategy
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ValidationNotificationTemplateCreatedBy"] = UNSET
    display_message_template: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_subject_template: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ValidationNotificationTemplateLastUpdatedBy"] = UNSET
    message_template: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notify_parent_organisation_unit_only: Union[Unset, bool] = UNSET
    notify_users_in_hierarchy_only: Union[Unset, bool] = UNSET
    recipient_user_groups: Union[Unset, list["ValidationNotificationTemplateRecipientUserGroupsItem"]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    subject_template: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ValidationNotificationTemplateUser"] = UNSET
    validation_rules: Union[Unset, list["ValidationNotificationTemplateValidationRulesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        send_strategy = self.send_strategy.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        display_message_template = self.display_message_template

        display_name = self.display_name

        display_subject_template = self.display_subject_template

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        message_template = self.message_template

        name = self.name

        notify_parent_organisation_unit_only = self.notify_parent_organisation_unit_only

        notify_users_in_hierarchy_only = self.notify_users_in_hierarchy_only

        recipient_user_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recipient_user_groups, Unset):
            recipient_user_groups = []
            for recipient_user_groups_item_data in self.recipient_user_groups:
                recipient_user_groups_item = recipient_user_groups_item_data.to_dict()
                recipient_user_groups.append(recipient_user_groups_item)

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        subject_template = self.subject_template

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        validation_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validation_rules, Unset):
            validation_rules = []
            for validation_rules_item_data in self.validation_rules:
                validation_rules_item = validation_rules_item_data.to_dict()
                validation_rules.append(validation_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sendStrategy": send_strategy,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if display_message_template is not UNSET:
            field_dict["displayMessageTemplate"] = display_message_template
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_subject_template is not UNSET:
            field_dict["displaySubjectTemplate"] = display_subject_template
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if message_template is not UNSET:
            field_dict["messageTemplate"] = message_template
        if name is not UNSET:
            field_dict["name"] = name
        if notify_parent_organisation_unit_only is not UNSET:
            field_dict["notifyParentOrganisationUnitOnly"] = notify_parent_organisation_unit_only
        if notify_users_in_hierarchy_only is not UNSET:
            field_dict["notifyUsersInHierarchyOnly"] = notify_users_in_hierarchy_only
        if recipient_user_groups is not UNSET:
            field_dict["recipientUserGroups"] = recipient_user_groups
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if subject_template is not UNSET:
            field_dict["subjectTemplate"] = subject_template
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if validation_rules is not UNSET:
            field_dict["validationRules"] = validation_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.validation_notification_template_created_by import ValidationNotificationTemplateCreatedBy
        from ..models.validation_notification_template_last_updated_by import (
            ValidationNotificationTemplateLastUpdatedBy,
        )
        from ..models.validation_notification_template_recipient_user_groups_item import (
            ValidationNotificationTemplateRecipientUserGroupsItem,
        )
        from ..models.validation_notification_template_user import ValidationNotificationTemplateUser
        from ..models.validation_notification_template_validation_rules_item import (
            ValidationNotificationTemplateValidationRulesItem,
        )

        d = src_dict.copy()
        send_strategy = ValidationNotificationTemplateSendStrategy(d.pop("sendStrategy"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ValidationNotificationTemplateCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ValidationNotificationTemplateCreatedBy.from_dict(_created_by)

        display_message_template = d.pop("displayMessageTemplate", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_subject_template = d.pop("displaySubjectTemplate", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ValidationNotificationTemplateLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ValidationNotificationTemplateLastUpdatedBy.from_dict(_last_updated_by)

        message_template = d.pop("messageTemplate", UNSET)

        name = d.pop("name", UNSET)

        notify_parent_organisation_unit_only = d.pop("notifyParentOrganisationUnitOnly", UNSET)

        notify_users_in_hierarchy_only = d.pop("notifyUsersInHierarchyOnly", UNSET)

        recipient_user_groups = []
        _recipient_user_groups = d.pop("recipientUserGroups", UNSET)
        for recipient_user_groups_item_data in _recipient_user_groups or []:
            recipient_user_groups_item = ValidationNotificationTemplateRecipientUserGroupsItem.from_dict(
                recipient_user_groups_item_data
            )

            recipient_user_groups.append(recipient_user_groups_item)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        subject_template = d.pop("subjectTemplate", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ValidationNotificationTemplateUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ValidationNotificationTemplateUser.from_dict(_user)

        validation_rules = []
        _validation_rules = d.pop("validationRules", UNSET)
        for validation_rules_item_data in _validation_rules or []:
            validation_rules_item = ValidationNotificationTemplateValidationRulesItem.from_dict(
                validation_rules_item_data
            )

            validation_rules.append(validation_rules_item)

        validation_notification_template = cls(
            send_strategy=send_strategy,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            display_message_template=display_message_template,
            display_name=display_name,
            display_subject_template=display_subject_template,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            message_template=message_template,
            name=name,
            notify_parent_organisation_unit_only=notify_parent_organisation_unit_only,
            notify_users_in_hierarchy_only=notify_users_in_hierarchy_only,
            recipient_user_groups=recipient_user_groups,
            sharing=sharing,
            subject_template=subject_template,
            translations=translations,
            user=user,
            validation_rules=validation_rules,
        )

        validation_notification_template.additional_properties = d
        return validation_notification_template

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
