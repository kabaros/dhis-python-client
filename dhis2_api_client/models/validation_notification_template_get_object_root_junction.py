from enum import Enum


class ValidationNotificationTemplateGetObjectRootJunction(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
