import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.program_rule_variable_program_rule_variable_source_type import (
    ProgramRuleVariableProgramRuleVariableSourceType,
)
from ..models.program_rule_variable_value_type import ProgramRuleVariableValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.program_rule_variable_created_by import ProgramRuleVariableCreatedBy
    from ..models.program_rule_variable_data_element import ProgramRuleVariableDataElement
    from ..models.program_rule_variable_last_updated_by import ProgramRuleVariableLastUpdatedBy
    from ..models.program_rule_variable_program import ProgramRuleVariableProgram
    from ..models.program_rule_variable_program_stage import ProgramRuleVariableProgramStage
    from ..models.program_rule_variable_tracked_entity_attribute import ProgramRuleVariableTrackedEntityAttribute
    from ..models.program_rule_variable_user import ProgramRuleVariableUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="ProgramRuleVariable")


@_attrs_define
class ProgramRuleVariable:
    """
    Attributes:
        program_rule_variable_source_type (ProgramRuleVariableProgramRuleVariableSourceType):
        value_type (ProgramRuleVariableValueType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, ProgramRuleVariableCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_element (Union[Unset, ProgramRuleVariableDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, ProgramRuleVariableLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        program (Union[Unset, ProgramRuleVariableProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_stage (Union[Unset, ProgramRuleVariableProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        sharing (Union[Unset, Sharing]):
        tracked_entity_attribute (Union[Unset, ProgramRuleVariableTrackedEntityAttribute]): A UID reference to a
            TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
        translations (Union[Unset, list['Translation']]):
        use_code_for_option_set (Union[Unset, bool]):
        user (Union[Unset, ProgramRuleVariableUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    program_rule_variable_source_type: ProgramRuleVariableProgramRuleVariableSourceType
    value_type: ProgramRuleVariableValueType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "ProgramRuleVariableCreatedBy"] = UNSET
    data_element: Union[Unset, "ProgramRuleVariableDataElement"] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "ProgramRuleVariableLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    program: Union[Unset, "ProgramRuleVariableProgram"] = UNSET
    program_stage: Union[Unset, "ProgramRuleVariableProgramStage"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    tracked_entity_attribute: Union[Unset, "ProgramRuleVariableTrackedEntityAttribute"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    use_code_for_option_set: Union[Unset, bool] = UNSET
    user: Union[Unset, "ProgramRuleVariableUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        program_rule_variable_source_type = self.program_rule_variable_source_type.value

        value_type = self.value_type.value

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

        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

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

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        tracked_entity_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_attribute, Unset):
            tracked_entity_attribute = self.tracked_entity_attribute.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        use_code_for_option_set = self.use_code_for_option_set

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "programRuleVariableSourceType": program_rule_variable_source_type,
                "valueType": value_type,
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
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
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
        if program is not UNSET:
            field_dict["program"] = program
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if tracked_entity_attribute is not UNSET:
            field_dict["trackedEntityAttribute"] = tracked_entity_attribute
        if translations is not UNSET:
            field_dict["translations"] = translations
        if use_code_for_option_set is not UNSET:
            field_dict["useCodeForOptionSet"] = use_code_for_option_set
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.program_rule_variable_created_by import ProgramRuleVariableCreatedBy
        from ..models.program_rule_variable_data_element import ProgramRuleVariableDataElement
        from ..models.program_rule_variable_last_updated_by import ProgramRuleVariableLastUpdatedBy
        from ..models.program_rule_variable_program import ProgramRuleVariableProgram
        from ..models.program_rule_variable_program_stage import ProgramRuleVariableProgramStage
        from ..models.program_rule_variable_tracked_entity_attribute import ProgramRuleVariableTrackedEntityAttribute
        from ..models.program_rule_variable_user import ProgramRuleVariableUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        program_rule_variable_source_type = ProgramRuleVariableProgramRuleVariableSourceType(
            d.pop("programRuleVariableSourceType")
        )

        value_type = ProgramRuleVariableValueType(d.pop("valueType"))

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
        created_by: Union[Unset, ProgramRuleVariableCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = ProgramRuleVariableCreatedBy.from_dict(_created_by)

        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, ProgramRuleVariableDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = ProgramRuleVariableDataElement.from_dict(_data_element)

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
        last_updated_by: Union[Unset, ProgramRuleVariableLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = ProgramRuleVariableLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, ProgramRuleVariableProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = ProgramRuleVariableProgram.from_dict(_program)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, ProgramRuleVariableProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = ProgramRuleVariableProgramStage.from_dict(_program_stage)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        _tracked_entity_attribute = d.pop("trackedEntityAttribute", UNSET)
        tracked_entity_attribute: Union[Unset, ProgramRuleVariableTrackedEntityAttribute]
        if isinstance(_tracked_entity_attribute, Unset):
            tracked_entity_attribute = UNSET
        else:
            tracked_entity_attribute = ProgramRuleVariableTrackedEntityAttribute.from_dict(_tracked_entity_attribute)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        use_code_for_option_set = d.pop("useCodeForOptionSet", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, ProgramRuleVariableUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ProgramRuleVariableUser.from_dict(_user)

        program_rule_variable = cls(
            program_rule_variable_source_type=program_rule_variable_source_type,
            value_type=value_type,
            access=access,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            data_element=data_element,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            program=program,
            program_stage=program_stage,
            sharing=sharing,
            tracked_entity_attribute=tracked_entity_attribute,
            translations=translations,
            use_code_for_option_set=use_code_for_option_set,
            user=user,
        )

        program_rule_variable.additional_properties = d
        return program_rule_variable

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
