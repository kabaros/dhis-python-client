from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_oidc_provider import LoginOidcProvider


T = TypeVar("T", bound="LoginConfigResponse")


@_attrs_define
class LoginConfigResponse:
    """
    Attributes:
        allow_account_recovery (Union[Unset, bool]):
        api_version (Union[Unset, str]):
        application_description (Union[Unset, str]):
        application_left_side_footer (Union[Unset, str]):
        application_notification (Union[Unset, str]):
        application_right_side_footer (Union[Unset, str]):
        application_title (Union[Unset, str]):
        country_flag (Union[Unset, str]):
        email_configured (Union[Unset, bool]):
        login_page_layout (Union[Unset, str]):
        login_page_logo (Union[Unset, str]):
        login_page_template (Union[Unset, str]):
        login_popup (Union[Unset, str]):
        oidc_providers (Union[Unset, list['LoginOidcProvider']]):
        recaptcha_site (Union[Unset, str]):
        self_registration_enabled (Union[Unset, bool]):
        self_registration_no_recaptcha (Union[Unset, bool]):
        ui_locale (Union[Unset, str]):
        use_custom_logo_front (Union[Unset, bool]):
    """

    allow_account_recovery: Union[Unset, bool] = UNSET
    api_version: Union[Unset, str] = UNSET
    application_description: Union[Unset, str] = UNSET
    application_left_side_footer: Union[Unset, str] = UNSET
    application_notification: Union[Unset, str] = UNSET
    application_right_side_footer: Union[Unset, str] = UNSET
    application_title: Union[Unset, str] = UNSET
    country_flag: Union[Unset, str] = UNSET
    email_configured: Union[Unset, bool] = UNSET
    login_page_layout: Union[Unset, str] = UNSET
    login_page_logo: Union[Unset, str] = UNSET
    login_page_template: Union[Unset, str] = UNSET
    login_popup: Union[Unset, str] = UNSET
    oidc_providers: Union[Unset, list["LoginOidcProvider"]] = UNSET
    recaptcha_site: Union[Unset, str] = UNSET
    self_registration_enabled: Union[Unset, bool] = UNSET
    self_registration_no_recaptcha: Union[Unset, bool] = UNSET
    ui_locale: Union[Unset, str] = UNSET
    use_custom_logo_front: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_account_recovery = self.allow_account_recovery

        api_version = self.api_version

        application_description = self.application_description

        application_left_side_footer = self.application_left_side_footer

        application_notification = self.application_notification

        application_right_side_footer = self.application_right_side_footer

        application_title = self.application_title

        country_flag = self.country_flag

        email_configured = self.email_configured

        login_page_layout = self.login_page_layout

        login_page_logo = self.login_page_logo

        login_page_template = self.login_page_template

        login_popup = self.login_popup

        oidc_providers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.oidc_providers, Unset):
            oidc_providers = []
            for oidc_providers_item_data in self.oidc_providers:
                oidc_providers_item = oidc_providers_item_data.to_dict()
                oidc_providers.append(oidc_providers_item)

        recaptcha_site = self.recaptcha_site

        self_registration_enabled = self.self_registration_enabled

        self_registration_no_recaptcha = self.self_registration_no_recaptcha

        ui_locale = self.ui_locale

        use_custom_logo_front = self.use_custom_logo_front

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_account_recovery is not UNSET:
            field_dict["allowAccountRecovery"] = allow_account_recovery
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version
        if application_description is not UNSET:
            field_dict["applicationDescription"] = application_description
        if application_left_side_footer is not UNSET:
            field_dict["applicationLeftSideFooter"] = application_left_side_footer
        if application_notification is not UNSET:
            field_dict["applicationNotification"] = application_notification
        if application_right_side_footer is not UNSET:
            field_dict["applicationRightSideFooter"] = application_right_side_footer
        if application_title is not UNSET:
            field_dict["applicationTitle"] = application_title
        if country_flag is not UNSET:
            field_dict["countryFlag"] = country_flag
        if email_configured is not UNSET:
            field_dict["emailConfigured"] = email_configured
        if login_page_layout is not UNSET:
            field_dict["loginPageLayout"] = login_page_layout
        if login_page_logo is not UNSET:
            field_dict["loginPageLogo"] = login_page_logo
        if login_page_template is not UNSET:
            field_dict["loginPageTemplate"] = login_page_template
        if login_popup is not UNSET:
            field_dict["loginPopup"] = login_popup
        if oidc_providers is not UNSET:
            field_dict["oidcProviders"] = oidc_providers
        if recaptcha_site is not UNSET:
            field_dict["recaptchaSite"] = recaptcha_site
        if self_registration_enabled is not UNSET:
            field_dict["selfRegistrationEnabled"] = self_registration_enabled
        if self_registration_no_recaptcha is not UNSET:
            field_dict["selfRegistrationNoRecaptcha"] = self_registration_no_recaptcha
        if ui_locale is not UNSET:
            field_dict["uiLocale"] = ui_locale
        if use_custom_logo_front is not UNSET:
            field_dict["useCustomLogoFront"] = use_custom_logo_front

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.login_oidc_provider import LoginOidcProvider

        d = src_dict.copy()
        allow_account_recovery = d.pop("allowAccountRecovery", UNSET)

        api_version = d.pop("apiVersion", UNSET)

        application_description = d.pop("applicationDescription", UNSET)

        application_left_side_footer = d.pop("applicationLeftSideFooter", UNSET)

        application_notification = d.pop("applicationNotification", UNSET)

        application_right_side_footer = d.pop("applicationRightSideFooter", UNSET)

        application_title = d.pop("applicationTitle", UNSET)

        country_flag = d.pop("countryFlag", UNSET)

        email_configured = d.pop("emailConfigured", UNSET)

        login_page_layout = d.pop("loginPageLayout", UNSET)

        login_page_logo = d.pop("loginPageLogo", UNSET)

        login_page_template = d.pop("loginPageTemplate", UNSET)

        login_popup = d.pop("loginPopup", UNSET)

        oidc_providers = []
        _oidc_providers = d.pop("oidcProviders", UNSET)
        for oidc_providers_item_data in _oidc_providers or []:
            oidc_providers_item = LoginOidcProvider.from_dict(oidc_providers_item_data)

            oidc_providers.append(oidc_providers_item)

        recaptcha_site = d.pop("recaptchaSite", UNSET)

        self_registration_enabled = d.pop("selfRegistrationEnabled", UNSET)

        self_registration_no_recaptcha = d.pop("selfRegistrationNoRecaptcha", UNSET)

        ui_locale = d.pop("uiLocale", UNSET)

        use_custom_logo_front = d.pop("useCustomLogoFront", UNSET)

        login_config_response = cls(
            allow_account_recovery=allow_account_recovery,
            api_version=api_version,
            application_description=application_description,
            application_left_side_footer=application_left_side_footer,
            application_notification=application_notification,
            application_right_side_footer=application_right_side_footer,
            application_title=application_title,
            country_flag=country_flag,
            email_configured=email_configured,
            login_page_layout=login_page_layout,
            login_page_logo=login_page_logo,
            login_page_template=login_page_template,
            login_popup=login_popup,
            oidc_providers=oidc_providers,
            recaptcha_site=recaptcha_site,
            self_registration_enabled=self_registration_enabled,
            self_registration_no_recaptcha=self_registration_no_recaptcha,
            ui_locale=ui_locale,
            use_custom_logo_front=use_custom_logo_front,
        )

        login_config_response.additional_properties = d
        return login_config_response

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
