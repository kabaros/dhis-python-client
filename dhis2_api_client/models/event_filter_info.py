from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_filter_info_assigned_user_mode import EventFilterInfoAssignedUserMode
from ..models.event_filter_info_event_status import EventFilterInfoEventStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_period import FilterPeriod


T = TypeVar("T", bound="EventFilterInfo")


@_attrs_define
class EventFilterInfo:
    """
    Attributes:
        assigned_user_mode (EventFilterInfoAssignedUserMode):
        event_status (EventFilterInfoEventStatus):
        assigned_users (Union[Unset, list[str]]):
        event_created_period (Union[Unset, FilterPeriod]):
        program_stage (Union[Unset, str]):
    """

    assigned_user_mode: EventFilterInfoAssignedUserMode
    event_status: EventFilterInfoEventStatus
    assigned_users: Union[Unset, list[str]] = UNSET
    event_created_period: Union[Unset, "FilterPeriod"] = UNSET
    program_stage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_user_mode = self.assigned_user_mode.value

        event_status = self.event_status.value

        assigned_users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigned_users, Unset):
            assigned_users = self.assigned_users

        event_created_period: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_created_period, Unset):
            event_created_period = self.event_created_period.to_dict()

        program_stage = self.program_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignedUserMode": assigned_user_mode,
                "eventStatus": event_status,
            }
        )
        if assigned_users is not UNSET:
            field_dict["assignedUsers"] = assigned_users
        if event_created_period is not UNSET:
            field_dict["eventCreatedPeriod"] = event_created_period
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.filter_period import FilterPeriod

        d = src_dict.copy()
        assigned_user_mode = EventFilterInfoAssignedUserMode(d.pop("assignedUserMode"))

        event_status = EventFilterInfoEventStatus(d.pop("eventStatus"))

        assigned_users = cast(list[str], d.pop("assignedUsers", UNSET))

        _event_created_period = d.pop("eventCreatedPeriod", UNSET)
        event_created_period: Union[Unset, FilterPeriod]
        if isinstance(_event_created_period, Unset):
            event_created_period = UNSET
        else:
            event_created_period = FilterPeriod.from_dict(_event_created_period)

        program_stage = d.pop("programStage", UNSET)

        event_filter_info = cls(
            assigned_user_mode=assigned_user_mode,
            event_status=event_status,
            assigned_users=assigned_users,
            event_created_period=event_created_period,
            program_stage=program_stage,
        )

        event_filter_info.additional_properties = d
        return event_filter_info

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
