from enum import Enum


class ApprovalStatusDtoState(str, Enum):
    ACCEPTED_HERE = "ACCEPTED_HERE"
    APPROVED_ABOVE = "APPROVED_ABOVE"
    APPROVED_HERE = "APPROVED_HERE"
    UNAPPROVABLE = "UNAPPROVABLE"
    UNAPPROVED_ABOVE = "UNAPPROVED_ABOVE"
    UNAPPROVED_READY = "UNAPPROVED_READY"
    UNAPPROVED_WAITING = "UNAPPROVED_WAITING"

    def __str__(self) -> str:
        return str(self.value)
