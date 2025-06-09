import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.org_unit_info_feature_type import OrgUnitInfoFeatureType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgUnitInfo")


@_attrs_define
class OrgUnitInfo:
    """
    Attributes:
        feature_type (OrgUnitInfoFeatureType):
        address (Union[Unset, str]):
        closed_date (Union[Unset, datetime.datetime]):
        code (Union[Unset, str]):
        comment (Union[Unset, str]):
        contact_person (Union[Unset, str]):
        description (Union[Unset, str]):
        email (Union[Unset, str]):
        id (Union[Unset, str]):
        image_id (Union[Unset, str]):
        latitude (Union[Unset, float]):
        level (Union[Unset, int]):
        level_name (Union[Unset, str]):
        longitude (Union[Unset, float]):
        name (Union[Unset, str]):
        opening_date (Union[Unset, datetime.datetime]):
        parent_name (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        short_name (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    feature_type: OrgUnitInfoFeatureType
    address: Union[Unset, str] = UNSET
    closed_date: Union[Unset, datetime.datetime] = UNSET
    code: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    contact_person: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    image_id: Union[Unset, str] = UNSET
    latitude: Union[Unset, float] = UNSET
    level: Union[Unset, int] = UNSET
    level_name: Union[Unset, str] = UNSET
    longitude: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    opening_date: Union[Unset, datetime.datetime] = UNSET
    parent_name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_type = self.feature_type.value

        address = self.address

        closed_date: Union[Unset, str] = UNSET
        if not isinstance(self.closed_date, Unset):
            closed_date = self.closed_date.isoformat()

        code = self.code

        comment = self.comment

        contact_person = self.contact_person

        description = self.description

        email = self.email

        id = self.id

        image_id = self.image_id

        latitude = self.latitude

        level = self.level

        level_name = self.level_name

        longitude = self.longitude

        name = self.name

        opening_date: Union[Unset, str] = UNSET
        if not isinstance(self.opening_date, Unset):
            opening_date = self.opening_date.isoformat()

        parent_name = self.parent_name

        phone_number = self.phone_number

        short_name = self.short_name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "featureType": feature_type,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if closed_date is not UNSET:
            field_dict["closedDate"] = closed_date
        if code is not UNSET:
            field_dict["code"] = code
        if comment is not UNSET:
            field_dict["comment"] = comment
        if contact_person is not UNSET:
            field_dict["contactPerson"] = contact_person
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if level is not UNSET:
            field_dict["level"] = level
        if level_name is not UNSET:
            field_dict["levelName"] = level_name
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if name is not UNSET:
            field_dict["name"] = name
        if opening_date is not UNSET:
            field_dict["openingDate"] = opening_date
        if parent_name is not UNSET:
            field_dict["parentName"] = parent_name
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        feature_type = OrgUnitInfoFeatureType(d.pop("featureType"))

        address = d.pop("address", UNSET)

        _closed_date = d.pop("closedDate", UNSET)
        closed_date: Union[Unset, datetime.datetime]
        if isinstance(_closed_date, Unset):
            closed_date = UNSET
        else:
            closed_date = isoparse(_closed_date)

        code = d.pop("code", UNSET)

        comment = d.pop("comment", UNSET)

        contact_person = d.pop("contactPerson", UNSET)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        image_id = d.pop("imageId", UNSET)

        latitude = d.pop("latitude", UNSET)

        level = d.pop("level", UNSET)

        level_name = d.pop("levelName", UNSET)

        longitude = d.pop("longitude", UNSET)

        name = d.pop("name", UNSET)

        _opening_date = d.pop("openingDate", UNSET)
        opening_date: Union[Unset, datetime.datetime]
        if isinstance(_opening_date, Unset):
            opening_date = UNSET
        else:
            opening_date = isoparse(_opening_date)

        parent_name = d.pop("parentName", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        short_name = d.pop("shortName", UNSET)

        url = d.pop("url", UNSET)

        org_unit_info = cls(
            feature_type=feature_type,
            address=address,
            closed_date=closed_date,
            code=code,
            comment=comment,
            contact_person=contact_person,
            description=description,
            email=email,
            id=id,
            image_id=image_id,
            latitude=latitude,
            level=level,
            level_name=level_name,
            longitude=longitude,
            name=name,
            opening_date=opening_date,
            parent_name=parent_name,
            phone_number=phone_number,
            short_name=short_name,
            url=url,
        )

        org_unit_info.additional_properties = d
        return org_unit_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
