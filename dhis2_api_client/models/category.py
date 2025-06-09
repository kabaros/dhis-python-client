import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.category_aggregation_type import CategoryAggregationType
from ..models.category_data_dimension_type import CategoryDataDimensionType
from ..models.category_value_type import CategoryValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.category_category_combos_item import CategoryCategoryCombosItem
    from ..models.category_category_options_item import CategoryCategoryOptionsItem
    from ..models.category_created_by import CategoryCreatedBy
    from ..models.category_items_item import CategoryItemsItem
    from ..models.category_last_updated_by import CategoryLastUpdatedBy
    from ..models.category_legend_set import CategoryLegendSet
    from ..models.category_option_set import CategoryOptionSet
    from ..models.category_program import CategoryProgram
    from ..models.category_program_stage import CategoryProgramStage
    from ..models.category_user import CategoryUser
    from ..models.dimension_item_keywords import DimensionItemKeywords
    from ..models.event_repetition import EventRepetition
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Category")


@_attrs_define
class Category:
    """
    Attributes:
        aggregation_type (CategoryAggregationType):
        data_dimension_type (CategoryDataDimensionType):
        value_type (CategoryValueType):
        access (Union[Unset, Access]):
        all_items (Union[Unset, bool]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        category_combos (Union[Unset, list['CategoryCategoryCombosItem']]):
        category_options (Union[Unset, list['CategoryCategoryOptionsItem']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, CategoryCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        data_dimension (Union[Unset, bool]):
        description (Union[Unset, str]):
        dimension (Union[Unset, str]):
        dimension_item_keywords (Union[Unset, DimensionItemKeywords]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        filter_ (Union[Unset, str]):
        form_name (Union[Unset, str]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        items (Union[Unset, list['CategoryItemsItem']]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, CategoryLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        legend_set (Union[Unset, CategoryLegendSet]): A UID reference to a LegendSet
            (Java name `org.hisp.dhis.legend.LegendSet`)
        name (Union[Unset, str]):
        option_set (Union[Unset, CategoryOptionSet]): A UID reference to a OptionSet
            (Java name `org.hisp.dhis.option.OptionSet`)
        program (Union[Unset, CategoryProgram]): A UID reference to a Program
            (Java name `org.hisp.dhis.program.Program`)
        program_stage (Union[Unset, CategoryProgramStage]): A UID reference to a ProgramStage
            (Java name `org.hisp.dhis.program.ProgramStage`)
        repetition (Union[Unset, EventRepetition]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, CategoryUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    aggregation_type: CategoryAggregationType
    data_dimension_type: CategoryDataDimensionType
    value_type: CategoryValueType
    access: Union[Unset, "Access"] = UNSET
    all_items: Union[Unset, bool] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    category_combos: Union[Unset, list["CategoryCategoryCombosItem"]] = UNSET
    category_options: Union[Unset, list["CategoryCategoryOptionsItem"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "CategoryCreatedBy"] = UNSET
    data_dimension: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    dimension: Union[Unset, str] = UNSET
    dimension_item_keywords: Union[Unset, "DimensionItemKeywords"] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    filter_: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    items: Union[Unset, list["CategoryItemsItem"]] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "CategoryLastUpdatedBy"] = UNSET
    legend_set: Union[Unset, "CategoryLegendSet"] = UNSET
    name: Union[Unset, str] = UNSET
    option_set: Union[Unset, "CategoryOptionSet"] = UNSET
    program: Union[Unset, "CategoryProgram"] = UNSET
    program_stage: Union[Unset, "CategoryProgramStage"] = UNSET
    repetition: Union[Unset, "EventRepetition"] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "CategoryUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_type = self.aggregation_type.value

        data_dimension_type = self.data_dimension_type.value

        value_type = self.value_type.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        all_items = self.all_items

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        category_combos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_combos, Unset):
            category_combos = []
            for category_combos_item_data in self.category_combos:
                category_combos_item = category_combos_item_data.to_dict()
                category_combos.append(category_combos_item)

        category_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category_options, Unset):
            category_options = []
            for category_options_item_data in self.category_options:
                category_options_item = category_options_item_data.to_dict()
                category_options.append(category_options_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data_dimension = self.data_dimension

        description = self.description

        dimension = self.dimension

        dimension_item_keywords: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dimension_item_keywords, Unset):
            dimension_item_keywords = self.dimension_item_keywords.to_dict()

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        filter_ = self.filter_

        form_name = self.form_name

        href = self.href

        id = self.id

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        legend_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legend_set, Unset):
            legend_set = self.legend_set.to_dict()

        name = self.name

        option_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.option_set, Unset):
            option_set = self.option_set.to_dict()

        program: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        program_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.program_stage, Unset):
            program_stage = self.program_stage.to_dict()

        repetition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.repetition, Unset):
            repetition = self.repetition.to_dict()

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

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregationType": aggregation_type,
                "dataDimensionType": data_dimension_type,
                "valueType": value_type,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if all_items is not UNSET:
            field_dict["allItems"] = all_items
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if category_combos is not UNSET:
            field_dict["categoryCombos"] = category_combos
        if category_options is not UNSET:
            field_dict["categoryOptions"] = category_options
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data_dimension is not UNSET:
            field_dict["dataDimension"] = data_dimension
        if description is not UNSET:
            field_dict["description"] = description
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if dimension_item_keywords is not UNSET:
            field_dict["dimensionItemKeywords"] = dimension_item_keywords
        if display_description is not UNSET:
            field_dict["displayDescription"] = display_description
        if display_form_name is not UNSET:
            field_dict["displayFormName"] = display_form_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_short_name is not UNSET:
            field_dict["displayShortName"] = display_short_name
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if items is not UNSET:
            field_dict["items"] = items
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_updated_by is not UNSET:
            field_dict["lastUpdatedBy"] = last_updated_by
        if legend_set is not UNSET:
            field_dict["legendSet"] = legend_set
        if name is not UNSET:
            field_dict["name"] = name
        if option_set is not UNSET:
            field_dict["optionSet"] = option_set
        if program is not UNSET:
            field_dict["program"] = program
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if repetition is not UNSET:
            field_dict["repetition"] = repetition
        if sharing is not UNSET:
            field_dict["sharing"] = sharing
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if translations is not UNSET:
            field_dict["translations"] = translations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.access import Access
        from ..models.attribute_value import AttributeValue
        from ..models.category_category_combos_item import CategoryCategoryCombosItem
        from ..models.category_category_options_item import CategoryCategoryOptionsItem
        from ..models.category_created_by import CategoryCreatedBy
        from ..models.category_items_item import CategoryItemsItem
        from ..models.category_last_updated_by import CategoryLastUpdatedBy
        from ..models.category_legend_set import CategoryLegendSet
        from ..models.category_option_set import CategoryOptionSet
        from ..models.category_program import CategoryProgram
        from ..models.category_program_stage import CategoryProgramStage
        from ..models.category_user import CategoryUser
        from ..models.dimension_item_keywords import DimensionItemKeywords
        from ..models.event_repetition import EventRepetition
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        aggregation_type = CategoryAggregationType(d.pop("aggregationType"))

        data_dimension_type = CategoryDataDimensionType(d.pop("dataDimensionType"))

        value_type = CategoryValueType(d.pop("valueType"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        all_items = d.pop("allItems", UNSET)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        category_combos = []
        _category_combos = d.pop("categoryCombos", UNSET)
        for category_combos_item_data in _category_combos or []:
            category_combos_item = CategoryCategoryCombosItem.from_dict(category_combos_item_data)

            category_combos.append(category_combos_item)

        category_options = []
        _category_options = d.pop("categoryOptions", UNSET)
        for category_options_item_data in _category_options or []:
            category_options_item = CategoryCategoryOptionsItem.from_dict(category_options_item_data)

            category_options.append(category_options_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, CategoryCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = CategoryCreatedBy.from_dict(_created_by)

        data_dimension = d.pop("dataDimension", UNSET)

        description = d.pop("description", UNSET)

        dimension = d.pop("dimension", UNSET)

        _dimension_item_keywords = d.pop("dimensionItemKeywords", UNSET)
        dimension_item_keywords: Union[Unset, DimensionItemKeywords]
        if isinstance(_dimension_item_keywords, Unset):
            dimension_item_keywords = UNSET
        else:
            dimension_item_keywords = DimensionItemKeywords.from_dict(_dimension_item_keywords)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        filter_ = d.pop("filter", UNSET)

        form_name = d.pop("formName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = CategoryItemsItem.from_dict(items_item_data)

            items.append(items_item)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, CategoryLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = CategoryLastUpdatedBy.from_dict(_last_updated_by)

        _legend_set = d.pop("legendSet", UNSET)
        legend_set: Union[Unset, CategoryLegendSet]
        if isinstance(_legend_set, Unset):
            legend_set = UNSET
        else:
            legend_set = CategoryLegendSet.from_dict(_legend_set)

        name = d.pop("name", UNSET)

        _option_set = d.pop("optionSet", UNSET)
        option_set: Union[Unset, CategoryOptionSet]
        if isinstance(_option_set, Unset):
            option_set = UNSET
        else:
            option_set = CategoryOptionSet.from_dict(_option_set)

        _program = d.pop("program", UNSET)
        program: Union[Unset, CategoryProgram]
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = CategoryProgram.from_dict(_program)

        _program_stage = d.pop("programStage", UNSET)
        program_stage: Union[Unset, CategoryProgramStage]
        if isinstance(_program_stage, Unset):
            program_stage = UNSET
        else:
            program_stage = CategoryProgramStage.from_dict(_program_stage)

        _repetition = d.pop("repetition", UNSET)
        repetition: Union[Unset, EventRepetition]
        if isinstance(_repetition, Unset):
            repetition = UNSET
        else:
            repetition = EventRepetition.from_dict(_repetition)

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

        _user = d.pop("user", UNSET)
        user: Union[Unset, CategoryUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CategoryUser.from_dict(_user)

        category = cls(
            aggregation_type=aggregation_type,
            data_dimension_type=data_dimension_type,
            value_type=value_type,
            access=access,
            all_items=all_items,
            attribute_values=attribute_values,
            category_combos=category_combos,
            category_options=category_options,
            code=code,
            created=created,
            created_by=created_by,
            data_dimension=data_dimension,
            description=description,
            dimension=dimension,
            dimension_item_keywords=dimension_item_keywords,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            filter_=filter_,
            form_name=form_name,
            href=href,
            id=id,
            items=items,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            legend_set=legend_set,
            name=name,
            option_set=option_set,
            program=program,
            program_stage=program_stage,
            repetition=repetition,
            sharing=sharing,
            short_name=short_name,
            translations=translations,
            user=user,
        )

        category.additional_properties = d
        return category

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
