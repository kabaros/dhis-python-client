import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.user_role_created_by import UserRoleCreatedBy
    from ..models.user_role_last_updated_by import UserRoleLastUpdatedBy
    from ..models.user_role_user import UserRoleUser
    from ..models.user_role_users_item import UserRoleUsersItem


T = TypeVar("T", bound="UserRole")


@_attrs_define
class UserRole:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        authorities (Union[Unset, list[str]]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, UserRoleCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, UserRoleLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        restrictions (Union[Unset, list[str]]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, UserRoleUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        users (Union[Unset, list['UserRoleUsersItem']]):
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    authorities: Union[Unset, list[str]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "UserRoleCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "UserRoleLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    restrictions: Union[Unset, list[str]] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "UserRoleUser"] = UNSET
    users: Union[Unset, list["UserRoleUsersItem"]] = UNSET
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

        authorities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.authorities, Unset):
            authorities = self.authorities

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

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

        name = self.name

        restrictions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if authorities is not UNSET:
            field_dict["authorities"] = authorities
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
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
        if name is not UNSET:
            field_dict["name"] = name
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.user_role_created_by import UserRoleCreatedBy
        from ..models.user_role_last_updated_by import UserRoleLastUpdatedBy
        from ..models.user_role_user import UserRoleUser
        from ..models.user_role_users_item import UserRoleUsersItem

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

        authorities = cast(list[str], d.pop("authorities", UNSET))

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, UserRoleCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserRoleCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

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
        last_updated_by: Union[Unset, UserRoleLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = UserRoleLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        restrictions = cast(list[str], d.pop("restrictions", UNSET))

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserRoleUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserRoleUser.from_dict(_user)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = UserRoleUsersItem.from_dict(users_item_data)

            users.append(users_item)

        user_role = cls(
            access=access,
            attribute_values=attribute_values,
            authorities=authorities,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            restrictions=restrictions,
            sharing=sharing,
            translations=translations,
            user=user,
            users=users,
        )

        user_role.additional_properties = d
        return user_role

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
