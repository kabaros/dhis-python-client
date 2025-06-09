from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_set_element_category_combo import DataSetElementCategoryCombo
    from ..models.data_set_element_data_element import DataSetElementDataElement
    from ..models.data_set_element_data_set import DataSetElementDataSet


T = TypeVar("T", bound="DataSetElement")


@_attrs_define
class DataSetElement:
    """
    Attributes:
        category_combo (Union[Unset, DataSetElementCategoryCombo]): A UID reference to a CategoryCombo
            (Java name `org.hisp.dhis.category.CategoryCombo`)
        data_element (Union[Unset, DataSetElementDataElement]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        data_set (Union[Unset, DataSetElementDataSet]): A UID reference to a DataSet
            (Java name `org.hisp.dhis.dataset.DataSet`)
    """

    category_combo: Union[Unset, "DataSetElementCategoryCombo"] = UNSET
    data_element: Union[Unset, "DataSetElementDataElement"] = UNSET
    data_set: Union[Unset, "DataSetElementDataSet"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_combo, Unset):
            category_combo = self.category_combo.to_dict()

        data_element: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_element, Unset):
            data_element = self.data_element.to_dict()

        data_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_set, Unset):
            data_set = self.data_set.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_combo is not UNSET:
            field_dict["categoryCombo"] = category_combo
        if data_element is not UNSET:
            field_dict["dataElement"] = data_element
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_set_element_category_combo import DataSetElementCategoryCombo
        from ..models.data_set_element_data_element import DataSetElementDataElement
        from ..models.data_set_element_data_set import DataSetElementDataSet

        d = src_dict.copy()
        _category_combo = d.pop("categoryCombo", UNSET)
        category_combo: Union[Unset, DataSetElementCategoryCombo]
        if isinstance(_category_combo, Unset):
            category_combo = UNSET
        else:
            category_combo = DataSetElementCategoryCombo.from_dict(_category_combo)

        _data_element = d.pop("dataElement", UNSET)
        data_element: Union[Unset, DataSetElementDataElement]
        if isinstance(_data_element, Unset):
            data_element = UNSET
        else:
            data_element = DataSetElementDataElement.from_dict(_data_element)

        _data_set = d.pop("dataSet", UNSET)
        data_set: Union[Unset, DataSetElementDataSet]
        if isinstance(_data_set, Unset):
            data_set = UNSET
        else:
            data_set = DataSetElementDataSet.from_dict(_data_set)

        data_set_element = cls(
            category_combo=category_combo,
            data_element=data_element,
            data_set=data_set,
        )

        data_set_element.additional_properties = d
        return data_set_element

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
