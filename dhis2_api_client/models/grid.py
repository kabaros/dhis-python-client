from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grid_header import GridHeader
    from ..models.grid_internal_meta_data import GridInternalMetaData
    from ..models.grid_meta_data import GridMetaData
    from ..models.grid_row_context import GridRowContext
    from ..models.grid_rows_item_item import GridRowsItemItem
    from ..models.grid_visible_rows_item_item import GridVisibleRowsItemItem
    from ..models.performance_metrics import PerformanceMetrics
    from ..models.reference import Reference


T = TypeVar("T", bound="Grid")


@_attrs_define
class Grid:
    """
    Attributes:
        header_width (int):
        height (int):
        visible_width (int):
        width (int):
        headers (Union[Unset, list['GridHeader']]):
        internal_meta_data (Union[Unset, GridInternalMetaData]):
        last_data_row (Union[Unset, bool]):
        meta_column_indexes (Union[Unset, list[int]]):
        meta_data (Union[Unset, GridMetaData]):
        metadata_headers (Union[Unset, list['GridHeader']]):
        performance_metrics (Union[Unset, PerformanceMetrics]):
        refs (Union[Unset, list['Reference']]):
        row_context (Union[Unset, GridRowContext]): keys are class java.lang.Integer
        rows (Union[Unset, list[list['GridRowsItemItem']]]):
        subtitle (Union[Unset, str]):
        table (Union[Unset, str]):
        title (Union[Unset, str]):
        visible_headers (Union[Unset, list['GridHeader']]):
        visible_rows (Union[Unset, list[list['GridVisibleRowsItemItem']]]):
    """

    header_width: int
    height: int
    visible_width: int
    width: int
    headers: Union[Unset, list["GridHeader"]] = UNSET
    internal_meta_data: Union[Unset, "GridInternalMetaData"] = UNSET
    last_data_row: Union[Unset, bool] = UNSET
    meta_column_indexes: Union[Unset, list[int]] = UNSET
    meta_data: Union[Unset, "GridMetaData"] = UNSET
    metadata_headers: Union[Unset, list["GridHeader"]] = UNSET
    performance_metrics: Union[Unset, "PerformanceMetrics"] = UNSET
    refs: Union[Unset, list["Reference"]] = UNSET
    row_context: Union[Unset, "GridRowContext"] = UNSET
    rows: Union[Unset, list[list["GridRowsItemItem"]]] = UNSET
    subtitle: Union[Unset, str] = UNSET
    table: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    visible_headers: Union[Unset, list["GridHeader"]] = UNSET
    visible_rows: Union[Unset, list[list["GridVisibleRowsItemItem"]]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header_width = self.header_width

        height = self.height

        visible_width = self.visible_width

        width = self.width

        headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        internal_meta_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.internal_meta_data, Unset):
            internal_meta_data = self.internal_meta_data.to_dict()

        last_data_row = self.last_data_row

        meta_column_indexes: Union[Unset, list[int]] = UNSET
        if not isinstance(self.meta_column_indexes, Unset):
            meta_column_indexes = self.meta_column_indexes

        meta_data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        metadata_headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_headers, Unset):
            metadata_headers = []
            for metadata_headers_item_data in self.metadata_headers:
                metadata_headers_item = metadata_headers_item_data.to_dict()
                metadata_headers.append(metadata_headers_item)

        performance_metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.performance_metrics, Unset):
            performance_metrics = self.performance_metrics.to_dict()

        refs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item = refs_item_data.to_dict()
                refs.append(refs_item)

        row_context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.row_context, Unset):
            row_context = self.row_context.to_dict()

        rows: Union[Unset, list[list[dict[str, Any]]]] = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = []
                for rows_item_item_data in rows_item_data:
                    rows_item_item = rows_item_item_data.to_dict()
                    rows_item.append(rows_item_item)

                rows.append(rows_item)

        subtitle = self.subtitle

        table = self.table

        title = self.title

        visible_headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.visible_headers, Unset):
            visible_headers = []
            for visible_headers_item_data in self.visible_headers:
                visible_headers_item = visible_headers_item_data.to_dict()
                visible_headers.append(visible_headers_item)

        visible_rows: Union[Unset, list[list[dict[str, Any]]]] = UNSET
        if not isinstance(self.visible_rows, Unset):
            visible_rows = []
            for visible_rows_item_data in self.visible_rows:
                visible_rows_item = []
                for visible_rows_item_item_data in visible_rows_item_data:
                    visible_rows_item_item = visible_rows_item_item_data.to_dict()
                    visible_rows_item.append(visible_rows_item_item)

                visible_rows.append(visible_rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headerWidth": header_width,
                "height": height,
                "visibleWidth": visible_width,
                "width": width,
            }
        )
        if headers is not UNSET:
            field_dict["headers"] = headers
        if internal_meta_data is not UNSET:
            field_dict["internalMetaData"] = internal_meta_data
        if last_data_row is not UNSET:
            field_dict["lastDataRow"] = last_data_row
        if meta_column_indexes is not UNSET:
            field_dict["metaColumnIndexes"] = meta_column_indexes
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if metadata_headers is not UNSET:
            field_dict["metadataHeaders"] = metadata_headers
        if performance_metrics is not UNSET:
            field_dict["performanceMetrics"] = performance_metrics
        if refs is not UNSET:
            field_dict["refs"] = refs
        if row_context is not UNSET:
            field_dict["rowContext"] = row_context
        if rows is not UNSET:
            field_dict["rows"] = rows
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if table is not UNSET:
            field_dict["table"] = table
        if title is not UNSET:
            field_dict["title"] = title
        if visible_headers is not UNSET:
            field_dict["visibleHeaders"] = visible_headers
        if visible_rows is not UNSET:
            field_dict["visibleRows"] = visible_rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.grid_header import GridHeader
        from ..models.grid_internal_meta_data import GridInternalMetaData
        from ..models.grid_meta_data import GridMetaData
        from ..models.grid_row_context import GridRowContext
        from ..models.grid_rows_item_item import GridRowsItemItem
        from ..models.grid_visible_rows_item_item import GridVisibleRowsItemItem
        from ..models.performance_metrics import PerformanceMetrics
        from ..models.reference import Reference

        d = src_dict.copy()
        header_width = d.pop("headerWidth")

        height = d.pop("height")

        visible_width = d.pop("visibleWidth")

        width = d.pop("width")

        headers = []
        _headers = d.pop("headers", UNSET)
        for headers_item_data in _headers or []:
            headers_item = GridHeader.from_dict(headers_item_data)

            headers.append(headers_item)

        _internal_meta_data = d.pop("internalMetaData", UNSET)
        internal_meta_data: Union[Unset, GridInternalMetaData]
        if isinstance(_internal_meta_data, Unset):
            internal_meta_data = UNSET
        else:
            internal_meta_data = GridInternalMetaData.from_dict(_internal_meta_data)

        last_data_row = d.pop("lastDataRow", UNSET)

        meta_column_indexes = cast(list[int], d.pop("metaColumnIndexes", UNSET))

        _meta_data = d.pop("metaData", UNSET)
        meta_data: Union[Unset, GridMetaData]
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = GridMetaData.from_dict(_meta_data)

        metadata_headers = []
        _metadata_headers = d.pop("metadataHeaders", UNSET)
        for metadata_headers_item_data in _metadata_headers or []:
            metadata_headers_item = GridHeader.from_dict(metadata_headers_item_data)

            metadata_headers.append(metadata_headers_item)

        _performance_metrics = d.pop("performanceMetrics", UNSET)
        performance_metrics: Union[Unset, PerformanceMetrics]
        if isinstance(_performance_metrics, Unset):
            performance_metrics = UNSET
        else:
            performance_metrics = PerformanceMetrics.from_dict(_performance_metrics)

        refs = []
        _refs = d.pop("refs", UNSET)
        for refs_item_data in _refs or []:
            refs_item = Reference.from_dict(refs_item_data)

            refs.append(refs_item)

        _row_context = d.pop("rowContext", UNSET)
        row_context: Union[Unset, GridRowContext]
        if isinstance(_row_context, Unset):
            row_context = UNSET
        else:
            row_context = GridRowContext.from_dict(_row_context)

        rows = []
        _rows = d.pop("rows", UNSET)
        for rows_item_data in _rows or []:
            rows_item = []
            _rows_item = rows_item_data
            for rows_item_item_data in _rows_item:
                rows_item_item = GridRowsItemItem.from_dict(rows_item_item_data)

                rows_item.append(rows_item_item)

            rows.append(rows_item)

        subtitle = d.pop("subtitle", UNSET)

        table = d.pop("table", UNSET)

        title = d.pop("title", UNSET)

        visible_headers = []
        _visible_headers = d.pop("visibleHeaders", UNSET)
        for visible_headers_item_data in _visible_headers or []:
            visible_headers_item = GridHeader.from_dict(visible_headers_item_data)

            visible_headers.append(visible_headers_item)

        visible_rows = []
        _visible_rows = d.pop("visibleRows", UNSET)
        for visible_rows_item_data in _visible_rows or []:
            visible_rows_item = []
            _visible_rows_item = visible_rows_item_data
            for visible_rows_item_item_data in _visible_rows_item:
                visible_rows_item_item = GridVisibleRowsItemItem.from_dict(visible_rows_item_item_data)

                visible_rows_item.append(visible_rows_item_item)

            visible_rows.append(visible_rows_item)

        grid = cls(
            header_width=header_width,
            height=height,
            visible_width=visible_width,
            width=width,
            headers=headers,
            internal_meta_data=internal_meta_data,
            last_data_row=last_data_row,
            meta_column_indexes=meta_column_indexes,
            meta_data=meta_data,
            metadata_headers=metadata_headers,
            performance_metrics=performance_metrics,
            refs=refs,
            row_context=row_context,
            rows=rows,
            subtitle=subtitle,
            table=table,
            title=title,
            visible_headers=visible_headers,
            visible_rows=visible_rows,
        )

        grid.additional_properties = d
        return grid

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
