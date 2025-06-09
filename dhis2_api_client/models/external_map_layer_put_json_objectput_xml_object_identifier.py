from enum import Enum


class ExternalMapLayerPutJsonObjectputXmlObjectIdentifier(str, Enum):
    CODE = "CODE"
    UID = "UID"

    def __str__(self) -> str:
        return str(self.value)
