import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sms_command_completeness_method import SMSCommandCompletenessMethod
from ..models.sms_command_parser_type import SMSCommandParserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.sharing import Sharing
    from ..models.sms_code import SMSCode
    from ..models.sms_command_created_by import SMSCommandCreatedBy
    from ..models.sms_command_dataset import SMSCommandDataset
    from ..models.sms_command_last_updated_by import SMSCommandLastUpdatedBy
    from ..models.sms_command_program import SMSCommandProgram
    from ..models.sms_command_program_stage import SMSCommandProgramStage
    from ..models.sms_command_user import SMSCommandUser
    from ..models.sms_command_user_group import SMSCommandUserGroup
    from ..models.sms_special_character import SMSSpecialCharacter
    from ..models.translation import Translation


T = TypeVar("T", bound="SMSCommand")


@_attrs_define
class SMSCommand:
    """
    Attributes:
        completeness_method (SMSCommandCompletenessMethod):
        parser_type (SMSCommandParserType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        code_value_separator (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, SMSCommandCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        current_period_used_for_reporting (Union[Unset, bool]):
        dataset (Union[Unset, SMSCommandDataset]): A UID reference to a DataSet
            (Java name `org.hisp.dhis.dataset.DataSet`)
        default_message (Union[Unset, str]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, SMSCommandLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        more_than_one_org_unit_message (Union[Unset, str]):
        name (Union[Unset, str]):
        no_user_message (Union[Unset, str]):
        program (Union[Unset, SMSCommandProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_stage (Union[Unset, SMSCommandProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        received_message (Union[Unset, str]):
        separator (Union[Unset, str]):
        sharing (Union[Unset, Sharing]):
        sms_codes (Union[Unset, list['SMSCode']]):
        special_characters (Union[Unset, list['SMSSpecialCharacter']]):
        success_message (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, SMSCommandUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_group (Union[Unset, SMSCommandUserGroup]): A UID reference to a UserGroup
            (Java name `org.hisp.dhis.user.UserGroup`)
        wrong_format_message (Union[Unset, str]):
    """

    completeness_method: SMSCommandCompletenessMethod
    parser_type: SMSCommandParserType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    code_value_separator: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "SMSCommandCreatedBy"] = UNSET
    current_period_used_for_reporting: Union[Unset, bool] = UNSET
    dataset: Union[Unset, "SMSCommandDataset"] = UNSET
    default_message: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "SMSCommandLastUpdatedBy"] = UNSET
    more_than_one_org_unit_message: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    no_user_message: Union[Unset, str] = UNSET
    program: Union[Unset, "SMSCommandProgram"] = UNSET
    program_stage: Union[Unset, "SMSCommandProgramStage"] = UNSET
    received_message: Union[Unset, str] = UNSET
    separator: Union[Unset, str] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    sms_codes: Union[Unset, list["SMSCode"]] = UNSET
    special_characters: Union[Unset, list["SMSSpecialCharacter"]] = UNSET
    success_message: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "SMSCommandUser"] = UNSET
    user_group: Union[Unset, "SMSCommandUserGroup"] = UNSET
    wrong_format_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completeness_method = self.completeness_method.value

        parser_type = self.parser_type.value

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

        code_value_separator = self.code_value_separator

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        current_period_used_for_reporting = self.current_period_used_for_reporting

        dataset: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dataset, Unset):
            dataset = self.dataset.to_dict()

        default_message = self.default_message

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

        more_than_one_org_unit_message = self.more_than_one_org_unit_message

        name = self.name

        no_user_message = self.no_user_message

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        received_message = self.received_message

        separator = self.separator

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        sms_codes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sms_codes, Unset):
            sms_codes = []
            for sms_codes_item_data in self.sms_codes:
                sms_codes_item = sms_codes_item_data.to_dict()
                sms_codes.append(sms_codes_item)

        special_characters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.special_characters, Unset):
            special_characters = []
            for special_characters_item_data in self.special_characters:
                special_characters_item = special_characters_item_data.to_dict()
                special_characters.append(special_characters_item)

        success_message = self.success_message

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_group, Unset):
            user_group = self.user_group.to_dict()

        wrong_format_message = self.wrong_format_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completenessMethod": completeness_method,
                "parserType": parser_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if code_value_separator is not UNSET:
            field_dict["codeValueSeparator"] = code_value_separator
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if current_period_used_for_reporting is not UNSET:
            field_dict["currentPeriodUsedForReporting"] = current_period_used_for_reporting
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if default_message is not UNSET:
            field_dict["defaultMessage"] = default_message
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
        if more_than_one_org_unit_message is not UNSET:
            field_dict["moreThanOneOrgUnitMessage"] = more_than_one_org_unit_message
        if name is not UNSET:
            field_dict["name"] = name
        if no_user_message is not UNSET:
            field_dict["noUserMessage"] = no_user_message
        if program is not UNSET:
            field_dict["program"] = program
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if received_message is not UNSET:
            field_dict["receivedMessage"] = received_message
        if separator is not UNSET:
            field_dict["separator"] = separator
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if sms_codes is not UNSET:
            field_dict["smsCodes"] = sms_codes
        if special_characters is not UNSET:
            field_dict["specialCharacters"] = special_characters
        if success_message is not UNSET:
            field_dict["successMessage"] = success_message
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if user_group is not UNSET:
            field_dict["userGroup"] = user_group
        if wrong_format_message is not UNSET:
            field_dict["wrongFormatMessage"] = wrong_format_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.sharing import Sharing
        from ..models.sms_code import SMSCode
        from ..models.sms_command_created_by import SMSCommandCreatedBy
        from ..models.sms_command_dataset import SMSCommandDataset
        from ..models.sms_command_last_updated_by import SMSCommandLastUpdatedBy
        from ..models.sms_command_program import SMSCommandProgram
        from ..models.sms_command_program_stage import SMSCommandProgramStage
        from ..models.sms_command_user import SMSCommandUser
        from ..models.sms_command_user_group import SMSCommandUserGroup
        from ..models.sms_special_character import SMSSpecialCharacter
        from ..models.translation import Translation

        d = src_dict.copy()
        completeness_method = SMSCommandCompletenessMethod(d.pop("completenessMethod"))

        parser_type = SMSCommandParserType(d.pop("parserType"))

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

        code_value_separator = d.pop("codeValueSeparator", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, SMSCommandCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = SMSCommandCreatedBy.from_dict(_created_by)

        current_period_used_for_reporting = d.pop("currentPeriodUsedForReporting", UNSET)

        _dataset = d.pop("dataset", UNSET)
        dataset: Union[Unset, SMSCommandDataset]
        if isinstance(_dataset, Unset):
            dataset = UNSET
        else:
            dataset = SMSCommandDataset.from_dict(_dataset)

        default_message = d.pop("defaultMessage", UNSET)

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
        last_updated_by: Union[Unset, SMSCommandLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = SMSCommandLastUpdatedBy.from_dict(_last_updated_by)

        more_than_one_org_unit_message = d.pop("moreThanOneOrgUnitMessage", UNSET)

        name = d.pop("name", UNSET)

        no_user_message = d.pop("noUserMessage", UNSET)

        _program = d.pop("program", UNSET)
        program: Union[Unset, SMSCommandProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = SMSCommandProgram.from_dict(_program)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, SMSCommandProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = SMSCommandProgramStage.from_dict(_program_stage)

        received_message = d.pop("receivedMessage", UNSET)

        separator = d.pop("separator", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        sms_codes = []
        _sms_codes = d.pop("smsCodes", UNSET)
        for sms_codes_item_data in _sms_codes or []:
            sms_codes_item = SMSCode.from_dict(sms_codes_item_data)

            sms_codes.append(sms_codes_item)

        special_characters = []
        _special_characters = d.pop("specialCharacters", UNSET)
        for special_characters_item_data in _special_characters or []:
            special_characters_item = SMSSpecialCharacter.from_dict(special_characters_item_data)

            special_characters.append(special_characters_item)

        success_message = d.pop("successMessage", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, SMSCommandUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = SMSCommandUser.from_dict(_user)

        _user_group = d.pop("userGroup", UNSET)
        user_group: Union[Unset, SMSCommandUserGroup]
        if isinstance(_user_group, Unset):
            user_group = UNSET
        else:
            user_group = SMSCommandUserGroup.from_dict(_user_group)

        wrong_format_message = d.pop("wrongFormatMessage", UNSET)

        sms_command = cls(
            completeness_method=completeness_method,
            parser_type=parser_type,
            access=access,
            attribute_values=attribute_values,
            code=code,
            code_value_separator=code_value_separator,
            created=created,
            created_by=created_by,
            current_period_used_for_reporting=current_period_used_for_reporting,
            dataset=dataset,
            default_message=default_message,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            more_than_one_org_unit_message=more_than_one_org_unit_message,
            name=name,
            no_user_message=no_user_message,
            program=program,
            program_stage=program_stage,
            received_message=received_message,
            separator=separator,
            sharing=sharing,
            sms_codes=sms_codes,
            special_characters=special_characters,
            success_message=success_message,
            translations=translations,
            user=user,
            user_group=user_group,
            wrong_format_message=wrong_format_message,
        )

        sms_command.additional_properties = d
        return sms_command

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
