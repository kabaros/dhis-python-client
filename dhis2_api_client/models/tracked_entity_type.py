import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.tracked_entity_type_feature_type import TrackedEntityTypeFeatureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.object_style import ObjectStyle
    from ..models.sharing import Sharing
    from ..models.tracked_entity_type_attribute import TrackedEntityTypeAttribute
    from ..models.tracked_entity_type_created_by import TrackedEntityTypeCreatedBy
    from ..models.tracked_entity_type_last_updated_by import TrackedEntityTypeLastUpdatedBy
    from ..models.tracked_entity_type_user import TrackedEntityTypeUser
    from ..models.translation import Translation


T = TypeVar("T", bound="TrackedEntityType")


@_attrs_define
class TrackedEntityType:
    """
    Attributes:
        feature_type (TrackedEntityTypeFeatureType):
        max_tei_count_to_return (int):
        min_attributes_required_to_search (int):
        access (Union[Unset, Access]):
        allow_audit_log (Union[Unset, bool]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, TrackedEntityTypeCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, TrackedEntityTypeLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        style (Union[Unset, ObjectStyle]):
        tracked_entity_type_attributes (Union[Unset, list['TrackedEntityTypeAttribute']]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, TrackedEntityTypeUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    feature_type: TrackedEntityTypeFeatureType
    max_tei_count_to_return: int
    min_attributes_required_to_search: int
    access: Union[Unset, "Access"] = UNSET
    allow_audit_log: Union[Unset, bool] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "TrackedEntityTypeCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "TrackedEntityTypeLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    tracked_entity_type_attributes: Union[Unset, list["TrackedEntityTypeAttribute"]] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "TrackedEntityTypeUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_type = self.feature_type.value

        max_tei_count_to_return = self.max_tei_count_to_return

        min_attributes_required_to_search = self.min_attributes_required_to_search

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        allow_audit_log = self.allow_audit_log

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

        description = self.description

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        tracked_entity_type_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracked_entity_type_attributes, Unset):
            tracked_entity_type_attributes = []
            for tracked_entity_type_attributes_item_data in self.tracked_entity_type_attributes:
                tracked_entity_type_attributes_item = tracked_entity_type_attributes_item_data.to_dict()
                tracked_entity_type_attributes.append(tracked_entity_type_attributes_item)

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
                "featureType": feature_type,
                "maxTeiCountToReturn": max_tei_count_to_return,
                "minAttributesRequiredToSearch": min_attributes_required_to_search,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if allow_audit_log is not UNSET:
            field_dict["allowAuditLog"] = allow_audit_log
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if form_name is not UNSET:
            field_dict["formName"] = form_name
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
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if style is not UNSET:
            field_dict["style"] = style
        if tracked_entity_type_attributes is not UNSET:
            field_dict["trackedEntityTypeAttributes"] = tracked_entity_type_attributes
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.object_style import ObjectStyle
        from ..models.sharing import Sharing
        from ..models.tracked_entity_type_attribute import TrackedEntityTypeAttribute
        from ..models.tracked_entity_type_created_by import TrackedEntityTypeCreatedBy
        from ..models.tracked_entity_type_last_updated_by import TrackedEntityTypeLastUpdatedBy
        from ..models.tracked_entity_type_user import TrackedEntityTypeUser
        from ..models.translation import Translation

        d = src_dict.copy()
        feature_type = TrackedEntityTypeFeatureType(d.pop("featureType"))

        max_tei_count_to_return = d.pop("maxTeiCountToReturn")

        min_attributes_required_to_search = d.pop("minAttributesRequiredToSearch")

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        allow_audit_log = d.pop("allowAuditLog", UNSET)

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
        created_by: Union[Unset, TrackedEntityTypeCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = TrackedEntityTypeCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, TrackedEntityTypeLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = TrackedEntityTypeLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        _style = d.pop("style", UNSET)
        style: Union[Unset, ObjectStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ObjectStyle.from_dict(_style)

        tracked_entity_type_attributes = []
        _tracked_entity_type_attributes = d.pop("trackedEntityTypeAttributes", UNSET)
        for tracked_entity_type_attributes_item_data in _tracked_entity_type_attributes or []:
            tracked_entity_type_attributes_item = TrackedEntityTypeAttribute.from_dict(
                tracked_entity_type_attributes_item_data
            )

            tracked_entity_type_attributes.append(tracked_entity_type_attributes_item)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, TrackedEntityTypeUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = TrackedEntityTypeUser.from_dict(_user)

        tracked_entity_type = cls(
            feature_type=feature_type,
            max_tei_count_to_return=max_tei_count_to_return,
            min_attributes_required_to_search=min_attributes_required_to_search,
            access=access,
            allow_audit_log=allow_audit_log,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            sharing=sharing,
            short_name=short_name,
            style=style,
            tracked_entity_type_attributes=tracked_entity_type_attributes,
            translations=translations,
            user=user,
        )

        tracked_entity_type.additional_properties = d
        return tracked_entity_type

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
