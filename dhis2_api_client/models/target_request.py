from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.target_request_import_strategy import TargetRequestImportStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetRequest")


@_attrs_define
class TargetRequest:
    """
    Attributes:
        import_strategy (TargetRequestImportStrategy):
        category_option_combo_id_scheme (Union[Unset, str]):
        data_element_id_scheme (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        id_scheme (Union[Unset, str]):
        org_unit_id_scheme (Union[Unset, str]):
        skip_audit (Union[Unset, bool]):
    """

    import_strategy: TargetRequestImportStrategy
    category_option_combo_id_scheme: Union[Unset, str] = UNSET
    data_element_id_scheme: Union[Unset, str] = UNSET
    dry_run: Union[Unset, bool] = UNSET
    id_scheme: Union[Unset, str] = UNSET
    org_unit_id_scheme: Union[Unset, str] = UNSET
    skip_audit: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_strategy = self.import_strategy.value

        category_option_combo_id_scheme = self.category_option_combo_id_scheme

        data_element_id_scheme = self.data_element_id_scheme

        dry_run = self.dry_run

        id_scheme = self.id_scheme

        org_unit_id_scheme = self.org_unit_id_scheme

        skip_audit = self.skip_audit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "importStrategy": import_strategy,
            }
        )
        if category_option_combo_id_scheme is not UNSET:
            field_dict["categoryOptionComboIdScheme"] = category_option_combo_id_scheme
        if data_element_id_scheme is not UNSET:
            field_dict["dataElementIdScheme"] = data_element_id_scheme
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if id_scheme is not UNSET:
            field_dict["idScheme"] = id_scheme
        if org_unit_id_scheme is not UNSET:
            field_dict["orgUnitIdScheme"] = org_unit_id_scheme
        if skip_audit is not UNSET:
            field_dict["skipAudit"] = skip_audit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        import_strategy = TargetRequestImportStrategy(d.pop("importStrategy"))

        category_option_combo_id_scheme = d.pop("categoryOptionComboIdScheme", UNSET)

        data_element_id_scheme = d.pop("dataElementIdScheme", UNSET)

        dry_run = d.pop("dryRun", UNSET)

        id_scheme = d.pop("idScheme", UNSET)

        org_unit_id_scheme = d.pop("orgUnitIdScheme", UNSET)

        skip_audit = d.pop("skipAudit", UNSET)

        target_request = cls(
            import_strategy=import_strategy,
            category_option_combo_id_scheme=category_option_combo_id_scheme,
            data_element_id_scheme=data_element_id_scheme,
            dry_run=dry_run,
            id_scheme=id_scheme,
            org_unit_id_scheme=org_unit_id_scheme,
            skip_audit=skip_audit,
        )

        target_request.additional_properties = d
        return target_request

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
