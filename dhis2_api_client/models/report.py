import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.report_cache_strategy import ReportCacheStrategy
from ..models.report_type import ReportType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.relative_periods import RelativePeriods
    from ..models.report_created_by import ReportCreatedBy
    from ..models.report_last_updated_by import ReportLastUpdatedBy
    from ..models.report_user import ReportUser
    from ..models.report_visualization import ReportVisualization
    from ..models.reporting_params import ReportingParams
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Report")


@_attrs_define
class Report:
    """
    Attributes:
        cache_strategy (ReportCacheStrategy):
        type_ (ReportType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ReportCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        design_content (Union[Unset, str]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ReportLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        relative_periods (Union[Unset, RelativePeriods]):
        report_params (Union[Unset, ReportingParams]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ReportUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        visualization (Union[Unset, ReportVisualization]): A UID reference to a Visualization
            (Java name `org.hisp.dhis.visualization.Visualization`)
    """

    cache_strategy: ReportCacheStrategy
    type_: ReportType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ReportCreatedBy"] = UNSET
    design_content: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ReportLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    relative_periods: Union[Unset, "RelativePeriods"] = UNSET
    report_params: Union[Unset, "ReportingParams"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ReportUser"] = UNSET
    visualization: Union[Unset, "ReportVisualization"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache_strategy = self.cache_strategy.value

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

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        design_content = self.design_content

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

        relative_periods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relative_periods, Unset):
            relative_periods = self.relative_periods.to_dict()

        report_params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.report_params, Unset):
            report_params = self.report_params.to_dict()

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

        visualization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.visualization, Unset):
            visualization = self.visualization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cacheStrategy": cache_strategy,
                "type": type_,
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
        if design_content is not UNSET:
            field_dict["designContent"] = design_content
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
        if relative_periods is not UNSET:
            field_dict["relativePeriods"] = relative_periods
        if report_params is not UNSET:
            field_dict["reportParams"] = report_params
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if visualization is not UNSET:
            field_dict["visualization"] = visualization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.relative_periods import RelativePeriods
        from ..models.report_created_by import ReportCreatedBy
        from ..models.report_last_updated_by import ReportLastUpdatedBy
        from ..models.report_user import ReportUser
        from ..models.report_visualization import ReportVisualization
        from ..models.reporting_params import ReportingParams
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        cache_strategy = ReportCacheStrategy(d.pop("cacheStrategy"))

        type_ = ReportType(d.pop("type"))

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
        created_by: Union[Unset, ReportCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ReportCreatedBy.from_dict(_created_by)

        design_content = d.pop("designContent", UNSET)

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
        last_updated_by: Union[Unset, ReportLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ReportLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _relative_periods = d.pop("relativePeriods", UNSET)
        relative_periods: Union[Unset, RelativePeriods]
        if isinstance(_relative_periods, Unset):
            relative_periods = UNSET
        else:
            relative_periods = RelativePeriods.from_dict(_relative_periods)

        _report_params = d.pop("reportParams", UNSET)
        report_params: Union[Unset, ReportingParams]
        if isinstance(_report_params, Unset):
            report_params = UNSET
        else:
            report_params = ReportingParams.from_dict(_report_params)

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
        user: Union[Unset, ReportUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ReportUser.from_dict(_user)

        _visualization = d.pop("visualization", UNSET)
        visualization: Union[Unset, ReportVisualization]
        if isinstance(_visualization, Unset):
            visualization = UNSET
        else:
            visualization = ReportVisualization.from_dict(_visualization)

        report = cls(
            cache_strategy=cache_strategy,
            type_=type_,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            design_content=design_content,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            relative_periods=relative_periods,
            report_params=report_params,
            sharing=sharing,
            translations=translations,
            user=user,
            visualization=visualization,
        )

        report.additional_properties = d
        return report

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
