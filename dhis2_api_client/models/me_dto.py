import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.me_dto_avatar import MeDtoAvatar
    from ..models.me_dto_data_view_organisation_units_item import MeDtoDataViewOrganisationUnitsItem
    from ..models.me_dto_organisation_units_item import MeDtoOrganisationUnitsItem
    from ..models.me_dto_pat_tokens_item import MeDtoPatTokensItem
    from ..models.me_dto_settings import MeDtoSettings
    from ..models.me_dto_tei_search_organisation_units_item import MeDtoTeiSearchOrganisationUnitsItem
    from ..models.me_dto_user_groups_item import MeDtoUserGroupsItem
    from ..models.me_dto_user_roles_item import MeDtoUserRolesItem
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.user_access import UserAccess
    from ..models.user_credentials_dto import UserCredentialsDto
    from ..models.user_group_access import UserGroupAccess


T = TypeVar("T", bound="MeDto")


@_attrs_define
class MeDto:
    """
    Attributes:
        access (Union[Unset, Access]):
        authorities (Union[Unset, list[str]]):
        avatar (Union[Unset, MeDtoAvatar]): A UID reference to a FileResource
            (Java name `org.hisp.dhis.fileresource.FileResource`)
        birthday (Union[Unset, datetime.datetime]):
        created (Union[Unset, datetime.datetime]):
        data_sets (Union[Unset, list[str]]):
        data_view_organisation_units (Union[Unset, list['MeDtoDataViewOrganisationUnitsItem']]):
        display_name (Union[Unset, str]):
        education (Union[Unset, str]):
        email (Union[Unset, str]):
        employer (Union[Unset, str]):
        external_access (Union[Unset, bool]):
        facebook_messenger (Union[Unset, str]):
        favorites (Union[Unset, list[str]]):
        first_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        id (Union[Unset, str]):
        impersonation (Union[Unset, str]):
        interests (Union[Unset, str]):
        introduction (Union[Unset, str]):
        job_title (Union[Unset, str]):
        languages (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        nationality (Union[Unset, str]):
        organisation_units (Union[Unset, list['MeDtoOrganisationUnitsItem']]):
        pat_tokens (Union[Unset, list['MeDtoPatTokensItem']]):
        phone_number (Union[Unset, str]):
        programs (Union[Unset, list[str]]):
        settings (Union[Unset, MeDtoSettings]):
        sharing (Union[Unset, Sharing]):
        skype (Union[Unset, str]):
        surname (Union[Unset, str]):
        tei_search_organisation_units (Union[Unset, list['MeDtoTeiSearchOrganisationUnitsItem']]):
        telegram (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        twitter (Union[Unset, str]):
        user_accesses (Union[Unset, list['UserAccess']]):
        user_credentials (Union[Unset, UserCredentialsDto]):
        user_group_accesses (Union[Unset, list['UserGroupAccess']]):
        user_groups (Union[Unset, list['MeDtoUserGroupsItem']]):
        user_roles (Union[Unset, list['MeDtoUserRolesItem']]):
        username (Union[Unset, str]):
        whats_app (Union[Unset, str]):
    """

    access: Union[Unset, "Access"] = UNSET
    authorities: Union[Unset, list[str]] = UNSET
    avatar: Union[Unset, "MeDtoAvatar"] = UNSET
    birthday: Union[Unset, datetime.datetime] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    data_sets: Union[Unset, list[str]] = UNSET
    data_view_organisation_units: Union[Unset, list["MeDtoDataViewOrganisationUnitsItem"]] = UNSET
    display_name: Union[Unset, str] = UNSET
    education: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    employer: Union[Unset, str] = UNSET
    external_access: Union[Unset, bool] = UNSET
    facebook_messenger: Union[Unset, str] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    first_name: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    impersonation: Union[Unset, str] = UNSET
    interests: Union[Unset, str] = UNSET
    introduction: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    languages: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    nationality: Union[Unset, str] = UNSET
    organisation_units: Union[Unset, list["MeDtoOrganisationUnitsItem"]] = UNSET
    pat_tokens: Union[Unset, list["MeDtoPatTokensItem"]] = UNSET
    phone_number: Union[Unset, str] = UNSET
    programs: Union[Unset, list[str]] = UNSET
    settings: Union[Unset, "MeDtoSettings"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    skype: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    tei_search_organisation_units: Union[Unset, list["MeDtoTeiSearchOrganisationUnitsItem"]] = UNSET
    telegram: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    twitter: Union[Unset, str] = UNSET
    user_accesses: Union[Unset, list["UserAccess"]] = UNSET
    user_credentials: Union[Unset, "UserCredentialsDto"] = UNSET
    user_group_accesses: Union[Unset, list["UserGroupAccess"]] = UNSET
    user_groups: Union[Unset, list["MeDtoUserGroupsItem"]] = UNSET
    user_roles: Union[Unset, list["MeDtoUserRolesItem"]] = UNSET
    username: Union[Unset, str] = UNSET
    whats_app: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        authorities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.authorities, Unset):
            authorities = self.authorities

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        data_sets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.data_sets, Unset):
            data_sets = self.data_sets

        data_view_organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_view_organisation_units, Unset):
            data_view_organisation_units = []
            for data_view_organisation_units_item_data in self.data_view_organisation_units:
                data_view_organisation_units_item = data_view_organisation_units_item_data.to_dict()
                data_view_organisation_units.append(data_view_organisation_units_item)

        display_name = self.display_name

        education = self.education

        email = self.email

        employer = self.employer

        external_access = self.external_access

        facebook_messenger = self.facebook_messenger

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        first_name = self.first_name

        gender = self.gender

        id = self.id

        impersonation = self.impersonation

        interests = self.interests

        introduction = self.introduction

        job_title = self.job_title

        languages = self.languages

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        name = self.name

        nationality = self.nationality

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        pat_tokens: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pat_tokens, Unset):
            pat_tokens = []
            for pat_tokens_item_data in self.pat_tokens:
                pat_tokens_item = pat_tokens_item_data.to_dict()
                pat_tokens.append(pat_tokens_item)

        phone_number = self.phone_number

        programs: Union[Unset, list[str]] = UNSET
        if not isinstance(self.programs, Unset):
            programs = self.programs

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        skype = self.skype

        surname = self.surname

        tei_search_organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tei_search_organisation_units, Unset):
            tei_search_organisation_units = []
            for tei_search_organisation_units_item_data in self.tei_search_organisation_units:
                tei_search_organisation_units_item = tei_search_organisation_units_item_data.to_dict()
                tei_search_organisation_units.append(tei_search_organisation_units_item)

        telegram = self.telegram

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        twitter = self.twitter

        user_accesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_accesses, Unset):
            user_accesses = []
            for user_accesses_item_data in self.user_accesses:
                user_accesses_item = user_accesses_item_data.to_dict()
                user_accesses.append(user_accesses_item)

        user_credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_credentials, Unset):
            user_credentials = self.user_credentials.to_dict()

        user_group_accesses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_group_accesses, Unset):
            user_group_accesses = []
            for user_group_accesses_item_data in self.user_group_accesses:
                user_group_accesses_item = user_group_accesses_item_data.to_dict()
                user_group_accesses.append(user_group_accesses_item)

        user_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = []
            for user_groups_item_data in self.user_groups:
                user_groups_item = user_groups_item_data.to_dict()
                user_groups.append(user_groups_item)

        user_roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_roles, Unset):
            user_roles = []
            for user_roles_item_data in self.user_roles:
                user_roles_item = user_roles_item_data.to_dict()
                user_roles.append(user_roles_item)

        username = self.username

        whats_app = self.whats_app

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if authorities is not UNSET:
            field_dict["authorities"] = authorities
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if created is not UNSET:
            field_dict["created"] = created
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if data_view_organisation_units is not UNSET:
            field_dict["dataViewOrganisationUnits"] = data_view_organisation_units
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if education is not UNSET:
            field_dict["education"] = education
        if email is not UNSET:
            field_dict["email"] = email
        if employer is not UNSET:
            field_dict["employer"] = employer
        if external_access is not UNSET:
            field_dict["externalAccess"] = external_access
        if facebook_messenger is not UNSET:
            field_dict["facebookMessenger"] = facebook_messenger
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if id is not UNSET:
            field_dict["id"] = id
        if impersonation is not UNSET:
            field_dict["impersonation"] = impersonation
        if interests is not UNSET:
            field_dict["interests"] = interests
        if introduction is not UNSET:
            field_dict["introduction"] = introduction
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if languages is not UNSET:
            field_dict["languages"] = languages
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if name is not UNSET:
            field_dict["name"] = name
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if pat_tokens is not UNSET:
            field_dict["patTokens"] = pat_tokens
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if programs is not UNSET:
            field_dict["programs"] = programs
        if settings is not UNSET:
            field_dict["settings"] = settings
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if skype is not UNSET:
            field_dict["skype"] = skype
        if surname is not UNSET:
            field_dict["surname"] = surname
        if tei_search_organisation_units is not UNSET:
            field_dict["teiSearchOrganisationUnits"] = tei_search_organisation_units
        if telegram is not UNSET:
            field_dict["telegram"] = telegram
        if translations is not UNSET:
            field_dict["translations"] = translations
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if user_accesses is not UNSET:
            field_dict["userAccesses"] = user_accesses
        if user_credentials is not UNSET:
            field_dict["userCredentials"] = user_credentials
        if user_group_accesses is not UNSET:
            field_dict["userGroupAccesses"] = user_group_accesses
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if user_roles is not UNSET:
            field_dict["userRoles"] = user_roles
        if username is not UNSET:
            field_dict["username"] = username
        if whats_app is not UNSET:
            field_dict["whatsApp"] = whats_app

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.me_dto_avatar import MeDtoAvatar
        from ..models.me_dto_data_view_organisation_units_item import MeDtoDataViewOrganisationUnitsItem
        from ..models.me_dto_organisation_units_item import MeDtoOrganisationUnitsItem
        from ..models.me_dto_pat_tokens_item import MeDtoPatTokensItem
        from ..models.me_dto_settings import MeDtoSettings
        from ..models.me_dto_tei_search_organisation_units_item import MeDtoTeiSearchOrganisationUnitsItem
        from ..models.me_dto_user_groups_item import MeDtoUserGroupsItem
        from ..models.me_dto_user_roles_item import MeDtoUserRolesItem
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.user_access import UserAccess
        from ..models.user_credentials_dto import UserCredentialsDto
        from ..models.user_group_access import UserGroupAccess

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        authorities = cast(list[str], d.pop("authorities", UNSET))

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, MeDtoAvatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = MeDtoAvatar.from_dict(_avatar)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.datetime]
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = isoparse(_birthday)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        data_sets = cast(list[str], d.pop("dataSets", UNSET))

        data_view_organisation_units = []
        _data_view_organisation_units = d.pop("dataViewOrganisationUnits", UNSET)
        for data_view_organisation_units_item_data in _data_view_organisation_units or []:
            data_view_organisation_units_item = MeDtoDataViewOrganisationUnitsItem.from_dict(
                data_view_organisation_units_item_data
            )

            data_view_organisation_units.append(data_view_organisation_units_item)

        display_name = d.pop("displayName", UNSET)

        education = d.pop("education", UNSET)

        email = d.pop("email", UNSET)

        employer = d.pop("employer", UNSET)

        external_access = d.pop("externalAccess", UNSET)

        facebook_messenger = d.pop("facebookMessenger", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        first_name = d.pop("firstName", UNSET)

        gender = d.pop("gender", UNSET)

        id = d.pop("id", UNSET)

        impersonation = d.pop("impersonation", UNSET)

        interests = d.pop("interests", UNSET)

        introduction = d.pop("introduction", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        languages = d.pop("languages", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        name = d.pop("name", UNSET)

        nationality = d.pop("nationality", UNSET)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = MeDtoOrganisationUnitsItem.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

        pat_tokens = []
        _pat_tokens = d.pop("patTokens", UNSET)
        for pat_tokens_item_data in _pat_tokens or []:
            pat_tokens_item = MeDtoPatTokensItem.from_dict(pat_tokens_item_data)

            pat_tokens.append(pat_tokens_item)

        phone_number = d.pop("phoneNumber", UNSET)

        programs = cast(list[str], d.pop("programs", UNSET))

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, MeDtoSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = MeDtoSettings.from_dict(_settings)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        skype = d.pop("skype", UNSET)

        surname = d.pop("surname", UNSET)

        tei_search_organisation_units = []
        _tei_search_organisation_units = d.pop("teiSearchOrganisationUnits", UNSET)
        for tei_search_organisation_units_item_data in _tei_search_organisation_units or []:
            tei_search_organisation_units_item = MeDtoTeiSearchOrganisationUnitsItem.from_dict(
                tei_search_organisation_units_item_data
            )

            tei_search_organisation_units.append(tei_search_organisation_units_item)

        telegram = d.pop("telegram", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        twitter = d.pop("twitter", UNSET)

        user_accesses = []
        _user_accesses = d.pop("userAccesses", UNSET)
        for user_accesses_item_data in _user_accesses or []:
            user_accesses_item = UserAccess.from_dict(user_accesses_item_data)

            user_accesses.append(user_accesses_item)

        _user_credentials = d.pop("userCredentials", UNSET)
        user_credentials: Union[Unset, UserCredentialsDto]
        if isinstance(_user_credentials, Unset):
            user_credentials = UNSET
        else:
            user_credentials = UserCredentialsDto.from_dict(_user_credentials)

        user_group_accesses = []
        _user_group_accesses = d.pop("userGroupAccesses", UNSET)
        for user_group_accesses_item_data in _user_group_accesses or []:
            user_group_accesses_item = UserGroupAccess.from_dict(user_group_accesses_item_data)

            user_group_accesses.append(user_group_accesses_item)

        user_groups = []
        _user_groups = d.pop("userGroups", UNSET)
        for user_groups_item_data in _user_groups or []:
            user_groups_item = MeDtoUserGroupsItem.from_dict(user_groups_item_data)

            user_groups.append(user_groups_item)

        user_roles = []
        _user_roles = d.pop("userRoles", UNSET)
        for user_roles_item_data in _user_roles or []:
            user_roles_item = MeDtoUserRolesItem.from_dict(user_roles_item_data)

            user_roles.append(user_roles_item)

        username = d.pop("username", UNSET)

        whats_app = d.pop("whatsApp", UNSET)

        me_dto = cls(
            access=access,
            authorities=authorities,
            avatar=avatar,
            birthday=birthday,
            created=created,
            data_sets=data_sets,
            data_view_organisation_units=data_view_organisation_units,
            display_name=display_name,
            education=education,
            email=email,
            employer=employer,
            external_access=external_access,
            facebook_messenger=facebook_messenger,
            favorites=favorites,
            first_name=first_name,
            gender=gender,
            id=id,
            impersonation=impersonation,
            interests=interests,
            introduction=introduction,
            job_title=job_title,
            languages=languages,
            last_updated=last_updated,
            name=name,
            nationality=nationality,
            organisation_units=organisation_units,
            pat_tokens=pat_tokens,
            phone_number=phone_number,
            programs=programs,
            settings=settings,
            sharing=sharing,
            skype=skype,
            surname=surname,
            tei_search_organisation_units=tei_search_organisation_units,
            telegram=telegram,
            translations=translations,
            twitter=twitter,
            user_accesses=user_accesses,
            user_credentials=user_credentials,
            user_group_accesses=user_group_accesses,
            user_groups=user_groups,
            user_roles=user_roles,
            username=username,
            whats_app=whats_app,
        )

        me_dto.additional_properties = d
        return me_dto

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
