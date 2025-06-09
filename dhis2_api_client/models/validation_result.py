import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_result_attribute_option_combo import ValidationResultAttributeOptionCombo
    from ..models.validation_result_organisation_unit import ValidationResultOrganisationUnit
    from ..models.validation_result_validation_rule import ValidationResultValidationRule


T = TypeVar("T", bound="ValidationResult")


@_attrs_define
class ValidationResult:
    """
    Attributes:
        day_in_period (int):
        id (int):
        attribute_option_combo (Union[Unset, ValidationResultAttributeOptionCombo]): A UID reference to a
            CategoryOptionCombo
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`)
        created (Union[Unset, datetime.datetime]):
        leftside_value (Union[Unset, float]):
        notification_sent (Union[Unset, bool]):
        organisation_unit (Union[Unset, ValidationResultOrganisationUnit]): A UID reference to a OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        period (Union[Unset, str]):
        rightside_value (Union[Unset, float]):
        validation_rule (Union[Unset, ValidationResultValidationRule]): A UID reference to a ValidationRule
            (Java name `org.hisp.dhis.validation.ValidationRule`)
    """

    day_in_period: int
    id: int
    attribute_option_combo: Union[Unset, "ValidationResultAttributeOptionCombo"] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    leftside_value: Union[Unset, float] = UNSET
    notification_sent: Union[Unset, bool] = UNSET
    organisation_unit: Union[Unset, "ValidationResultOrganisationUnit"] = UNSET
    period: Union[Unset, str] = UNSET
    rightside_value: Union[Unset, float] = UNSET
    validation_rule: Union[Unset, "ValidationResultValidationRule"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_in_period = self.day_in_period

        id = self.id

        attribute_option_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute_option_combo, Unset):
            attribute_option_combo = self.attribute_option_combo.to_dict()

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        leftside_value = self.leftside_value

        notification_sent = self.notification_sent

        organisation_unit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organisation_unit, Unset):
            organisation_unit = self.organisation_unit.to_dict()

        period = self.period

        rightside_value = self.rightside_value

        validation_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.validation_rule, Unset):
            validation_rule = self.validation_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dayInPeriod": day_in_period,
                "id": id,
            }
        )
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if created is not UNSET:
            field_dict["created"] = created
        if leftside_value is not UNSET:
            field_dict["leftsideValue"] = leftside_value
        if notification_sent is not UNSET:
            field_dict["notificationSent"] = notification_sent
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if period is not UNSET:
            field_dict["period"] = period
        if rightside_value is not UNSET:
            field_dict["rightsideValue"] = rightside_value
        if validation_rule is not UNSET:
            field_dict["validationRule"] = validation_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.validation_result_attribute_option_combo import ValidationResultAttributeOptionCombo
        from ..models.validation_result_organisation_unit import ValidationResultOrganisationUnit
        from ..models.validation_result_validation_rule import ValidationResultValidationRule

        d = src_dict.copy()
        day_in_period = d.pop("dayInPeriod")

        id = d.pop("id")

        _attribute_option_combo = d.pop("attributeOptionCombo", UNSET)
        attribute_option_combo: Union[Unset, ValidationResultAttributeOptionCombo]
        if isinstance(_attribute_option_combo, Unset):
            attribute_option_combo = UNSET
        else:
            attribute_option_combo = ValidationResultAttributeOptionCombo.from_dict(_attribute_option_combo)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        leftside_value = d.pop("leftsideValue", UNSET)

        notification_sent = d.pop("notificationSent", UNSET)

        _organisation_unit = d.pop("organisationUnit", UNSET)
        organisation_unit: Union[Unset, ValidationResultOrganisationUnit]
        if isinstance(_organisation_unit, Unset):
            organisation_unit = UNSET
        else:
            organisation_unit = ValidationResultOrganisationUnit.from_dict(_organisation_unit)

        period = d.pop("period", UNSET)

        rightside_value = d.pop("rightsideValue", UNSET)

        _validation_rule = d.pop("validationRule", UNSET)
        validation_rule: Union[Unset, ValidationResultValidationRule]
        if isinstance(_validation_rule, Unset):
            validation_rule = UNSET
        else:
            validation_rule = ValidationResultValidationRule.from_dict(_validation_rule)

        validation_result = cls(
            day_in_period=day_in_period,
            id=id,
            attribute_option_combo=attribute_option_combo,
            created=created,
            leftside_value=leftside_value,
            notification_sent=notification_sent,
            organisation_unit=organisation_unit,
            period=period,
            rightside_value=rightside_value,
            validation_rule=validation_rule,
        )

        validation_result.additional_properties = d
        return validation_result

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
