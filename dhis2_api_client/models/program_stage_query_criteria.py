from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.program_stage_query_criteria_assigned_user_mode import ProgramStageQueryCriteriaAssignedUserMode
from ..models.program_stage_query_criteria_enrollment_status import ProgramStageQueryCriteriaEnrollmentStatus
from ..models.program_stage_query_criteria_event_status import ProgramStageQueryCriteriaEventStatus
from ..models.program_stage_query_criteria_ou_mode import ProgramStageQueryCriteriaOuMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_value_filter import AttributeValueFilter
    from ..models.date_filter_period import DateFilterPeriod
    from ..models.event_data_filter import EventDataFilter


T = TypeVar("T", bound="ProgramStageQueryCriteria")


@_attrs_define
class ProgramStageQueryCriteria:
    """
    Attributes:
        assigned_user_mode (ProgramStageQueryCriteriaAssignedUserMode):
        enrollment_status (ProgramStageQueryCriteriaEnrollmentStatus):
        event_status (ProgramStageQueryCriteriaEventStatus):
        ou_mode (ProgramStageQueryCriteriaOuMode):
        assigned_users (Union[Unset, list[str]]):
        attribute_value_filters (Union[Unset, list['AttributeValueFilter']]):
        data_filters (Union[Unset, list['EventDataFilter']]):
        display_column_order (Union[Unset, list[str]]):
        enrolled_at (Union[Unset, DateFilterPeriod]):
        enrollment_occurred_at (Union[Unset, DateFilterPeriod]):
        event_created_at (Union[Unset, DateFilterPeriod]):
        event_occurred_at (Union[Unset, DateFilterPeriod]):
        event_scheduled_at (Union[Unset, DateFilterPeriod]):
        follow_up (Union[Unset, bool]):
        order (Union[Unset, str]):
        org_unit (Union[Unset, str]):
    """

    assigned_user_mode: ProgramStageQueryCriteriaAssignedUserMode
    enrollment_status: ProgramStageQueryCriteriaEnrollmentStatus
    event_status: ProgramStageQueryCriteriaEventStatus
    ou_mode: ProgramStageQueryCriteriaOuMode
    assigned_users: Union[Unset, list[str]] = UNSET
    attribute_value_filters: Union[Unset, list["AttributeValueFilter"]] = UNSET
    data_filters: Union[Unset, list["EventDataFilter"]] = UNSET
    display_column_order: Union[Unset, list[str]] = UNSET
    enrolled_at: Union[Unset, "DateFilterPeriod"] = UNSET
    enrollment_occurred_at: Union[Unset, "DateFilterPeriod"] = UNSET
    event_created_at: Union[Unset, "DateFilterPeriod"] = UNSET
    event_occurred_at: Union[Unset, "DateFilterPeriod"] = UNSET
    event_scheduled_at: Union[Unset, "DateFilterPeriod"] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    order: Union[Unset, str] = UNSET
    org_unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_user_mode = self.assigned_user_mode.value

        enrollment_status = self.enrollment_status.value

        event_status = self.event_status.value

        ou_mode = self.ou_mode.value

        assigned_users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigned_users, Unset):
            assigned_users = self.assigned_users

        attribute_value_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_value_filters, Unset):
            attribute_value_filters = []
            for attribute_value_filters_item_data in self.attribute_value_filters:
                attribute_value_filters_item = attribute_value_filters_item_data.to_dict()
                attribute_value_filters.append(attribute_value_filters_item)

        data_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_filters, Unset):
            data_filters = []
            for data_filters_item_data in self.data_filters:
                data_filters_item = data_filters_item_data.to_dict()
                data_filters.append(data_filters_item)

        display_column_order: Union[Unset, list[str]] = UNSET
        if not isinstance(self.display_column_order, Unset):
            display_column_order = self.display_column_order

        enrolled_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrolled_at, Unset):
            enrolled_at = self.enrolled_at.to_dict()

        enrollment_occurred_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_occurred_at, Unset):
            enrollment_occurred_at = self.enrollment_occurred_at.to_dict()

        event_created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_created_at, Unset):
            event_created_at = self.event_created_at.to_dict()

        event_occurred_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_occurred_at, Unset):
            event_occurred_at = self.event_occurred_at.to_dict()

        event_scheduled_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_scheduled_at, Unset):
            event_scheduled_at = self.event_scheduled_at.to_dict()

        follow_up = self.follow_up

        order = self.order

        org_unit = self.org_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignedUserMode": assigned_user_mode,
                "enrollmentStatus": enrollment_status,
                "eventStatus": event_status,
                "ouMode": ou_mode,
            }
        )
        if assigned_users is not UNSET:
            field_dict["assignedUsers"] = assigned_users
        if attribute_value_filters is not UNSET:
            field_dict["attributeValueFilters"] = attribute_value_filters
        if data_filters is not UNSET:
            field_dict["dataFilters"] = data_filters
        if display_column_order is not UNSET:
            field_dict["displayColumnOrder"] = display_column_order
        if enrolled_at is not UNSET:
            field_dict["enrolledAt"] = enrolled_at
        if enrollment_occurred_at is not UNSET:
            field_dict["enrollmentOccurredAt"] = enrollment_occurred_at
        if event_created_at is not UNSET:
            field_dict["eventCreatedAt"] = event_created_at
        if event_occurred_at is not UNSET:
            field_dict["eventOccurredAt"] = event_occurred_at
        if event_scheduled_at is not UNSET:
            field_dict["eventScheduledAt"] = event_scheduled_at
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if order is not UNSET:
            field_dict["order"] = order
        if org_unit is not UNSET:
            field_dict["orgUnit"] = org_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attribute_value_filter import AttributeValueFilter
        from ..models.date_filter_period import DateFilterPeriod
        from ..models.event_data_filter import EventDataFilter

        d = src_dict.copy()
        assigned_user_mode = ProgramStageQueryCriteriaAssignedUserMode(d.pop("assignedUserMode"))

        enrollment_status = ProgramStageQueryCriteriaEnrollmentStatus(d.pop("enrollmentStatus"))

        event_status = ProgramStageQueryCriteriaEventStatus(d.pop("eventStatus"))

        ou_mode = ProgramStageQueryCriteriaOuMode(d.pop("ouMode"))

        assigned_users = cast(list[str], d.pop("assignedUsers", UNSET))

        attribute_value_filters = []
        _attribute_value_filters = d.pop("attributeValueFilters", UNSET)
        for attribute_value_filters_item_data in _attribute_value_filters or []:
            attribute_value_filters_item = AttributeValueFilter.from_dict(attribute_value_filters_item_data)

            attribute_value_filters.append(attribute_value_filters_item)

        data_filters = []
        _data_filters = d.pop("dataFilters", UNSET)
        for data_filters_item_data in _data_filters or []:
            data_filters_item = EventDataFilter.from_dict(data_filters_item_data)

            data_filters.append(data_filters_item)

        display_column_order = cast(list[str], d.pop("displayColumnOrder", UNSET))

        _enrolled_at = d.pop("enrolledAt", UNSET)
        enrolled_at: Union[Unset, DateFilterPeriod]
        if isinstance(_enrolled_at, Unset):
            enrolled_at = UNSET
        else:
            enrolled_at = DateFilterPeriod.from_dict(_enrolled_at)

        _enrollment_occurred_at = d.pop("enrollmentOccurredAt", UNSET)
        enrollment_occurred_at: Union[Unset, DateFilterPeriod]
        if isinstance(_enrollment_occurred_at, Unset):
            enrollment_occurred_at = UNSET
        else:
            enrollment_occurred_at = DateFilterPeriod.from_dict(_enrollment_occurred_at)

        _event_created_at = d.pop("eventCreatedAt", UNSET)
        event_created_at: Union[Unset, DateFilterPeriod]
        if isinstance(_event_created_at, Unset):
            event_created_at = UNSET
        else:
            event_created_at = DateFilterPeriod.from_dict(_event_created_at)

        _event_occurred_at = d.pop("eventOccurredAt", UNSET)
        event_occurred_at: Union[Unset, DateFilterPeriod]
        if isinstance(_event_occurred_at, Unset):
            event_occurred_at = UNSET
        else:
            event_occurred_at = DateFilterPeriod.from_dict(_event_occurred_at)

        _event_scheduled_at = d.pop("eventScheduledAt", UNSET)
        event_scheduled_at: Union[Unset, DateFilterPeriod]
        if isinstance(_event_scheduled_at, Unset):
            event_scheduled_at = UNSET
        else:
            event_scheduled_at = DateFilterPeriod.from_dict(_event_scheduled_at)

        follow_up = d.pop("followUp", UNSET)

        order = d.pop("order", UNSET)

        org_unit = d.pop("orgUnit", UNSET)

        program_stage_query_criteria = cls(
            assigned_user_mode=assigned_user_mode,
            enrollment_status=enrollment_status,
            event_status=event_status,
            ou_mode=ou_mode,
            assigned_users=assigned_users,
            attribute_value_filters=attribute_value_filters,
            data_filters=data_filters,
            display_column_order=display_column_order,
            enrolled_at=enrolled_at,
            enrollment_occurred_at=enrollment_occurred_at,
            event_created_at=event_created_at,
            event_occurred_at=event_occurred_at,
            event_scheduled_at=event_scheduled_at,
            follow_up=follow_up,
            order=order,
            org_unit=org_unit,
        )

        program_stage_query_criteria.additional_properties = d
        return program_stage_query_criteria

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
