import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.metadata_item_aggregation_type import MetadataItemAggregationType
from ..models.metadata_item_dimension_item_type import MetadataItemDimensionItemType
from ..models.metadata_item_dimension_type import MetadataItemDimensionType
from ..models.metadata_item_total_aggregation_type import MetadataItemTotalAggregationType
from ..models.metadata_item_value_type import MetadataItemValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_item_indicator_type import MetadataItemIndicatorType
    from ..models.metadata_item_options_item import MetadataItemOptionsItem
    from ..models.object_style import ObjectStyle


T = TypeVar("T", bound="MetadataItem")


@_attrs_define
class MetadataItem:
    """
    Attributes:
        aggregation_type (MetadataItemAggregationType):
        dimension_item_type (MetadataItemDimensionItemType):
        dimension_type (MetadataItemDimensionType):
        total_aggregation_type (MetadataItemTotalAggregationType):
        value_type (MetadataItemValueType):
        code (Union[Unset, str]):
        description (Union[Unset, str]):
        end_date (Union[Unset, datetime.datetime]):
        expression (Union[Unset, str]):
        indicator_type (Union[Unset, MetadataItemIndicatorType]): A UID reference to a IndicatorType
            (Java name `org.hisp.dhis.indicator.IndicatorType`)
        legend_set (Union[Unset, str]):
        name (Union[Unset, str]):
        options (Union[Unset, list['MetadataItemOptionsItem']]):
        start_date (Union[Unset, datetime.datetime]):
        style (Union[Unset, ObjectStyle]):
        uid (Union[Unset, str]):
    """

    aggregation_type: MetadataItemAggregationType
    dimension_item_type: MetadataItemDimensionItemType
    dimension_type: MetadataItemDimensionType
    total_aggregation_type: MetadataItemTotalAggregationType
    value_type: MetadataItemValueType
    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    expression: Union[Unset, str] = UNSET
    indicator_type: Union[Unset, "MetadataItemIndicatorType"] = UNSET
    legend_set: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    options: Union[Unset, list["MetadataItemOptionsItem"]] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    style: Union[Unset, "ObjectStyle"] = UNSET
    uid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        dimension_item_type = self.dimension_item_type.value

        dimension_type = self.dimension_type.value

        total_aggregation_type = self.total_aggregation_type.value

        value_type = self.value_type.value

        code = self.code

        description = self.description

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        expression = self.expression

        indicator_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.indicator_type, Unset):
            indicator_type = self.indicator_type.to_dict()

        legend_set = self.legend_set

        name = self.name

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        style: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.to_dict()

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "dimensionItemType": dimension_item_type,
                "dimensionType": dimension_type,
                "totalAggregationType": total_aggregation_type,
                "valueType": value_type,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if expression is not UNSET:
            field_dict["expression"] = expression
        if indicator_type is not UNSET:
            field_dict["indicatorType"] = indicator_type
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if style is not UNSET:
            field_dict["style"] = style
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.metadata_item_indicator_type import MetadataItemIndicatorType
        from ..models.metadata_item_options_item import MetadataItemOptionsItem
        from ..models.object_style import ObjectStyle

        d = src_dict.copy()
        aggregation_type = MetadataItemAggregationType(d.pop("aggregationType"))

        dimension_item_type = MetadataItemDimensionItemType(d.pop("dimensionItemType"))

        dimension_type = MetadataItemDimensionType(d.pop("dimensionType"))

        total_aggregation_type = MetadataItemTotalAggregationType(d.pop("totalAggregationType"))

        value_type = MetadataItemValueType(d.pop("valueType"))

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        expression = d.pop("expression", UNSET)

        _indicator_type = d.pop("indicatorType", UNSET)
        indicator_type: Union[Unset, MetadataItemIndicatorType]
        if isinstance(_indicator_type, Unset):
            indicator_type = UNSET
        else:
            indicator_type = MetadataItemIndicatorType.from_dict(_indicator_type)

        legend_set = d.pop("legendSet", UNSET)

        name = d.pop("name", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = MetadataItemOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _style = d.pop("style", UNSET)
        style: Union[Unset, ObjectStyle]
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = ObjectStyle.from_dict(_style)

        uid = d.pop("uid", UNSET)

        metadata_item = cls(
            aggregation_type=aggregation_type,
            dimension_item_type=dimension_item_type,
            dimension_type=dimension_type,
            total_aggregation_type=total_aggregation_type,
            value_type=value_type,
            code=code,
            description=description,
            end_date=end_date,
            expression=expression,
            indicator_type=indicator_type,
            legend_set=legend_set,
            name=name,
            options=options,
            start_date=start_date,
            style=style,
            uid=uid,
        )

        metadata_item.additional_properties = d
        return metadata_item

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
