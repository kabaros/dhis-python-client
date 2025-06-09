import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.api_token_type import ApiTokenType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.api_token_created_by import ApiTokenCreatedBy
    from ..models.api_token_last_updated_by import ApiTokenLastUpdatedBy
    from ..models.api_token_user import ApiTokenUser
    from ..models.attribute_value import AttributeValue
    from ..models.ip_allowed_list import IpAllowedList
    from ..models.method_allowed_list import MethodAllowedList
    from ..models.referer_allowed_list import RefererAllowedList
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ApiToken")


@_attrs_define
class ApiToken:
    """
    Attributes:
        type_ (ApiTokenType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        attributes (Union[Unset, list[Union['IpAllowedList', 'MethodAllowedList', 'RefererAllowedList']]]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ApiTokenCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        display_name (Union[Unset, str]):
        expire (Union[Unset, int]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ApiTokenLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ApiTokenUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        version (Union[Unset, int]):
    """

    type_: ApiTokenType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    attributes: Union[Unset, list[Union["IpAllowedList", "MethodAllowedList", "RefererAllowedList"]]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ApiTokenCreatedBy"] = UNSET
    display_name: Union[Unset, str] = UNSET
    expire: Union[Unset, int] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ApiTokenLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ApiTokenUser"] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ip_allowed_list import IpAllowedList
        from ..models.referer_allowed_list import RefererAllowedList

        type_ = self.type_.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item: dict[str, Any]
                if isinstance(attributes_item_data, IpAllowedList):
                    attributes_item = attributes_item_data.to_dict()
                elif isinstance(attributes_item_data, RefererAllowedList):
                    attributes_item = attributes_item_data.to_dict()
                else:
                    attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        display_name = self.display_name

        expire = self.expire

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

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if expire is not UNSET:
            field_dict["expire"] = expire
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
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.api_token_created_by import ApiTokenCreatedBy
        from ..models.api_token_last_updated_by import ApiTokenLastUpdatedBy
        from ..models.api_token_user import ApiTokenUser
        from ..models.attribute_value import AttributeValue
        from ..models.ip_allowed_list import IpAllowedList
        from ..models.method_allowed_list import MethodAllowedList
        from ..models.referer_allowed_list import RefererAllowedList
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        type_ = ApiTokenType(d.pop("type"))

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

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:

            def _parse_attributes_item(
                data: object,
            ) -> Union["IpAllowedList", "MethodAllowedList", "RefererAllowedList"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    attributes_item_type_0 = IpAllowedList.from_dict(data)

                    return attributes_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    attributes_item_type_1 = RefererAllowedList.from_dict(data)

                    return attributes_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_item_type_2 = MethodAllowedList.from_dict(data)

                return attributes_item_type_2

            attributes_item = _parse_attributes_item(attributes_item_data)

            attributes.append(attributes_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ApiTokenCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ApiTokenCreatedBy.from_dict(_created_by)

        display_name = d.pop("displayName", UNSET)

        expire = d.pop("expire", UNSET)

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
        last_updated_by: Union[Unset, ApiTokenLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ApiTokenLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

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
        user: Union[Unset, ApiTokenUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ApiTokenUser.from_dict(_user)

        version = d.pop("version", UNSET)

        api_token = cls(
            type_=type_,
            access=access,
            attribute_values=attribute_values,
            attributes=attributes,
            code=code,
            created=created,
            created_by=created_by,
            display_name=display_name,
            expire=expire,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            sharing=sharing,
            translations=translations,
            user=user,
            version=version,
        )

        api_token.additional_properties = d
        return api_token

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
