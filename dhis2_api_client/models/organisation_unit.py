import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.organisation_unit_aggregation_type import OrganisationUnitAggregationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.organisation_unit_ancestors_item import OrganisationUnitAncestorsItem
    from ..models.organisation_unit_children_item import OrganisationUnitChildrenItem
    from ..models.organisation_unit_created_by import OrganisationUnitCreatedBy
    from ..models.organisation_unit_data_sets_item import OrganisationUnitDataSetsItem
    from ..models.organisation_unit_geometry import OrganisationUnitGeometry
    from ..models.organisation_unit_image import OrganisationUnitImage
    from ..models.organisation_unit_last_updated_by import OrganisationUnitLastUpdatedBy
    from ..models.organisation_unit_legend_set import OrganisationUnitLegendSet
    from ..models.organisation_unit_legend_sets_item import OrganisationUnitLegendSetsItem
    from ..models.organisation_unit_organisation_unit_groups_item import OrganisationUnitOrganisationUnitGroupsItem
    from ..models.organisation_unit_parent import OrganisationUnitParent
    from ..models.organisation_unit_programs_item import OrganisationUnitProgramsItem
    from ..models.organisation_unit_user import OrganisationUnitUser
    from ..models.organisation_unit_users_item import OrganisationUnitUsersItem
    from ..models.query_modifiers import QueryModifiers
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="OrganisationUnit")


@_attrs_define
class OrganisationUnit:
    """
    Attributes:
        aggregation_type (OrganisationUnitAggregationType):
        level (int):
        access (Union[Unset, Access]):
        address (Union[Unset, str]):
        ancestors (Union[Unset, list['OrganisationUnitAncestorsItem']]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        children (Union[Unset, list['OrganisationUnitChildrenItem']]):
        closed_date (Union[Unset, datetime.datetime]):
        code (Union[Unset, str]):
        comment (Union[Unset, str]):
        contact_person (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, OrganisationUnitCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_sets (Union[Unset, list['OrganisationUnitDataSetsItem']]):
        description (Union[Unset, str]):
        dimension_item (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        email (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        geometry (Union[Unset, OrganisationUnitGeometry]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        image (Union[Unset, OrganisationUnitImage]): A UID reference to a FileResource
            (Java name `org.hisp.dhis.fileresource.FileResource`)
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, OrganisationUnitLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        leaf (Union[Unset, bool]):
        legend_set (Union[Unset, OrganisationUnitLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        legend_sets (Union[Unset, list['OrganisationUnitLegendSetsItem']]):
        member_count (Union[Unset, int]):
        name (Union[Unset, str]):
        opening_date (Union[Unset, datetime.datetime]):
        organisation_unit_groups (Union[Unset, list['OrganisationUnitOrganisationUnitGroupsItem']]):
        parent (Union[Unset, OrganisationUnitParent]): A UID reference to a OrganisationUnit
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`)
        path (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        programs (Union[Unset, list['OrganisationUnitProgramsItem']]):
        query_mods (Union[Unset, QueryModifiers]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        type_ (Union[Unset, str]):
        url (Union[Unset, str]):
        user (Union[Unset, OrganisationUnitUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        users (Union[Unset, list['OrganisationUnitUsersItem']]):
    """

    aggregation_type: OrganisationUnitAggregationType
    level: int
    access: Union[Unset, "Access"] = UNSET
    address: Union[Unset, str] = UNSET
    ancestors: Union[Unset, list["OrganisationUnitAncestorsItem"]] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    children: Union[Unset, list["OrganisationUnitChildrenItem"]] = UNSET
    closed_date: Union[Unset, datetime.datetime] = UNSET
    code: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    contact_person: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "OrganisationUnitCreatedBy"] = UNSET
    data_sets: Union[Unset, list["OrganisationUnitDataSetsItem"]] = UNSET
    description: Union[Unset, str] = UNSET
    dimension_item: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    geometry: Union[Unset, "OrganisationUnitGeometry"] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    image: Union[Unset, "OrganisationUnitImage"] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "OrganisationUnitLastUpdatedBy"] = UNSET
    leaf: Union[Unset, bool] = UNSET
    legend_set: Union[Unset, "OrganisationUnitLegendSet"] = UNSET
    legend_sets: Union[Unset, list["OrganisationUnitLegendSetsItem"]] = UNSET
    member_count: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    opening_date: Union[Unset, datetime.datetime] = UNSET
    organisation_unit_groups: Union[Unset, list["OrganisationUnitOrganisationUnitGroupsItem"]] = UNSET
    parent: Union[Unset, "OrganisationUnitParent"] = UNSET
    path: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    programs: Union[Unset, list["OrganisationUnitProgramsItem"]] = UNSET
    query_mods: Union[Unset, "QueryModifiers"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    type_: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user: Union[Unset, "OrganisationUnitUser"] = UNSET
    users: Union[Unset, list["OrganisationUnitUsersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        level = self.level

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        address = self.address

        ancestors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = []
            for ancestors_item_data in self.ancestors:
                ancestors_item = ancestors_item_data.to_dict()
                ancestors.append(ancestors_item)

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        closed_date: Union[Unset, str] = UNSET
        if not isinstance(self.closed_date, Unset):
            closed_date = self.closed_date.isoformat()

        code = self.code

        comment = self.comment

        contact_person = self.contact_person

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_sets, Unset):
            data_sets = []
            for data_sets_item_data in self.data_sets:
                data_sets_item = data_sets_item_data.to_dict()
                data_sets.append(data_sets_item)

        description = self.description

        dimension_item = self.dimension_item

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        email = self.email

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        geometry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        href = self.href

        id = self.id

        image: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        leaf = self.leaf

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        legend_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.legend_sets, Unset):
            legend_sets = []
            for legend_sets_item_data in self.legend_sets:
                legend_sets_item = legend_sets_item_data.to_dict()
                legend_sets.append(legend_sets_item)

        member_count = self.member_count

        name = self.name

        opening_date: Union[Unset, str] = UNSET
        if not isinstance(self.opening_date, Unset):
            opening_date = self.opening_date.isoformat()

        organisation_unit_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_unit_groups, Unset):
            organisation_unit_groups = []
            for organisation_unit_groups_item_data in self.organisation_unit_groups:
                organisation_unit_groups_item = organisation_unit_groups_item_data.to_dict()
                organisation_unit_groups.append(organisation_unit_groups_item)

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        path = self.path

        phone_number = self.phone_number

        programs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.programs, Unset):
            programs = []
            for programs_item_data in self.programs:
                programs_item = programs_item_data.to_dict()
                programs.append(programs_item)

        query_mods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query_mods, Unset):
            query_mods = self.query_mods.to_dict()

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        short_name = self.short_name

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        type_ = self.type_

        url = self.url

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "level": level,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if address is not UNSET:
            field_dict["address"] = address
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if children is not UNSET:
            field_dict["children"] = children
        if closed_date is not UNSET:
            field_dict["closedDate"] = closed_date
        if code is not UNSET:
            field_dict["code"] = code
        if comment is not UNSET:
            field_dict["comment"] = comment
        if contact_person is not UNSET:
            field_dict["contactPerson"] = contact_person
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if description is not UNSET:
            field_dict["description"] = description
        if dimension_item is not UNSET:
            field_dict["dimensionItem"] = dimension_item
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if email is not UNSET:
            field_dict["email"] = email
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if leaf is not UNSET:
            field_dict["leaf"] = leaf
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if legend_sets is not UNSET:
            field_dict["legendSets"] = legend_sets
        if member_count is not UNSET:
            field_dict["memberCount"] = member_count
        if name is not UNSET:
            field_dict["name"] = name
        if opening_date is not UNSET:
            field_dict["openingDate"] = opening_date
        if organisation_unit_groups is not UNSET:
            field_dict["organisationUnitGroups"] = organisation_unit_groups
        if parent is not UNSET:
            field_dict["parent"] = parent
        if path is not UNSET:
            field_dict["path"] = path
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if programs is not UNSET:
            field_dict["programs"] = programs
        if query_mods is not UNSET:
            field_dict["queryMods"] = query_mods
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if translations is not UNSET:
            field_dict["translations"] = translations
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url
        if user is not UNSET:
            field_dict["user"] = user
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.organisation_unit_ancestors_item import OrganisationUnitAncestorsItem
        from ..models.organisation_unit_children_item import OrganisationUnitChildrenItem
        from ..models.organisation_unit_created_by import OrganisationUnitCreatedBy
        from ..models.organisation_unit_data_sets_item import OrganisationUnitDataSetsItem
        from ..models.organisation_unit_geometry import OrganisationUnitGeometry
        from ..models.organisation_unit_image import OrganisationUnitImage
        from ..models.organisation_unit_last_updated_by import OrganisationUnitLastUpdatedBy
        from ..models.organisation_unit_legend_set import OrganisationUnitLegendSet
        from ..models.organisation_unit_legend_sets_item import OrganisationUnitLegendSetsItem
        from ..models.organisation_unit_organisation_unit_groups_item import OrganisationUnitOrganisationUnitGroupsItem
        from ..models.organisation_unit_parent import OrganisationUnitParent
        from ..models.organisation_unit_programs_item import OrganisationUnitProgramsItem
        from ..models.organisation_unit_user import OrganisationUnitUser
        from ..models.organisation_unit_users_item import OrganisationUnitUsersItem
        from ..models.query_modifiers import QueryModifiers
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = OrganisationUnitAggregationType(d.pop("aggregationType"))

        level = d.pop("level")

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        address = d.pop("address", UNSET)

        ancestors = []
        _ancestors = d.pop("ancestors", UNSET)
        for ancestors_item_data in _ancestors or []:
            ancestors_item = OrganisationUnitAncestorsItem.from_dict(ancestors_item_data)

            ancestors.append(ancestors_item)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = OrganisationUnitChildrenItem.from_dict(children_item_data)

            children.append(children_item)

        _closed_date = d.pop("closedDate", UNSET)
        closed_date: Union[Unset, datetime.datetime]
        if isinstance(_closed_date, Unset):
            closed_date = UNSET
        else:
            closed_date = isoparse(_closed_date)

        code = d.pop("code", UNSET)

        comment = d.pop("comment", UNSET)

        contact_person = d.pop("contactPerson", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, OrganisationUnitCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = OrganisationUnitCreatedBy.from_dict(_created_by)

        data_sets = []
        _data_sets = d.pop("dataSets", UNSET)
        for data_sets_item_data in _data_sets or []:
            data_sets_item = OrganisationUnitDataSetsItem.from_dict(data_sets_item_data)

            data_sets.append(data_sets_item)

        description = d.pop("description", UNSET)

        dimension_item = d.pop("dimensionItem", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        email = d.pop("email", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: Union[Unset, OrganisationUnitGeometry]
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = OrganisationUnitGeometry.from_dict(_geometry)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _image = d.pop("image", UNSET)
        image: Union[Unset, OrganisationUnitImage]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = OrganisationUnitImage.from_dict(_image)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, OrganisationUnitLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = OrganisationUnitLastUpdatedBy.from_dict(_last_updated_by)

        leaf = d.pop("leaf", UNSET)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, OrganisationUnitLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = OrganisationUnitLegendSet.from_dict(_legend_set)

        legend_sets = []
        _legend_sets = d.pop("legendSets", UNSET)
        for legend_sets_item_data in _legend_sets or []:
            legend_sets_item = OrganisationUnitLegendSetsItem.from_dict(legend_sets_item_data)

            legend_sets.append(legend_sets_item)

        member_count = d.pop("memberCount", UNSET)

        name = d.pop("name", UNSET)

        _opening_date = d.pop("openingDate", UNSET)
        opening_date: Union[Unset, datetime.datetime]
        if isinstance(_opening_date, Unset):
            opening_date = UNSET
        else:
            opening_date = isoparse(_opening_date)

        organisation_unit_groups = []
        _organisation_unit_groups = d.pop("organisationUnitGroups", UNSET)
        for organisation_unit_groups_item_data in _organisation_unit_groups or []:
            organisation_unit_groups_item = OrganisationUnitOrganisationUnitGroupsItem.from_dict(
                organisation_unit_groups_item_data
            )

            organisation_unit_groups.append(organisation_unit_groups_item)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, OrganisationUnitParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = OrganisationUnitParent.from_dict(_parent)

        path = d.pop("path", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        programs = []
        _programs = d.pop("programs", UNSET)
        for programs_item_data in _programs or []:
            programs_item = OrganisationUnitProgramsItem.from_dict(programs_item_data)

            programs.append(programs_item)

        _query_mods = d.pop("queryMods", UNSET)
        query_mods: Union[Unset, QueryModifiers]
        if isinstance(_query_mods, Unset):
            query_mods = UNSET
        else:
            query_mods = QueryModifiers.from_dict(_query_mods)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        short_name = d.pop("shortName", UNSET)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, OrganisationUnitUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = OrganisationUnitUser.from_dict(_user)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = OrganisationUnitUsersItem.from_dict(users_item_data)

            users.append(users_item)

        organisation_unit = cls(
            aggregation_type=aggregation_type,
            level=level,
            access=access,
            address=address,
            ancestors=ancestors,
            attribute_values=attribute_values,
            children=children,
            closed_date=closed_date,
            code=code,
            comment=comment,
            contact_person=contact_person,
            created=created,
            created_by=created_by,
            data_sets=data_sets,
            description=description,
            dimension_item=dimension_item,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            email=email,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            geometry=geometry,
            href=href,
            id=id,
            image=image,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            leaf=leaf,
            legend_set=legend_set,
            legend_sets=legend_sets,
            member_count=member_count,
            name=name,
            opening_date=opening_date,
            organisation_unit_groups=organisation_unit_groups,
            parent=parent,
            path=path,
            phone_number=phone_number,
            programs=programs,
            query_mods=query_mods,
            sharing=sharing,
            short_name=short_name,
            translations=translations,
            type_=type_,
            url=url,
            user=user,
            users=users,
        )

        organisation_unit.additional_properties = d
        return organisation_unit

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
