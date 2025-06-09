from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_value import DataValue


T = TypeVar("T", bound="DataValueSet")


@_attrs_define
class DataValueSet:
    """
    Attributes:
        attribute_category_options (Union[Unset, list[str]]):
        attribute_option_combo (Union[Unset, str]):
        category_option_combo_id_scheme (Union[Unset, str]):
        complete_date (Union[Unset, str]):
        data_element_id_scheme (Union[Unset, str]):
        data_set (Union[Unset, str]):
        data_set_id_scheme (Union[Unset, str]):
        data_values (Union[Unset, list['DataValue']]):
        dry_run (Union[Unset, bool]):
        id_scheme (Union[Unset, str]):
        org_unit (Union[Unset, str]):
        org_unit_id_scheme (Union[Unset, str]):
        period (Union[Unset, str]):
        strategy (Union[Unset, str]):
    """

    attribute_category_options: Union[Unset, list[str]] = UNSET
    attribute_option_combo: Union[Unset, str] = UNSET
    category_option_combo_id_scheme: Union[Unset, str] = UNSET
    complete_date: Union[Unset, str] = UNSET
    data_element_id_scheme: Union[Unset, str] = UNSET
    data_set: Union[Unset, str] = UNSET
    data_set_id_scheme: Union[Unset, str] = UNSET
    data_values: Union[Unset, list["DataValue"]] = UNSET
    dry_run: Union[Unset, bool] = UNSET
    id_scheme: Union[Unset, str] = UNSET
    org_unit: Union[Unset, str] = UNSET
    org_unit_id_scheme: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    strategy: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attribute_category_options: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attribute_category_options, Unset):
            attribute_category_options = self.attribute_category_options

        attribute_option_combo = self.attribute_option_combo

        category_option_combo_id_scheme = self.category_option_combo_id_scheme

        complete_date = self.complete_date

        data_element_id_scheme = self.data_element_id_scheme

        data_set = self.data_set

        data_set_id_scheme = self.data_set_id_scheme

        data_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_values, Unset):
            data_values = []
            for data_values_item_data in self.data_values:
                data_values_item = data_values_item_data.to_dict()
                data_values.append(data_values_item)

        dry_run = self.dry_run

        id_scheme = self.id_scheme

        org_unit = self.org_unit

        org_unit_id_scheme = self.org_unit_id_scheme

        period = self.period

        strategy = self.strategy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_category_options is not UNSET:
            field_dict["attributeCategoryOptions"] = attribute_category_options
        if attribute_option_combo is not UNSET:
            field_dict["attributeOptionCombo"] = attribute_option_combo
        if category_option_combo_id_scheme is not UNSET:
            field_dict["categoryOptionComboIdScheme"] = category_option_combo_id_scheme
        if complete_date is not UNSET:
            field_dict["completeDate"] = complete_date
        if data_element_id_scheme is not UNSET:
            field_dict["dataElementIdScheme"] = data_element_id_scheme
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set
        if data_set_id_scheme is not UNSET:
            field_dict["dataSetIdScheme"] = data_set_id_scheme
        if data_values is not UNSET:
            field_dict["dataValues"] = data_values
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if id_scheme is not UNSET:
            field_dict["idScheme"] = id_scheme
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit
        if org_unit_id_scheme is not UNSET:
            field_dict["orgUnitIdScheme"] = org_unit_id_scheme
        if period is not UNSET:
            field_dict["period"] = period
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_value import DataValue

        d = src_dict.copy()
        attribute_category_options = cast(list[str], d.pop("attributeCategoryOptions", UNSET))

        attribute_option_combo = d.pop("attributeOptionCombo", UNSET)

        category_option_combo_id_scheme = d.pop("categoryOptionComboIdScheme", UNSET)

        complete_date = d.pop("completeDate", UNSET)

        data_element_id_scheme = d.pop("dataElementIdScheme", UNSET)

        data_set = d.pop("dataSet", UNSET)

        data_set_id_scheme = d.pop("dataSetIdScheme", UNSET)

        data_values = []
        _data_values = d.pop("dataValues", UNSET)
        for data_values_item_data in _data_values or []:
            data_values_item = DataValue.from_dict(data_values_item_data)

            data_values.append(data_values_item)

        dry_run = d.pop("dryRun", UNSET)

        id_scheme = d.pop("idScheme", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        org_unit_id_scheme = d.pop("orgUnitIdScheme", UNSET)

        period = d.pop("period", UNSET)

        strategy = d.pop("strategy", UNSET)

        data_value_set = cls(
            attribute_category_options=attribute_category_options,
            attribute_option_combo=attribute_option_combo,
            category_option_combo_id_scheme=category_option_combo_id_scheme,
            complete_date=complete_date,
            data_element_id_scheme=data_element_id_scheme,
            data_set=data_set,
            data_set_id_scheme=data_set_id_scheme,
            data_values=data_values,
            dry_run=dry_run,
            id_scheme=id_scheme,
            org_unit=org_unit,
            org_unit_id_scheme=org_unit_id_scheme,
            period=period,
            strategy=strategy,
        )

        data_value_set.additional_properties = d
        return data_value_set

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
