import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_value_audit_dto_audit_type import DataValueAuditDtoAuditType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataValueAuditDto")


@_attrs_define
class DataValueAuditDto:
    """
    Attributes:
        audit_type (DataValueAuditDtoAuditType):
        attribute_option_combo (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        category_option_combo (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        created (Union[Unset, datetime.datetime]):
        data_element (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        modified_by (Union[Unset, str]):
        org_unit (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        period (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    audit_type: DataValueAuditDtoAuditType
    attribute_option_combo: Union[Unset, str] = UNSET
    category_option_combo: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    data_element: Union[Unset, str] = UNSET
    modified_by: Union[Unset, str] = UNSET
    org_unit: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audit_type = self.audit_type.value

        attribute_option_combo = self.attribute_option_combo

        category_option_combo = self.category_option_combo

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        data_element = self.data_element

        modified_by = self.modified_by

        org_unit = self.org_unit

        period = self.period

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auditType": audit_type,
            }
        )
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if category_option_combo is not UNSET:
            field_dict["categoryOptionCombo"] = category_option_combo
        if created is not UNSET:
            field_dict["created"] = created
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if period is not UNSET:
            field_dict["period"] = period
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        audit_type = DataValueAuditDtoAuditType(d.pop("auditType"))

        attribute_option_combo = d.pop("attributeOptionCombo", UNSET)

        category_option_combo = d.pop("categoryOptionCombo", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        data_element = d.pop("dataElement", UNSET)

        modified_by = d.pop("modifiedBy", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        period = d.pop("period", UNSET)

        value = d.pop("value", UNSET)

        data_value_audit_dto = cls(
            audit_type=audit_type,
            attribute_option_combo=attribute_option_combo,
            category_option_combo=category_option_combo,
            created=created,
            data_element=data_element,
            modified_by=modified_by,
            org_unit=org_unit,
            period=period,
            value=value,
        )

        data_value_audit_dto.additional_properties = d
        return data_value_audit_dto

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
