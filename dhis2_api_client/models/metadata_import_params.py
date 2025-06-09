from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.metadata_import_params_atomic_mode import MetadataImportParamsAtomicMode
from ..models.metadata_import_params_flush_mode import MetadataImportParamsFlushMode
from ..models.metadata_import_params_identifier import MetadataImportParamsIdentifier
from ..models.metadata_import_params_import_mode import MetadataImportParamsImportMode
from ..models.metadata_import_params_import_report_mode import MetadataImportParamsImportReportMode
from ..models.metadata_import_params_import_strategy import MetadataImportParamsImportStrategy
from ..models.metadata_import_params_preheat_mode import MetadataImportParamsPreheatMode
from ..models.metadata_import_params_user_override_mode import MetadataImportParamsUserOverrideMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataImportParams")


@_attrs_define
class MetadataImportParams:
    """
    Attributes:
        atomic_mode (MetadataImportParamsAtomicMode):
        flush_mode (MetadataImportParamsFlushMode):
        identifier (MetadataImportParamsIdentifier):
        import_mode (MetadataImportParamsImportMode):
        import_report_mode (MetadataImportParamsImportReportMode):
        import_strategy (MetadataImportParamsImportStrategy):
        preheat_mode (MetadataImportParamsPreheatMode):
        user_override_mode (MetadataImportParamsUserOverrideMode):
        async_ (Union[Unset, bool]):
        metadata_sync_import (Union[Unset, bool]):
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        skip_sharing (Union[Unset, bool]):
        skip_translation (Union[Unset, bool]):
        skip_validation (Union[Unset, bool]):
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
    """

    atomic_mode: MetadataImportParamsAtomicMode
    flush_mode: MetadataImportParamsFlushMode
    identifier: MetadataImportParamsIdentifier
    import_mode: MetadataImportParamsImportMode
    import_report_mode: MetadataImportParamsImportReportMode
    import_strategy: MetadataImportParamsImportStrategy
    preheat_mode: MetadataImportParamsPreheatMode
    user_override_mode: MetadataImportParamsUserOverrideMode
    async_: Union[Unset, bool] = UNSET
    metadata_sync_import: Union[Unset, bool] = UNSET
    override_user: Union[Unset, str] = UNSET
    skip_sharing: Union[Unset, bool] = UNSET
    skip_translation: Union[Unset, bool] = UNSET
    skip_validation: Union[Unset, bool] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        atomic_mode = self.atomic_mode.value

        flush_mode = self.flush_mode.value

        identifier = self.identifier.value

        import_mode = self.import_mode.value

        import_report_mode = self.import_report_mode.value

        import_strategy = self.import_strategy.value

        preheat_mode = self.preheat_mode.value

        user_override_mode = self.user_override_mode.value

        async_ = self.async_

        metadata_sync_import = self.metadata_sync_import

        override_user = self.override_user

        skip_sharing = self.skip_sharing

        skip_translation = self.skip_translation

        skip_validation = self.skip_validation

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "atomicMode": atomic_mode,
                "flushMode": flush_mode,
                "identifier": identifier,
                "importMode": import_mode,
                "importReportMode": import_report_mode,
                "importStrategy": import_strategy,
                "preheatMode": preheat_mode,
                "userOverrideMode": user_override_mode,
            }
        )
        if async_ is not UNSET:
            field_dict["async"] = async_
        if metadata_sync_import is not UNSET:
            field_dict["metadataSyncImport"] = metadata_sync_import
        if override_user is not UNSET:
            field_dict["overrideUser"] = override_user
        if skip_sharing is not UNSET:
            field_dict["skipSharing"] = skip_sharing
        if skip_translation is not UNSET:
            field_dict["skipTranslation"] = skip_translation
        if skip_validation is not UNSET:
            field_dict["skipValidation"] = skip_validation
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        atomic_mode = MetadataImportParamsAtomicMode(d.pop("atomicMode"))

        flush_mode = MetadataImportParamsFlushMode(d.pop("flushMode"))

        identifier = MetadataImportParamsIdentifier(d.pop("identifier"))

        import_mode = MetadataImportParamsImportMode(d.pop("importMode"))

        import_report_mode = MetadataImportParamsImportReportMode(d.pop("importReportMode"))

        import_strategy = MetadataImportParamsImportStrategy(d.pop("importStrategy"))

        preheat_mode = MetadataImportParamsPreheatMode(d.pop("preheatMode"))

        user_override_mode = MetadataImportParamsUserOverrideMode(d.pop("userOverrideMode"))

        async_ = d.pop("async", UNSET)

        metadata_sync_import = d.pop("metadataSyncImport", UNSET)

        override_user = d.pop("overrideUser", UNSET)

        skip_sharing = d.pop("skipSharing", UNSET)

        skip_translation = d.pop("skipTranslation", UNSET)

        skip_validation = d.pop("skipValidation", UNSET)

        user = d.pop("user", UNSET)

        metadata_import_params = cls(
            atomic_mode=atomic_mode,
            flush_mode=flush_mode,
            identifier=identifier,
            import_mode=import_mode,
            import_report_mode=import_report_mode,
            import_strategy=import_strategy,
            preheat_mode=preheat_mode,
            user_override_mode=user_override_mode,
            async_=async_,
            metadata_sync_import=metadata_sync_import,
            override_user=override_user,
            skip_sharing=skip_sharing,
            skip_translation=skip_translation,
            skip_validation=skip_validation,
            user=user,
        )

        metadata_import_params.additional_properties = d
        return metadata_import_params

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
