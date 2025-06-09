import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.data_approval_workflow_period_type import DataApprovalWorkflowPeriodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.data_approval_workflow_category_combo import DataApprovalWorkflowCategoryCombo
    from ..models.data_approval_workflow_created_by import DataApprovalWorkflowCreatedBy
    from ..models.data_approval_workflow_data_approval_levels_item import DataApprovalWorkflowDataApprovalLevelsItem
    from ..models.data_approval_workflow_data_sets_item import DataApprovalWorkflowDataSetsItem
    from ..models.data_approval_workflow_last_updated_by import DataApprovalWorkflowLastUpdatedBy
    from ..models.data_approval_workflow_user import DataApprovalWorkflowUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="DataApprovalWorkflow")


@_attrs_define
class DataApprovalWorkflow:
    """
    Attributes:
        access (Union[Unset, Access]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_combo (Union[Unset, DataApprovalWorkflowCategoryCombo]): A UID reference to a CategoryCombo
            (Java name `org.hisp.dhis.category.CategoryCombo`)
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, DataApprovalWorkflowCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_approval_levels (Union[Unset, list['DataApprovalWorkflowDataApprovalLevelsItem']]):
        data_sets (Union[Unset, list['DataApprovalWorkflowDataSetsItem']]):
        display_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, DataApprovalWorkflowLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        period_type (Union[Unset, DataApprovalWorkflowPeriodType]):
        sharing (Union[Unset, Sharing]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, DataApprovalWorkflowUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    access: Union[Unset, "Access"] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_combo: Union[Unset, "DataApprovalWorkflowCategoryCombo"] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "DataApprovalWorkflowCreatedBy"] = UNSET
    data_approval_levels: Union[Unset, list["DataApprovalWorkflowDataApprovalLevelsItem"]] = UNSET
    data_sets: Union[Unset, list["DataApprovalWorkflowDataSetsItem"]] = UNSET
    display_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "DataApprovalWorkflowLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    period_type: Union[Unset, DataApprovalWorkflowPeriodType] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "DataApprovalWorkflowUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        category_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_combo, Unset):
            category_combo = self.category_combo.to_dict()

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_approval_levels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_approval_levels, Unset):
            data_approval_levels = []
            for data_approval_levels_item_data in self.data_approval_levels:
                data_approval_levels_item = data_approval_levels_item_data.to_dict()
                data_approval_levels.append(data_approval_levels_item)

        data_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_sets, Unset):
            data_sets = []
            for data_sets_item_data in self.data_sets:
                data_sets_item = data_sets_item_data.to_dict()
                data_sets.append(data_sets_item)

        display_name = self.display_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        period_type: Union[Unset, str] = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value

        sharing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sharing, Unset):
            sharing = self.sharing.to_dict()

        translations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.translations, Unset):
            translations = []
            for translations_item_data in self.translations:
                translations_item = translations_item_data.to_dict()
                translations.append(translations_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_combo is not UNSET:
            field_dict["categoryCombo"] = category_combo
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_approval_levels is not UNSET:
            field_dict["dataApprovalLevels"] = data_approval_levels
        if data_sets is not UNSET:
            field_dict["dataSets"] = data_sets
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if name is not UNSET:
            field_dict["name"] = name
        if period_type is not UNSET:
            field_dict["periodType"] = period_type
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.data_approval_workflow_category_combo import DataApprovalWorkflowCategoryCombo
        from ..models.data_approval_workflow_created_by import DataApprovalWorkflowCreatedBy
        from ..models.data_approval_workflow_data_approval_levels_item import DataApprovalWorkflowDataApprovalLevelsItem
        from ..models.data_approval_workflow_data_sets_item import DataApprovalWorkflowDataSetsItem
        from ..models.data_approval_workflow_last_updated_by import DataApprovalWorkflowLastUpdatedBy
        from ..models.data_approval_workflow_user import DataApprovalWorkflowUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        _category_combo = d.pop("categoryCombo", UNSET)
        category_combo: Union[Unset, DataApprovalWorkflowCategoryCombo]
        if isinstance(_category_combo, Unset):
            category_combo = UNSET
        else:
            category_combo = DataApprovalWorkflowCategoryCombo.from_dict(_category_combo)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, DataApprovalWorkflowCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = DataApprovalWorkflowCreatedBy.from_dict(_created_by)

        data_approval_levels = []
        _data_approval_levels = d.pop("dataApprovalLevels", UNSET)
        for data_approval_levels_item_data in _data_approval_levels or []:
            data_approval_levels_item = DataApprovalWorkflowDataApprovalLevelsItem.from_dict(
                data_approval_levels_item_data
            )

            data_approval_levels.append(data_approval_levels_item)

        data_sets = []
        _data_sets = d.pop("dataSets", UNSET)
        for data_sets_item_data in _data_sets or []:
            data_sets_item = DataApprovalWorkflowDataSetsItem.from_dict(data_sets_item_data)

            data_sets.append(data_sets_item)

        display_name = d.pop("displayName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, DataApprovalWorkflowLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = DataApprovalWorkflowLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        _period_type = d.pop("periodType", UNSET)
        period_type: Union[Unset, DataApprovalWorkflowPeriodType]
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = DataApprovalWorkflowPeriodType(_period_type)

        _sharing = d.pop("sharing", UNSET)
        sharing: Union[Unset, Sharing]
        if isinstance(_sharing, Unset):
            sharing = UNSET
        else:
            sharing = Sharing.from_dict(_sharing)

        translations = []
        _translations = d.pop("translations", UNSET)
        for translations_item_data in _translations or []:
            translations_item = Translation.from_dict(translations_item_data)

            translations.append(translations_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, DataApprovalWorkflowUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = DataApprovalWorkflowUser.from_dict(_user)

        data_approval_workflow = cls(
            access=access,
            attribute_values=attribute_values,
            category_combo=category_combo,
            code=code,
            created=created,
            created_by=created_by,
            data_approval_levels=data_approval_levels,
            data_sets=data_sets,
            display_name=display_name,
            favorite=favorite,
            favorites=favorites,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            period_type=period_type,
            sharing=sharing,
            translations=translations,
            user=user,
        )

        data_approval_workflow.additional_properties = d
        return data_approval_workflow

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
