import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.map_created_by import MapCreatedBy
    from ..models.map_interpretations_item import MapInterpretationsItem
    from ..models.map_last_updated_by import MapLastUpdatedBy
    from ..models.map_user import MapUser
    from ..models.map_view import MapView
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Map")


@_attrs_define
class Map:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        basemap (Union[Unset, str]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, MapCreatedBy]): A UID reference to a User
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
        interpretations (Union[Unset, list['MapInterpretationsItem']]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, MapLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        latitude (Union[Unset, float]):
        longitude (Union[Unset, float]):
        map_views (Union[Unset, list['MapView']]):
        name (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        subscribed (Union[Unset, bool]):
        subscribers (Union[Unset, list[str]]):
        title (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, MapUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        zoom (Union[Unset, int]):
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    basemap: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "MapCreatedBy"] = UNSET
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
    interpretations: Union[Unset, list["MapInterpretationsItem"]] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "MapLastUpdatedBy"] = UNSET
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    map_views: Union[Unset, list["MapView"]] = UNSET
    name: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    subscribed: Union[Unset, bool] = UNSET
    subscribers: Union[Unset, list[str]] = UNSET
    title: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "MapUser"] = UNSET
    zoom: Union[Unset, int] = UNSET
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

        basemap = self.basemap

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

        interpretations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interpretations, Unset):
            interpretations = []
            for interpretations_item_data in self.interpretations:
                interpretations_item = interpretations_item_data.to_dict()
                interpretations.append(interpretations_item)

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        latitude = self.latitude

        longitude = self.longitude

        map_views: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.map_views, Unset):
            map_views = []
            for map_views_item_data in self.map_views:
                map_views_item = map_views_item_data.to_dict()
                map_views.append(map_views_item)

        name = self.name

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        subscribed = self.subscribed

        subscribers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscribers, Unset):
            subscribers = self.subscribers

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

        zoom = self.zoom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if basemap is not UNSET:
            field_dict["basemap"] = basemap
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
        if interpretations is not UNSET:
            field_dict["interpretations"] = interpretations
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if map_views is not UNSET:
            field_dict["mapViews"] = map_views
        if name is not UNSET:
            field_dict["name"] = name
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if subscribers is not UNSET:
            field_dict["subscribers"] = subscribers
        if title is not UNSET:
            field_dict["title"] = title
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if zoom is not UNSET:
            field_dict["zoom"] = zoom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.map_created_by import MapCreatedBy
        from ..models.map_interpretations_item import MapInterpretationsItem
        from ..models.map_last_updated_by import MapLastUpdatedBy
        from ..models.map_user import MapUser
        from ..models.map_view import MapView
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

        basemap = d.pop("basemap", UNSET)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, MapCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = MapCreatedBy.from_dict(_created_by)

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

        interpretations = []
        _interpretations = d.pop("interpretations", UNSET)
        for interpretations_item_data in _interpretations or []:
            interpretations_item = MapInterpretationsItem.from_dict(interpretations_item_data)

            interpretations.append(interpretations_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, MapLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = MapLastUpdatedBy.from_dict(_last_updated_by)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        map_views = []
        _map_views = d.pop("mapViews", UNSET)
        for map_views_item_data in _map_views or []:
            map_views_item = MapView.from_dict(map_views_item_data)

            map_views.append(map_views_item)

        name = d.pop("name", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        subscribers = cast(list[str], d.pop("subscribers", UNSET))

        title = d.pop("title", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, MapUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = MapUser.from_dict(_user)

        zoom = d.pop("zoom", UNSET)

        map_ = cls(
            access=access,
            attribute_values=attribute_values,
            basemap=basemap,
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
            interpretations=interpretations,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            latitude=latitude,
            longitude=longitude,
            map_views=map_views,
            name=name,
            sharing=sharing,
            short_name=short_name,
            subscribed=subscribed,
            subscribers=subscribers,
            title=title,
            translations=translations,
            user=user,
            zoom=zoom,
        )

        map_.additional_properties = d
        return map_

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
