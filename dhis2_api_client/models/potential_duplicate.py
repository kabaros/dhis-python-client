import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.potential_duplicate_status import PotentialDuplicateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.potential_duplicate_created_by import PotentialDuplicateCreatedBy
    from ..models.potential_duplicate_last_updated_by import PotentialDuplicateLastUpdatedBy
    from ..models.potential_duplicate_user import PotentialDuplicateUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="PotentialDuplicate")


@_attrs_define
class PotentialDuplicate:
    """
    Attributes:
        status (PotentialDuplicateStatus):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, PotentialDuplicateCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        created_by_user_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        duplicate (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, PotentialDuplicateLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        last_updated_by_user_name (Union[Unset, str]):
        name (Union[Unset, str]):
        original (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, PotentialDuplicateUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    status: PotentialDuplicateStatus
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "PotentialDuplicateCreatedBy"] = UNSET
    created_by_user_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    duplicate: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "PotentialDuplicateLastUpdatedBy"] = UNSET
    last_updated_by_user_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    original: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "PotentialDuplicateUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

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

        created_by_user_name = self.created_by_user_name

        display_name = self.display_name

        duplicate = self.duplicate

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

        last_updated_by_user_name = self.last_updated_by_user_name

        name = self.name

        original = self.original

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
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
        if created_by_user_name is not UNSET:
            field_dict["createdByUserName"] = created_by_user_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if duplicate is not UNSET:
            field_dict["duplicate"] = duplicate
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
        if last_updated_by_user_name is not UNSET:
            field_dict["lastUpdatedByUserName"] = last_updated_by_user_name
        if name is not UNSET:
            field_dict["name"] = name
        if original is not UNSET:
            field_dict["original"] = original
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.potential_duplicate_created_by import PotentialDuplicateCreatedBy
        from ..models.potential_duplicate_last_updated_by import PotentialDuplicateLastUpdatedBy
        from ..models.potential_duplicate_user import PotentialDuplicateUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        status = PotentialDuplicateStatus(d.pop("status"))

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
        created_by: Union[Unset, PotentialDuplicateCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = PotentialDuplicateCreatedBy.from_dict(_created_by)

        created_by_user_name = d.pop("createdByUserName", UNSET)

        display_name = d.pop("displayName", UNSET)

        duplicate = d.pop("duplicate", UNSET)

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
        last_updated_by: Union[Unset, PotentialDuplicateLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = PotentialDuplicateLastUpdatedBy.from_dict(_last_updated_by)

        last_updated_by_user_name = d.pop("lastUpdatedByUserName", UNSET)

        name = d.pop("name", UNSET)

        original = d.pop("original", UNSET)

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
        user: Union[Unset, PotentialDuplicateUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PotentialDuplicateUser.from_dict(_user)

        potential_duplicate = cls(
            status=status,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            created_by_user_name=created_by_user_name,
            display_name=display_name,
            duplicate=duplicate,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            last_updated_by_user_name=last_updated_by_user_name,
            name=name,
            original=original,
            sharing=sharing,
            translations=translations,
            user=user,
        )

        potential_duplicate.additional_properties = d
        return potential_duplicate

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
