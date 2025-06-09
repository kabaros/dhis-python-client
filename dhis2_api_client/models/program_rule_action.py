import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_rule_action_program_rule_action_evaluation_environments_item import (
    ProgramRuleActionProgramRuleActionEvaluationEnvironmentsItem,
)
from ..models.program_rule_action_program_rule_action_evaluation_time import (
    ProgramRuleActionProgramRuleActionEvaluationTime,
)
from ..models.program_rule_action_program_rule_action_type import ProgramRuleActionProgramRuleActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_rule_action_created_by import ProgramRuleActionCreatedBy
    from ..models.program_rule_action_data_element import ProgramRuleActionDataElement
    from ..models.program_rule_action_last_updated_by import ProgramRuleActionLastUpdatedBy
    from ..models.program_rule_action_option import ProgramRuleActionOption
    from ..models.program_rule_action_option_group import ProgramRuleActionOptionGroup
    from ..models.program_rule_action_program_indicator import ProgramRuleActionProgramIndicator
    from ..models.program_rule_action_program_rule import ProgramRuleActionProgramRule
    from ..models.program_rule_action_program_stage import ProgramRuleActionProgramStage
    from ..models.program_rule_action_program_stage_section import ProgramRuleActionProgramStageSection
    from ..models.program_rule_action_tracked_entity_attribute import ProgramRuleActionTrackedEntityAttribute
    from ..models.program_rule_action_user import ProgramRuleActionUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramRuleAction")


@_attrs_define
class ProgramRuleAction:
    """
    Attributes:
        program_rule_action_evaluation_time (ProgramRuleActionProgramRuleActionEvaluationTime):
        program_rule_action_type (ProgramRuleActionProgramRuleActionType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        content (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramRuleActionCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data (Union[Unset, str]):
        data_element (Union[Unset, ProgramRuleActionDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        display_content (Union[Unset, str]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramRuleActionLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        location (Union[Unset, str]):
        name (Union[Unset, str]):
        option (Union[Unset, ProgramRuleActionOption]): A UID reference to a Option
            (Java name `org.hisp.dhis.option.Option`)
        option_group (Union[Unset, ProgramRuleActionOptionGroup]): A UID reference to a OptionGroup
            (Java name `org.hisp.dhis.option.OptionGroup`)
        program_indicator (Union[Unset, ProgramRuleActionProgramIndicator]): A UID reference to a ProgramIndicator
            (Java name `org.hisp.dhis.program.ProgramIndicator`)
        program_rule (Union[Unset, ProgramRuleActionProgramRule]): A UID reference to a ProgramRule
            (Java name `org.hisp.dhis.programrule.ProgramRule`)
        program_rule_action_evaluation_environments (Union[Unset,
            list[ProgramRuleActionProgramRuleActionEvaluationEnvironmentsItem]]):
        program_stage (Union[Unset, ProgramRuleActionProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        program_stage_section (Union[Unset, ProgramRuleActionProgramStageSection]): A UID reference to a
            ProgramStageSection
            (Java name `org.hisp.dhis.program.ProgramStageSection`)
        sharing (Union[Unset, Sharing]):
        template_uid (Union[Unset, str]):
        tracked_entity_attribute (Union[Unset, ProgramRuleActionTrackedEntityAttribute]): A UID reference to a
            TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramRuleActionUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    program_rule_action_evaluation_time: ProgramRuleActionProgramRuleActionEvaluationTime
    program_rule_action_type: ProgramRuleActionProgramRuleActionType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramRuleActionCreatedBy"] = UNSET
    data: Union[Unset, str] = UNSET
    data_element: Union[Unset, "ProgramRuleActionDataElement"] = UNSET
    display_content: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramRuleActionLastUpdatedBy"] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    option: Union[Unset, "ProgramRuleActionOption"] = UNSET
    option_group: Union[Unset, "ProgramRuleActionOptionGroup"] = UNSET
    program_indicator: Union[Unset, "ProgramRuleActionProgramIndicator"] = UNSET
    program_rule: Union[Unset, "ProgramRuleActionProgramRule"] = UNSET
    program_rule_action_evaluation_environments: Union[
        Unset, list[ProgramRuleActionProgramRuleActionEvaluationEnvironmentsItem]
    ] = UNSET
    program_stage: Union[Unset, "ProgramRuleActionProgramStage"] = UNSET
    program_stage_section: Union[Unset, "ProgramRuleActionProgramStageSection"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    template_uid: Union[Unset, str] = UNSET
    tracked_entity_attribute: Union[Unset, "ProgramRuleActionTrackedEntityAttribute"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramRuleActionUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        program_rule_action_evaluation_time = self.program_rule_action_evaluation_time.value

        program_rule_action_type = self.program_rule_action_type.value

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

        content = self.content

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data = self.data

        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

        display_content = self.display_content

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

        location = self.location

        name = self.name

        option: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.option, Unset):
            option = self.option.to_dict()

        option_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.option_group, Unset):
            option_group = self.option_group.to_dict()

        program_indicator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_indicator, Unset):
            program_indicator = self.program_indicator.to_dict()

        program_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_rule, Unset):
            program_rule = self.program_rule.to_dict()

        program_rule_action_evaluation_environments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.program_rule_action_evaluation_environments, Unset):
            program_rule_action_evaluation_environments = []
            for (
                program_rule_action_evaluation_environments_item_data
            ) in self.program_rule_action_evaluation_environments:
                program_rule_action_evaluation_environments_item = (
                    program_rule_action_evaluation_environments_item_data.value
                )
                program_rule_action_evaluation_environments.append(program_rule_action_evaluation_environments_item)

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        program_stage_section: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage_section, Unset):
            program_stage_section = self.program_stage_section.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        template_uid = self.template_uid

        tracked_entity_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_attribute, Unset):
            tracked_entity_attribute = self.tracked_entity_attribute.to_dict()

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
                "programRuleActionEvaluationTime": program_rule_action_evaluation_time,
                "programRuleActionType": program_rule_action_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if content is not UNSET:
            field_dict["content"] = content
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data is not UNSET:
            field_dict["data"] = data
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if display_content is not UNSET:
            field_dict["displayContent"] = display_content
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
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if option is not UNSET:
            field_dict["option"] = option
        if option_group is not UNSET:
            field_dict["optionGroup"] = option_group
        if program_indicator is not UNSET:
            field_dict["programIndicator"] = program_indicator
        if program_rule is not UNSET:
            field_dict["programRule"] = program_rule
        if program_rule_action_evaluation_environments is not UNSET:
            field_dict["programRuleActionEvaluationEnvironments"] = program_rule_action_evaluation_environments
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if program_stage_section is not UNSET:
            field_dict["programStageSection"] = program_stage_section
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if template_uid is not UNSET:
            field_dict["templateUid"] = template_uid
        if tracked_entity_attribute is not UNSET:
            field_dict["trackedEntityAttribute"] = tracked_entity_attribute
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.program_rule_action_created_by import ProgramRuleActionCreatedBy
        from ..models.program_rule_action_data_element import ProgramRuleActionDataElement
        from ..models.program_rule_action_last_updated_by import ProgramRuleActionLastUpdatedBy
        from ..models.program_rule_action_option import ProgramRuleActionOption
        from ..models.program_rule_action_option_group import ProgramRuleActionOptionGroup
        from ..models.program_rule_action_program_indicator import ProgramRuleActionProgramIndicator
        from ..models.program_rule_action_program_rule import ProgramRuleActionProgramRule
        from ..models.program_rule_action_program_stage import ProgramRuleActionProgramStage
        from ..models.program_rule_action_program_stage_section import ProgramRuleActionProgramStageSection
        from ..models.program_rule_action_tracked_entity_attribute import ProgramRuleActionTrackedEntityAttribute
        from ..models.program_rule_action_user import ProgramRuleActionUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        program_rule_action_evaluation_time = ProgramRuleActionProgramRuleActionEvaluationTime(
            d.pop("programRuleActionEvaluationTime")
        )

        program_rule_action_type = ProgramRuleActionProgramRuleActionType(d.pop("programRuleActionType"))

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

        content = d.pop("content", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ProgramRuleActionCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramRuleActionCreatedBy.from_dict(_created_by)

        data = d.pop("data", UNSET)

        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, ProgramRuleActionDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = ProgramRuleActionDataElement.from_dict(_data_element)

        display_content = d.pop("displayContent", UNSET)

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
        last_updated_by: Union[Unset, ProgramRuleActionLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramRuleActionLastUpdatedBy.from_dict(_last_updated_by)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        _option = d.pop("option", UNSET)
        option: Union[Unset, ProgramRuleActionOption]
        if isinstance(_option, Unset):
            option = UNSET
        else:
            option = ProgramRuleActionOption.from_dict(_option)

        _option_group = d.pop("optionGroup", UNSET)
        option_group: Union[Unset, ProgramRuleActionOptionGroup]
        if isinstance(_option_group, Unset):
            option_group = UNSET
        else:
            option_group = ProgramRuleActionOptionGroup.from_dict(_option_group)

        _program_indicator = d.pop("programIndicator", UNSET)
        program_indicator: Union[Unset, ProgramRuleActionProgramIndicator]
        if isinstance(_program_indicator, Unset):
            program_indicator = UNSET
        else:
            program_indicator = ProgramRuleActionProgramIndicator.from_dict(_program_indicator)

        _program_rule = d.pop("programRule", UNSET)
        program_rule: Union[Unset, ProgramRuleActionProgramRule]
        if isinstance(_program_rule, Unset):
            program_rule = UNSET
        else:
            program_rule = ProgramRuleActionProgramRule.from_dict(_program_rule)

        program_rule_action_evaluation_environments = []
        _program_rule_action_evaluation_environments = d.pop("programRuleActionEvaluationEnvironments", UNSET)
        for program_rule_action_evaluation_environments_item_data in _program_rule_action_evaluation_environments or []:
            program_rule_action_evaluation_environments_item = (
                ProgramRuleActionProgramRuleActionEvaluationEnvironmentsItem(
                    program_rule_action_evaluation_environments_item_data
                )
            )

            program_rule_action_evaluation_environments.append(program_rule_action_evaluation_environments_item)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, ProgramRuleActionProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = ProgramRuleActionProgramStage.from_dict(_program_stage)

        _program_stage_section = d.pop("programStageSection", UNSET)
        program_stage_section: Union[Unset, ProgramRuleActionProgramStageSection]
        if isinstance(_program_stage_section, Unset):
            program_stage_section = UNSET
        else:
            program_stage_section = ProgramRuleActionProgramStageSection.from_dict(_program_stage_section)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        template_uid = d.pop("templateUid", UNSET)

        _tracked_entity_attribute = d.pop("trackedEntityAttribute", UNSET)
        tracked_entity_attribute: Union[Unset, ProgramRuleActionTrackedEntityAttribute]
        if isinstance(_tracked_entity_attribute, Unset):
            tracked_entity_attribute = UNSET
        else:
            tracked_entity_attribute = ProgramRuleActionTrackedEntityAttribute.from_dict(_tracked_entity_attribute)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramRuleActionUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramRuleActionUser.from_dict(_user)

        program_rule_action = cls(
            program_rule_action_evaluation_time=program_rule_action_evaluation_time,
            program_rule_action_type=program_rule_action_type,
            access=access,
            attribute_values=attribute_values,
            code=code,
            content=content,
            created=created,
            created_by=created_by,
            data=data,
            data_element=data_element,
            display_content=display_content,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            location=location,
            name=name,
            option=option,
            option_group=option_group,
            program_indicator=program_indicator,
            program_rule=program_rule,
            program_rule_action_evaluation_environments=program_rule_action_evaluation_environments,
            program_stage=program_stage,
            program_stage_section=program_stage_section,
            sharing=sharing,
            template_uid=template_uid,
            tracked_entity_attribute=tracked_entity_attribute,
            translations=translations,
            user=user,
        )

        program_rule_action.additional_properties = d
        return program_rule_action

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
