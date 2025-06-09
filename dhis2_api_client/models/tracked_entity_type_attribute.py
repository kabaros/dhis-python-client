import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracked_entity_type_attribute_value_type import TrackedEntityTypeAttributeValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.sharing import Sharing
    from ..models.tracked_entity_type_attribute_created_by import TrackedEntityTypeAttributeCreatedBy
    from ..models.tracked_entity_type_attribute_last_updated_by import TrackedEntityTypeAttributeLastUpdatedBy
    from ..models.tracked_entity_type_attribute_tracked_entity_attribute import (
        TrackedEntityTypeAttributeTrackedEntityAttribute,
    )
    from ..models.tracked_entity_type_attribute_tracked_entity_type import TrackedEntityTypeAttributeTrackedEntityType
    from ..models.tracked_entity_type_attribute_user import TrackedEntityTypeAttributeUser
    from ..models.translation import Translation


T = TypeVar("T", bound="TrackedEntityTypeAttribute")


@_attrs_define
class TrackedEntityTypeAttribute:
    """
    Attributes:
        value_type (TrackedEntityTypeAttributeValueType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, TrackedEntityTypeAttributeCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        display_in_list (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, TrackedEntityTypeAttributeLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        mandatory (Union[Unset, bool]):
        searchable (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        tracked_entity_attribute (Union[Unset, TrackedEntityTypeAttributeTrackedEntityAttribute]): A UID reference to a
            TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        tracked_entity_type (Union[Unset, TrackedEntityTypeAttributeTrackedEntityType]): A UID reference to a
            TrackedEntityType
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityType`)
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, TrackedEntityTypeAttributeUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    value_type: TrackedEntityTypeAttributeValueType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "TrackedEntityTypeAttributeCreatedBy"] = UNSET
    display_in_list: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "TrackedEntityTypeAttributeLastUpdatedBy"] = UNSET
    mandatory: Union[Unset, bool] = UNSET
    searchable: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    tracked_entity_attribute: Union[Unset, "TrackedEntityTypeAttributeTrackedEntityAttribute"] = UNSET
    tracked_entity_type: Union[Unset, "TrackedEntityTypeAttributeTrackedEntityType"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "TrackedEntityTypeAttributeUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_type = self.value_type.value

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

        display_in_list = self.display_in_list

        display_name = self.display_name

        display_short_name = self.display_short_name

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

        mandatory = self.mandatory

        searchable = self.searchable

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        tracked_entity_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_attribute, Unset):
            tracked_entity_attribute = self.tracked_entity_attribute.to_dict()

        tracked_entity_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_type, Unset):
            tracked_entity_type = self.tracked_entity_type.to_dict()

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
                "valueType": value_type,
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
        if display_in_list is not UNSET:
            field_dict["displayInList"] = display_in_list
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
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
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if tracked_entity_attribute is not UNSET:
            field_dict["trackedEntityAttribute"] = tracked_entity_attribute
        if tracked_entity_type is not UNSET:
            field_dict["trackedEntityType"] = tracked_entity_type
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.sharing import Sharing
        from ..models.tracked_entity_type_attribute_created_by import TrackedEntityTypeAttributeCreatedBy
        from ..models.tracked_entity_type_attribute_last_updated_by import TrackedEntityTypeAttributeLastUpdatedBy
        from ..models.tracked_entity_type_attribute_tracked_entity_attribute import (
            TrackedEntityTypeAttributeTrackedEntityAttribute,
        )
        from ..models.tracked_entity_type_attribute_tracked_entity_type import (
            TrackedEntityTypeAttributeTrackedEntityType,
        )
        from ..models.tracked_entity_type_attribute_user import TrackedEntityTypeAttributeUser
        from ..models.translation import Translation

        d = src_dict.copy()
        value_type = TrackedEntityTypeAttributeValueType(d.pop("valueType"))

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
        created_by: Union[Unset, TrackedEntityTypeAttributeCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackedEntityTypeAttributeCreatedBy.from_dict(_created_by)

        display_in_list = d.pop("displayInList", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

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
        last_updated_by: Union[Unset, TrackedEntityTypeAttributeLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = TrackedEntityTypeAttributeLastUpdatedBy.from_dict(_last_updated_by)

        mandatory = d.pop("mandatory", UNSET)

        searchable = d.pop("searchable", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        _tracked_entity_attribute = d.pop("trackedEntityAttribute", UNSET)
        tracked_entity_attribute: Union[Unset, TrackedEntityTypeAttributeTrackedEntityAttribute]
        if isinstance(_tracked_entity_attribute, Unset):
            tracked_entity_attribute = UNSET
        else:
            tracked_entity_attribute = TrackedEntityTypeAttributeTrackedEntityAttribute.from_dict(
                _tracked_entity_attribute
            )

        _tracked_entity_type = d.pop("trackedEntityType", UNSET)
        tracked_entity_type: Union[Unset, TrackedEntityTypeAttributeTrackedEntityType]
        if isinstance(_tracked_entity_type, Unset):
            tracked_entity_type = UNSET
        else:
            tracked_entity_type = TrackedEntityTypeAttributeTrackedEntityType.from_dict(_tracked_entity_type)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, TrackedEntityTypeAttributeUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TrackedEntityTypeAttributeUser.from_dict(_user)

        tracked_entity_type_attribute = cls(
            value_type=value_type,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            display_in_list=display_in_list,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            mandatory=mandatory,
            searchable=searchable,
            sharing=sharing,
            tracked_entity_attribute=tracked_entity_attribute,
            tracked_entity_type=tracked_entity_type,
            translations=translations,
            user=user,
        )

        tracked_entity_type_attribute.additional_properties = d
        return tracked_entity_type_attribute

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
