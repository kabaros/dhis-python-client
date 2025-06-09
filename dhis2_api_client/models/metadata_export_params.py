from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_export_params_defaults import MetadataExportParamsDefaults
from ..models.metadata_export_params_inclusion_strategy import MetadataExportParamsInclusionStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metadata_export_params_object_export_with_dependencies import (
        MetadataExportParamsObjectExportWithDependencies,
    )
    from ..models.user_details import UserDetails


T = TypeVar("T", bound="MetadataExportParams")


@_attrs_define
class MetadataExportParams:
    """
    Attributes:
        defaults (MetadataExportParamsDefaults):
        classes (Union[Unset, list[str]]):
        current_user_details (Union[Unset, UserDetails]):
        default_fields (Union[Unset, list[str]]):
        default_filter (Union[Unset, list[str]]):
        default_order (Union[Unset, list[str]]):
        download (Union[Unset, bool]):
        export_with_dependencies (Union[Unset, bool]):
        inclusion_strategy (Union[Unset, MetadataExportParamsInclusionStrategy]):
        object_export_with_dependencies (Union[Unset, MetadataExportParamsObjectExportWithDependencies]): A UID
            reference to a any type of object
            (Java name `org.hisp.dhis.common.IdentifiableObject`)
        skip_sharing (Union[Unset, bool]):
    """

    defaults: MetadataExportParamsDefaults
    classes: Union[Unset, list[str]] = UNSET
    current_user_details: Union[Unset, "UserDetails"] = UNSET
    default_fields: Union[Unset, list[str]] = UNSET
    default_filter: Union[Unset, list[str]] = UNSET
    default_order: Union[Unset, list[str]] = UNSET
    download: Union[Unset, bool] = UNSET
    export_with_dependencies: Union[Unset, bool] = UNSET
    inclusion_strategy: Union[Unset, MetadataExportParamsInclusionStrategy] = UNSET
    object_export_with_dependencies: Union[Unset, "MetadataExportParamsObjectExportWithDependencies"] = UNSET
    skip_sharing: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        defaults = self.defaults.value

        classes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = self.classes

        current_user_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.current_user_details, Unset):
            current_user_details = self.current_user_details.to_dict()

        default_fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.default_fields, Unset):
            default_fields = self.default_fields

        default_filter: Union[Unset, list[str]] = UNSET
        if not isinstance(self.default_filter, Unset):
            default_filter = self.default_filter

        default_order: Union[Unset, list[str]] = UNSET
        if not isinstance(self.default_order, Unset):
            default_order = self.default_order

        download = self.download

        export_with_dependencies = self.export_with_dependencies

        inclusion_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.inclusion_strategy, Unset):
            inclusion_strategy = self.inclusion_strategy.value

        object_export_with_dependencies: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_export_with_dependencies, Unset):
            object_export_with_dependencies = self.object_export_with_dependencies.to_dict()

        skip_sharing = self.skip_sharing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "defaults": defaults,
            }
        )
        if classes is not UNSET:
            field_dict["classes"] = classes
        if current_user_details is not UNSET:
            field_dict["currentUserDetails"] = current_user_details
        if default_fields is not UNSET:
            field_dict["defaultFields"] = default_fields
        if default_filter is not UNSET:
            field_dict["defaultFilter"] = default_filter
        if default_order is not UNSET:
            field_dict["defaultOrder"] = default_order
        if download is not UNSET:
            field_dict["download"] = download
        if export_with_dependencies is not UNSET:
            field_dict["exportWithDependencies"] = export_with_dependencies
        if inclusion_strategy is not UNSET:
            field_dict["inclusionStrategy"] = inclusion_strategy
        if object_export_with_dependencies is not UNSET:
            field_dict["objectExportWithDependencies"] = object_export_with_dependencies
        if skip_sharing is not UNSET:
            field_dict["skipSharing"] = skip_sharing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.metadata_export_params_object_export_with_dependencies import (
            MetadataExportParamsObjectExportWithDependencies,
        )
        from ..models.user_details import UserDetails

        d = src_dict.copy()
        defaults = MetadataExportParamsDefaults(d.pop("defaults"))

        classes = cast(list[str], d.pop("classes", UNSET))

        _current_user_details = d.pop("currentUserDetails", UNSET)
        current_user_details: Union[Unset, UserDetails]
        if isinstance(_current_user_details, Unset):
            current_user_details = UNSET
        else:
            current_user_details = UserDetails.from_dict(_current_user_details)

        default_fields = cast(list[str], d.pop("defaultFields", UNSET))

        default_filter = cast(list[str], d.pop("defaultFilter", UNSET))

        default_order = cast(list[str], d.pop("defaultOrder", UNSET))

        download = d.pop("download", UNSET)

        export_with_dependencies = d.pop("exportWithDependencies", UNSET)

        _inclusion_strategy = d.pop("inclusionStrategy", UNSET)
        inclusion_strategy: Union[Unset, MetadataExportParamsInclusionStrategy]
        if isinstance(_inclusion_strategy, Unset):
            inclusion_strategy = UNSET
        else:
            inclusion_strategy = MetadataExportParamsInclusionStrategy(_inclusion_strategy)

        _object_export_with_dependencies = d.pop("objectExportWithDependencies", UNSET)
        object_export_with_dependencies: Union[Unset, MetadataExportParamsObjectExportWithDependencies]
        if isinstance(_object_export_with_dependencies, Unset):
            object_export_with_dependencies = UNSET
        else:
            object_export_with_dependencies = MetadataExportParamsObjectExportWithDependencies.from_dict(
                _object_export_with_dependencies
            )

        skip_sharing = d.pop("skipSharing", UNSET)

        metadata_export_params = cls(
            defaults=defaults,
            classes=classes,
            current_user_details=current_user_details,
            default_fields=default_fields,
            default_filter=default_filter,
            default_order=default_order,
            download=download,
            export_with_dependencies=export_with_dependencies,
            inclusion_strategy=inclusion_strategy,
            object_export_with_dependencies=object_export_with_dependencies,
            skip_sharing=skip_sharing,
        )

        metadata_export_params.additional_properties = d
        return metadata_export_params

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
