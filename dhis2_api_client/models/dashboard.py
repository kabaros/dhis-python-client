import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.dashboard_created_by import DashboardCreatedBy
    from ..models.dashboard_item import DashboardItem
    from ..models.dashboard_last_updated_by import DashboardLastUpdatedBy
    from ..models.dashboard_user import DashboardUser
    from ..models.item_config import ItemConfig
    from ..models.layout import Layout
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Dashboard")


@_attrs_define
class Dashboard:
    """
    Attributes:
        item_count (int):
        access (Union[Unset, Access]):
        allowed_filters (Union[Unset, list[str]]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, DashboardCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        dashboard_items (Union[Unset, list['DashboardItem']]):
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
        item_config (Union[Unset, ItemConfig]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, DashboardLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        layout (Union[Unset, Layout]):
        name (Union[Unset, str]):
        restrict_filters (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, DashboardUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    item_count: int
    access: Union[Unset, "Access"] = UNSET
    allowed_filters: Union[Unset, list[str]] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "DashboardCreatedBy"] = UNSET
    dashboard_items: Union[Unset, list["DashboardItem"]] = UNSET
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
    item_config: Union[Unset, "ItemConfig"] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "DashboardLastUpdatedBy"] = UNSET
    layout: Union[Unset, "Layout"] = UNSET
    name: Union[Unset, str] = UNSET
    restrict_filters: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "DashboardUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_count = self.item_count

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        allowed_filters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_filters, Unset):
            allowed_filters = self.allowed_filters

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

        dashboard_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dashboard_items, Unset):
            dashboard_items = []
            for dashboard_items_item_data in self.dashboard_items:
                dashboard_items_item = dashboard_items_item_data.to_dict()
                dashboard_items.append(dashboard_items_item)

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

        item_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item_config, Unset):
            item_config = self.item_config.to_dict()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        layout: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.layout, Unset):
            layout = self.layout.to_dict()

        name = self.name

        restrict_filters = self.restrict_filters

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

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
                "itemCount": item_count,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if allowed_filters is not UNSET:
            field_dict["allowedFilters"] = allowed_filters
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if dashboard_items is not UNSET:
            field_dict["dashboardItems"] = dashboard_items
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
        if item_config is not UNSET:
            field_dict["itemConfig"] = item_config
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if layout is not UNSET:
            field_dict["layout"] = layout
        if name is not UNSET:
            field_dict["name"] = name
        if restrict_filters is not UNSET:
            field_dict["restrictFilters"] = restrict_filters
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.dashboard_created_by import DashboardCreatedBy
        from ..models.dashboard_item import DashboardItem
        from ..models.dashboard_last_updated_by import DashboardLastUpdatedBy
        from ..models.dashboard_user import DashboardUser
        from ..models.item_config import ItemConfig
        from ..models.layout import Layout
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        item_count = d.pop("itemCount")

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        allowed_filters = cast(list[str], d.pop("allowedFilters", UNSET))

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
        created_by: Union[Unset, DashboardCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = DashboardCreatedBy.from_dict(_created_by)

        dashboard_items = []
        _dashboard_items = d.pop("dashboardItems", UNSET)
        for dashboard_items_item_data in _dashboard_items or []:
            dashboard_items_item = DashboardItem.from_dict(dashboard_items_item_data)

            dashboard_items.append(dashboard_items_item)

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

        _item_config = d.pop("itemConfig", UNSET)
        item_config: Union[Unset, ItemConfig]
        if isinstance(_item_config, Unset):
            item_config = UNSET
        else:
            item_config = ItemConfig.from_dict(_item_config)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, DashboardLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = DashboardLastUpdatedBy.from_dict(_last_updated_by)

        _layout = d.pop("layout", UNSET)
        layout: Union[Unset, Layout]
        if isinstance(_layout, Unset):
            layout = UNSET
        else:
            layout = Layout.from_dict(_layout)

        name = d.pop("name", UNSET)

        restrict_filters = d.pop("restrictFilters", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, DashboardUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = DashboardUser.from_dict(_user)

        dashboard = cls(
            item_count=item_count,
            access=access,
            allowed_filters=allowed_filters,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            dashboard_items=dashboard_items,
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
            item_config=item_config,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            layout=layout,
            name=name,
            restrict_filters=restrict_filters,
            sharing=sharing,
            short_name=short_name,
            translations=translations,
            user=user,
        )

        dashboard.additional_properties = d
        return dashboard

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
