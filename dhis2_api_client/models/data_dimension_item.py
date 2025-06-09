from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.data_dimension_item_data_dimension_item_type import DataDimensionItemDataDimensionItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_dimension_item_data_element import DataDimensionItemDataElement
    from ..models.data_dimension_item_expression_dimension_item import DataDimensionItemExpressionDimensionItem
    from ..models.data_dimension_item_indicator import DataDimensionItemIndicator
    from ..models.data_dimension_item_program_indicator import DataDimensionItemProgramIndicator
    from ..models.data_dimension_item_subexpression_dimension_item import DataDimensionItemSubexpressionDimensionItem
    from ..models.data_element_operand import DataElementOperand
    from ..models.program_data_element_dimension_item import ProgramDataElementDimensionItem
    from ..models.program_tracked_entity_attribute_dimension_item import ProgramTrackedEntityAttributeDimensionItem
    from ..models.reporting_rate import ReportingRate


T = TypeVar("T", bound="DataDimensionItem")


@_attrs_define
class DataDimensionItem:
    """
    Attributes:
        data_dimension_item_type (DataDimensionItemDataDimensionItemType):
        data_element (Union[Unset, DataDimensionItemDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        data_element_operand (Union[Unset, DataElementOperand]):
        expression_dimension_item (Union[Unset, DataDimensionItemExpressionDimensionItem]): A UID reference to a
            ExpressionDimensionItem
            (Java name `org.hisp.dhis.expressiondimensionitem.ExpressionDimensionItem`)
        indicator (Union[Unset, DataDimensionItemIndicator]): A UID reference to a Indicator
            (Java name `org.hisp.dhis.indicator.Indicator`)
        program_attribute (Union[Unset, ProgramTrackedEntityAttributeDimensionItem]):
        program_data_element (Union[Unset, ProgramDataElementDimensionItem]):
        program_indicator (Union[Unset, DataDimensionItemProgramIndicator]): A UID reference to a ProgramIndicator
            (Java name `org.hisp.dhis.program.ProgramIndicator`)
        reporting_rate (Union[Unset, ReportingRate]):
        subexpression_dimension_item (Union[Unset, DataDimensionItemSubexpressionDimensionItem]): A UID reference to a
            SubexpressionDimensionItem
            (Java name `org.hisp.dhis.subexpression.SubexpressionDimensionItem`)
    """

    data_dimension_item_type: DataDimensionItemDataDimensionItemType
    data_element: Union[Unset, "DataDimensionItemDataElement"] = UNSET
    data_element_operand: Union[Unset, "DataElementOperand"] = UNSET
    expression_dimension_item: Union[Unset, "DataDimensionItemExpressionDimensionItem"] = UNSET
    indicator: Union[Unset, "DataDimensionItemIndicator"] = UNSET
    program_attribute: Union[Unset, "ProgramTrackedEntityAttributeDimensionItem"] = UNSET
    program_data_element: Union[Unset, "ProgramDataElementDimensionItem"] = UNSET
    program_indicator: Union[Unset, "DataDimensionItemProgramIndicator"] = UNSET
    reporting_rate: Union[Unset, "ReportingRate"] = UNSET
    subexpression_dimension_item: Union[Unset, "DataDimensionItemSubexpressionDimensionItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_dimension_item_type = self.data_dimension_item_type.value

        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

        data_element_operand: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element_operand, Unset):
            data_element_operand = self.data_element_operand.to_dict()

        expression_dimension_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.expression_dimension_item, Unset):
            expression_dimension_item = self.expression_dimension_item.to_dict()

        indicator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.indicator, Unset):
            indicator = self.indicator.to_dict()

        program_attribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_attribute, Unset):
            program_attribute = self.program_attribute.to_dict()

        program_data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_data_element, Unset):
            program_data_element = self.program_data_element.to_dict()

        program_indicator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_indicator, Unset):
            program_indicator = self.program_indicator.to_dict()

        reporting_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reporting_rate, Unset):
            reporting_rate = self.reporting_rate.to_dict()

        subexpression_dimension_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subexpression_dimension_item, Unset):
            subexpression_dimension_item = self.subexpression_dimension_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataDimensionItemType": data_dimension_item_type,
            }
        )
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if data_element_operand is not UNSET:
            field_dict["dataElementOperand"] = data_element_operand
        if expression_dimension_item is not UNSET:
            field_dict["expressionDimensionItem"] = expression_dimension_item
        if indicator is not UNSET:
            field_dict["indicator"] = indicator
        if program_attribute is not UNSET:
            field_dict["programAttribute"] = program_attribute
        if program_data_element is not UNSET:
            field_dict["programDataElement"] = program_data_element
        if program_indicator is not UNSET:
            field_dict["programIndicator"] = program_indicator
        if reporting_rate is not UNSET:
            field_dict["reportingRate"] = reporting_rate
        if subexpression_dimension_item is not UNSET:
            field_dict["subexpressionDimensionItem"] = subexpression_dimension_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_dimension_item_data_element import DataDimensionItemDataElement
        from ..models.data_dimension_item_expression_dimension_item import DataDimensionItemExpressionDimensionItem
        from ..models.data_dimension_item_indicator import DataDimensionItemIndicator
        from ..models.data_dimension_item_program_indicator import DataDimensionItemProgramIndicator
        from ..models.data_dimension_item_subexpression_dimension_item import (
            DataDimensionItemSubexpressionDimensionItem,
        )
        from ..models.data_element_operand import DataElementOperand
        from ..models.program_data_element_dimension_item import ProgramDataElementDimensionItem
        from ..models.program_tracked_entity_attribute_dimension_item import ProgramTrackedEntityAttributeDimensionItem
        from ..models.reporting_rate import ReportingRate

        d = src_dict.copy()
        data_dimension_item_type = DataDimensionItemDataDimensionItemType(d.pop("dataDimensionItemType"))

        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, DataDimensionItemDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = DataDimensionItemDataElement.from_dict(_data_element)

        _data_element_operand = d.pop("dataElementOperand", UNSET)
        data_element_operand: Union[Unset, DataElementOperand]
        if isinstance(_data_element_operand, Unset):
            data_element_operand = UNSET
        else:
            data_element_operand = DataElementOperand.from_dict(_data_element_operand)

        _expression_dimension_item = d.pop("expressionDimensionItem", UNSET)
        expression_dimension_item: Union[Unset, DataDimensionItemExpressionDimensionItem]
        if isinstance(_expression_dimension_item, Unset):
            expression_dimension_item = UNSET
        else:
            expression_dimension_item = DataDimensionItemExpressionDimensionItem.from_dict(_expression_dimension_item)

        _indicator = d.pop("indicator", UNSET)
        indicator: Union[Unset, DataDimensionItemIndicator]
        if isinstance(_indicator, Unset):
            indicator = UNSET
        else:
            indicator = DataDimensionItemIndicator.from_dict(_indicator)

        _program_attribute = d.pop("programAttribute", UNSET)
        program_attribute: Union[Unset, ProgramTrackedEntityAttributeDimensionItem]
        if isinstance(_program_attribute, Unset):
            program_attribute = UNSET
        else:
            program_attribute = ProgramTrackedEntityAttributeDimensionItem.from_dict(_program_attribute)

        _program_data_element = d.pop("programDataElement", UNSET)
        program_data_element: Union[Unset, ProgramDataElementDimensionItem]
        if isinstance(_program_data_element, Unset):
            program_data_element = UNSET
        else:
            program_data_element = ProgramDataElementDimensionItem.from_dict(_program_data_element)

        _program_indicator = d.pop("programIndicator", UNSET)
        program_indicator: Union[Unset, DataDimensionItemProgramIndicator]
        if isinstance(_program_indicator, Unset):
            program_indicator = UNSET
        else:
            program_indicator = DataDimensionItemProgramIndicator.from_dict(_program_indicator)

        _reporting_rate = d.pop("reportingRate", UNSET)
        reporting_rate: Union[Unset, ReportingRate]
        if isinstance(_reporting_rate, Unset):
            reporting_rate = UNSET
        else:
            reporting_rate = ReportingRate.from_dict(_reporting_rate)

        _subexpression_dimension_item = d.pop("subexpressionDimensionItem", UNSET)
        subexpression_dimension_item: Union[Unset, DataDimensionItemSubexpressionDimensionItem]
        if isinstance(_subexpression_dimension_item, Unset):
            subexpression_dimension_item = UNSET
        else:
            subexpression_dimension_item = DataDimensionItemSubexpressionDimensionItem.from_dict(
                _subexpression_dimension_item
            )

        data_dimension_item = cls(
            data_dimension_item_type=data_dimension_item_type,
            data_element=data_element,
            data_element_operand=data_element_operand,
            expression_dimension_item=expression_dimension_item,
            indicator=indicator,
            program_attribute=program_attribute,
            program_data_element=program_data_element,
            program_indicator=program_indicator,
            reporting_rate=reporting_rate,
            subexpression_dimension_item=subexpression_dimension_item,
        )

        data_dimension_item.additional_properties = d
        return data_dimension_item

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
