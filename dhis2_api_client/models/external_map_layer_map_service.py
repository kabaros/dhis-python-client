from enum import Enum


class ExternalMapLayerMapService(str, Enum):
    ARCGIS_FEATURE = "ARCGIS_FEATURE"
    GEOJSON_URL = "GEOJSON_URL"
    TMS = "TMS"
    VECTOR_STYLE = "VECTOR_STYLE"
    WMS = "WMS"
    XYZ = "XYZ"

    def __str__(self) -> str:
        return str(self.value)
