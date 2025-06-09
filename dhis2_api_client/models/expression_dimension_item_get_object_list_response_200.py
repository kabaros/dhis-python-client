from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expression_dimension_item import ExpressionDimensionItem
    from ..models.pager import Pager


T = TypeVar("T", bound="ExpressionDimensionItemGetObjectListResponse200")


@_attrs_define
class ExpressionDimensionItemGetObjectListResponse200:
    """
    Attributes:
        pager (Union[Unset, Pager]):
        expression_dimension_items (Union[Unset, list['ExpressionDimensionItem']]):
    """

    pager: Union[Unset, "Pager"] = UNSET
    expression_dimension_items: Union[Unset, list["ExpressionDimensionItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pager: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pager, Unset):
            pager = self.pager.to_dict()

        expression_dimension_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.expression_dimension_items, Unset):
            expression_dimension_items = []
            for expression_dimension_items_item_data in self.expression_dimension_items:
                expression_dimension_items_item = expression_dimension_items_item_data.to_dict()
                expression_dimension_items.append(expression_dimension_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pager is not UNSET:
            field_dict["pager"] = pager
        if expression_dimension_items is not UNSET:
            field_dict["expressionDimensionItems"] = expression_dimension_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.expression_dimension_item import ExpressionDimensionItem
        from ..models.pager import Pager

        d = src_dict.copy()
        _pager = d.pop("pager", UNSET)
        pager: Union[Unset, Pager]
        if isinstance(_pager, Unset):
            pager = UNSET
        else:
            pager = Pager.from_dict(_pager)

        expression_dimension_items = []
        _expression_dimension_items = d.pop("expressionDimensionItems", UNSET)
        for expression_dimension_items_item_data in _expression_dimension_items or []:
            expression_dimension_items_item = ExpressionDimensionItem.from_dict(expression_dimension_items_item_data)

            expression_dimension_items.append(expression_dimension_items_item)

        expression_dimension_item_get_object_list_response_200 = cls(
            pager=pager,
            expression_dimension_items=expression_dimension_items,
        )

        expression_dimension_item_get_object_list_response_200.additional_properties = d
        return expression_dimension_item_get_object_list_response_200

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
