from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_summary_active_users import DataSummaryActiveUsers
    from ..models.data_summary_data_value_count import DataSummaryDataValueCount
    from ..models.data_summary_event_count import DataSummaryEventCount
    from ..models.data_summary_object_counts import DataSummaryObjectCounts
    from ..models.data_summary_user_invitations import DataSummaryUserInvitations
    from ..models.dhis_2_info import Dhis2Info


T = TypeVar("T", bound="DataSummary")


@_attrs_define
class DataSummary:
    """
    Attributes:
        active_users (Union[Unset, DataSummaryActiveUsers]): keys are class java.lang.Integer
        data_value_count (Union[Unset, DataSummaryDataValueCount]): keys are class java.lang.Integer
        event_count (Union[Unset, DataSummaryEventCount]): keys are class java.lang.Integer
        object_counts (Union[Unset, DataSummaryObjectCounts]):
        system (Union[Unset, Dhis2Info]):
        user_invitations (Union[Unset, DataSummaryUserInvitations]):
    """

    active_users: Union[Unset, "DataSummaryActiveUsers"] = UNSET
    data_value_count: Union[Unset, "DataSummaryDataValueCount"] = UNSET
    event_count: Union[Unset, "DataSummaryEventCount"] = UNSET
    object_counts: Union[Unset, "DataSummaryObjectCounts"] = UNSET
    system: Union[Unset, "Dhis2Info"] = UNSET
    user_invitations: Union[Unset, "DataSummaryUserInvitations"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_users: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.active_users, Unset):
            active_users = self.active_users.to_dict()

        data_value_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_value_count, Unset):
            data_value_count = self.data_value_count.to_dict()

        event_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_count, Unset):
            event_count = self.event_count.to_dict()

        object_counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.object_counts, Unset):
            object_counts = self.object_counts.to_dict()

        system: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system, Unset):
            system = self.system.to_dict()

        user_invitations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user_invitations, Unset):
            user_invitations = self.user_invitations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_users is not UNSET:
            field_dict["activeUsers"] = active_users
        if data_value_count is not UNSET:
            field_dict["dataValueCount"] = data_value_count
        if event_count is not UNSET:
            field_dict["eventCount"] = event_count
        if object_counts is not UNSET:
            field_dict["objectCounts"] = object_counts
        if system is not UNSET:
            field_dict["system"] = system
        if user_invitations is not UNSET:
            field_dict["userInvitations"] = user_invitations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_summary_active_users import DataSummaryActiveUsers
        from ..models.data_summary_data_value_count import DataSummaryDataValueCount
        from ..models.data_summary_event_count import DataSummaryEventCount
        from ..models.data_summary_object_counts import DataSummaryObjectCounts
        from ..models.data_summary_user_invitations import DataSummaryUserInvitations
        from ..models.dhis_2_info import Dhis2Info

        d = src_dict.copy()
        _active_users = d.pop("activeUsers", UNSET)
        active_users: Union[Unset, DataSummaryActiveUsers]
        if isinstance(_active_users, Unset):
            active_users = UNSET
        else:
            active_users = DataSummaryActiveUsers.from_dict(_active_users)

        _data_value_count = d.pop("dataValueCount", UNSET)
        data_value_count: Union[Unset, DataSummaryDataValueCount]
        if isinstance(_data_value_count, Unset):
            data_value_count = UNSET
        else:
            data_value_count = DataSummaryDataValueCount.from_dict(_data_value_count)

        _event_count = d.pop("eventCount", UNSET)
        event_count: Union[Unset, DataSummaryEventCount]
        if isinstance(_event_count, Unset):
            event_count = UNSET
        else:
            event_count = DataSummaryEventCount.from_dict(_event_count)

        _object_counts = d.pop("objectCounts", UNSET)
        object_counts: Union[Unset, DataSummaryObjectCounts]
        if isinstance(_object_counts, Unset):
            object_counts = UNSET
        else:
            object_counts = DataSummaryObjectCounts.from_dict(_object_counts)

        _system = d.pop("system", UNSET)
        system: Union[Unset, Dhis2Info]
        if isinstance(_system, Unset):
            system = UNSET
        else:
            system = Dhis2Info.from_dict(_system)

        _user_invitations = d.pop("userInvitations", UNSET)
        user_invitations: Union[Unset, DataSummaryUserInvitations]
        if isinstance(_user_invitations, Unset):
            user_invitations = UNSET
        else:
            user_invitations = DataSummaryUserInvitations.from_dict(_user_invitations)

        data_summary = cls(
            active_users=active_users,
            data_value_count=data_value_count,
            event_count=event_count,
            object_counts=object_counts,
            system=system,
            user_invitations=user_invitations,
        )

        data_summary.additional_properties = d
        return data_summary

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
