import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_configuration_job_status import JobConfigurationJobStatus
from ..models.job_configuration_job_type import JobConfigurationJobType
from ..models.job_configuration_last_executed_status import JobConfigurationLastExecutedStatus
from ..models.job_configuration_scheduling_type import JobConfigurationSchedulingType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.aggregate_data_exchange_job_parameters import AggregateDataExchangeJobParameters
    from ..models.analytics_job_parameters import AnalyticsJobParameters
    from ..models.attribute_value import AttributeValue
    from ..models.continuous_analytics_job_parameters import ContinuousAnalyticsJobParameters
    from ..models.data_integrity_details_job_parameters import DataIntegrityDetailsJobParameters
    from ..models.data_integrity_job_parameters import DataIntegrityJobParameters
    from ..models.data_synchronization_job_parameters import DataSynchronizationJobParameters
    from ..models.disable_inactive_users_job_parameters import DisableInactiveUsersJobParameters
    from ..models.event_programs_data_synchronization_job_parameters import (
        EventProgramsDataSynchronizationJobParameters,
    )
    from ..models.geo_json_import_job_params import GeoJsonImportJobParams
    from ..models.html_push_analytics_job_parameters import HtmlPushAnalyticsJobParameters
    from ..models.import_options import ImportOptions
    from ..models.job_configuration_created_by import JobConfigurationCreatedBy
    from ..models.job_configuration_last_updated_by import JobConfigurationLastUpdatedBy
    from ..models.job_configuration_user import JobConfigurationUser
    from ..models.lock_exception_cleanup_job_parameters import LockExceptionCleanupJobParameters
    from ..models.metadata_import_params import MetadataImportParams
    from ..models.metadata_sync_job_parameters import MetadataSyncJobParameters
    from ..models.monitoring_job_parameters import MonitoringJobParameters
    from ..models.predictor_job_parameters import PredictorJobParameters
    from ..models.push_analysis_job_parameters import PushAnalysisJobParameters
    from ..models.sharing import Sharing
    from ..models.sms_job_parameters import SmsJobParameters
    from ..models.sql_view_update_parameters import SqlViewUpdateParameters
    from ..models.test_job_parameters import TestJobParameters
    from ..models.tracker_programs_data_synchronization_job_parameters import (
        TrackerProgramsDataSynchronizationJobParameters,
    )
    from ..models.tracker_trigram_index_job_parameters import TrackerTrigramIndexJobParameters
    from ..models.translation import Translation


T = TypeVar("T", bound="JobConfiguration")


@_attrs_define
class JobConfiguration:
    """
    Attributes:
        job_status (JobConfigurationJobStatus):
        job_type (JobConfigurationJobType):
        last_executed_status (JobConfigurationLastExecutedStatus):
        scheduling_type (JobConfigurationSchedulingType):
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        configurable (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, JobConfigurationCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        cron_expression (Union[Unset, str]):
        delay (Union[Unset, int]):
        display_name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        error_codes (Union[Unset, str]):
        executed_by (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        job_parameters (Union['AggregateDataExchangeJobParameters', 'AnalyticsJobParameters',
            'ContinuousAnalyticsJobParameters', 'DataIntegrityDetailsJobParameters', 'DataIntegrityJobParameters',
            'DataSynchronizationJobParameters', 'DisableInactiveUsersJobParameters',
            'EventProgramsDataSynchronizationJobParameters', 'GeoJsonImportJobParams', 'HtmlPushAnalyticsJobParameters',
            'ImportOptions', 'LockExceptionCleanupJobParameters', 'MetadataImportParams', 'MetadataSyncJobParameters',
            'MonitoringJobParameters', 'PredictorJobParameters', 'PushAnalysisJobParameters', 'SmsJobParameters',
            'SqlViewUpdateParameters', 'TestJobParameters', 'TrackerProgramsDataSynchronizationJobParameters',
            'TrackerTrigramIndexJobParameters', Unset]):
        last_alive (Union[Unset, datetime.datetime]):
        last_executed (Union[Unset, datetime.datetime]):
        last_finished (Union[Unset, datetime.datetime]):
        last_runtime_execution (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, JobConfigurationLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        leader_only_job (Union[Unset, bool]):
        max_delayed_execution_time (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        next_execution_time (Union[Unset, datetime.datetime]):
        queue_name (Union[Unset, str]):
        queue_position (Union[Unset, int]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, JobConfigurationUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        user_uid (Union[Unset, str]):
    """

    job_status: JobConfigurationJobStatus
    job_type: JobConfigurationJobType
    last_executed_status: JobConfigurationLastExecutedStatus
    scheduling_type: JobConfigurationSchedulingType
    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    configurable: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "JobConfigurationCreatedBy"] = UNSET
    cron_expression: Union[Unset, str] = UNSET
    delay: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    error_codes: Union[Unset, str] = UNSET
    executed_by: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    job_parameters: Union[
        "AggregateDataExchangeJobParameters",
        "AnalyticsJobParameters",
        "ContinuousAnalyticsJobParameters",
        "DataIntegrityDetailsJobParameters",
        "DataIntegrityJobParameters",
        "DataSynchronizationJobParameters",
        "DisableInactiveUsersJobParameters",
        "EventProgramsDataSynchronizationJobParameters",
        "GeoJsonImportJobParams",
        "HtmlPushAnalyticsJobParameters",
        "ImportOptions",
        "LockExceptionCleanupJobParameters",
        "MetadataImportParams",
        "MetadataSyncJobParameters",
        "MonitoringJobParameters",
        "PredictorJobParameters",
        "PushAnalysisJobParameters",
        "SmsJobParameters",
        "SqlViewUpdateParameters",
        "TestJobParameters",
        "TrackerProgramsDataSynchronizationJobParameters",
        "TrackerTrigramIndexJobParameters",
        Unset,
    ] = UNSET
    last_alive: Union[Unset, datetime.datetime] = UNSET
    last_executed: Union[Unset, datetime.datetime] = UNSET
    last_finished: Union[Unset, datetime.datetime] = UNSET
    last_runtime_execution: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "JobConfigurationLastUpdatedBy"] = UNSET
    leader_only_job: Union[Unset, bool] = UNSET
    max_delayed_execution_time: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    next_execution_time: Union[Unset, datetime.datetime] = UNSET
    queue_name: Union[Unset, str] = UNSET
    queue_position: Union[Unset, int] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "JobConfigurationUser"] = UNSET
    user_uid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.aggregate_data_exchange_job_parameters import AggregateDataExchangeJobParameters
        from ..models.analytics_job_parameters import AnalyticsJobParameters
        from ..models.continuous_analytics_job_parameters import ContinuousAnalyticsJobParameters
        from ..models.data_integrity_details_job_parameters import DataIntegrityDetailsJobParameters
        from ..models.data_integrity_job_parameters import DataIntegrityJobParameters
        from ..models.data_synchronization_job_parameters import DataSynchronizationJobParameters
        from ..models.disable_inactive_users_job_parameters import DisableInactiveUsersJobParameters
        from ..models.event_programs_data_synchronization_job_parameters import (
            EventProgramsDataSynchronizationJobParameters,
        )
        from ..models.html_push_analytics_job_parameters import HtmlPushAnalyticsJobParameters
        from ..models.import_options import ImportOptions
        from ..models.lock_exception_cleanup_job_parameters import LockExceptionCleanupJobParameters
        from ..models.metadata_import_params import MetadataImportParams
        from ..models.metadata_sync_job_parameters import MetadataSyncJobParameters
        from ..models.monitoring_job_parameters import MonitoringJobParameters
        from ..models.predictor_job_parameters import PredictorJobParameters
        from ..models.push_analysis_job_parameters import PushAnalysisJobParameters
        from ..models.sms_job_parameters import SmsJobParameters
        from ..models.sql_view_update_parameters import SqlViewUpdateParameters
        from ..models.test_job_parameters import TestJobParameters
        from ..models.tracker_programs_data_synchronization_job_parameters import (
            TrackerProgramsDataSynchronizationJobParameters,
        )
        from ..models.tracker_trigram_index_job_parameters import TrackerTrigramIndexJobParameters

        job_status = self.job_status.value

        job_type = self.job_type.value

        last_executed_status = self.last_executed_status.value

        scheduling_type = self.scheduling_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        configurable = self.configurable

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        cron_expression = self.cron_expression

        delay = self.delay

        display_name = self.display_name

        enabled = self.enabled

        error_codes = self.error_codes

        executed_by = self.executed_by

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        href = self.href

        id = self.id

        job_parameters: Union[Unset, dict[str, Any]]
        if isinstance(self.job_parameters, Unset):
            job_parameters = UNSET
        elif isinstance(self.job_parameters, MetadataImportParams):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, ImportOptions):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, AnalyticsJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, ContinuousAnalyticsJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, MonitoringJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, PredictorJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, PushAnalysisJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, HtmlPushAnalyticsJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, SmsJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, MetadataSyncJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, EventProgramsDataSynchronizationJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, TrackerProgramsDataSynchronizationJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, DataSynchronizationJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, DisableInactiveUsersJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, TrackerTrigramIndexJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, DataIntegrityJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, DataIntegrityDetailsJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, AggregateDataExchangeJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, SqlViewUpdateParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, LockExceptionCleanupJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, TestJobParameters):
            job_parameters = self.job_parameters.to_dict()
        elif isinstance(self.job_parameters, ImportOptions):
            job_parameters = self.job_parameters.to_dict()
        else:
            job_parameters = self.job_parameters.to_dict()

        last_alive: Union[Unset, str] = UNSET
        if not isinstance(self.last_alive, Unset):
            last_alive = self.last_alive.isoformat()

        last_executed: Union[Unset, str] = UNSET
        if not isinstance(self.last_executed, Unset):
            last_executed = self.last_executed.isoformat()

        last_finished: Union[Unset, str] = UNSET
        if not isinstance(self.last_finished, Unset):
            last_finished = self.last_finished.isoformat()

        last_runtime_execution = self.last_runtime_execution

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        leader_only_job = self.leader_only_job

        max_delayed_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.max_delayed_execution_time, Unset):
            max_delayed_execution_time = self.max_delayed_execution_time.isoformat()

        name = self.name

        next_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_execution_time, Unset):
            next_execution_time = self.next_execution_time.isoformat()

        queue_name = self.queue_name

        queue_position = self.queue_position

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_uid = self.user_uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobStatus": job_status,
                "jobType": job_type,
                "lastExecutedStatus": last_executed_status,
                "schedulingType": scheduling_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if configurable is not UNSET:
            field_dict["configurable"] = configurable
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if delay is not UNSET:
            field_dict["delay"] = delay
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if error_codes is not UNSET:
            field_dict["errorCodes"] = error_codes
        if executed_by is not UNSET:
            field_dict["executedBy"] = executed_by
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if job_parameters is not UNSET:
            field_dict["jobParameters"] = job_parameters
        if last_alive is not UNSET:
            field_dict["lastAlive"] = last_alive
        if last_executed is not UNSET:
            field_dict["lastExecuted"] = last_executed
        if last_finished is not UNSET:
            field_dict["lastFinished"] = last_finished
        if last_runtime_execution is not UNSET:
            field_dict["lastRuntimeExecution"] = last_runtime_execution
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if leader_only_job is not UNSET:
            field_dict["leaderOnlyJob"] = leader_only_job
        if max_delayed_execution_time is not UNSET:
            field_dict["maxDelayedExecutionTime"] = max_delayed_execution_time
        if name is not UNSET:
            field_dict["name"] = name
        if next_execution_time is not UNSET:
            field_dict["nextExecutionTime"] = next_execution_time
        if queue_name is not UNSET:
            field_dict["queueName"] = queue_name
        if queue_position is not UNSET:
            field_dict["queuePosition"] = queue_position
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.aggregate_data_exchange_job_parameters import AggregateDataExchangeJobParameters
        from ..models.analytics_job_parameters import AnalyticsJobParameters
        from ..models.attribute_value import AttributeValue
        from ..models.continuous_analytics_job_parameters import ContinuousAnalyticsJobParameters
        from ..models.data_integrity_details_job_parameters import DataIntegrityDetailsJobParameters
        from ..models.data_integrity_job_parameters import DataIntegrityJobParameters
        from ..models.data_synchronization_job_parameters import DataSynchronizationJobParameters
        from ..models.disable_inactive_users_job_parameters import DisableInactiveUsersJobParameters
        from ..models.event_programs_data_synchronization_job_parameters import (
            EventProgramsDataSynchronizationJobParameters,
        )
        from ..models.geo_json_import_job_params import GeoJsonImportJobParams
        from ..models.html_push_analytics_job_parameters import HtmlPushAnalyticsJobParameters
        from ..models.import_options import ImportOptions
        from ..models.job_configuration_created_by import JobConfigurationCreatedBy
        from ..models.job_configuration_last_updated_by import JobConfigurationLastUpdatedBy
        from ..models.job_configuration_user import JobConfigurationUser
        from ..models.lock_exception_cleanup_job_parameters import LockExceptionCleanupJobParameters
        from ..models.metadata_import_params import MetadataImportParams
        from ..models.metadata_sync_job_parameters import MetadataSyncJobParameters
        from ..models.monitoring_job_parameters import MonitoringJobParameters
        from ..models.predictor_job_parameters import PredictorJobParameters
        from ..models.push_analysis_job_parameters import PushAnalysisJobParameters
        from ..models.sharing import Sharing
        from ..models.sms_job_parameters import SmsJobParameters
        from ..models.sql_view_update_parameters import SqlViewUpdateParameters
        from ..models.test_job_parameters import TestJobParameters
        from ..models.tracker_programs_data_synchronization_job_parameters import (
            TrackerProgramsDataSynchronizationJobParameters,
        )
        from ..models.tracker_trigram_index_job_parameters import TrackerTrigramIndexJobParameters
        from ..models.translation import Translation

        d = src_dict.copy()
        job_status = JobConfigurationJobStatus(d.pop("jobStatus"))

        job_type = JobConfigurationJobType(d.pop("jobType"))

        last_executed_status = JobConfigurationLastExecutedStatus(d.pop("lastExecutedStatus"))

        scheduling_type = JobConfigurationSchedulingType(d.pop("schedulingType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        configurable = d.pop("configurable", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, JobConfigurationCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = JobConfigurationCreatedBy.from_dict(_created_by)

        cron_expression = d.pop("cronExpression", UNSET)

        delay = d.pop("delay", UNSET)

        display_name = d.pop("displayName", UNSET)

        enabled = d.pop("enabled", UNSET)

        error_codes = d.pop("errorCodes", UNSET)

        executed_by = d.pop("executedBy", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        def _parse_job_parameters(
            data: object,
        ) -> Union[
            "AggregateDataExchangeJobParameters",
            "AnalyticsJobParameters",
            "ContinuousAnalyticsJobParameters",
            "DataIntegrityDetailsJobParameters",
            "DataIntegrityJobParameters",
            "DataSynchronizationJobParameters",
            "DisableInactiveUsersJobParameters",
            "EventProgramsDataSynchronizationJobParameters",
            "GeoJsonImportJobParams",
            "HtmlPushAnalyticsJobParameters",
            "ImportOptions",
            "LockExceptionCleanupJobParameters",
            "MetadataImportParams",
            "MetadataSyncJobParameters",
            "MonitoringJobParameters",
            "PredictorJobParameters",
            "PushAnalysisJobParameters",
            "SmsJobParameters",
            "SqlViewUpdateParameters",
            "TestJobParameters",
            "TrackerProgramsDataSynchronizationJobParameters",
            "TrackerTrigramIndexJobParameters",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_0 = MetadataImportParams.from_dict(data)

                return job_parameters_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_1 = ImportOptions.from_dict(data)

                return job_parameters_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_2 = AnalyticsJobParameters.from_dict(data)

                return job_parameters_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_3 = ContinuousAnalyticsJobParameters.from_dict(data)

                return job_parameters_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_4 = MonitoringJobParameters.from_dict(data)

                return job_parameters_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_5 = PredictorJobParameters.from_dict(data)

                return job_parameters_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_6 = PushAnalysisJobParameters.from_dict(data)

                return job_parameters_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_7 = HtmlPushAnalyticsJobParameters.from_dict(data)

                return job_parameters_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_8 = SmsJobParameters.from_dict(data)

                return job_parameters_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_9 = MetadataSyncJobParameters.from_dict(data)

                return job_parameters_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_10 = EventProgramsDataSynchronizationJobParameters.from_dict(data)

                return job_parameters_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_11 = TrackerProgramsDataSynchronizationJobParameters.from_dict(data)

                return job_parameters_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_12 = DataSynchronizationJobParameters.from_dict(data)

                return job_parameters_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_13 = DisableInactiveUsersJobParameters.from_dict(data)

                return job_parameters_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_14 = TrackerTrigramIndexJobParameters.from_dict(data)

                return job_parameters_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_15 = DataIntegrityJobParameters.from_dict(data)

                return job_parameters_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_16 = DataIntegrityDetailsJobParameters.from_dict(data)

                return job_parameters_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_17 = AggregateDataExchangeJobParameters.from_dict(data)

                return job_parameters_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_18 = SqlViewUpdateParameters.from_dict(data)

                return job_parameters_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_19 = LockExceptionCleanupJobParameters.from_dict(data)

                return job_parameters_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_20 = TestJobParameters.from_dict(data)

                return job_parameters_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_parameters_type_21 = ImportOptions.from_dict(data)

                return job_parameters_type_21
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            job_parameters_type_22 = GeoJsonImportJobParams.from_dict(data)

            return job_parameters_type_22

        job_parameters = _parse_job_parameters(d.pop("jobParameters", UNSET))

        _last_alive = d.pop("lastAlive", UNSET)
        last_alive: Union[Unset, datetime.datetime]
        if isinstance(_last_alive, Unset):
            last_alive = UNSET
        else:
            last_alive = isoparse(_last_alive)

        _last_executed = d.pop("lastExecuted", UNSET)
        last_executed: Union[Unset, datetime.datetime]
        if isinstance(_last_executed, Unset):
            last_executed = UNSET
        else:
            last_executed = isoparse(_last_executed)

        _last_finished = d.pop("lastFinished", UNSET)
        last_finished: Union[Unset, datetime.datetime]
        if isinstance(_last_finished, Unset):
            last_finished = UNSET
        else:
            last_finished = isoparse(_last_finished)

        last_runtime_execution = d.pop("lastRuntimeExecution", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, JobConfigurationLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = JobConfigurationLastUpdatedBy.from_dict(_last_updated_by)

        leader_only_job = d.pop("leaderOnlyJob", UNSET)

        _max_delayed_execution_time = d.pop("maxDelayedExecutionTime", UNSET)
        max_delayed_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_max_delayed_execution_time, Unset):
            max_delayed_execution_time = UNSET
        else:
            max_delayed_execution_time = isoparse(_max_delayed_execution_time)

        name = d.pop("name", UNSET)

        _next_execution_time = d.pop("nextExecutionTime", UNSET)
        next_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_next_execution_time, Unset):
            next_execution_time = UNSET
        else:
            next_execution_time = isoparse(_next_execution_time)

        queue_name = d.pop("queueName", UNSET)

        queue_position = d.pop("queuePosition", UNSET)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, JobConfigurationUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = JobConfigurationUser.from_dict(_user)

        user_uid = d.pop("userUid", UNSET)

        job_configuration = cls(
            job_status=job_status,
            job_type=job_type,
            last_executed_status=last_executed_status,
            scheduling_type=scheduling_type,
            access=access,
            attribute_values=attribute_values,
            code=code,
            configurable=configurable,
            created=created,
            created_by=created_by,
            cron_expression=cron_expression,
            delay=delay,
            display_name=display_name,
            enabled=enabled,
            error_codes=error_codes,
            executed_by=executed_by,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            job_parameters=job_parameters,
            last_alive=last_alive,
            last_executed=last_executed,
            last_finished=last_finished,
            last_runtime_execution=last_runtime_execution,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            leader_only_job=leader_only_job,
            max_delayed_execution_time=max_delayed_execution_time,
            name=name,
            next_execution_time=next_execution_time,
            queue_name=queue_name,
            queue_position=queue_position,
            sharing=sharing,
            translations=translations,
            user=user,
            user_uid=user_uid,
        )

        job_configuration.additional_properties = d
        return job_configuration

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
