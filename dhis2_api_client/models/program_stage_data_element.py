import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_stage_data_element_created_by import ProgramStageDataElementCreatedBy
    from ..models.program_stage_data_element_data_element import ProgramStageDataElementDataElement
    from ..models.program_stage_data_element_last_updated_by import ProgramStageDataElementLastUpdatedBy
    from ..models.program_stage_data_element_program_stage import ProgramStageDataElementProgramStage
    from ..models.program_stage_data_element_user import ProgramStageDataElementUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramStageDataElement")


@_attrs_define
class ProgramStageDataElement:
    """
    Attributes:
        access (Union[Unset, Access]):
        allow_future_date (Union[Unset, bool]):
        allow_provided_elsewhere (Union[Unset, bool]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        compulsory (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramStageDataElementCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_element (Union[Unset, ProgramStageDataElementDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        display_in_reports (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramStageDataElementLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        program_stage (Union[Unset, ProgramStageDataElementProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        render_options_as_radio (Union[Unset, bool]):
        render_type (Union[Unset, Any]): The exact type is unknown.
            (Java type was: `org.hisp.dhis.render.DeviceRenderTypeMap<org.hisp.dhis.render.type.ValueTypeRenderingObject>`)
        sharing (Union[Unset, Sharing]):
        skip_analytics (Union[Unset, bool]):
        skip_synchronization (Union[Unset, bool]):
        sort_order (Union[Unset, int]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramStageDataElementUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    allow_future_date: Union[Unset, bool] = UNSET
    allow_provided_elsewhere: Union[Unset, bool] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    compulsory: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramStageDataElementCreatedBy"] = UNSET
    data_element: Union[Unset, "ProgramStageDataElementDataElement"] = UNSET
    display_in_reports: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramStageDataElementLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    program_stage: Union[Unset, "ProgramStageDataElementProgramStage"] = UNSET
    render_options_as_radio: Union[Unset, bool] = UNSET
    render_type: Union[Unset, Any] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    skip_analytics: Union[Unset, bool] = UNSET
    skip_synchronization: Union[Unset, bool] = UNSET
    sort_order: Union[Unset, int] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramStageDataElementUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        allow_future_date = self.allow_future_date

        allow_provided_elsewhere = self.allow_provided_elsewhere

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        compulsory = self.compulsory

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

        display_in_reports = self.display_in_reports

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

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        render_options_as_radio = self.render_options_as_radio

        render_type = self.render_type

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        skip_analytics = self.skip_analytics

        skip_synchronization = self.skip_synchronization

        sort_order = self.sort_order

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
        if allow_future_date is not UNSET:
            field_dict["allowFutureDate"] = allow_future_date
        if allow_provided_elsewhere is not UNSET:
            field_dict["allowProvidedElsewhere"] = allow_provided_elsewhere
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if compulsory is not UNSET:
            field_dict["compulsory"] = compulsory
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if display_in_reports is not UNSET:
            field_dict["displayInReports"] = display_in_reports
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
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if render_options_as_radio is not UNSET:
            field_dict["renderOptionsAsRadio"] = render_options_as_radio
        if render_type is not UNSET:
            field_dict["renderType"] = render_type
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if skip_analytics is not UNSET:
            field_dict["skipAnalytics"] = skip_analytics
        if skip_synchronization is not UNSET:
            field_dict["skipSynchronization"] = skip_synchronization
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.program_stage_data_element_created_by import ProgramStageDataElementCreatedBy
        from ..models.program_stage_data_element_data_element import ProgramStageDataElementDataElement
        from ..models.program_stage_data_element_last_updated_by import ProgramStageDataElementLastUpdatedBy
        from ..models.program_stage_data_element_program_stage import ProgramStageDataElementProgramStage
        from ..models.program_stage_data_element_user import ProgramStageDataElementUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        allow_future_date = d.pop("allowFutureDate", UNSET)

        allow_provided_elsewhere = d.pop("allowProvidedElsewhere", UNSET)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        compulsory = d.pop("compulsory", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ProgramStageDataElementCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramStageDataElementCreatedBy.from_dict(_created_by)

        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, ProgramStageDataElementDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = ProgramStageDataElementDataElement.from_dict(_data_element)

        display_in_reports = d.pop("displayInReports", UNSET)

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
        last_updated_by: Union[Unset, ProgramStageDataElementLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramStageDataElementLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, ProgramStageDataElementProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = ProgramStageDataElementProgramStage.from_dict(_program_stage)

        render_options_as_radio = d.pop("renderOptionsAsRadio", UNSET)

        render_type = d.pop("renderType", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        skip_analytics = d.pop("skipAnalytics", UNSET)

        skip_synchronization = d.pop("skipSynchronization", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramStageDataElementUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramStageDataElementUser.from_dict(_user)

        program_stage_data_element = cls(
            access=access,
            allow_future_date=allow_future_date,
            allow_provided_elsewhere=allow_provided_elsewhere,
            attribute_values=attribute_values,
            code=code,
            compulsory=compulsory,
            created=created,
            created_by=created_by,
            data_element=data_element,
            display_in_reports=display_in_reports,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            program_stage=program_stage,
            render_options_as_radio=render_options_as_radio,
            render_type=render_type,
            sharing=sharing,
            skip_analytics=skip_analytics,
            skip_synchronization=skip_synchronization,
            sort_order=sort_order,
            translations=translations,
            user=user,
        )

        program_stage_data_element.additional_properties = d
        return program_stage_data_element

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
