import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_info import DatabaseInfo


T = TypeVar("T", bound="SystemInfo")


@_attrs_define
class SystemInfo:
    """
    Attributes:
        build_time (Union[Unset, datetime.datetime]):
        calendar (Union[Unset, str]):
        cluster_hostname (Union[Unset, str]):
        context_path (Union[Unset, str]):
        cpu_cores (Union[Unset, int]):
        database_info (Union[Unset, DatabaseInfo]):
        date_format (Union[Unset, str]):
        email_configured (Union[Unset, bool]):
        encryption (Union[Unset, bool]):
        environment_variable (Union[Unset, str]):
        external_directory (Union[Unset, str]):
        file_store_provider (Union[Unset, str]):
        instance_base_url (Union[Unset, str]):
        interval_since_last_analytics_table_partition_success (Union[Unset, str]):
        interval_since_last_analytics_table_success (Union[Unset, str]):
        is_metadata_sync_enabled (Union[Unset, bool]):
        is_metadata_version_enabled (Union[Unset, bool]):
        jasper_reports_version (Union[Unset, str]):
        java_opts (Union[Unset, str]):
        java_vendor (Union[Unset, str]):
        java_version (Union[Unset, str]):
        last_analytics_table_partition_runtime (Union[Unset, str]):
        last_analytics_table_partition_success (Union[Unset, datetime.datetime]):
        last_analytics_table_runtime (Union[Unset, str]):
        last_analytics_table_success (Union[Unset, datetime.datetime]):
        last_metadata_version_sync_attempt (Union[Unset, datetime.datetime]):
        last_system_monitoring_success (Union[Unset, datetime.datetime]):
        memory_info (Union[Unset, str]):
        node_id (Union[Unset, str]):
        os_architecture (Union[Unset, str]):
        os_name (Union[Unset, str]):
        os_version (Union[Unset, str]):
        read_only_mode (Union[Unset, str]):
        read_replica_count (Union[Unset, int]):
        redis_enabled (Union[Unset, bool]):
        redis_hostname (Union[Unset, str]):
        revision (Union[Unset, str]):
        server_date (Union[Unset, datetime.datetime]):
        server_time_zone_display_name (Union[Unset, str]):
        server_time_zone_id (Union[Unset, str]):
        system_id (Union[Unset, str]):
        system_metadata_version (Union[Unset, str]):
        system_monitoring_url (Union[Unset, str]):
        system_name (Union[Unset, str]):
        user_agent (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    build_time: Union[Unset, datetime.datetime] = UNSET
    calendar: Union[Unset, str] = UNSET
    cluster_hostname: Union[Unset, str] = UNSET
    context_path: Union[Unset, str] = UNSET
    cpu_cores: Union[Unset, int] = UNSET
    database_info: Union[Unset, "DatabaseInfo"] = UNSET
    date_format: Union[Unset, str] = UNSET
    email_configured: Union[Unset, bool] = UNSET
    encryption: Union[Unset, bool] = UNSET
    environment_variable: Union[Unset, str] = UNSET
    external_directory: Union[Unset, str] = UNSET
    file_store_provider: Union[Unset, str] = UNSET
    instance_base_url: Union[Unset, str] = UNSET
    interval_since_last_analytics_table_partition_success: Union[Unset, str] = UNSET
    interval_since_last_analytics_table_success: Union[Unset, str] = UNSET
    is_metadata_sync_enabled: Union[Unset, bool] = UNSET
    is_metadata_version_enabled: Union[Unset, bool] = UNSET
    jasper_reports_version: Union[Unset, str] = UNSET
    java_opts: Union[Unset, str] = UNSET
    java_vendor: Union[Unset, str] = UNSET
    java_version: Union[Unset, str] = UNSET
    last_analytics_table_partition_runtime: Union[Unset, str] = UNSET
    last_analytics_table_partition_success: Union[Unset, datetime.datetime] = UNSET
    last_analytics_table_runtime: Union[Unset, str] = UNSET
    last_analytics_table_success: Union[Unset, datetime.datetime] = UNSET
    last_metadata_version_sync_attempt: Union[Unset, datetime.datetime] = UNSET
    last_system_monitoring_success: Union[Unset, datetime.datetime] = UNSET
    memory_info: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    os_architecture: Union[Unset, str] = UNSET
    os_name: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    read_only_mode: Union[Unset, str] = UNSET
    read_replica_count: Union[Unset, int] = UNSET
    redis_enabled: Union[Unset, bool] = UNSET
    redis_hostname: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    server_date: Union[Unset, datetime.datetime] = UNSET
    server_time_zone_display_name: Union[Unset, str] = UNSET
    server_time_zone_id: Union[Unset, str] = UNSET
    system_id: Union[Unset, str] = UNSET
    system_metadata_version: Union[Unset, str] = UNSET
    system_monitoring_url: Union[Unset, str] = UNSET
    system_name: Union[Unset, str] = UNSET
    user_agent: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_time: Union[Unset, str] = UNSET
        if not isinstance(self.build_time, Unset):
            build_time = self.build_time.isoformat()

        calendar = self.calendar

        cluster_hostname = self.cluster_hostname

        context_path = self.context_path

        cpu_cores = self.cpu_cores

        database_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.database_info, Unset):
            database_info = self.database_info.to_dict()

        date_format = self.date_format

        email_configured = self.email_configured

        encryption = self.encryption

        environment_variable = self.environment_variable

        external_directory = self.external_directory

        file_store_provider = self.file_store_provider

        instance_base_url = self.instance_base_url

        interval_since_last_analytics_table_partition_success = (
            self.interval_since_last_analytics_table_partition_success
        )

        interval_since_last_analytics_table_success = self.interval_since_last_analytics_table_success

        is_metadata_sync_enabled = self.is_metadata_sync_enabled

        is_metadata_version_enabled = self.is_metadata_version_enabled

        jasper_reports_version = self.jasper_reports_version

        java_opts = self.java_opts

        java_vendor = self.java_vendor

        java_version = self.java_version

        last_analytics_table_partition_runtime = self.last_analytics_table_partition_runtime

        last_analytics_table_partition_success: Union[Unset, str] = UNSET
        if not isinstance(self.last_analytics_table_partition_success, Unset):
            last_analytics_table_partition_success = self.last_analytics_table_partition_success.isoformat()

        last_analytics_table_runtime = self.last_analytics_table_runtime

        last_analytics_table_success: Union[Unset, str] = UNSET
        if not isinstance(self.last_analytics_table_success, Unset):
            last_analytics_table_success = self.last_analytics_table_success.isoformat()

        last_metadata_version_sync_attempt: Union[Unset, str] = UNSET
        if not isinstance(self.last_metadata_version_sync_attempt, Unset):
            last_metadata_version_sync_attempt = self.last_metadata_version_sync_attempt.isoformat()

        last_system_monitoring_success: Union[Unset, str] = UNSET
        if not isinstance(self.last_system_monitoring_success, Unset):
            last_system_monitoring_success = self.last_system_monitoring_success.isoformat()

        memory_info = self.memory_info

        node_id = self.node_id

        os_architecture = self.os_architecture

        os_name = self.os_name

        os_version = self.os_version

        read_only_mode = self.read_only_mode

        read_replica_count = self.read_replica_count

        redis_enabled = self.redis_enabled

        redis_hostname = self.redis_hostname

        revision = self.revision

        server_date: Union[Unset, str] = UNSET
        if not isinstance(self.server_date, Unset):
            server_date = self.server_date.isoformat()

        server_time_zone_display_name = self.server_time_zone_display_name

        server_time_zone_id = self.server_time_zone_id

        system_id = self.system_id

        system_metadata_version = self.system_metadata_version

        system_monitoring_url = self.system_monitoring_url

        system_name = self.system_name

        user_agent = self.user_agent

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_time is not UNSET:
            field_dict["buildTime"] = build_time
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if cluster_hostname is not UNSET:
            field_dict["clusterHostname"] = cluster_hostname
        if context_path is not UNSET:
            field_dict["contextPath"] = context_path
        if cpu_cores is not UNSET:
            field_dict["cpuCores"] = cpu_cores
        if database_info is not UNSET:
            field_dict["databaseInfo"] = database_info
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if email_configured is not UNSET:
            field_dict["emailConfigured"] = email_configured
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if environment_variable is not UNSET:
            field_dict["environmentVariable"] = environment_variable
        if external_directory is not UNSET:
            field_dict["externalDirectory"] = external_directory
        if file_store_provider is not UNSET:
            field_dict["fileStoreProvider"] = file_store_provider
        if instance_base_url is not UNSET:
            field_dict["instanceBaseUrl"] = instance_base_url
        if interval_since_last_analytics_table_partition_success is not UNSET:
            field_dict["intervalSinceLastAnalyticsTablePartitionSuccess"] = (
                interval_since_last_analytics_table_partition_success
            )
        if interval_since_last_analytics_table_success is not UNSET:
            field_dict["intervalSinceLastAnalyticsTableSuccess"] = interval_since_last_analytics_table_success
        if is_metadata_sync_enabled is not UNSET:
            field_dict["isMetadataSyncEnabled"] = is_metadata_sync_enabled
        if is_metadata_version_enabled is not UNSET:
            field_dict["isMetadataVersionEnabled"] = is_metadata_version_enabled
        if jasper_reports_version is not UNSET:
            field_dict["jasperReportsVersion"] = jasper_reports_version
        if java_opts is not UNSET:
            field_dict["javaOpts"] = java_opts
        if java_vendor is not UNSET:
            field_dict["javaVendor"] = java_vendor
        if java_version is not UNSET:
            field_dict["javaVersion"] = java_version
        if last_analytics_table_partition_runtime is not UNSET:
            field_dict["lastAnalyticsTablePartitionRuntime"] = last_analytics_table_partition_runtime
        if last_analytics_table_partition_success is not UNSET:
            field_dict["lastAnalyticsTablePartitionSuccess"] = last_analytics_table_partition_success
        if last_analytics_table_runtime is not UNSET:
            field_dict["lastAnalyticsTableRuntime"] = last_analytics_table_runtime
        if last_analytics_table_success is not UNSET:
            field_dict["lastAnalyticsTableSuccess"] = last_analytics_table_success
        if last_metadata_version_sync_attempt is not UNSET:
            field_dict["lastMetadataVersionSyncAttempt"] = last_metadata_version_sync_attempt
        if last_system_monitoring_success is not UNSET:
            field_dict["lastSystemMonitoringSuccess"] = last_system_monitoring_success
        if memory_info is not UNSET:
            field_dict["memoryInfo"] = memory_info
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if os_architecture is not UNSET:
            field_dict["osArchitecture"] = os_architecture
        if os_name is not UNSET:
            field_dict["osName"] = os_name
        if os_version is not UNSET:
            field_dict["osVersion"] = os_version
        if read_only_mode is not UNSET:
            field_dict["readOnlyMode"] = read_only_mode
        if read_replica_count is not UNSET:
            field_dict["readReplicaCount"] = read_replica_count
        if redis_enabled is not UNSET:
            field_dict["redisEnabled"] = redis_enabled
        if redis_hostname is not UNSET:
            field_dict["redisHostname"] = redis_hostname
        if revision is not UNSET:
            field_dict["revision"] = revision
        if server_date is not UNSET:
            field_dict["serverDate"] = server_date
        if server_time_zone_display_name is not UNSET:
            field_dict["serverTimeZoneDisplayName"] = server_time_zone_display_name
        if server_time_zone_id is not UNSET:
            field_dict["serverTimeZoneId"] = server_time_zone_id
        if system_id is not UNSET:
            field_dict["systemId"] = system_id
        if system_metadata_version is not UNSET:
            field_dict["systemMetadataVersion"] = system_metadata_version
        if system_monitoring_url is not UNSET:
            field_dict["systemMonitoringUrl"] = system_monitoring_url
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.database_info import DatabaseInfo

        d = src_dict.copy()
        _build_time = d.pop("buildTime", UNSET)
        build_time: Union[Unset, datetime.datetime]
        if isinstance(_build_time, Unset):
            build_time = UNSET
        else:
            build_time = isoparse(_build_time)

        calendar = d.pop("calendar", UNSET)

        cluster_hostname = d.pop("clusterHostname", UNSET)

        context_path = d.pop("contextPath", UNSET)

        cpu_cores = d.pop("cpuCores", UNSET)

        _database_info = d.pop("databaseInfo", UNSET)
        database_info: Union[Unset, DatabaseInfo]
        if isinstance(_database_info, Unset):
            database_info = UNSET
        else:
            database_info = DatabaseInfo.from_dict(_database_info)

        date_format = d.pop("dateFormat", UNSET)

        email_configured = d.pop("emailConfigured", UNSET)

        encryption = d.pop("encryption", UNSET)

        environment_variable = d.pop("environmentVariable", UNSET)

        external_directory = d.pop("externalDirectory", UNSET)

        file_store_provider = d.pop("fileStoreProvider", UNSET)

        instance_base_url = d.pop("instanceBaseUrl", UNSET)

        interval_since_last_analytics_table_partition_success = d.pop(
            "intervalSinceLastAnalyticsTablePartitionSuccess", UNSET
        )

        interval_since_last_analytics_table_success = d.pop("intervalSinceLastAnalyticsTableSuccess", UNSET)

        is_metadata_sync_enabled = d.pop("isMetadataSyncEnabled", UNSET)

        is_metadata_version_enabled = d.pop("isMetadataVersionEnabled", UNSET)

        jasper_reports_version = d.pop("jasperReportsVersion", UNSET)

        java_opts = d.pop("javaOpts", UNSET)

        java_vendor = d.pop("javaVendor", UNSET)

        java_version = d.pop("javaVersion", UNSET)

        last_analytics_table_partition_runtime = d.pop("lastAnalyticsTablePartitionRuntime", UNSET)

        _last_analytics_table_partition_success = d.pop("lastAnalyticsTablePartitionSuccess", UNSET)
        last_analytics_table_partition_success: Union[Unset, datetime.datetime]
        if isinstance(_last_analytics_table_partition_success, Unset):
            last_analytics_table_partition_success = UNSET
        else:
            last_analytics_table_partition_success = isoparse(_last_analytics_table_partition_success)

        last_analytics_table_runtime = d.pop("lastAnalyticsTableRuntime", UNSET)

        _last_analytics_table_success = d.pop("lastAnalyticsTableSuccess", UNSET)
        last_analytics_table_success: Union[Unset, datetime.datetime]
        if isinstance(_last_analytics_table_success, Unset):
            last_analytics_table_success = UNSET
        else:
            last_analytics_table_success = isoparse(_last_analytics_table_success)

        _last_metadata_version_sync_attempt = d.pop("lastMetadataVersionSyncAttempt", UNSET)
        last_metadata_version_sync_attempt: Union[Unset, datetime.datetime]
        if isinstance(_last_metadata_version_sync_attempt, Unset):
            last_metadata_version_sync_attempt = UNSET
        else:
            last_metadata_version_sync_attempt = isoparse(_last_metadata_version_sync_attempt)

        _last_system_monitoring_success = d.pop("lastSystemMonitoringSuccess", UNSET)
        last_system_monitoring_success: Union[Unset, datetime.datetime]
        if isinstance(_last_system_monitoring_success, Unset):
            last_system_monitoring_success = UNSET
        else:
            last_system_monitoring_success = isoparse(_last_system_monitoring_success)

        memory_info = d.pop("memoryInfo", UNSET)

        node_id = d.pop("nodeId", UNSET)

        os_architecture = d.pop("osArchitecture", UNSET)

        os_name = d.pop("osName", UNSET)

        os_version = d.pop("osVersion", UNSET)

        read_only_mode = d.pop("readOnlyMode", UNSET)

        read_replica_count = d.pop("readReplicaCount", UNSET)

        redis_enabled = d.pop("redisEnabled", UNSET)

        redis_hostname = d.pop("redisHostname", UNSET)

        revision = d.pop("revision", UNSET)

        _server_date = d.pop("serverDate", UNSET)
        server_date: Union[Unset, datetime.datetime]
        if isinstance(_server_date, Unset):
            server_date = UNSET
        else:
            server_date = isoparse(_server_date)

        server_time_zone_display_name = d.pop("serverTimeZoneDisplayName", UNSET)

        server_time_zone_id = d.pop("serverTimeZoneId", UNSET)

        system_id = d.pop("systemId", UNSET)

        system_metadata_version = d.pop("systemMetadataVersion", UNSET)

        system_monitoring_url = d.pop("systemMonitoringUrl", UNSET)

        system_name = d.pop("systemName", UNSET)

        user_agent = d.pop("userAgent", UNSET)

        version = d.pop("version", UNSET)

        system_info = cls(
            build_time=build_time,
            calendar=calendar,
            cluster_hostname=cluster_hostname,
            context_path=context_path,
            cpu_cores=cpu_cores,
            database_info=database_info,
            date_format=date_format,
            email_configured=email_configured,
            encryption=encryption,
            environment_variable=environment_variable,
            external_directory=external_directory,
            file_store_provider=file_store_provider,
            instance_base_url=instance_base_url,
            interval_since_last_analytics_table_partition_success=interval_since_last_analytics_table_partition_success,
            interval_since_last_analytics_table_success=interval_since_last_analytics_table_success,
            is_metadata_sync_enabled=is_metadata_sync_enabled,
            is_metadata_version_enabled=is_metadata_version_enabled,
            jasper_reports_version=jasper_reports_version,
            java_opts=java_opts,
            java_vendor=java_vendor,
            java_version=java_version,
            last_analytics_table_partition_runtime=last_analytics_table_partition_runtime,
            last_analytics_table_partition_success=last_analytics_table_partition_success,
            last_analytics_table_runtime=last_analytics_table_runtime,
            last_analytics_table_success=last_analytics_table_success,
            last_metadata_version_sync_attempt=last_metadata_version_sync_attempt,
            last_system_monitoring_success=last_system_monitoring_success,
            memory_info=memory_info,
            node_id=node_id,
            os_architecture=os_architecture,
            os_name=os_name,
            os_version=os_version,
            read_only_mode=read_only_mode,
            read_replica_count=read_replica_count,
            redis_enabled=redis_enabled,
            redis_hostname=redis_hostname,
            revision=revision,
            server_date=server_date,
            server_time_zone_display_name=server_time_zone_display_name,
            server_time_zone_id=server_time_zone_id,
            system_id=system_id,
            system_metadata_version=system_metadata_version,
            system_monitoring_url=system_monitoring_url,
            system_name=system_name,
            user_agent=user_agent,
            version=version,
        )

        system_info.additional_properties = d
        return system_info

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
