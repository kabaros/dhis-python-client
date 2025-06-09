from enum import Enum


class MetadataWorkflowGetProposalRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
