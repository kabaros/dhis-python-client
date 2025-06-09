from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.geo_json_import_job_params_id_type import GeoJsonImportJobParamsIdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoJsonImportJobParams")


@_attrs_define
class GeoJsonImportJobParams:
    """
    Attributes:
        id_type (GeoJsonImportJobParamsIdType):
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        org_unit_id_property (Union[Unset, str]):
    """

    id_type: GeoJsonImportJobParamsIdType
    attribute_id: Union[Unset, str] = UNSET
    dry_run: Union[Unset, bool] = UNSET
    org_unit_id_property: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id_type = self.id_type.value

        attribute_id = self.attribute_id

        dry_run = self.dry_run

        org_unit_id_property = self.org_unit_id_property

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idType": id_type,
            }
        )
        if attribute_id is not UNSET:
            field_dict["attributeId"] = attribute_id
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if org_unit_id_property is not UNSET:
            field_dict["orgUnitIdProperty"] = org_unit_id_property

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id_type = GeoJsonImportJobParamsIdType(d.pop("idType"))

        attribute_id = d.pop("attributeId", UNSET)

        dry_run = d.pop("dryRun", UNSET)

        org_unit_id_property = d.pop("orgUnitIdProperty", UNSET)

        geo_json_import_job_params = cls(
            id_type=id_type,
            attribute_id=attribute_id,
            dry_run=dry_run,
            org_unit_id_property=org_unit_id_property,
        )

        geo_json_import_job_params.additional_properties = d
        return geo_json_import_job_params

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
