from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_request_aggregation_type import SourceRequestAggregationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="SourceRequest")


@_attrs_define
class SourceRequest:
    """
    Attributes:
        aggregation_type (SourceRequestAggregationType):
        dx (Union[Unset, list[str]]):
        filters (Union[Unset, list['Filter']]):
        input_id_scheme (Union[Unset, str]):
        name (Union[Unset, str]):
        ou (Union[Unset, list[str]]):
        output_data_element_id_scheme (Union[Unset, str]):
        output_data_item_id_scheme (Union[Unset, str]):
        output_id_scheme (Union[Unset, str]):
        output_org_unit_id_scheme (Union[Unset, str]):
        pe (Union[Unset, list[str]]):
        visualization (Union[Unset, str]):
    """

    aggregation_type: SourceRequestAggregationType
    dx: Union[Unset, list[str]] = UNSET
    filters: Union[Unset, list["Filter"]] = UNSET
    input_id_scheme: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    ou: Union[Unset, list[str]] = UNSET
    output_data_element_id_scheme: Union[Unset, str] = UNSET
    output_data_item_id_scheme: Union[Unset, str] = UNSET
    output_id_scheme: Union[Unset, str] = UNSET
    output_org_unit_id_scheme: Union[Unset, str] = UNSET
    pe: Union[Unset, list[str]] = UNSET
    visualization: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        dx: Union[Unset, list[str]] = UNSET
        if not isinstance(self.dx, Unset):
            dx = self.dx

        filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        input_id_scheme = self.input_id_scheme

        name = self.name

        ou: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ou, Unset):
            ou = self.ou

        output_data_element_id_scheme = self.output_data_element_id_scheme

        output_data_item_id_scheme = self.output_data_item_id_scheme

        output_id_scheme = self.output_id_scheme

        output_org_unit_id_scheme = self.output_org_unit_id_scheme

        pe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pe, Unset):
            pe = self.pe

        visualization = self.visualization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
            }
        )
        if dx is not UNSET:
            field_dict["dx"] = dx
        if filters is not UNSET:
            field_dict["filters"] = filters
        if input_id_scheme is not UNSET:
            field_dict["inputIdScheme"] = input_id_scheme
        if name is not UNSET:
            field_dict["name"] = name
        if ou is not UNSET:
            field_dict["ou"] = ou
        if output_data_element_id_scheme is not UNSET:
            field_dict["outputDataElementIdScheme"] = output_data_element_id_scheme
        if output_data_item_id_scheme is not UNSET:
            field_dict["outputDataItemIdScheme"] = output_data_item_id_scheme
        if output_id_scheme is not UNSET:
            field_dict["outputIdScheme"] = output_id_scheme
        if output_org_unit_id_scheme is not UNSET:
            field_dict["outputOrgUnitIdScheme"] = output_org_unit_id_scheme
        if pe is not UNSET:
            field_dict["pe"] = pe
        if visualization is not UNSET:
            field_dict["visualization"] = visualization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.filter_ import Filter

        d = src_dict.copy()
        aggregation_type = SourceRequestAggregationType(d.pop("aggregationType"))

        dx = cast(list[str], d.pop("dx", UNSET))

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = Filter.from_dict(filters_item_data)

            filters.append(filters_item)

        input_id_scheme = d.pop("inputIdScheme", UNSET)

        name = d.pop("name", UNSET)

        ou = cast(list[str], d.pop("ou", UNSET))

        output_data_element_id_scheme = d.pop("outputDataElementIdScheme", UNSET)

        output_data_item_id_scheme = d.pop("outputDataItemIdScheme", UNSET)

        output_id_scheme = d.pop("outputIdScheme", UNSET)

        output_org_unit_id_scheme = d.pop("outputOrgUnitIdScheme", UNSET)

        pe = cast(list[str], d.pop("pe", UNSET))

        visualization = d.pop("visualization", UNSET)

        source_request = cls(
            aggregation_type=aggregation_type,
            dx=dx,
            filters=filters,
            input_id_scheme=input_id_scheme,
            name=name,
            ou=ou,
            output_data_element_id_scheme=output_data_element_id_scheme,
            output_data_item_id_scheme=output_data_item_id_scheme,
            output_id_scheme=output_id_scheme,
            output_org_unit_id_scheme=output_org_unit_id_scheme,
            pe=pe,
            visualization=visualization,
        )

        source_request.additional_properties = d
        return source_request

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
