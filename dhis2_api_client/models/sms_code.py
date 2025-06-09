from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sms_code_data_element import SMSCodeDataElement
    from ..models.sms_code_option_id import SMSCodeOptionId
    from ..models.sms_code_tracked_entity_attribute import SMSCodeTrackedEntityAttribute


T = TypeVar("T", bound="SMSCode")


@_attrs_define
class SMSCode:
    """
    Attributes:
        code (Union[Unset, str]):
        compulsory (Union[Unset, bool]):
        data_element (Union[Unset, SMSCodeDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        formula (Union[Unset, str]):
        option_id (Union[Unset, SMSCodeOptionId]): A UID reference to a CategoryOptionCombo
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`)
        tracked_entity_attribute (Union[Unset, SMSCodeTrackedEntityAttribute]): A UID reference to a
            TrackedEntityAttribute
            (Java name `org.hisp.dhis.trackedentity.TrackedEntityAttribute`)
    """

    code: Union[Unset, str] = UNSET
    compulsory: Union[Unset, bool] = UNSET
    data_element: Union[Unset, "SMSCodeDataElement"] = UNSET
    formula: Union[Unset, str] = UNSET
    option_id: Union[Unset, "SMSCodeOptionId"] = UNSET
    tracked_entity_attribute: Union[Unset, "SMSCodeTrackedEntityAttribute"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        compulsory = self.compulsory

        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

        formula = self.formula

        option_id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.option_id, Unset):
            option_id = self.option_id.to_dict()

        tracked_entity_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tracked_entity_attribute, Unset):
            tracked_entity_attribute = self.tracked_entity_attribute.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if compulsory is not UNSET:
            field_dict["compulsory"] = compulsory
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if formula is not UNSET:
            field_dict["formula"] = formula
        if option_id is not UNSET:
            field_dict["optionId"] = option_id
        if tracked_entity_attribute is not UNSET:
            field_dict["trackedEntityAttribute"] = tracked_entity_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sms_code_data_element import SMSCodeDataElement
        from ..models.sms_code_option_id import SMSCodeOptionId
        from ..models.sms_code_tracked_entity_attribute import SMSCodeTrackedEntityAttribute

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        compulsory = d.pop("compulsory", UNSET)

        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, SMSCodeDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = SMSCodeDataElement.from_dict(_data_element)

        formula = d.pop("formula", UNSET)

        _option_id = d.pop("optionId", UNSET)
        option_id: Union[Unset, SMSCodeOptionId]
        if isinstance(_option_id, Unset):
            option_id = UNSET
        else:
            option_id = SMSCodeOptionId.from_dict(_option_id)

        _tracked_entity_attribute = d.pop("trackedEntityAttribute", UNSET)
        tracked_entity_attribute: Union[Unset, SMSCodeTrackedEntityAttribute]
        if isinstance(_tracked_entity_attribute, Unset):
            tracked_entity_attribute = UNSET
        else:
            tracked_entity_attribute = SMSCodeTrackedEntityAttribute.from_dict(_tracked_entity_attribute)

        sms_code = cls(
            code=code,
            compulsory=compulsory,
            data_element=data_element,
            formula=formula,
            option_id=option_id,
            tracked_entity_attribute=tracked_entity_attribute,
        )

        sms_code.additional_properties = d
        return sms_code

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
