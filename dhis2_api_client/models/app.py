from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_app_state import AppAppState
from ..models.app_app_storage_source import AppAppStorageSource
from ..models.app_app_type import AppAppType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_activities import AppActivities
    from ..models.app_developer import AppDeveloper
    from ..models.app_icons import AppIcons
    from ..models.app_settings import AppSettings


T = TypeVar("T", bound="App")


@_attrs_define
class App:
    """
    Attributes:
        app_state (AppAppState):
        app_storage_source (AppAppStorageSource):
        app_type (AppAppType):
        activities (Union[Unset, AppActivities]):
        app_hub_id (Union[Unset, str]):
        authorities (Union[Unset, list[str]]):
        base_url (Union[Unset, str]):
        bundled (Union[Unset, bool]):
        core_app (Union[Unset, bool]):
        default_locale (Union[Unset, str]):
        description (Union[Unset, str]):
        developer (Union[Unset, AppDeveloper]):
        folder_name (Union[Unset, str]):
        icons (Union[Unset, AppIcons]):
        installs_allowed_from (Union[Unset, list[str]]):
        key (Union[Unset, str]):
        launch_url (Union[Unset, str]):
        launch_path (Union[Unset, str]):
        name (Union[Unset, str]):
        plugin_launch_url (Union[Unset, str]):
        plugin_launch_path (Union[Unset, str]):
        plugin_type (Union[Unset, str]):
        settings (Union[Unset, AppSettings]):
        short_name (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    app_state: AppAppState
    app_storage_source: AppAppStorageSource
    app_type: AppAppType
    activities: Union[Unset, "AppActivities"] = UNSET
    app_hub_id: Union[Unset, str] = UNSET
    authorities: Union[Unset, list[str]] = UNSET
    base_url: Union[Unset, str] = UNSET
    bundled: Union[Unset, bool] = UNSET
    core_app: Union[Unset, bool] = UNSET
    default_locale: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    developer: Union[Unset, "AppDeveloper"] = UNSET
    folder_name: Union[Unset, str] = UNSET
    icons: Union[Unset, "AppIcons"] = UNSET
    installs_allowed_from: Union[Unset, list[str]] = UNSET
    key: Union[Unset, str] = UNSET
    launch_url: Union[Unset, str] = UNSET
    launch_path: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    plugin_launch_url: Union[Unset, str] = UNSET
    plugin_launch_path: Union[Unset, str] = UNSET
    plugin_type: Union[Unset, str] = UNSET
    settings: Union[Unset, "AppSettings"] = UNSET
    short_name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_state = self.app_state.value

        app_storage_source = self.app_storage_source.value

        app_type = self.app_type.value

        activities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activities, Unset):
            activities = self.activities.to_dict()

        app_hub_id = self.app_hub_id

        authorities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.authorities, Unset):
            authorities = self.authorities

        base_url = self.base_url

        bundled = self.bundled

        core_app = self.core_app

        default_locale = self.default_locale

        description = self.description

        developer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.developer, Unset):
            developer = self.developer.to_dict()

        folder_name = self.folder_name

        icons: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.icons, Unset):
            icons = self.icons.to_dict()

        installs_allowed_from: Union[Unset, list[str]] = UNSET
        if not isinstance(self.installs_allowed_from, Unset):
            installs_allowed_from = self.installs_allowed_from

        key = self.key

        launch_url = self.launch_url

        launch_path = self.launch_path

        name = self.name

        plugin_launch_url = self.plugin_launch_url

        plugin_launch_path = self.plugin_launch_path

        plugin_type = self.plugin_type

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        short_name = self.short_name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appState": app_state,
                "appStorageSource": app_storage_source,
                "appType": app_type,
            }
        )
        if activities is not UNSET:
            field_dict["activities"] = activities
        if app_hub_id is not UNSET:
            field_dict["app_hub_id"] = app_hub_id
        if authorities is not UNSET:
            field_dict["authorities"] = authorities
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if bundled is not UNSET:
            field_dict["bundled"] = bundled
        if core_app is not UNSET:
            field_dict["core_app"] = core_app
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if description is not UNSET:
            field_dict["description"] = description
        if developer is not UNSET:
            field_dict["developer"] = developer
        if folder_name is not UNSET:
            field_dict["folderName"] = folder_name
        if icons is not UNSET:
            field_dict["icons"] = icons
        if installs_allowed_from is not UNSET:
            field_dict["installs_allowed_from"] = installs_allowed_from
        if key is not UNSET:
            field_dict["key"] = key
        if launch_url is not UNSET:
            field_dict["launchUrl"] = launch_url
        if launch_path is not UNSET:
            field_dict["launch_path"] = launch_path
        if name is not UNSET:
            field_dict["name"] = name
        if plugin_launch_url is not UNSET:
            field_dict["pluginLaunchUrl"] = plugin_launch_url
        if plugin_launch_path is not UNSET:
            field_dict["plugin_launch_path"] = plugin_launch_path
        if plugin_type is not UNSET:
            field_dict["plugin_type"] = plugin_type
        if settings is not UNSET:
            field_dict["settings"] = settings
        if short_name is not UNSET:
            field_dict["short_name"] = short_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.app_activities import AppActivities
        from ..models.app_developer import AppDeveloper
        from ..models.app_icons import AppIcons
        from ..models.app_settings import AppSettings

        d = src_dict.copy()
        app_state = AppAppState(d.pop("appState"))

        app_storage_source = AppAppStorageSource(d.pop("appStorageSource"))

        app_type = AppAppType(d.pop("appType"))

        _activities = d.pop("activities", UNSET)
        activities: Union[Unset, AppActivities]
        if isinstance(_activities, Unset):
            activities = UNSET
        else:
            activities = AppActivities.from_dict(_activities)

        app_hub_id = d.pop("app_hub_id", UNSET)

        authorities = cast(list[str], d.pop("authorities", UNSET))

        base_url = d.pop("baseUrl", UNSET)

        bundled = d.pop("bundled", UNSET)

        core_app = d.pop("core_app", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        description = d.pop("description", UNSET)

        _developer = d.pop("developer", UNSET)
        developer: Union[Unset, AppDeveloper]
        if isinstance(_developer, Unset):
            developer = UNSET
        else:
            developer = AppDeveloper.from_dict(_developer)

        folder_name = d.pop("folderName", UNSET)

        _icons = d.pop("icons", UNSET)
        icons: Union[Unset, AppIcons]
        if isinstance(_icons, Unset):
            icons = UNSET
        else:
            icons = AppIcons.from_dict(_icons)

        installs_allowed_from = cast(list[str], d.pop("installs_allowed_from", UNSET))

        key = d.pop("key", UNSET)

        launch_url = d.pop("launchUrl", UNSET)

        launch_path = d.pop("launch_path", UNSET)

        name = d.pop("name", UNSET)

        plugin_launch_url = d.pop("pluginLaunchUrl", UNSET)

        plugin_launch_path = d.pop("plugin_launch_path", UNSET)

        plugin_type = d.pop("plugin_type", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, AppSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = AppSettings.from_dict(_settings)

        short_name = d.pop("short_name", UNSET)

        version = d.pop("version", UNSET)

        app = cls(
            app_state=app_state,
            app_storage_source=app_storage_source,
            app_type=app_type,
            activities=activities,
            app_hub_id=app_hub_id,
            authorities=authorities,
            base_url=base_url,
            bundled=bundled,
            core_app=core_app,
            default_locale=default_locale,
            description=description,
            developer=developer,
            folder_name=folder_name,
            icons=icons,
            installs_allowed_from=installs_allowed_from,
            key=key,
            launch_url=launch_url,
            launch_path=launch_path,
            name=name,
            plugin_launch_url=plugin_launch_url,
            plugin_launch_path=plugin_launch_path,
            plugin_type=plugin_type,
            settings=settings,
            short_name=short_name,
            version=version,
        )

        app.additional_properties = d
        return app

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
