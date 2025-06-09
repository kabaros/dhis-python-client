from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_query_criteria_assigned_user_mode import EventQueryCriteriaAssignedUserMode
from ..models.event_query_criteria_ou_mode import EventQueryCriteriaOuMode
from ..models.event_query_criteria_status import EventQueryCriteriaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_filter_period import DateFilterPeriod
    from ..models.event_data_filter import EventDataFilter


T = TypeVar("T", bound="EventQueryCriteria")


@_attrs_define
class EventQueryCriteria:
    """
    Attributes:
        assigned_user_mode (EventQueryCriteriaAssignedUserMode):
        ou_mode (EventQueryCriteriaOuMode):
        status (EventQueryCriteriaStatus):
        assigned_users (Union[Unset, list[str]]):
        completed_date (Union[Unset, DateFilterPeriod]):
        data_filters (Union[Unset, list['EventDataFilter']]):
        display_column_order (Union[Unset, list[str]]):
        due_date (Union[Unset, DateFilterPeriod]):
        event_date (Union[Unset, DateFilterPeriod]):
        events (Union[Unset, list[str]]):
        follow_up (Union[Unset, bool]):
        last_updated_date (Union[Unset, DateFilterPeriod]):
        order (Union[Unset, str]):
        organisation_unit (Union[Unset, str]):
    """

    assigned_user_mode: EventQueryCriteriaAssignedUserMode
    ou_mode: EventQueryCriteriaOuMode
    status: EventQueryCriteriaStatus
    assigned_users: Union[Unset, list[str]] = UNSET
    completed_date: Union[Unset, "DateFilterPeriod"] = UNSET
    data_filters: Union[Unset, list["EventDataFilter"]] = UNSET
    display_column_order: Union[Unset, list[str]] = UNSET
    due_date: Union[Unset, "DateFilterPeriod"] = UNSET
    event_date: Union[Unset, "DateFilterPeriod"] = UNSET
    events: Union[Unset, list[str]] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    last_updated_date: Union[Unset, "DateFilterPeriod"] = UNSET
    order: Union[Unset, str] = UNSET
    organisation_unit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_user_mode = self.assigned_user_mode.value

        ou_mode = self.ou_mode.value

        status = self.status.value

        assigned_users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigned_users, Unset):
            assigned_users = self.assigned_users

        completed_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.to_dict()

        data_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_filters, Unset):
            data_filters = []
            for data_filters_item_data in self.data_filters:
                data_filters_item = data_filters_item_data.to_dict()
                data_filters.append(data_filters_item)

        display_column_order: Union[Unset, list[str]] = UNSET
        if not isinstance(self.display_column_order, Unset):
            display_column_order = self.display_column_order

        due_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.to_dict()

        event_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.to_dict()

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        follow_up = self.follow_up

        last_updated_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.to_dict()

        order = self.order

        organisation_unit = self.organisation_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignedUserMode": assigned_user_mode,
                "ouMode": ou_mode,
                "status": status,
            }
        )
        if assigned_users is not UNSET:
            field_dict["assignedUsers"] = assigned_users
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if data_filters is not UNSET:
            field_dict["dataFilters"] = data_filters
        if display_column_order is not UNSET:
            field_dict["displayColumnOrder"] = display_column_order
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if events is not UNSET:
            field_dict["events"] = events
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if last_updated_date is not UNSET:
            field_dict["lastUpdatedDate"] = last_updated_date
        if order is not UNSET:
            field_dict["order"] = order
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.date_filter_period import DateFilterPeriod
        from ..models.event_data_filter import EventDataFilter

        d = src_dict.copy()
        assigned_user_mode = EventQueryCriteriaAssignedUserMode(d.pop("assignedUserMode"))

        ou_mode = EventQueryCriteriaOuMode(d.pop("ouMode"))

        status = EventQueryCriteriaStatus(d.pop("status"))

        assigned_users = cast(list[str], d.pop("assignedUsers", UNSET))

        _completed_date = d.pop("completedDate", UNSET)
        completed_date: Union[Unset, DateFilterPeriod]
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = DateFilterPeriod.from_dict(_completed_date)

        data_filters = []
        _data_filters = d.pop("dataFilters", UNSET)
        for data_filters_item_data in _data_filters or []:
            data_filters_item = EventDataFilter.from_dict(data_filters_item_data)

            data_filters.append(data_filters_item)

        display_column_order = cast(list[str], d.pop("displayColumnOrder", UNSET))

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, DateFilterPeriod]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = DateFilterPeriod.from_dict(_due_date)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, DateFilterPeriod]
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = DateFilterPeriod.from_dict(_event_date)

        events = cast(list[str], d.pop("events", UNSET))

        follow_up = d.pop("followUp", UNSET)

        _last_updated_date = d.pop("lastUpdatedDate", UNSET)
        last_updated_date: Union[Unset, DateFilterPeriod]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = DateFilterPeriod.from_dict(_last_updated_date)

        order = d.pop("order", UNSET)

        organisation_unit = d.pop("organisationUnit", UNSET)

        event_query_criteria = cls(
            assigned_user_mode=assigned_user_mode,
            ou_mode=ou_mode,
            status=status,
            assigned_users=assigned_users,
            completed_date=completed_date,
            data_filters=data_filters,
            display_column_order=display_column_order,
            due_date=due_date,
            event_date=event_date,
            events=events,
            follow_up=follow_up,
            last_updated_date=last_updated_date,
            order=order,
            organisation_unit=organisation_unit,
        )

        event_query_criteria.additional_properties = d
        return event_query_criteria

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
