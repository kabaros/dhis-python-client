import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.icon_created_by import IconCreatedBy
    from ..models.icon_file_resource import IconFileResource


T = TypeVar("T", bound="Icon")


@_attrs_define
class Icon:
    """
    Attributes:
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, IconCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        custom (Union[Unset, bool]):
        description (Union[Unset, str]):
        file_resource (Union[Unset, IconFileResource]): A UID reference to a FileResource
            (Java name `org.hisp.dhis.fileresource.FileResource`)
        href (Union[Unset, str]):
        key (Union[Unset, str]):
        keywords (Union[Unset, list[str]]):
        last_updated (Union[Unset, datetime.datetime]):
    """

    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "IconCreatedBy"] = UNSET
    custom: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    file_resource: Union[Unset, "IconFileResource"] = UNSET
    href: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        custom = self.custom

        description = self.description

        file_resource: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file_resource, Unset):
            file_resource = self.file_resource.to_dict()

        href = self.href

        key = self.key

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if custom is not UNSET:
            field_dict["custom"] = custom
        if description is not UNSET:
            field_dict["description"] = description
        if file_resource is not UNSET:
            field_dict["fileResource"] = file_resource
        if href is not UNSET:
            field_dict["href"] = href
        if key is not UNSET:
            field_dict["key"] = key
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.icon_created_by import IconCreatedBy
        from ..models.icon_file_resource import IconFileResource

        d = src_dict.copy()
        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, IconCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = IconCreatedBy.from_dict(_created_by)

        custom = d.pop("custom", UNSET)

        description = d.pop("description", UNSET)

        _file_resource = d.pop("fileResource", UNSET)
        file_resource: Union[Unset, IconFileResource]
        if isinstance(_file_resource, Unset):
            file_resource = UNSET
        else:
            file_resource = IconFileResource.from_dict(_file_resource)

        href = d.pop("href", UNSET)

        key = d.pop("key", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        icon = cls(
            created=created,
            created_by=created_by,
            custom=custom,
            description=description,
            file_resource=file_resource,
            href=href,
            key=key,
            keywords=keywords,
            last_updated=last_updated,
        )

        icon.additional_properties = d
        return icon

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
