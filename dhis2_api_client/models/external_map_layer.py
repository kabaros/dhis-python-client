import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.external_map_layer_image_format import ExternalMapLayerImageFormat
from ..models.external_map_layer_map_layer_position import ExternalMapLayerMapLayerPosition
from ..models.external_map_layer_map_service import ExternalMapLayerMapService
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.external_map_layer_created_by import ExternalMapLayerCreatedBy
    from ..models.external_map_layer_last_updated_by import ExternalMapLayerLastUpdatedBy
    from ..models.external_map_layer_legend_set import ExternalMapLayerLegendSet
    from ..models.external_map_layer_user import ExternalMapLayerUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ExternalMapLayer")


@_attrs_define
class ExternalMapLayer:
    """
    Attributes:
        image_format (ExternalMapLayerImageFormat):
        map_layer_position (ExternalMapLayerMapLayerPosition):
        map_service (ExternalMapLayerMapService):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        attribution (Union[Unset, str]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ExternalMapLayerCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ExternalMapLayerLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        layers (Union[Unset, str]):
        legend_set (Union[Unset, ExternalMapLayerLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_set_url (Union[Unset, str]):
        name (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        url (Union[Unset, str]):
        user (Union[Unset, ExternalMapLayerUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    image_format: ExternalMapLayerImageFormat
    map_layer_position: ExternalMapLayerMapLayerPosition
    map_service: ExternalMapLayerMapService
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    attribution: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ExternalMapLayerCreatedBy"] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ExternalMapLayerLastUpdatedBy"] = UNSET
    layers: Union[Unset, str] = UNSET
    legend_set: Union[Unset, "ExternalMapLayerLegendSet"] = UNSET
    legend_set_url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, "ExternalMapLayerUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_format = self.image_format.value

        map_layer_position = self.map_layer_position.value

        map_service = self.map_service.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        attribution = self.attribution

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

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

        layers = self.layers

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        legend_set_url = self.legend_set_url

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

        url = self.url

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "imageFormat": image_format,
                "mapLayerPosition": map_layer_position,
                "mapService": map_service,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if attribution is not UNSET:
            field_dict["attribution"] = attribution
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
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
        if layers is not UNSET:
            field_dict["layers"] = layers
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_set_url is not UNSET:
            field_dict["legendSetUrl"] = legend_set_url
        if name is not UNSET:
            field_dict["name"] = name
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.external_map_layer_created_by import ExternalMapLayerCreatedBy
        from ..models.external_map_layer_last_updated_by import ExternalMapLayerLastUpdatedBy
        from ..models.external_map_layer_legend_set import ExternalMapLayerLegendSet
        from ..models.external_map_layer_user import ExternalMapLayerUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        image_format = ExternalMapLayerImageFormat(d.pop("imageFormat"))

        map_layer_position = ExternalMapLayerMapLayerPosition(d.pop("mapLayerPosition"))

        map_service = ExternalMapLayerMapService(d.pop("mapService"))

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

        attribution = d.pop("attribution", UNSET)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ExternalMapLayerCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ExternalMapLayerCreatedBy.from_dict(_created_by)

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
        last_updated_by: Union[Unset, ExternalMapLayerLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ExternalMapLayerLastUpdatedBy.from_dict(_last_updated_by)

        layers = d.pop("layers", UNSET)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, ExternalMapLayerLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = ExternalMapLayerLegendSet.from_dict(_legend_set)

        legend_set_url = d.pop("legendSetUrl", UNSET)

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

        url = d.pop("url", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ExternalMapLayerUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ExternalMapLayerUser.from_dict(_user)

        external_map_layer = cls(
            image_format=image_format,
            map_layer_position=map_layer_position,
            map_service=map_service,
            access=access,
            attribute_values=attribute_values,
            attribution=attribution,
            code=code,
            created=created,
            created_by=created_by,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            layers=layers,
            legend_set=legend_set,
            legend_set_url=legend_set_url,
            name=name,
            sharing=sharing,
            translations=translations,
            url=url,
            user=user,
        )

        external_map_layer.additional_properties = d
        return external_map_layer

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
