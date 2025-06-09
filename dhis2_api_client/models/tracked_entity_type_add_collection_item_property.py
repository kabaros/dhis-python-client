from enum import Enum


class TrackedEntityTypeAddCollectionItemProperty(str, Enum):
    ACCESS = "access"
    ALLOWAUDITLOG = "allowAuditLog"
    ATTRIBUTEVALUES = "attributeValues"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DISPLAYDESCRIPTION = "displayDescription"
    DISPLAYFORMNAME = "displayFormName"
    DISPLAYNAME = "displayName"
    DISPLAYSHORTNAME = "displayShortName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FEATURETYPE = "featureType"
    FORMNAME = "formName"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    MAXTEICOUNTTORETURN = "maxTeiCountToReturn"
    MINATTRIBUTESREQUIREDTOSEARCH = "minAttributesRequiredToSearch"
    NAME = "name"
    SHARING = "sharing"
    SHORTNAME = "shortName"
    STYLE = "style"
    TRACKEDENTITYTYPEATTRIBUTES = "trackedEntityTypeAttributes"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
