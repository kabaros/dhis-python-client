import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.sharing import Sharing
    from ..models.translation import Translation
    from ..models.user_avatar import UserAvatar
    from ..models.user_cat_dimension_constraints_item import UserCatDimensionConstraintsItem
    from ..models.user_cogs_dimension_constraints_item import UserCogsDimensionConstraintsItem
    from ..models.user_created_by import UserCreatedBy
    from ..models.user_credentials_dto import UserCredentialsDto
    from ..models.user_data_view_organisation_units_item import UserDataViewOrganisationUnitsItem
    from ..models.user_last_updated_by import UserLastUpdatedBy
    from ..models.user_organisation_units_item import UserOrganisationUnitsItem
    from ..models.user_settings import UserSettings
    from ..models.user_tei_search_organisation_units_item import UserTeiSearchOrganisationUnitsItem
    from ..models.user_user import UserUser
    from ..models.user_user_groups_item import UserUserGroupsItem
    from ..models.user_user_roles_item import UserUserRolesItem


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        access (Union[Unset, Access]):
        account_expiry (Union[Unset, datetime.datetime]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        avatar (Union[Unset, UserAvatar]): A UID reference to a FileResource
            (Java name `org.hisp.dhis.fileresource.FileResource`)
        birthday (Union[Unset, datetime.datetime]):
        cat_dimension_constraints (Union[Unset, list['UserCatDimensionConstraintsItem']]):
        code (Union[Unset, str]):
        cogs_dimension_constraints (Union[Unset, list['UserCogsDimensionConstraintsItem']]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, UserCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_view_max_organisation_unit_level (Union[Unset, int]):
        data_view_organisation_units (Union[Unset, list['UserDataViewOrganisationUnitsItem']]):
        disabled (Union[Unset, bool]):
        display_name (Union[Unset, str]):
        education (Union[Unset, str]):
        email (Union[Unset, str]):
        employer (Union[Unset, str]):
        external_auth (Union[Unset, bool]):
        facebook_messenger (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        first_name (Union[Unset, str]):
        gender (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        interests (Union[Unset, str]):
        introduction (Union[Unset, str]):
        invitation (Union[Unset, bool]):
        job_title (Union[Unset, str]):
        languages (Union[Unset, str]):
        last_checked_interpretations (Union[Unset, datetime.datetime]):
        last_login (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, UserLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        ldap_id (Union[Unset, str]):
        nationality (Union[Unset, str]):
        open_id (Union[Unset, str]):
        organisation_units (Union[Unset, list['UserOrganisationUnitsItem']]):
        password (Union[Unset, str]):
        password_last_updated (Union[Unset, datetime.datetime]):
        phone_number (Union[Unset, str]):
        self_registered (Union[Unset, bool]):
        settings (Union[Unset, UserSettings]):
        sharing (Union[Unset, Sharing]):
        skype (Union[Unset, str]):
        surname (Union[Unset, str]):
        tei_search_organisation_units (Union[Unset, list['UserTeiSearchOrganisationUnitsItem']]):
        telegram (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        twitter (Union[Unset, str]):
        two_factor_enabled (Union[Unset, bool]):
        user (Union[Unset, UserUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_credentials (Union[Unset, UserCredentialsDto]):
        user_groups (Union[Unset, list['UserUserGroupsItem']]):
        user_roles (Union[Unset, list['UserUserRolesItem']]):
        username (Union[Unset, str]):
        welcome_message (Union[Unset, str]):
        whats_app (Union[Unset, str]):
    """

    access: Union[Unset, "Access"] = UNSET
    account_expiry: Union[Unset, datetime.datetime] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    avatar: Union[Unset, "UserAvatar"] = UNSET
    birthday: Union[Unset, datetime.datetime] = UNSET
    cat_dimension_constraints: Union[Unset, list["UserCatDimensionConstraintsItem"]] = UNSET
    code: Union[Unset, str] = UNSET
    cogs_dimension_constraints: Union[Unset, list["UserCogsDimensionConstraintsItem"]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "UserCreatedBy"] = UNSET
    data_view_max_organisation_unit_level: Union[Unset, int] = UNSET
    data_view_organisation_units: Union[Unset, list["UserDataViewOrganisationUnitsItem"]] = UNSET
    disabled: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    education: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    employer: Union[Unset, str] = UNSET
    external_auth: Union[Unset, bool] = UNSET
    facebook_messenger: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    first_name: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interests: Union[Unset, str] = UNSET
    introduction: Union[Unset, str] = UNSET
    invitation: Union[Unset, bool] = UNSET
    job_title: Union[Unset, str] = UNSET
    languages: Union[Unset, str] = UNSET
    last_checked_interpretations: Union[Unset, datetime.datetime] = UNSET
    last_login: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "UserLastUpdatedBy"] = UNSET
    ldap_id: Union[Unset, str] = UNSET
    nationality: Union[Unset, str] = UNSET
    open_id: Union[Unset, str] = UNSET
    organisation_units: Union[Unset, list["UserOrganisationUnitsItem"]] = UNSET
    password: Union[Unset, str] = UNSET
    password_last_updated: Union[Unset, datetime.datetime] = UNSET
    phone_number: Union[Unset, str] = UNSET
    self_registered: Union[Unset, bool] = UNSET
    settings: Union[Unset, "UserSettings"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    skype: Union[Unset, str] = UNSET
    surname: Union[Unset, str] = UNSET
    tei_search_organisation_units: Union[Unset, list["UserTeiSearchOrganisationUnitsItem"]] = UNSET
    telegram: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    twitter: Union[Unset, str] = UNSET
    two_factor_enabled: Union[Unset, bool] = UNSET
    user: Union[Unset, "UserUser"] = UNSET
    user_credentials: Union[Unset, "UserCredentialsDto"] = UNSET
    user_groups: Union[Unset, list["UserUserGroupsItem"]] = UNSET
    user_roles: Union[Unset, list["UserUserRolesItem"]] = UNSET
    username: Union[Unset, str] = UNSET
    welcome_message: Union[Unset, str] = UNSET
    whats_app: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        account_expiry: Union[Unset, str] = UNSET
        if not isinstance(self.account_expiry, Unset):
            account_expiry = self.account_expiry.isoformat()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        cat_dimension_constraints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cat_dimension_constraints, Unset):
            cat_dimension_constraints = []
            for cat_dimension_constraints_item_data in self.cat_dimension_constraints:
                cat_dimension_constraints_item = cat_dimension_constraints_item_data.to_dict()
                cat_dimension_constraints.append(cat_dimension_constraints_item)

        code = self.code

        cogs_dimension_constraints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cogs_dimension_constraints, Unset):
            cogs_dimension_constraints = []
            for cogs_dimension_constraints_item_data in self.cogs_dimension_constraints:
                cogs_dimension_constraints_item = cogs_dimension_constraints_item_data.to_dict()
                cogs_dimension_constraints.append(cogs_dimension_constraints_item)

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_view_max_organisation_unit_level = self.data_view_max_organisation_unit_level

        data_view_organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_view_organisation_units, Unset):
            data_view_organisation_units = []
            for data_view_organisation_units_item_data in self.data_view_organisation_units:
                data_view_organisation_units_item = data_view_organisation_units_item_data.to_dict()
                data_view_organisation_units.append(data_view_organisation_units_item)

        disabled = self.disabled

        display_name = self.display_name

        education = self.education

        email = self.email

        employer = self.employer

        external_auth = self.external_auth

        facebook_messenger = self.facebook_messenger

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        first_name = self.first_name

        gender = self.gender

        href = self.href

        id = self.id

        interests = self.interests

        introduction = self.introduction

        invitation = self.invitation

        job_title = self.job_title

        languages = self.languages

        last_checked_interpretations: Union[Unset, str] = UNSET
        if not isinstance(self.last_checked_interpretations, Unset):
            last_checked_interpretations = self.last_checked_interpretations.isoformat()

        last_login: Union[Unset, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        ldap_id = self.ldap_id

        nationality = self.nationality

        open_id = self.open_id

        organisation_units: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_units, Unset):
            organisation_units = []
            for organisation_units_item_data in self.organisation_units:
                organisation_units_item = organisation_units_item_data.to_dict()
                organisation_units.append(organisation_units_item)

        password = self.password

        password_last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.password_last_updated, Unset):
            password_last_updated = self.password_last_updated.isoformat()

        phone_number = self.phone_number

        self_registered = self.self_registered

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

        two_factor_enabled = self.two_factor_enabled

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_credentials, Unset):
            user_credentials = self.user_credentials.to_dict()

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

        welcome_message = self.welcome_message

        whats_app = self.whats_app

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if account_expiry is not UNSET:
            field_dict["accountExpiry"] = account_expiry
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if cat_dimension_constraints is not UNSET:
            field_dict["catDimensionConstraints"] = cat_dimension_constraints
        if code is not UNSET:
            field_dict["code"] = code
        if cogs_dimension_constraints is not UNSET:
            field_dict["cogsDimensionConstraints"] = cogs_dimension_constraints
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_view_max_organisation_unit_level is not UNSET:
            field_dict["dataViewMaxOrganisationUnitLevel"] = data_view_max_organisation_unit_level
        if data_view_organisation_units is not UNSET:
            field_dict["dataViewOrganisationUnits"] = data_view_organisation_units
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if education is not UNSET:
            field_dict["education"] = education
        if email is not UNSET:
            field_dict["email"] = email
        if employer is not UNSET:
            field_dict["employer"] = employer
        if external_auth is not UNSET:
            field_dict["externalAuth"] = external_auth
        if facebook_messenger is not UNSET:
            field_dict["facebookMessenger"] = facebook_messenger
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if interests is not UNSET:
            field_dict["interests"] = interests
        if introduction is not UNSET:
            field_dict["introduction"] = introduction
        if invitation is not UNSET:
            field_dict["invitation"] = invitation
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if languages is not UNSET:
            field_dict["languages"] = languages
        if last_checked_interpretations is not UNSET:
            field_dict["lastCheckedInterpretations"] = last_checked_interpretations
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if ldap_id is not UNSET:
            field_dict["ldapId"] = ldap_id
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if open_id is not UNSET:
            field_dict["openId"] = open_id
        if organisation_units is not UNSET:
            field_dict["organisationUnits"] = organisation_units
        if password is not UNSET:
            field_dict["password"] = password
        if password_last_updated is not UNSET:
            field_dict["passwordLastUpdated"] = password_last_updated
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if self_registered is not UNSET:
            field_dict["selfRegistered"] = self_registered
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
        if two_factor_enabled is not UNSET:
            field_dict["twoFactorEnabled"] = two_factor_enabled
        if user is not UNSET:
            field_dict["user"] = user
        if user_credentials is not UNSET:
            field_dict["userCredentials"] = user_credentials
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if user_roles is not UNSET:
            field_dict["userRoles"] = user_roles
        if username is not UNSET:
            field_dict["username"] = username
        if welcome_message is not UNSET:
            field_dict["welcomeMessage"] = welcome_message
        if whats_app is not UNSET:
            field_dict["whatsApp"] = whats_app

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.sharing import Sharing
        from ..models.translation import Translation
        from ..models.user_avatar import UserAvatar
        from ..models.user_cat_dimension_constraints_item import UserCatDimensionConstraintsItem
        from ..models.user_cogs_dimension_constraints_item import UserCogsDimensionConstraintsItem
        from ..models.user_created_by import UserCreatedBy
        from ..models.user_credentials_dto import UserCredentialsDto
        from ..models.user_data_view_organisation_units_item import UserDataViewOrganisationUnitsItem
        from ..models.user_last_updated_by import UserLastUpdatedBy
        from ..models.user_organisation_units_item import UserOrganisationUnitsItem
        from ..models.user_settings import UserSettings
        from ..models.user_tei_search_organisation_units_item import UserTeiSearchOrganisationUnitsItem
        from ..models.user_user import UserUser
        from ..models.user_user_groups_item import UserUserGroupsItem
        from ..models.user_user_roles_item import UserUserRolesItem

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        _account_expiry = d.pop("accountExpiry", UNSET)
        account_expiry: Union[Unset, datetime.datetime]
        if isinstance(_account_expiry, Unset):
            account_expiry = UNSET
        else:
            account_expiry = isoparse(_account_expiry)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, UserAvatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = UserAvatar.from_dict(_avatar)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.datetime]
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = isoparse(_birthday)

        cat_dimension_constraints = []
        _cat_dimension_constraints = d.pop("catDimensionConstraints", UNSET)
        for cat_dimension_constraints_item_data in _cat_dimension_constraints or []:
            cat_dimension_constraints_item = UserCatDimensionConstraintsItem.from_dict(
                cat_dimension_constraints_item_data
            )

            cat_dimension_constraints.append(cat_dimension_constraints_item)

        code = d.pop("code", UNSET)

        cogs_dimension_constraints = []
        _cogs_dimension_constraints = d.pop("cogsDimensionConstraints", UNSET)
        for cogs_dimension_constraints_item_data in _cogs_dimension_constraints or []:
            cogs_dimension_constraints_item = UserCogsDimensionConstraintsItem.from_dict(
                cogs_dimension_constraints_item_data
            )

            cogs_dimension_constraints.append(cogs_dimension_constraints_item)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, UserCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UserCreatedBy.from_dict(_created_by)

        data_view_max_organisation_unit_level = d.pop("dataViewMaxOrganisationUnitLevel", UNSET)

        data_view_organisation_units = []
        _data_view_organisation_units = d.pop("dataViewOrganisationUnits", UNSET)
        for data_view_organisation_units_item_data in _data_view_organisation_units or []:
            data_view_organisation_units_item = UserDataViewOrganisationUnitsItem.from_dict(
                data_view_organisation_units_item_data
            )

            data_view_organisation_units.append(data_view_organisation_units_item)

        disabled = d.pop("disabled", UNSET)

        display_name = d.pop("displayName", UNSET)

        education = d.pop("education", UNSET)

        email = d.pop("email", UNSET)

        employer = d.pop("employer", UNSET)

        external_auth = d.pop("externalAuth", UNSET)

        facebook_messenger = d.pop("facebookMessenger", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        first_name = d.pop("firstName", UNSET)

        gender = d.pop("gender", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        interests = d.pop("interests", UNSET)

        introduction = d.pop("introduction", UNSET)

        invitation = d.pop("invitation", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        languages = d.pop("languages", UNSET)

        _last_checked_interpretations = d.pop("lastCheckedInterpretations", UNSET)
        last_checked_interpretations: Union[Unset, datetime.datetime]
        if isinstance(_last_checked_interpretations, Unset):
            last_checked_interpretations = UNSET
        else:
            last_checked_interpretations = isoparse(_last_checked_interpretations)

        _last_login = d.pop("lastLogin", UNSET)
        last_login: Union[Unset, datetime.datetime]
        if isinstance(_last_login, Unset):
            last_login = UNSET
        else:
            last_login = isoparse(_last_login)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, UserLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = UserLastUpdatedBy.from_dict(_last_updated_by)

        ldap_id = d.pop("ldapId", UNSET)

        nationality = d.pop("nationality", UNSET)

        open_id = d.pop("openId", UNSET)

        organisation_units = []
        _organisation_units = d.pop("organisationUnits", UNSET)
        for organisation_units_item_data in _organisation_units or []:
            organisation_units_item = UserOrganisationUnitsItem.from_dict(organisation_units_item_data)

            organisation_units.append(organisation_units_item)

        password = d.pop("password", UNSET)

        _password_last_updated = d.pop("passwordLastUpdated", UNSET)
        password_last_updated: Union[Unset, datetime.datetime]
        if isinstance(_password_last_updated, Unset):
            password_last_updated = UNSET
        else:
            password_last_updated = isoparse(_password_last_updated)

        phone_number = d.pop("phoneNumber", UNSET)

        self_registered = d.pop("selfRegistered", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, UserSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = UserSettings.from_dict(_settings)

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
            tei_search_organisation_units_item = UserTeiSearchOrganisationUnitsItem.from_dict(
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

        two_factor_enabled = d.pop("twoFactorEnabled", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserUser.from_dict(_user)

        _user_credentials = d.pop("userCredentials", UNSET)
        user_credentials: Union[Unset, UserCredentialsDto]
        if isinstance(_user_credentials, Unset):
            user_credentials = UNSET
        else:
            user_credentials = UserCredentialsDto.from_dict(_user_credentials)

        user_groups = []
        _user_groups = d.pop("userGroups", UNSET)
        for user_groups_item_data in _user_groups or []:
            user_groups_item = UserUserGroupsItem.from_dict(user_groups_item_data)

            user_groups.append(user_groups_item)

        user_roles = []
        _user_roles = d.pop("userRoles", UNSET)
        for user_roles_item_data in _user_roles or []:
            user_roles_item = UserUserRolesItem.from_dict(user_roles_item_data)

            user_roles.append(user_roles_item)

        username = d.pop("username", UNSET)

        welcome_message = d.pop("welcomeMessage", UNSET)

        whats_app = d.pop("whatsApp", UNSET)

        user = cls(
            access=access,
            account_expiry=account_expiry,
            attribute_values=attribute_values,
            avatar=avatar,
            birthday=birthday,
            cat_dimension_constraints=cat_dimension_constraints,
            code=code,
            cogs_dimension_constraints=cogs_dimension_constraints,
            created=created,
            created_by=created_by,
            data_view_max_organisation_unit_level=data_view_max_organisation_unit_level,
            data_view_organisation_units=data_view_organisation_units,
            disabled=disabled,
            display_name=display_name,
            education=education,
            email=email,
            employer=employer,
            external_auth=external_auth,
            facebook_messenger=facebook_messenger,
            favorite=favorite,
            favorites=favorites,
            first_name=first_name,
            gender=gender,
            href=href,
            id=id,
            interests=interests,
            introduction=introduction,
            invitation=invitation,
            job_title=job_title,
            languages=languages,
            last_checked_interpretations=last_checked_interpretations,
            last_login=last_login,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            ldap_id=ldap_id,
            nationality=nationality,
            open_id=open_id,
            organisation_units=organisation_units,
            password=password,
            password_last_updated=password_last_updated,
            phone_number=phone_number,
            self_registered=self_registered,
            settings=settings,
            sharing=sharing,
            skype=skype,
            surname=surname,
            tei_search_organisation_units=tei_search_organisation_units,
            telegram=telegram,
            translations=translations,
            twitter=twitter,
            two_factor_enabled=two_factor_enabled,
            user=user,
            user_credentials=user_credentials,
            user_groups=user_groups,
            user_roles=user_roles,
            username=username,
            welcome_message=welcome_message,
            whats_app=whats_app,
        )

        user.additional_properties = d
        return user

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
