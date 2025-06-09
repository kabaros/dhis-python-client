import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataApprovalPermissions")


@_attrs_define
class DataApprovalPermissions:
    """
    Attributes:
        accepted_at (Union[Unset, datetime.datetime]):
        accepted_by (Union[Unset, str]):
        approved_at (Union[Unset, datetime.datetime]):
        approved_by (Union[Unset, str]):
        may_accept (Union[Unset, bool]):
        may_approve (Union[Unset, bool]):
        may_read_data (Union[Unset, bool]):
        may_unaccept (Union[Unset, bool]):
        may_unapprove (Union[Unset, bool]):
        state (Union[Unset, str]):
    """

    accepted_at: Union[Unset, datetime.datetime] = UNSET
    accepted_by: Union[Unset, str] = UNSET
    approved_at: Union[Unset, datetime.datetime] = UNSET
    approved_by: Union[Unset, str] = UNSET
    may_accept: Union[Unset, bool] = UNSET
    may_approve: Union[Unset, bool] = UNSET
    may_read_data: Union[Unset, bool] = UNSET
    may_unaccept: Union[Unset, bool] = UNSET
    may_unapprove: Union[Unset, bool] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_at: Union[Unset, str] = UNSET
        if not isinstance(self.accepted_at, Unset):
            accepted_at = self.accepted_at.isoformat()

        accepted_by = self.accepted_by

        approved_at: Union[Unset, str] = UNSET
        if not isinstance(self.approved_at, Unset):
            approved_at = self.approved_at.isoformat()

        approved_by = self.approved_by

        may_accept = self.may_accept

        may_approve = self.may_approve

        may_read_data = self.may_read_data

        may_unaccept = self.may_unaccept

        may_unapprove = self.may_unapprove

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_at is not UNSET:
            field_dict["acceptedAt"] = accepted_at
        if accepted_by is not UNSET:
            field_dict["acceptedBy"] = accepted_by
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if may_accept is not UNSET:
            field_dict["mayAccept"] = may_accept
        if may_approve is not UNSET:
            field_dict["mayApprove"] = may_approve
        if may_read_data is not UNSET:
            field_dict["mayReadData"] = may_read_data
        if may_unaccept is not UNSET:
            field_dict["mayUnaccept"] = may_unaccept
        if may_unapprove is not UNSET:
            field_dict["mayUnapprove"] = may_unapprove
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _accepted_at = d.pop("acceptedAt", UNSET)
        accepted_at: Union[Unset, datetime.datetime]
        if isinstance(_accepted_at, Unset):
            accepted_at = UNSET
        else:
            accepted_at = isoparse(_accepted_at)

        accepted_by = d.pop("acceptedBy", UNSET)

        _approved_at = d.pop("approvedAt", UNSET)
        approved_at: Union[Unset, datetime.datetime]
        if isinstance(_approved_at, Unset):
            approved_at = UNSET
        else:
            approved_at = isoparse(_approved_at)

        approved_by = d.pop("approvedBy", UNSET)

        may_accept = d.pop("mayAccept", UNSET)

        may_approve = d.pop("mayApprove", UNSET)

        may_read_data = d.pop("mayReadData", UNSET)

        may_unaccept = d.pop("mayUnaccept", UNSET)

        may_unapprove = d.pop("mayUnapprove", UNSET)

        state = d.pop("state", UNSET)

        data_approval_permissions = cls(
            accepted_at=accepted_at,
            accepted_by=accepted_by,
            approved_at=approved_at,
            approved_by=approved_by,
            may_accept=may_accept,
            may_approve=may_approve,
            may_read_data=may_read_data,
            may_unaccept=may_unaccept,
            may_unapprove=may_unapprove,
            state=state,
        )

        data_approval_permissions.additional_properties = d
        return data_approval_permissions

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
