import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.sharing import Sharing
    from ..models.user_credentials_dto_cat_dimension_constraints_item import (
        UserCredentialsDtoCatDimensionConstraintsItem,
    )
    from ..models.user_credentials_dto_cogs_dimension_constraints_item import (
        UserCredentialsDtoCogsDimensionConstraintsItem,
    )
    from ..models.user_credentials_dto_user_roles_item import UserCredentialsDtoUserRolesItem


T = TypeVar("T", bound="UserCredentialsDto")


@_attrs_define
class UserCredentialsDto:
    """
    Attributes:
        access (Union[Unset, Access]):
        account_expiry (Union[Unset, datetime.datetime]):
        cat_dimension_constraints (Union[Unset, list['UserCredentialsDtoCatDimensionConstraintsItem']]):
        cogs_dimension_constraints (Union[Unset, list['UserCredentialsDtoCogsDimensionConstraintsItem']]):
        disabled (Union[Unset, bool]):
        external_auth (Union[Unset, bool]):
        id (Union[Unset, str]):
        id_token (Union[Unset, str]):
        invitation (Union[Unset, bool]):
        last_login (Union[Unset, datetime.datetime]):
        ldap_id (Union[Unset, str]):
        open_id (Union[Unset, str]):
        password (Union[Unset, str]):
        password_last_updated (Union[Unset, datetime.datetime]):
        previous_passwords (Union[Unset, list[str]]):
        restore_expiry (Union[Unset, datetime.datetime]):
        restore_token (Union[Unset, str]):
        self_registered (Union[Unset, bool]):
        sharing (Union[Unset, Sharing]):
        two_fa (Union[Unset, bool]):
        uid (Union[Unset, str]):
        user_roles (Union[Unset, list['UserCredentialsDtoUserRolesItem']]):
        username (Union[Unset, str]):
        uuid (Union[Unset, str]):
    """

    access: Union[Unset, "Access"] = UNSET
    account_expiry: Union[Unset, datetime.datetime] = UNSET
    cat_dimension_constraints: Union[Unset, list["UserCredentialsDtoCatDimensionConstraintsItem"]] = UNSET
    cogs_dimension_constraints: Union[Unset, list["UserCredentialsDtoCogsDimensionConstraintsItem"]] = UNSET
    disabled: Union[Unset, bool] = UNSET
    external_auth: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    id_token: Union[Unset, str] = UNSET
    invitation: Union[Unset, bool] = UNSET
    last_login: Union[Unset, datetime.datetime] = UNSET
    ldap_id: Union[Unset, str] = UNSET
    open_id: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    password_last_updated: Union[Unset, datetime.datetime] = UNSET
    previous_passwords: Union[Unset, list[str]] = UNSET
    restore_expiry: Union[Unset, datetime.datetime] = UNSET
    restore_token: Union[Unset, str] = UNSET
    self_registered: Union[Unset, bool] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    two_fa: Union[Unset, bool] = UNSET
    uid: Union[Unset, str] = UNSET
    user_roles: Union[Unset, list["UserCredentialsDtoUserRolesItem"]] = UNSET
    username: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        account_expiry: Union[Unset, str] = UNSET
        if not isinstance(self.account_expiry, Unset):
            account_expiry = self.account_expiry.isoformat()

        cat_dimension_constraints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cat_dimension_constraints, Unset):
            cat_dimension_constraints = []
            for cat_dimension_constraints_item_data in self.cat_dimension_constraints:
                cat_dimension_constraints_item = cat_dimension_constraints_item_data.to_dict()
                cat_dimension_constraints.append(cat_dimension_constraints_item)

        cogs_dimension_constraints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cogs_dimension_constraints, Unset):
            cogs_dimension_constraints = []
            for cogs_dimension_constraints_item_data in self.cogs_dimension_constraints:
                cogs_dimension_constraints_item = cogs_dimension_constraints_item_data.to_dict()
                cogs_dimension_constraints.append(cogs_dimension_constraints_item)

        disabled = self.disabled

        external_auth = self.external_auth

        id = self.id

        id_token = self.id_token

        invitation = self.invitation

        last_login: Union[Unset, str] = UNSET
        if not isinstance(self.last_login, Unset):
            last_login = self.last_login.isoformat()

        ldap_id = self.ldap_id

        open_id = self.open_id

        password = self.password

        password_last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.password_last_updated, Unset):
            password_last_updated = self.password_last_updated.isoformat()

        previous_passwords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.previous_passwords, Unset):
            previous_passwords = self.previous_passwords

        restore_expiry: Union[Unset, str] = UNSET
        if not isinstance(self.restore_expiry, Unset):
            restore_expiry = self.restore_expiry.isoformat()

        restore_token = self.restore_token

        self_registered = self.self_registered

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        two_fa = self.two_fa

        uid = self.uid

        user_roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_roles, Unset):
            user_roles = []
            for user_roles_item_data in self.user_roles:
                user_roles_item = user_roles_item_data.to_dict()
                user_roles.append(user_roles_item)

        username = self.username

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if account_expiry is not UNSET:
            field_dict["accountExpiry"] = account_expiry
        if cat_dimension_constraints is not UNSET:
            field_dict["catDimensionConstraints"] = cat_dimension_constraints
        if cogs_dimension_constraints is not UNSET:
            field_dict["cogsDimensionConstraints"] = cogs_dimension_constraints
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if external_auth is not UNSET:
            field_dict["externalAuth"] = external_auth
        if id is not UNSET:
            field_dict["id"] = id
        if id_token is not UNSET:
            field_dict["idToken"] = id_token
        if invitation is not UNSET:
            field_dict["invitation"] = invitation
        if last_login is not UNSET:
            field_dict["lastLogin"] = last_login
        if ldap_id is not UNSET:
            field_dict["ldapId"] = ldap_id
        if open_id is not UNSET:
            field_dict["openId"] = open_id
        if password is not UNSET:
            field_dict["password"] = password
        if password_last_updated is not UNSET:
            field_dict["passwordLastUpdated"] = password_last_updated
        if previous_passwords is not UNSET:
            field_dict["previousPasswords"] = previous_passwords
        if restore_expiry is not UNSET:
            field_dict["restoreExpiry"] = restore_expiry
        if restore_token is not UNSET:
            field_dict["restoreToken"] = restore_token
        if self_registered is not UNSET:
            field_dict["selfRegistered"] = self_registered
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if two_fa is not UNSET:
            field_dict["twoFA"] = two_fa
        if uid is not UNSET:
            field_dict["uid"] = uid
        if user_roles is not UNSET:
            field_dict["userRoles"] = user_roles
        if username is not UNSET:
            field_dict["username"] = username
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.sharing import Sharing
        from ..models.user_credentials_dto_cat_dimension_constraints_item import (
            UserCredentialsDtoCatDimensionConstraintsItem,
        )
        from ..models.user_credentials_dto_cogs_dimension_constraints_item import (
            UserCredentialsDtoCogsDimensionConstraintsItem,
        )
        from ..models.user_credentials_dto_user_roles_item import UserCredentialsDtoUserRolesItem

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

        cat_dimension_constraints = []
        _cat_dimension_constraints = d.pop("catDimensionConstraints", UNSET)
        for cat_dimension_constraints_item_data in _cat_dimension_constraints or []:
            cat_dimension_constraints_item = UserCredentialsDtoCatDimensionConstraintsItem.from_dict(
                cat_dimension_constraints_item_data
            )

            cat_dimension_constraints.append(cat_dimension_constraints_item)

        cogs_dimension_constraints = []
        _cogs_dimension_constraints = d.pop("cogsDimensionConstraints", UNSET)
        for cogs_dimension_constraints_item_data in _cogs_dimension_constraints or []:
            cogs_dimension_constraints_item = UserCredentialsDtoCogsDimensionConstraintsItem.from_dict(
                cogs_dimension_constraints_item_data
            )

            cogs_dimension_constraints.append(cogs_dimension_constraints_item)

        disabled = d.pop("disabled", UNSET)

        external_auth = d.pop("externalAuth", UNSET)

        id = d.pop("id", UNSET)

        id_token = d.pop("idToken", UNSET)

        invitation = d.pop("invitation", UNSET)

        _last_login = d.pop("lastLogin", UNSET)
        last_login: Union[Unset, datetime.datetime]
        if isinstance(_last_login, Unset):
            last_login = UNSET
        else:
            last_login = isoparse(_last_login)

        ldap_id = d.pop("ldapId", UNSET)

        open_id = d.pop("openId", UNSET)

        password = d.pop("password", UNSET)

        _password_last_updated = d.pop("passwordLastUpdated", UNSET)
        password_last_updated: Union[Unset, datetime.datetime]
        if isinstance(_password_last_updated, Unset):
            password_last_updated = UNSET
        else:
            password_last_updated = isoparse(_password_last_updated)

        previous_passwords = cast(list[str], d.pop("previousPasswords", UNSET))

        _restore_expiry = d.pop("restoreExpiry", UNSET)
        restore_expiry: Union[Unset, datetime.datetime]
        if isinstance(_restore_expiry, Unset):
            restore_expiry = UNSET
        else:
            restore_expiry = isoparse(_restore_expiry)

        restore_token = d.pop("restoreToken", UNSET)

        self_registered = d.pop("selfRegistered", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        two_fa = d.pop("twoFA", UNSET)

        uid = d.pop("uid", UNSET)

        user_roles = []
        _user_roles = d.pop("userRoles", UNSET)
        for user_roles_item_data in _user_roles or []:
            user_roles_item = UserCredentialsDtoUserRolesItem.from_dict(user_roles_item_data)

            user_roles.append(user_roles_item)

        username = d.pop("username", UNSET)

        uuid = d.pop("uuid", UNSET)

        user_credentials_dto = cls(
            access=access,
            account_expiry=account_expiry,
            cat_dimension_constraints=cat_dimension_constraints,
            cogs_dimension_constraints=cogs_dimension_constraints,
            disabled=disabled,
            external_auth=external_auth,
            id=id,
            id_token=id_token,
            invitation=invitation,
            last_login=last_login,
            ldap_id=ldap_id,
            open_id=open_id,
            password=password,
            password_last_updated=password_last_updated,
            previous_passwords=previous_passwords,
            restore_expiry=restore_expiry,
            restore_token=restore_token,
            self_registered=self_registered,
            sharing=sharing,
            two_fa=two_fa,
            uid=uid,
            user_roles=user_roles,
            username=username,
            uuid=uuid,
        )

        user_credentials_dto.additional_properties = d
        return user_credentials_dto

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
