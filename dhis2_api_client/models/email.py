from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_recipients_item import EmailRecipientsItem
    from ..models.email_sender import EmailSender


T = TypeVar("T", bound="Email")


@_attrs_define
class Email:
    """
    Attributes:
        recipients (Union[Unset, list['EmailRecipientsItem']]):
        sender (Union[Unset, EmailSender]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        subject (Union[Unset, str]):
        text (Union[Unset, str]):
    """

    recipients: Union[Unset, list["EmailRecipientsItem"]] = UNSET
    sender: Union[Unset, "EmailSender"] = UNSET
    subject: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipients: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        sender: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        subject = self.subject

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if sender is not UNSET:
            field_dict["sender"] = sender
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.email_recipients_item import EmailRecipientsItem
        from ..models.email_sender import EmailSender

        d = src_dict.copy()
        recipients = []
        _recipients = d.pop("recipients", UNSET)
        for recipients_item_data in _recipients or []:
            recipients_item = EmailRecipientsItem.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        _sender = d.pop("sender", UNSET)
        sender: Union[Unset, EmailSender]
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = EmailSender.from_dict(_sender)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        email = cls(
            recipients=recipients,
            sender=sender,
            subject=subject,
            text=text,
        )

        email.additional_properties = d
        return email

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
