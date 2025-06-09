import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_rule_created_by import ProgramRuleCreatedBy
    from ..models.program_rule_last_updated_by import ProgramRuleLastUpdatedBy
    from ..models.program_rule_program import ProgramRuleProgram
    from ..models.program_rule_program_rule_actions_item import ProgramRuleProgramRuleActionsItem
    from ..models.program_rule_program_stage import ProgramRuleProgramStage
    from ..models.program_rule_user import ProgramRuleUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramRule")


@_attrs_define
class ProgramRule:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        condition (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramRuleCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramRuleLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        priority (Union[Unset, int]):
        program (Union[Unset, ProgramRuleProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_rule_actions (Union[Unset, list['ProgramRuleProgramRuleActionsItem']]):
        program_stage (Union[Unset, ProgramRuleProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, ProgramRuleUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    condition: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramRuleCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramRuleLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    program: Union[Unset, "ProgramRuleProgram"] = UNSET
    program_rule_actions: Union[Unset, list["ProgramRuleProgramRuleActionsItem"]] = UNSET
    program_stage: Union[Unset, "ProgramRuleProgramStage"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "ProgramRuleUser"] = UNSET
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

        condition = self.condition

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

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        priority = self.priority

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_rule_actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.program_rule_actions, Unset):
            program_rule_actions = []
            for program_rule_actions_item_data in self.program_rule_actions:
                program_rule_actions_item = program_rule_actions_item_data.to_dict()
                program_rule_actions.append(program_rule_actions_item)

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

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
        if condition is not UNSET:
            field_dict["condition"] = condition
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
        if priority is not UNSET:
            field_dict["priority"] = priority
        if program is not UNSET:
            field_dict["program"] = program
        if program_rule_actions is not UNSET:
            field_dict["programRuleActions"] = program_rule_actions
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
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
        from ..models.program_rule_created_by import ProgramRuleCreatedBy
        from ..models.program_rule_last_updated_by import ProgramRuleLastUpdatedBy
        from ..models.program_rule_program import ProgramRuleProgram
        from ..models.program_rule_program_rule_actions_item import ProgramRuleProgramRuleActionsItem
        from ..models.program_rule_program_stage import ProgramRuleProgramStage
        from ..models.program_rule_user import ProgramRuleUser
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

        condition = d.pop("condition", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, ProgramRuleCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramRuleCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

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
        last_updated_by: Union[Unset, ProgramRuleLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramRuleLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        priority = d.pop("priority", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, ProgramRuleProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = ProgramRuleProgram.from_dict(_program)

        program_rule_actions = []
        _program_rule_actions = d.pop("programRuleActions", UNSET)
        for program_rule_actions_item_data in _program_rule_actions or []:
            program_rule_actions_item = ProgramRuleProgramRuleActionsItem.from_dict(program_rule_actions_item_data)

            program_rule_actions.append(program_rule_actions_item)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, ProgramRuleProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = ProgramRuleProgramStage.from_dict(_program_stage)

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
        user: Union[Unset, ProgramRuleUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramRuleUser.from_dict(_user)

        program_rule = cls(
            access=access,
            attribute_values=attribute_values,
            code=code,
            condition=condition,
            created=created,
            created_by=created_by,
            description=description,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            priority=priority,
            program=program,
            program_rule_actions=program_rule_actions,
            program_stage=program_stage,
            sharing=sharing,
            translations=translations,
            user=user,
        )

        program_rule.additional_properties = d
        return program_rule

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
