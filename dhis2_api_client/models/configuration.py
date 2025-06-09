from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.configuration_infrastructural_period_type import ConfigurationInfrastructuralPeriodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration_facility_org_unit_group_set import ConfigurationFacilityOrgUnitGroupSet
    from ..models.configuration_facility_org_unit_level import ConfigurationFacilityOrgUnitLevel
    from ..models.configuration_feedback_recipients import ConfigurationFeedbackRecipients
    from ..models.configuration_infrastructural_data_elements import ConfigurationInfrastructuralDataElements
    from ..models.configuration_infrastructural_indicators import ConfigurationInfrastructuralIndicators
    from ..models.configuration_offline_organisation_unit_level import ConfigurationOfflineOrganisationUnitLevel
    from ..models.configuration_self_registration_org_unit import ConfigurationSelfRegistrationOrgUnit
    from ..models.configuration_self_registration_role import ConfigurationSelfRegistrationRole
    from ..models.configuration_system_update_notification_recipients import (
        ConfigurationSystemUpdateNotificationRecipients,
    )


T = TypeVar("T", bound="Configuration")


@_attrs_define
class Configuration:
    """
    Attributes:
        cors_allowlist (Union[Unset, list[str]]):
        cors_whitelist (Union[Unset, list[str]]):
        facility_org_unit_group_set (Union[Unset, ConfigurationFacilityOrgUnitGroupSet]): A UID reference to a
            OrganisationUnitGroupSet
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroupSet`)
        facility_org_unit_level (Union[Unset, ConfigurationFacilityOrgUnitLevel]): A UID reference to a
            OrganisationUnitLevel
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitLevel`)
        feedback_recipients (Union[Unset, ConfigurationFeedbackRecipients]): A UID reference to a UserGroup
            (Java name `org.hisp.dhis.user.UserGroup`)
        infrastructural_data_elements (Union[Unset, ConfigurationInfrastructuralDataElements]): A UID reference to a
            DataElementGroup
            (Java name `org.hisp.dhis.dataelement.DataElementGroup`)
        infrastructural_indicators (Union[Unset, ConfigurationInfrastructuralIndicators]): A UID reference to a
            IndicatorGroup
            (Java name `org.hisp.dhis.indicator.IndicatorGroup`)
        infrastructural_period_type (Union[Unset, ConfigurationInfrastructuralPeriodType]):
        offline_organisation_unit_level (Union[Unset, ConfigurationOfflineOrganisationUnitLevel]): A UID reference to a
            OrganisationUnitLevel
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitLevel`)
        self_registration_org_unit (Union[Unset, ConfigurationSelfRegistrationOrgUnit]): A UID reference to a
            OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        self_registration_role (Union[Unset, ConfigurationSelfRegistrationRole]): A UID reference to a UserRole
            (Java name `org.hisp.dhis.user.UserRole`)
        system_id (Union[Unset, str]):
        system_update_notification_recipients (Union[Unset, ConfigurationSystemUpdateNotificationRecipients]): A UID
            reference to a UserGroup
            (Java name `org.hisp.dhis.user.UserGroup`)
    """

    cors_allowlist: Union[Unset, list[str]] = UNSET
    cors_whitelist: Union[Unset, list[str]] = UNSET
    facility_org_unit_group_set: Union[Unset, "ConfigurationFacilityOrgUnitGroupSet"] = UNSET
    facility_org_unit_level: Union[Unset, "ConfigurationFacilityOrgUnitLevel"] = UNSET
    feedback_recipients: Union[Unset, "ConfigurationFeedbackRecipients"] = UNSET
    infrastructural_data_elements: Union[Unset, "ConfigurationInfrastructuralDataElements"] = UNSET
    infrastructural_indicators: Union[Unset, "ConfigurationInfrastructuralIndicators"] = UNSET
    infrastructural_period_type: Union[Unset, ConfigurationInfrastructuralPeriodType] = UNSET
    offline_organisation_unit_level: Union[Unset, "ConfigurationOfflineOrganisationUnitLevel"] = UNSET
    self_registration_org_unit: Union[Unset, "ConfigurationSelfRegistrationOrgUnit"] = UNSET
    self_registration_role: Union[Unset, "ConfigurationSelfRegistrationRole"] = UNSET
    system_id: Union[Unset, str] = UNSET
    system_update_notification_recipients: Union[Unset, "ConfigurationSystemUpdateNotificationRecipients"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cors_allowlist: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cors_allowlist, Unset):
            cors_allowlist = self.cors_allowlist

        cors_whitelist: Union[Unset, list[str]] = UNSET
        if not isinstance(self.cors_whitelist, Unset):
            cors_whitelist = self.cors_whitelist

        facility_org_unit_group_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.facility_org_unit_group_set, Unset):
            facility_org_unit_group_set = self.facility_org_unit_group_set.to_dict()

        facility_org_unit_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.facility_org_unit_level, Unset):
            facility_org_unit_level = self.facility_org_unit_level.to_dict()

        feedback_recipients: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.feedback_recipients, Unset):
            feedback_recipients = self.feedback_recipients.to_dict()

        infrastructural_data_elements: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.infrastructural_data_elements, Unset):
            infrastructural_data_elements = self.infrastructural_data_elements.to_dict()

        infrastructural_indicators: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.infrastructural_indicators, Unset):
            infrastructural_indicators = self.infrastructural_indicators.to_dict()

        infrastructural_period_type: Union[Unset, str] = UNSET
        if not isinstance(self.infrastructural_period_type, Unset):
            infrastructural_period_type = self.infrastructural_period_type.value

        offline_organisation_unit_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.offline_organisation_unit_level, Unset):
            offline_organisation_unit_level = self.offline_organisation_unit_level.to_dict()

        self_registration_org_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_registration_org_unit, Unset):
            self_registration_org_unit = self.self_registration_org_unit.to_dict()

        self_registration_role: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_registration_role, Unset):
            self_registration_role = self.self_registration_role.to_dict()

        system_id = self.system_id

        system_update_notification_recipients: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system_update_notification_recipients, Unset):
            system_update_notification_recipients = self.system_update_notification_recipients.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cors_allowlist is not UNSET:
            field_dict["corsAllowlist"] = cors_allowlist
        if cors_whitelist is not UNSET:
            field_dict["corsWhitelist"] = cors_whitelist
        if facility_org_unit_group_set is not UNSET:
            field_dict["facilityOrgUnitGroupSet"] = facility_org_unit_group_set
        if facility_org_unit_level is not UNSET:
            field_dict["facilityOrgUnitLevel"] = facility_org_unit_level
        if feedback_recipients is not UNSET:
            field_dict["feedbackRecipients"] = feedback_recipients
        if infrastructural_data_elements is not UNSET:
            field_dict["infrastructuralDataElements"] = infrastructural_data_elements
        if infrastructural_indicators is not UNSET:
            field_dict["infrastructuralIndicators"] = infrastructural_indicators
        if infrastructural_period_type is not UNSET:
            field_dict["infrastructuralPeriodType"] = infrastructural_period_type
        if offline_organisation_unit_level is not UNSET:
            field_dict["offlineOrganisationUnitLevel"] = offline_organisation_unit_level
        if self_registration_org_unit is not UNSET:
            field_dict["selfRegistrationOrgUnit"] = self_registration_org_unit
        if self_registration_role is not UNSET:
            field_dict["selfRegistrationRole"] = self_registration_role
        if system_id is not UNSET:
            field_dict["systemId"] = system_id
        if system_update_notification_recipients is not UNSET:
            field_dict["systemUpdateNotificationRecipients"] = system_update_notification_recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.configuration_facility_org_unit_group_set import ConfigurationFacilityOrgUnitGroupSet
        from ..models.configuration_facility_org_unit_level import ConfigurationFacilityOrgUnitLevel
        from ..models.configuration_feedback_recipients import ConfigurationFeedbackRecipients
        from ..models.configuration_infrastructural_data_elements import ConfigurationInfrastructuralDataElements
        from ..models.configuration_infrastructural_indicators import ConfigurationInfrastructuralIndicators
        from ..models.configuration_offline_organisation_unit_level import ConfigurationOfflineOrganisationUnitLevel
        from ..models.configuration_self_registration_org_unit import ConfigurationSelfRegistrationOrgUnit
        from ..models.configuration_self_registration_role import ConfigurationSelfRegistrationRole
        from ..models.configuration_system_update_notification_recipients import (
            ConfigurationSystemUpdateNotificationRecipients,
        )

        d = src_dict.copy()
        cors_allowlist = cast(list[str], d.pop("corsAllowlist", UNSET))

        cors_whitelist = cast(list[str], d.pop("corsWhitelist", UNSET))

        _facility_org_unit_group_set = d.pop("facilityOrgUnitGroupSet", UNSET)
        facility_org_unit_group_set: Union[Unset, ConfigurationFacilityOrgUnitGroupSet]
        if isinstance(_facility_org_unit_group_set, Unset):
            facility_org_unit_group_set = UNSET
        else:
            facility_org_unit_group_set = ConfigurationFacilityOrgUnitGroupSet.from_dict(_facility_org_unit_group_set)

        _facility_org_unit_level = d.pop("facilityOrgUnitLevel", UNSET)
        facility_org_unit_level: Union[Unset, ConfigurationFacilityOrgUnitLevel]
        if isinstance(_facility_org_unit_level, Unset):
            facility_org_unit_level = UNSET
        else:
            facility_org_unit_level = ConfigurationFacilityOrgUnitLevel.from_dict(_facility_org_unit_level)

        _feedback_recipients = d.pop("feedbackRecipients", UNSET)
        feedback_recipients: Union[Unset, ConfigurationFeedbackRecipients]
        if isinstance(_feedback_recipients, Unset):
            feedback_recipients = UNSET
        else:
            feedback_recipients = ConfigurationFeedbackRecipients.from_dict(_feedback_recipients)

        _infrastructural_data_elements = d.pop("infrastructuralDataElements", UNSET)
        infrastructural_data_elements: Union[Unset, ConfigurationInfrastructuralDataElements]
        if isinstance(_infrastructural_data_elements, Unset):
            infrastructural_data_elements = UNSET
        else:
            infrastructural_data_elements = ConfigurationInfrastructuralDataElements.from_dict(
                _infrastructural_data_elements
            )

        _infrastructural_indicators = d.pop("infrastructuralIndicators", UNSET)
        infrastructural_indicators: Union[Unset, ConfigurationInfrastructuralIndicators]
        if isinstance(_infrastructural_indicators, Unset):
            infrastructural_indicators = UNSET
        else:
            infrastructural_indicators = ConfigurationInfrastructuralIndicators.from_dict(_infrastructural_indicators)

        _infrastructural_period_type = d.pop("infrastructuralPeriodType", UNSET)
        infrastructural_period_type: Union[Unset, ConfigurationInfrastructuralPeriodType]
        if isinstance(_infrastructural_period_type, Unset):
            infrastructural_period_type = UNSET
        else:
            infrastructural_period_type = ConfigurationInfrastructuralPeriodType(_infrastructural_period_type)

        _offline_organisation_unit_level = d.pop("offlineOrganisationUnitLevel", UNSET)
        offline_organisation_unit_level: Union[Unset, ConfigurationOfflineOrganisationUnitLevel]
        if isinstance(_offline_organisation_unit_level, Unset):
            offline_organisation_unit_level = UNSET
        else:
            offline_organisation_unit_level = ConfigurationOfflineOrganisationUnitLevel.from_dict(
                _offline_organisation_unit_level
            )

        _self_registration_org_unit = d.pop("selfRegistrationOrgUnit", UNSET)
        self_registration_org_unit: Union[Unset, ConfigurationSelfRegistrationOrgUnit]
        if isinstance(_self_registration_org_unit, Unset):
            self_registration_org_unit = UNSET
        else:
            self_registration_org_unit = ConfigurationSelfRegistrationOrgUnit.from_dict(_self_registration_org_unit)

        _self_registration_role = d.pop("selfRegistrationRole", UNSET)
        self_registration_role: Union[Unset, ConfigurationSelfRegistrationRole]
        if isinstance(_self_registration_role, Unset):
            self_registration_role = UNSET
        else:
            self_registration_role = ConfigurationSelfRegistrationRole.from_dict(_self_registration_role)

        system_id = d.pop("systemId", UNSET)

        _system_update_notification_recipients = d.pop("systemUpdateNotificationRecipients", UNSET)
        system_update_notification_recipients: Union[Unset, ConfigurationSystemUpdateNotificationRecipients]
        if isinstance(_system_update_notification_recipients, Unset):
            system_update_notification_recipients = UNSET
        else:
            system_update_notification_recipients = ConfigurationSystemUpdateNotificationRecipients.from_dict(
                _system_update_notification_recipients
            )

        configuration = cls(
            cors_allowlist=cors_allowlist,
            cors_whitelist=cors_whitelist,
            facility_org_unit_group_set=facility_org_unit_group_set,
            facility_org_unit_level=facility_org_unit_level,
            feedback_recipients=feedback_recipients,
            infrastructural_data_elements=infrastructural_data_elements,
            infrastructural_indicators=infrastructural_indicators,
            infrastructural_period_type=infrastructural_period_type,
            offline_organisation_unit_level=offline_organisation_unit_level,
            self_registration_org_unit=self_registration_org_unit,
            self_registration_role=self_registration_role,
            system_id=system_id,
            system_update_notification_recipients=system_update_notification_recipients,
        )

        configuration.additional_properties = d
        return configuration

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
