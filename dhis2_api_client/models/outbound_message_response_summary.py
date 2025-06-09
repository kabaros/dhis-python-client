from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outbound_message_response_summary_batch_type import OutboundMessageResponseSummaryBatchType
from ..models.outbound_message_response_summary_status import OutboundMessageResponseSummaryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutboundMessageResponseSummary")


@_attrs_define
class OutboundMessageResponseSummary:
    """
    Attributes:
        batch_type (OutboundMessageResponseSummaryBatchType):
        failed (int):
        pending (int):
        sent (int):
        status (OutboundMessageResponseSummaryStatus):
        total (int):
        error_message (Union[Unset, str]):
        response_message (Union[Unset, str]):
    """

    batch_type: OutboundMessageResponseSummaryBatchType
    failed: int
    pending: int
    sent: int
    status: OutboundMessageResponseSummaryStatus
    total: int
    error_message: Union[Unset, str] = UNSET
    response_message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_type = self.batch_type.value

        failed = self.failed

        pending = self.pending

        sent = self.sent

        status = self.status.value

        total = self.total

        error_message = self.error_message

        response_message = self.response_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batchType": batch_type,
                "failed": failed,
                "pending": pending,
                "sent": sent,
                "status": status,
                "total": total,
            }
        )
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if response_message is not UNSET:
            field_dict["responseMessage"] = response_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        batch_type = OutboundMessageResponseSummaryBatchType(d.pop("batchType"))

        failed = d.pop("failed")

        pending = d.pop("pending")

        sent = d.pop("sent")

        status = OutboundMessageResponseSummaryStatus(d.pop("status"))

        total = d.pop("total")

        error_message = d.pop("errorMessage", UNSET)

        response_message = d.pop("responseMessage", UNSET)

        outbound_message_response_summary = cls(
            batch_type=batch_type,
            failed=failed,
            pending=pending,
            sent=sent,
            status=status,
            total=total,
            error_message=error_message,
            response_message=response_message,
        )

        outbound_message_response_summary.additional_properties = d
        return outbound_message_response_summary

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
