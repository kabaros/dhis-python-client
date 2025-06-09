from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_value_category_dto import DataValueCategoryDto


T = TypeVar("T", bound="DataValueFollowUpRequest")


@_attrs_define
class DataValueFollowUpRequest:
    """
    Attributes:
        attribute (Union[Unset, DataValueCategoryDto]):
        attribute_option_combo (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        category_option_combo (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        data_element (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        followup (Union[Unset, bool]):
        org_unit (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        period (Union[Unset, str]):
    """

    attribute: Union[Unset, "DataValueCategoryDto"] = UNSET
    attribute_option_combo: Union[Unset, str] = UNSET
    category_option_combo: Union[Unset, str] = UNSET
    data_element: Union[Unset, str] = UNSET
    followup: Union[Unset, bool] = UNSET
    org_unit: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

        attribute_option_combo = self.attribute_option_combo

        category_option_combo = self.category_option_combo

        data_element = self.data_element

        followup = self.followup

        org_unit = self.org_unit

        period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if category_option_combo is not UNSET:
            field_dict["categoryOptionCombo"] = category_option_combo
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if followup is not UNSET:
            field_dict["followup"] = followup
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if period is not UNSET:
            field_dict["period"] = period

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

        attribute_option_combo = d.pop("attributeOptionCombo", UNSET)

        category_option_combo = d.pop("categoryOptionCombo", UNSET)

        data_element = d.pop("dataElement", UNSET)

        followup = d.pop("followup", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        period = d.pop("period", UNSET)

        data_value_follow_up_request = cls(
            attribute=attribute,
            attribute_option_combo=attribute_option_combo,
            category_option_combo=category_option_combo,
            data_element=data_element,
            followup=followup,
            org_unit=org_unit,
            period=period,
        )

        data_value_follow_up_request.additional_properties = d
        return data_value_follow_up_request

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
