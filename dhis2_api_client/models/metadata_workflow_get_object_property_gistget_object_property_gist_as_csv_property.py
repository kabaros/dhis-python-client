from enum import Enum


class MetadataWorkflowGetObjectPropertyGistgetObjectPropertyGistAsCsvProperty(str, Enum):
    CHANGE = "change"
    COMMENT = "comment"
    CREATED = "created"
    CREATEDBY = "createdBy"
    FINALISED = "finalised"
    FINALISEDBY = "finalisedBy"
    ID = "id"
    REASON = "reason"
    STATUS = "status"
    TARGET = "target"
    TARGETID = "targetId"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
