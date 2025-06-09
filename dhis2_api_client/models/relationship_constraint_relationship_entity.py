from enum import Enum


class RelationshipConstraintRelationshipEntity(str, Enum):
    PROGRAM_INSTANCE = "PROGRAM_INSTANCE"
    PROGRAM_STAGE_INSTANCE = "PROGRAM_STAGE_INSTANCE"
    TRACKED_ENTITY_INSTANCE = "TRACKED_ENTITY_INSTANCE"

    def __str__(self) -> str:
        return str(self.value)
