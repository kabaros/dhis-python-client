import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.indicator_group_created_by import IndicatorGroupCreatedBy
    from ..models.indicator_group_group_sets_item import IndicatorGroupGroupSetsItem
    from ..models.indicator_group_indicator_group_set import IndicatorGroupIndicatorGroupSet
    from ..models.indicator_group_indicators_item import IndicatorGroupIndicatorsItem
    from ..models.indicator_group_last_updated_by import IndicatorGroupLastUpdatedBy
    from ..models.indicator_group_user import IndicatorGroupUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="IndicatorGroup")


@_attrs_define
class IndicatorGroup:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, IndicatorGroupCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        group_sets (Union[Unset, list['IndicatorGroupGroupSetsItem']]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        indicator_group_set (Union[Unset, IndicatorGroupIndicatorGroupSet]): A UID reference to a IndicatorGroupSet
            (Java name `org.hisp.dhis.indicator.IndicatorGroupSet`)
        indicators (Union[Unset, list['IndicatorGroupIndicatorsItem']]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, IndicatorGroupLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, IndicatorGroupUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "IndicatorGroupCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    group_sets: Union[Unset, list["IndicatorGroupGroupSetsItem"]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    indicator_group_set: Union[Unset, "IndicatorGroupIndicatorGroupSet"] = UNSET
    indicators: Union[Unset, list["IndicatorGroupIndicatorsItem"]] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "IndicatorGroupLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "IndicatorGroupUser"] = UNSET
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

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        display_name = self.display_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        group_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.group_sets, Unset):
            group_sets = []
            for group_sets_item_data in self.group_sets:
                group_sets_item = group_sets_item_data.to_dict()
                group_sets.append(group_sets_item)

        href = self.href

        id = self.id

        indicator_group_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.indicator_group_set, Unset):
            indicator_group_set = self.indicator_group_set.to_dict()

        indicators: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.indicators, Unset):
            indicators = []
            for indicators_item_data in self.indicators:
                indicators_item = indicators_item_data.to_dict()
                indicators.append(indicators_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if group_sets is not UNSET:
            field_dict["groupSets"] = group_sets
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if indicator_group_set is not UNSET:
            field_dict["indicatorGroupSet"] = indicator_group_set
        if indicators is not UNSET:
            field_dict["indicators"] = indicators
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.indicator_group_created_by import IndicatorGroupCreatedBy
        from ..models.indicator_group_group_sets_item import IndicatorGroupGroupSetsItem
        from ..models.indicator_group_indicator_group_set import IndicatorGroupIndicatorGroupSet
        from ..models.indicator_group_indicators_item import IndicatorGroupIndicatorsItem
        from ..models.indicator_group_last_updated_by import IndicatorGroupLastUpdatedBy
        from ..models.indicator_group_user import IndicatorGroupUser
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

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, IndicatorGroupCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = IndicatorGroupCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        group_sets = []
        _group_sets = d.pop("groupSets", UNSET)
        for group_sets_item_data in _group_sets or []:
            group_sets_item = IndicatorGroupGroupSetsItem.from_dict(group_sets_item_data)

            group_sets.append(group_sets_item)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _indicator_group_set = d.pop("indicatorGroupSet", UNSET)
        indicator_group_set: Union[Unset, IndicatorGroupIndicatorGroupSet]
        if isinstance(_indicator_group_set, Unset):
            indicator_group_set = UNSET
        else:
            indicator_group_set = IndicatorGroupIndicatorGroupSet.from_dict(_indicator_group_set)

        indicators = []
        _indicators = d.pop("indicators", UNSET)
        for indicators_item_data in _indicators or []:
            indicators_item = IndicatorGroupIndicatorsItem.from_dict(indicators_item_data)

            indicators.append(indicators_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, IndicatorGroupLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = IndicatorGroupLastUpdatedBy.from_dict(_last_updated_by)

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
        user: Union[Unset, IndicatorGroupUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = IndicatorGroupUser.from_dict(_user)

        indicator_group = cls(
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            group_sets=group_sets,
            href=href,
            id=id,
            indicator_group_set=indicator_group_set,
            indicators=indicators,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            sharing=sharing,
            translations=translations,
            user=user,
        )

        indicator_group.additional_properties = d
        return indicator_group

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
