from enum import Enum


class PropertyPropertyType(str, Enum):
    BOOLEAN = "BOOLEAN"
    COLLECTION = "COLLECTION"
    COLOR = "COLOR"
    COMPLEX = "COMPLEX"
    CONSTANT = "CONSTANT"
    DATE = "DATE"
    DEFAULT = "DEFAULT"
    EMAIL = "EMAIL"
    GEOLOCATION = "GEOLOCATION"
    IDENTIFIER = "IDENTIFIER"
    INTEGER = "INTEGER"
    NUMBER = "NUMBER"
    PASSWORD = "PASSWORD"
    PHONENUMBER = "PHONENUMBER"
    REFERENCE = "REFERENCE"
    TEXT = "TEXT"
    URL = "URL"
    USERNAME = "USERNAME"

    def __str__(self) -> str:
        return str(self.value)
