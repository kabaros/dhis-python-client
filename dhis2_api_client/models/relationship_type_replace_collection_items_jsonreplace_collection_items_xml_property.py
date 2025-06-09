from enum import Enum


class RelationshipTypeReplaceCollectionItemsJsonreplaceCollectionItemsXmlProperty(str, Enum):
    ACCESS = "access"
    ATTRIBUTEVALUES = "attributeValues"
    BIDIRECTIONAL = "bidirectional"
    CODE = "code"
    CREATED = "created"
    CREATEDBY = "createdBy"
    DESCRIPTION = "description"
    DISPLAYFROMTONAME = "displayFromToName"
    DISPLAYNAME = "displayName"
    DISPLAYTOFROMNAME = "displayToFromName"
    FAVORITE = "favorite"
    FAVORITES = "favorites"
    FROMCONSTRAINT = "fromConstraint"
    FROMTONAME = "fromToName"
    HREF = "href"
    ID = "id"
    LASTUPDATED = "lastUpdated"
    LASTUPDATEDBY = "lastUpdatedBy"
    NAME = "name"
    REFERRAL = "referral"
    SHARING = "sharing"
    TOCONSTRAINT = "toConstraint"
    TOFROMNAME = "toFromName"
    TRANSLATIONS = "translations"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
