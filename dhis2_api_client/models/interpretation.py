import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.interpretation_type import InterpretationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.interpretation_comments_item import InterpretationCommentsItem
    from ..models.interpretation_created_by import InterpretationCreatedBy
    from ..models.interpretation_data_set import InterpretationDataSet
    from ..models.interpretation_event_chart import InterpretationEventChart
    from ..models.interpretation_event_report import InterpretationEventReport
    from ..models.interpretation_event_visualization import InterpretationEventVisualization
    from ..models.interpretation_last_updated_by import InterpretationLastUpdatedBy
    from ..models.interpretation_liked_by_item import InterpretationLikedByItem
    from ..models.interpretation_map import InterpretationMap
    from ..models.interpretation_organisation_unit import InterpretationOrganisationUnit
    from ..models.interpretation_user import InterpretationUser
    from ..models.interpretation_visualization import InterpretationVisualization
    from ..models.mention import Mention
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Interpretation")


@_attrs_define
class Interpretation:
    """
    Attributes:
        likes (int):
        type_ (InterpretationType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        comments (Union[Unset, list['InterpretationCommentsItem']]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, InterpretationCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_set (Union[Unset, InterpretationDataSet]): A UID reference to a DataSet
            (Java name `org.hisp.dhis.dataset.DataSet`)
        display_name (Union[Unset, str]):
        event_chart (Union[Unset, InterpretationEventChart]): A UID reference to a EventChart
            (Java name `org.hisp.dhis.eventchart.EventChart`)
        event_report (Union[Unset, InterpretationEventReport]): A UID reference to a EventReport
            (Java name `org.hisp.dhis.eventreport.EventReport`)
        event_visualization (Union[Unset, InterpretationEventVisualization]): A UID reference to a EventVisualization
            (Java name `org.hisp.dhis.eventvisualization.EventVisualization`)
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, InterpretationLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        liked_by (Union[Unset, list['InterpretationLikedByItem']]):
        map_ (Union[Unset, InterpretationMap]): A UID reference to a Map
            (Java name `org.hisp.dhis.mapping.Map`)
        mentions (Union[Unset, list['Mention']]):
        organisation_unit (Union[Unset, InterpretationOrganisationUnit]): A UID reference to a OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        period (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        text (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, InterpretationUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        visualization (Union[Unset, InterpretationVisualization]): A UID reference to a Visualization
            (Java name `org.hisp.dhis.visualization.Visualization`)
    """

    likes: int
    type_: InterpretationType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    comments: Union[Unset, list["InterpretationCommentsItem"]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "InterpretationCreatedBy"] = UNSET
    data_set: Union[Unset, "InterpretationDataSet"] = UNSET
    display_name: Union[Unset, str] = UNSET
    event_chart: Union[Unset, "InterpretationEventChart"] = UNSET
    event_report: Union[Unset, "InterpretationEventReport"] = UNSET
    event_visualization: Union[Unset, "InterpretationEventVisualization"] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "InterpretationLastUpdatedBy"] = UNSET
    liked_by: Union[Unset, list["InterpretationLikedByItem"]] = UNSET
    map_: Union[Unset, "InterpretationMap"] = UNSET
    mentions: Union[Unset, list["Mention"]] = UNSET
    organisation_unit: Union[Unset, "InterpretationOrganisationUnit"] = UNSET
    period: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    text: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "InterpretationUser"] = UNSET
    visualization: Union[Unset, "InterpretationVisualization"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        likes = self.likes

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

        comments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_set, Unset):
            data_set = self.data_set.to_dict()

        display_name = self.display_name

        event_chart: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_chart, Unset):
            event_chart = self.event_chart.to_dict()

        event_report: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_report, Unset):
            event_report = self.event_report.to_dict()

        event_visualization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_visualization, Unset):
            event_visualization = self.event_visualization.to_dict()

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

        liked_by: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.liked_by, Unset):
            liked_by = []
            for liked_by_item_data in self.liked_by:
                liked_by_item = liked_by_item_data.to_dict()
                liked_by.append(liked_by_item)

        map_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.map_, Unset):
            map_ = self.map_.to_dict()

        mentions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mentions, Unset):
            mentions = []
            for mentions_item_data in self.mentions:
                mentions_item = mentions_item_data.to_dict()
                mentions.append(mentions_item)

        organisation_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit, Unset):
            organisation_unit = self.organisation_unit.to_dict()

        period = self.period

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        text = self.text

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
                "likes": likes,
                "type": type_,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if comments is not UNSET:
            field_dict["comments"] = comments
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if event_chart is not UNSET:
            field_dict["eventChart"] = event_chart
        if event_report is not UNSET:
            field_dict["eventReport"] = event_report
        if event_visualization is not UNSET:
            field_dict["eventVisualization"] = event_visualization
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
        if liked_by is not UNSET:
            field_dict["likedBy"] = liked_by
        if map_ is not UNSET:
            field_dict["map"] = map_
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if period is not UNSET:
            field_dict["period"] = period
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if text is not UNSET:
            field_dict["text"] = text
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
        from ..models.interpretation_comments_item import InterpretationCommentsItem
        from ..models.interpretation_created_by import InterpretationCreatedBy
        from ..models.interpretation_data_set import InterpretationDataSet
        from ..models.interpretation_event_chart import InterpretationEventChart
        from ..models.interpretation_event_report import InterpretationEventReport
        from ..models.interpretation_event_visualization import InterpretationEventVisualization
        from ..models.interpretation_last_updated_by import InterpretationLastUpdatedBy
        from ..models.interpretation_liked_by_item import InterpretationLikedByItem
        from ..models.interpretation_map import InterpretationMap
        from ..models.interpretation_organisation_unit import InterpretationOrganisationUnit
        from ..models.interpretation_user import InterpretationUser
        from ..models.interpretation_visualization import InterpretationVisualization
        from ..models.mention import Mention
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        likes = d.pop("likes")

        type_ = InterpretationType(d.pop("type"))

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

        comments = []
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = InterpretationCommentsItem.from_dict(comments_item_data)

            comments.append(comments_item)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, InterpretationCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = InterpretationCreatedBy.from_dict(_created_by)

        _data_set = d.pop("dataSet", UNSET)
        data_set: Union[Unset, InterpretationDataSet]
        if isinstance(_data_set, Unset):
            data_set = UNSET
        else:
            data_set = InterpretationDataSet.from_dict(_data_set)

        display_name = d.pop("displayName", UNSET)

        _event_chart = d.pop("eventChart", UNSET)
        event_chart: Union[Unset, InterpretationEventChart]
        if isinstance(_event_chart, Unset):
            event_chart = UNSET
        else:
            event_chart = InterpretationEventChart.from_dict(_event_chart)

        _event_report = d.pop("eventReport", UNSET)
        event_report: Union[Unset, InterpretationEventReport]
        if isinstance(_event_report, Unset):
            event_report = UNSET
        else:
            event_report = InterpretationEventReport.from_dict(_event_report)

        _event_visualization = d.pop("eventVisualization", UNSET)
        event_visualization: Union[Unset, InterpretationEventVisualization]
        if isinstance(_event_visualization, Unset):
            event_visualization = UNSET
        else:
            event_visualization = InterpretationEventVisualization.from_dict(_event_visualization)

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
        last_updated_by: Union[Unset, InterpretationLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = InterpretationLastUpdatedBy.from_dict(_last_updated_by)

        liked_by = []
        _liked_by = d.pop("likedBy", UNSET)
        for liked_by_item_data in _liked_by or []:
            liked_by_item = InterpretationLikedByItem.from_dict(liked_by_item_data)

            liked_by.append(liked_by_item)

        _map_ = d.pop("map", UNSET)
        map_: Union[Unset, InterpretationMap]
        if isinstance(_map_, Unset):
            map_ = UNSET
        else:
            map_ = InterpretationMap.from_dict(_map_)

        mentions = []
        _mentions = d.pop("mentions", UNSET)
        for mentions_item_data in _mentions or []:
            mentions_item = Mention.from_dict(mentions_item_data)

            mentions.append(mentions_item)

        _organisation_unit = d.pop("organisationUnit", UNSET)
        organisation_unit: Union[Unset, InterpretationOrganisationUnit]
        if isinstance(_organisation_unit, Unset):
            organisation_unit = UNSET
        else:
            organisation_unit = InterpretationOrganisationUnit.from_dict(_organisation_unit)

        period = d.pop("period", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        text = d.pop("text", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, InterpretationUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = InterpretationUser.from_dict(_user)

        _visualization = d.pop("visualization", UNSET)
        visualization: Union[Unset, InterpretationVisualization]
        if isinstance(_visualization, Unset):
            visualization = UNSET
        else:
            visualization = InterpretationVisualization.from_dict(_visualization)

        interpretation = cls(
            likes=likes,
            type_=type_,
            access=access,
            attribute_values=attribute_values,
            code=code,
            comments=comments,
            created=created,
            created_by=created_by,
            data_set=data_set,
            display_name=display_name,
            event_chart=event_chart,
            event_report=event_report,
            event_visualization=event_visualization,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            liked_by=liked_by,
            map_=map_,
            mentions=mentions,
            organisation_unit=organisation_unit,
            period=period,
            sharing=sharing,
            text=text,
            translations=translations,
            user=user,
            visualization=visualization,
        )

        interpretation.additional_properties = d
        return interpretation

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
