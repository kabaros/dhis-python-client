from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.granted_authority import GrantedAuthority
    from ..models.user_details_user_settings import UserDetailsUserSettings


T = TypeVar("T", bound="UserDetails")


@_attrs_define
class UserDetails:
    """
    Attributes:
        account_non_expired (Union[Unset, bool]):
        account_non_locked (Union[Unset, bool]):
        all_authorities (Union[Unset, list[str]]):
        authorities (Union[Unset, list['GrantedAuthority']]):
        code (Union[Unset, str]):
        credentials_non_expired (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        external_auth (Union[Unset, bool]):
        first_name (Union[Unset, str]):
        id (Union[Unset, int]):
        password (Union[Unset, str]):
        super_ (Union[Unset, bool]):
        surname (Union[Unset, str]):
        two_factor_enabled (Union[Unset, bool]):
        uid (Union[Unset, str]):
        user_data_org_unit_ids (Union[Unset, list[str]]):
        user_group_ids (Union[Unset, list[str]]):
        user_org_unit_ids (Union[Unset, list[str]]):
        user_role_ids (Union[Unset, list[str]]):
        user_search_org_unit_ids (Union[Unset, list[str]]):
        user_settings (Union[Unset, UserDetailsUserSettings]):
        username (Union[Unset, str]):
    """

    account_non_expired: Union[Unset, bool] = UNSET
    account_non_locked: Union[Unset, bool] = UNSET
    all_authorities: Union[Unset, list[str]] = UNSET
    authorities: Union[Unset, list["GrantedAuthority"]] = UNSET
    code: Union[Unset, str] = UNSET
    credentials_non_expired: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    external_auth: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    password: Union[Unset, str] = UNSET
    super_: Union[Unset, bool] = UNSET
    surname: Union[Unset, str] = UNSET
    two_factor_enabled: Union[Unset, bool] = UNSET
    uid: Union[Unset, str] = UNSET
    user_data_org_unit_ids: Union[Unset, list[str]] = UNSET
    user_group_ids: Union[Unset, list[str]] = UNSET
    user_org_unit_ids: Union[Unset, list[str]] = UNSET
    user_role_ids: Union[Unset, list[str]] = UNSET
    user_search_org_unit_ids: Union[Unset, list[str]] = UNSET
    user_settings: Union[Unset, "UserDetailsUserSettings"] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_non_expired = self.account_non_expired

        account_non_locked = self.account_non_locked

        all_authorities: Union[Unset, list[str]] = UNSET
        if not isinstance(self.all_authorities, Unset):
            all_authorities = self.all_authorities

        authorities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.authorities, Unset):
            authorities = []
            for authorities_item_data in self.authorities:
                authorities_item = authorities_item_data.to_dict()
                authorities.append(authorities_item)

        code = self.code

        credentials_non_expired = self.credentials_non_expired

        enabled = self.enabled

        external_auth = self.external_auth

        first_name = self.first_name

        id = self.id

        password = self.password

        super_ = self.super_

        surname = self.surname

        two_factor_enabled = self.two_factor_enabled

        uid = self.uid

        user_data_org_unit_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_data_org_unit_ids, Unset):
            user_data_org_unit_ids = self.user_data_org_unit_ids

        user_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_group_ids, Unset):
            user_group_ids = self.user_group_ids

        user_org_unit_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_org_unit_ids, Unset):
            user_org_unit_ids = self.user_org_unit_ids

        user_role_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_role_ids, Unset):
            user_role_ids = self.user_role_ids

        user_search_org_unit_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.user_search_org_unit_ids, Unset):
            user_search_org_unit_ids = self.user_search_org_unit_ids

        user_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_settings, Unset):
            user_settings = self.user_settings.to_dict()

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_non_expired is not UNSET:
            field_dict["accountNonExpired"] = account_non_expired
        if account_non_locked is not UNSET:
            field_dict["accountNonLocked"] = account_non_locked
        if all_authorities is not UNSET:
            field_dict["allAuthorities"] = all_authorities
        if authorities is not UNSET:
            field_dict["authorities"] = authorities
        if code is not UNSET:
            field_dict["code"] = code
        if credentials_non_expired is not UNSET:
            field_dict["credentialsNonExpired"] = credentials_non_expired
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if external_auth is not UNSET:
            field_dict["externalAuth"] = external_auth
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if password is not UNSET:
            field_dict["password"] = password
        if super_ is not UNSET:
            field_dict["super"] = super_
        if surname is not UNSET:
            field_dict["surname"] = surname
        if two_factor_enabled is not UNSET:
            field_dict["twoFactorEnabled"] = two_factor_enabled
        if uid is not UNSET:
            field_dict["uid"] = uid
        if user_data_org_unit_ids is not UNSET:
            field_dict["userDataOrgUnitIds"] = user_data_org_unit_ids
        if user_group_ids is not UNSET:
            field_dict["userGroupIds"] = user_group_ids
        if user_org_unit_ids is not UNSET:
            field_dict["userOrgUnitIds"] = user_org_unit_ids
        if user_role_ids is not UNSET:
            field_dict["userRoleIds"] = user_role_ids
        if user_search_org_unit_ids is not UNSET:
            field_dict["userSearchOrgUnitIds"] = user_search_org_unit_ids
        if user_settings is not UNSET:
            field_dict["userSettings"] = user_settings
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.granted_authority import GrantedAuthority
        from ..models.user_details_user_settings import UserDetailsUserSettings

        d = src_dict.copy()
        account_non_expired = d.pop("accountNonExpired", UNSET)

        account_non_locked = d.pop("accountNonLocked", UNSET)

        all_authorities = cast(list[str], d.pop("allAuthorities", UNSET))

        authorities = []
        _authorities = d.pop("authorities", UNSET)
        for authorities_item_data in _authorities or []:
            authorities_item = GrantedAuthority.from_dict(authorities_item_data)

            authorities.append(authorities_item)

        code = d.pop("code", UNSET)

        credentials_non_expired = d.pop("credentialsNonExpired", UNSET)

        enabled = d.pop("enabled", UNSET)

        external_auth = d.pop("externalAuth", UNSET)

        first_name = d.pop("firstName", UNSET)

        id = d.pop("id", UNSET)

        password = d.pop("password", UNSET)

        super_ = d.pop("super", UNSET)

        surname = d.pop("surname", UNSET)

        two_factor_enabled = d.pop("twoFactorEnabled", UNSET)

        uid = d.pop("uid", UNSET)

        user_data_org_unit_ids = cast(list[str], d.pop("userDataOrgUnitIds", UNSET))

        user_group_ids = cast(list[str], d.pop("userGroupIds", UNSET))

        user_org_unit_ids = cast(list[str], d.pop("userOrgUnitIds", UNSET))

        user_role_ids = cast(list[str], d.pop("userRoleIds", UNSET))

        user_search_org_unit_ids = cast(list[str], d.pop("userSearchOrgUnitIds", UNSET))

        _user_settings = d.pop("userSettings", UNSET)
        user_settings: Union[Unset, UserDetailsUserSettings]
        if isinstance(_user_settings, Unset):
            user_settings = UNSET
        else:
            user_settings = UserDetailsUserSettings.from_dict(_user_settings)

        username = d.pop("username", UNSET)

        user_details = cls(
            account_non_expired=account_non_expired,
            account_non_locked=account_non_locked,
            all_authorities=all_authorities,
            authorities=authorities,
            code=code,
            credentials_non_expired=credentials_non_expired,
            enabled=enabled,
            external_auth=external_auth,
            first_name=first_name,
            id=id,
            password=password,
            super_=super_,
            surname=surname,
            two_factor_enabled=two_factor_enabled,
            uid=uid,
            user_data_org_unit_ids=user_data_org_unit_ids,
            user_group_ids=user_group_ids,
            user_org_unit_ids=user_org_unit_ids,
            user_role_ids=user_role_ids,
            user_search_org_unit_ids=user_search_org_unit_ids,
            user_settings=user_settings,
            username=username,
        )

        user_details.additional_properties = d
        return user_details

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
