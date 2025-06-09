from enum import Enum


class ExternalMapLayerImageFormat(str, Enum):
    JPG = "JPG"
    PNG = "PNG"

    def __str__(self) -> str:
        return str(self.value)
