import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_value_category_dto import DataValueCategoryDto


T = TypeVar("T", bound="DataValueDto")


@_attrs_define
class DataValueDto:
    """
    Attributes:
        attribute (Union[Unset, DataValueCategoryDto]):
        category_option_combo (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        comment (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        data_element (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        data_set (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        follow_up (Union[Unset, bool]):
        force (Union[Unset, bool]):
        last_updated (Union[Unset, datetime.datetime]):
        org_unit (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        period (Union[Unset, str]):
        stored_by (Union[Unset, str]):
        value (Union[Unset, str]):
    """

    attribute: Union[Unset, "DataValueCategoryDto"] = UNSET
    category_option_combo: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    data_element: Union[Unset, str] = UNSET
    data_set: Union[Unset, str] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    force: Union[Unset, bool] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    org_unit: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    stored_by: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

        category_option_combo = self.category_option_combo

        comment = self.comment

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        data_element = self.data_element

        data_set = self.data_set

        follow_up = self.follow_up

        force = self.force

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        org_unit = self.org_unit

        period = self.period

        stored_by = self.stored_by

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if category_option_combo is not UNSET:
            field_dict["categoryOptionCombo"] = category_option_combo
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created is not UNSET:
            field_dict["created"] = created
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if force is not UNSET:
            field_dict["force"] = force
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if period is not UNSET:
            field_dict["period"] = period
        if stored_by is not UNSET:
            field_dict["storedBy"] = stored_by
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_value_category_dto import DataValueCategoryDto

        d = src_dict.copy()
        _attribute = d.pop("attribute", UNSET)
        attribute: Union[Unset, DataValueCategoryDto]
        if isinstance(_attribute, Unset):
            attribute = UNSET
        else:
            attribute = DataValueCategoryDto.from_dict(_attribute)

        category_option_combo = d.pop("categoryOptionCombo", UNSET)

        comment = d.pop("comment", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        data_element = d.pop("dataElement", UNSET)

        data_set = d.pop("dataSet", UNSET)

        follow_up = d.pop("followUp", UNSET)

        force = d.pop("force", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        org_unit = d.pop("orgUnit", UNSET)

        period = d.pop("period", UNSET)

        stored_by = d.pop("storedBy", UNSET)

        value = d.pop("value", UNSET)

        data_value_dto = cls(
            attribute=attribute,
            category_option_combo=category_option_combo,
            comment=comment,
            created=created,
            data_element=data_element,
            data_set=data_set,
            follow_up=follow_up,
            force=force,
            last_updated=last_updated,
            org_unit=org_unit,
            period=period,
            stored_by=stored_by,
            value=value,
        )

        data_value_dto.additional_properties = d
        return data_value_dto

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
