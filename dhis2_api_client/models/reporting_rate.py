import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reporting_rate_aggregation_type import ReportingRateAggregationType
from ..models.reporting_rate_metric import ReportingRateMetric
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.query_modifiers import QueryModifiers
    from ..models.reporting_rate_created_by import ReportingRateCreatedBy
    from ..models.reporting_rate_data_set import ReportingRateDataSet
    from ..models.reporting_rate_last_updated_by import ReportingRateLastUpdatedBy
    from ..models.reporting_rate_legend_set import ReportingRateLegendSet
    from ..models.reporting_rate_user import ReportingRateUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ReportingRate")


@_attrs_define
class ReportingRate:
    """
    Attributes:
        aggregation_type (ReportingRateAggregationType):
        metric (ReportingRateMetric):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ReportingRateCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_set (Union[Unset, ReportingRateDataSet]): A UID reference to a DataSet
            (Java name `org.hisp.dhis.dataset.DataSet`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ReportingRateLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, ReportingRateLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ReportingRateUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    aggregation_type: ReportingRateAggregationType
    metric: ReportingRateMetric
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ReportingRateCreatedBy"] = UNSET
    data_set: Union[Unset, "ReportingRateDataSet"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ReportingRateLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "ReportingRateLegendSet"] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ReportingRateUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        metric = self.metric.value

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

        data_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_set, Unset):
            data_set = self.data_set.to_dict()

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

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

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
                "aggregationType": aggregation_type,
                "metric": metric,
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
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
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
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
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
        from ..models.query_modifiers import QueryModifiers
        from ..models.reporting_rate_created_by import ReportingRateCreatedBy
        from ..models.reporting_rate_data_set import ReportingRateDataSet
        from ..models.reporting_rate_last_updated_by import ReportingRateLastUpdatedBy
        from ..models.reporting_rate_legend_set import ReportingRateLegendSet
        from ..models.reporting_rate_user import ReportingRateUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = ReportingRateAggregationType(d.pop("aggregationType"))

        metric = ReportingRateMetric(d.pop("metric"))

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
        created_by: Union[Unset, ReportingRateCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ReportingRateCreatedBy.from_dict(_created_by)

        _data_set = d.pop("dataSet", UNSET)
        data_set: Union[Unset, ReportingRateDataSet]
        if isinstance(_data_set, Unset):
            data_set = UNSET
        else:
            data_set = ReportingRateDataSet.from_dict(_data_set)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, ReportingRateLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ReportingRateLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, ReportingRateLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = ReportingRateLegendSet.from_dict(_legend_set)

        _query_mods = d.pop("queryMods", UNSET)
        query_mods: Union[Unset, QueryModifiers]
        if isinstance(_query_mods, Unset):
            query_mods = UNSET
        else:
            query_mods = QueryModifiers.from_dict(_query_mods)

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
        user: Union[Unset, ReportingRateUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ReportingRateUser.from_dict(_user)

        reporting_rate = cls(
            aggregation_type=aggregation_type,
            metric=metric,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            data_set=data_set,
            description=description,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            href=href,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            query_mods=query_mods,
            sharing=sharing,
            translations=translations,
            user=user,
        )

        reporting_rate.additional_properties = d
        return reporting_rate

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
