from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.program_message_recipients_organisation_unit import ProgramMessageRecipientsOrganisationUnit
    from ..models.program_message_recipients_tracked_entity import ProgramMessageRecipientsTrackedEntity


T = TypeVar("T", bound="ProgramMessageRecipients")


@_attrs_define
class ProgramMessageRecipients:
    """
    Attributes:
        email_addresses (Union[Unset, list[str]]):
        organisation_unit (Union[Unset, ProgramMessageRecipientsOrganisationUnit]): A UID reference to a
            OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        phone_numbers (Union[Unset, list[str]]):
        tracked_entity (Union[Unset, ProgramMessageRecipientsTrackedEntity]): A UID reference to a TrackedEntity
            (Java name `org.hisp.dhis.trackedentity.TrackedEntity`)
    """

    email_addresses: Union[Unset, list[str]] = UNSET
    organisation_unit: Union[Unset, "ProgramMessageRecipientsOrganisationUnit"] = UNSET
    phone_numbers: Union[Unset, list[str]] = UNSET
    tracked_entity: Union[Unset, "ProgramMessageRecipientsTrackedEntity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.email_addresses, Unset):
            email_addresses = self.email_addresses

        organisation_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit, Unset):
            organisation_unit = self.organisation_unit.to_dict()

        phone_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = self.phone_numbers

        tracked_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity, Unset):
            tracked_entity = self.tracked_entity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_addresses is not UNSET:
            field_dict["emailAddresses"] = email_addresses
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if phone_numbers is not UNSET:
            field_dict["phoneNumbers"] = phone_numbers
        if tracked_entity is not UNSET:
            field_dict["trackedEntity"] = tracked_entity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.program_message_recipients_organisation_unit import ProgramMessageRecipientsOrganisationUnit
        from ..models.program_message_recipients_tracked_entity import ProgramMessageRecipientsTrackedEntity

        d = src_dict.copy()
        email_addresses = cast(list[str], d.pop("emailAddresses", UNSET))

        _organisation_unit = d.pop("organisationUnit", UNSET)
        organisation_unit: Union[Unset, ProgramMessageRecipientsOrganisationUnit]
        if isinstance(_organisation_unit, Unset):
            organisation_unit = UNSET
        else:
            organisation_unit = ProgramMessageRecipientsOrganisationUnit.from_dict(_organisation_unit)

        phone_numbers = cast(list[str], d.pop("phoneNumbers", UNSET))

        _tracked_entity = d.pop("trackedEntity", UNSET)
        tracked_entity: Union[Unset, ProgramMessageRecipientsTrackedEntity]
        if isinstance(_tracked_entity, Unset):
            tracked_entity = UNSET
        else:
            tracked_entity = ProgramMessageRecipientsTrackedEntity.from_dict(_tracked_entity)

        program_message_recipients = cls(
            email_addresses=email_addresses,
            organisation_unit=organisation_unit,
            phone_numbers=phone_numbers,
            tracked_entity=tracked_entity,
        )

        program_message_recipients.additional_properties = d
        return program_message_recipients

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
