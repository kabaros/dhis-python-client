import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.push_analysis_created_by import PushAnalysisCreatedBy
    from ..models.push_analysis_dashboard import PushAnalysisDashboard
    from ..models.push_analysis_last_updated_by import PushAnalysisLastUpdatedBy
    from ..models.push_analysis_recipient_user_groups_item import PushAnalysisRecipientUserGroupsItem
    from ..models.push_analysis_user import PushAnalysisUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="PushAnalysis")


@_attrs_define
class PushAnalysis:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, PushAnalysisCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        dashboard (Union[Unset, PushAnalysisDashboard]): A UID reference to a Dashboard
            (Java name `org.hisp.dhis.dashboard.Dashboard`)
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, PushAnalysisLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        message (Union[Unset, str]):
        name (Union[Unset, str]):
        recipient_user_groups (Union[Unset, list['PushAnalysisRecipientUserGroupsItem']]):
        sharing (Union[Unset, Sharing]):
        title (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, PushAnalysisUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "PushAnalysisCreatedBy"] = UNSET
    dashboard: Union[Unset, "PushAnalysisDashboard"] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "PushAnalysisLastUpdatedBy"] = UNSET
    message: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    recipient_user_groups: Union[Unset, list["PushAnalysisRecipientUserGroupsItem"]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    title: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "PushAnalysisUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        dashboard: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dashboard, Unset):
            dashboard = self.dashboard.to_dict()

        display_name = self.display_name

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

        message = self.message

        name = self.name

        recipient_user_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recipient_user_groups, Unset):
            recipient_user_groups = []
            for recipient_user_groups_item_data in self.recipient_user_groups:
                recipient_user_groups_item = recipient_user_groups_item_data.to_dict()
                recipient_user_groups.append(recipient_user_groups_item)

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        title = self.title

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
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
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if recipient_user_groups is not UNSET:
            field_dict["recipientUserGroups"] = recipient_user_groups
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if title is not UNSET:
            field_dict["title"] = title
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.push_analysis_created_by import PushAnalysisCreatedBy
        from ..models.push_analysis_dashboard import PushAnalysisDashboard
        from ..models.push_analysis_last_updated_by import PushAnalysisLastUpdatedBy
        from ..models.push_analysis_recipient_user_groups_item import PushAnalysisRecipientUserGroupsItem
        from ..models.push_analysis_user import PushAnalysisUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
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
        created_by: Union[Unset, PushAnalysisCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = PushAnalysisCreatedBy.from_dict(_created_by)

        _dashboard = d.pop("dashboard", UNSET)
        dashboard: Union[Unset, PushAnalysisDashboard]
        if isinstance(_dashboard, Unset):
            dashboard = UNSET
        else:
            dashboard = PushAnalysisDashboard.from_dict(_dashboard)

        display_name = d.pop("displayName", UNSET)

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
        last_updated_by: Union[Unset, PushAnalysisLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = PushAnalysisLastUpdatedBy.from_dict(_last_updated_by)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        recipient_user_groups = []
        _recipient_user_groups = d.pop("recipientUserGroups", UNSET)
        for recipient_user_groups_item_data in _recipient_user_groups or []:
            recipient_user_groups_item = PushAnalysisRecipientUserGroupsItem.from_dict(recipient_user_groups_item_data)

            recipient_user_groups.append(recipient_user_groups_item)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        title = d.pop("title", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, PushAnalysisUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PushAnalysisUser.from_dict(_user)

        push_analysis = cls(
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            dashboard=dashboard,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            message=message,
            name=name,
            recipient_user_groups=recipient_user_groups,
            sharing=sharing,
            title=title,
            translations=translations,
            user=user,
        )

        push_analysis.additional_properties = d
        return push_analysis

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
