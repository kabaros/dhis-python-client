import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.predictor_organisation_unit_descendants import PredictorOrganisationUnitDescendants
from ..models.predictor_period_type import PredictorPeriodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.attribute_value import AttributeValue
    from ..models.expression import Expression
    from ..models.predictor_created_by import PredictorCreatedBy
    from ..models.predictor_last_updated_by import PredictorLastUpdatedBy
    from ..models.predictor_organisation_unit_levels_item import PredictorOrganisationUnitLevelsItem
    from ..models.predictor_output import PredictorOutput
    from ..models.predictor_output_combo import PredictorOutputCombo
    from ..models.predictor_predictor_groups_item import PredictorPredictorGroupsItem
    from ..models.predictor_user import PredictorUser
    from ..models.sharing import Sharing
    from ..models.translation import Translation


T = TypeVar("T", bound="Predictor")


@_attrs_define
class Predictor:
    """
    Attributes:
        organisation_unit_descendants (PredictorOrganisationUnitDescendants):
        access (Union[Unset, Access]):
        annual_sample_count (Union[Unset, int]):
        attribute_values (Union[Unset, list['AttributeValue']]):
        code (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, PredictorCreatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        description (Union[Unset, str]):
        display_description (Union[Unset, str]):
        display_form_name (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_short_name (Union[Unset, str]):
        favorite (Union[Unset, bool]):
        favorites (Union[Unset, list[str]]):
        form_name (Union[Unset, str]):
        generator (Union[Unset, Expression]):
        href (Union[Unset, str]):
        id (Union[Unset, str]):
        last_updated (Union[Unset, datetime.datetime]):
        last_updated_by (Union[Unset, PredictorLastUpdatedBy]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
        name (Union[Unset, str]):
        organisation_unit_levels (Union[Unset, list['PredictorOrganisationUnitLevelsItem']]):
        output (Union[Unset, PredictorOutput]): A UID reference to a DataElement
            (Java name `org.hisp.dhis.dataelement.DataElement`)
        output_combo (Union[Unset, PredictorOutputCombo]): A UID reference to a CategoryOptionCombo
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`)
        period_type (Union[Unset, PredictorPeriodType]):
        predictor_groups (Union[Unset, list['PredictorPredictorGroupsItem']]):
        sample_skip_test (Union[Unset, Expression]):
        sequential_sample_count (Union[Unset, int]):
        sequential_skip_count (Union[Unset, int]):
        sharing (Union[Unset, Sharing]):
        short_name (Union[Unset, str]):
        translations (Union[Unset, list['Translation']]):
        user (Union[Unset, PredictorUser]): A UID reference to a User
            (Java name `org.hisp.dhis.user.User`)
    """

    organisation_unit_descendants: PredictorOrganisationUnitDescendants
    access: Union[Unset, "Access"] = UNSET
    annual_sample_count: Union[Unset, int] = UNSET
    attribute_values: Union[Unset, list["AttributeValue"]] = UNSET
    code: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "PredictorCreatedBy"] = UNSET
    description: Union[Unset, str] = UNSET
    display_description: Union[Unset, str] = UNSET
    display_form_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_short_name: Union[Unset, str] = UNSET
    favorite: Union[Unset, bool] = UNSET
    favorites: Union[Unset, list[str]] = UNSET
    form_name: Union[Unset, str] = UNSET
    generator: Union[Unset, "Expression"] = UNSET
    href: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_updated_by: Union[Unset, "PredictorLastUpdatedBy"] = UNSET
    name: Union[Unset, str] = UNSET
    organisation_unit_levels: Union[Unset, list["PredictorOrganisationUnitLevelsItem"]] = UNSET
    output: Union[Unset, "PredictorOutput"] = UNSET
    output_combo: Union[Unset, "PredictorOutputCombo"] = UNSET
    period_type: Union[Unset, PredictorPeriodType] = UNSET
    predictor_groups: Union[Unset, list["PredictorPredictorGroupsItem"]] = UNSET
    sample_skip_test: Union[Unset, "Expression"] = UNSET
    sequential_sample_count: Union[Unset, int] = UNSET
    sequential_skip_count: Union[Unset, int] = UNSET
    sharing: Union[Unset, "Sharing"] = UNSET
    short_name: Union[Unset, str] = UNSET
    translations: Union[Unset, list["Translation"]] = UNSET
    user: Union[Unset, "PredictorUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organisation_unit_descendants = self.organisation_unit_descendants.value

        access: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        annual_sample_count = self.annual_sample_count

        attribute_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            attribute_values = []
            for attribute_values_item_data in self.attribute_values:
                attribute_values_item = attribute_values_item_data.to_dict()
                attribute_values.append(attribute_values_item)

        code = self.code

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        display_description = self.display_description

        display_form_name = self.display_form_name

        display_name = self.display_name

        display_short_name = self.display_short_name

        favorite = self.favorite

        favorites: Union[Unset, list[str]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        form_name = self.form_name

        generator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.generator, Unset):
            generator = self.generator.to_dict()

        href = self.href

        id = self.id

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_updated_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_by, Unset):
            last_updated_by = self.last_updated_by.to_dict()

        name = self.name

        organisation_unit_levels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.organisation_unit_levels, Unset):
            organisation_unit_levels = []
            for organisation_unit_levels_item_data in self.organisation_unit_levels:
                organisation_unit_levels_item = organisation_unit_levels_item_data.to_dict()
                organisation_unit_levels.append(organisation_unit_levels_item)

        output: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        output_combo: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.output_combo, Unset):
            output_combo = self.output_combo.to_dict()

        period_type: Union[Unset, str] = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value

        predictor_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.predictor_groups, Unset):
            predictor_groups = []
            for predictor_groups_item_data in self.predictor_groups:
                predictor_groups_item = predictor_groups_item_data.to_dict()
                predictor_groups.append(predictor_groups_item)

        sample_skip_test: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sample_skip_test, Unset):
            sample_skip_test = self.sample_skip_test.to_dict()

        sequential_sample_count = self.sequential_sample_count

        sequential_skip_count = self.sequential_skip_count

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
                "organisationUnitDescendants": organisation_unit_descendants,
            }
        )
        if access is not UNSET:
            field_dict["access"] = access
        if annual_sample_count is not UNSET:
            field_dict["annualSampleCount"] = annual_sample_count
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values
        if code is not UNSET:
            field_dict["code"] = code
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
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
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if generator is not UNSET:
            field_dict["generator"] = generator
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
        if organisation_unit_levels is not UNSET:
            field_dict["organisationUnitLevels"] = organisation_unit_levels
        if output is not UNSET:
            field_dict["output"] = output
        if output_combo is not UNSET:
            field_dict["outputCombo"] = output_combo
        if period_type is not UNSET:
            field_dict["periodType"] = period_type
        if predictor_groups is not UNSET:
            field_dict["predictorGroups"] = predictor_groups
        if sample_skip_test is not UNSET:
            field_dict["sampleSkipTest"] = sample_skip_test
        if sequential_sample_count is not UNSET:
            field_dict["sequentialSampleCount"] = sequential_sample_count
        if sequential_skip_count is not UNSET:
            field_dict["sequentialSkipCount"] = sequential_skip_count
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
        from ..models.expression import Expression
        from ..models.predictor_created_by import PredictorCreatedBy
        from ..models.predictor_last_updated_by import PredictorLastUpdatedBy
        from ..models.predictor_organisation_unit_levels_item import PredictorOrganisationUnitLevelsItem
        from ..models.predictor_output import PredictorOutput
        from ..models.predictor_output_combo import PredictorOutputCombo
        from ..models.predictor_predictor_groups_item import PredictorPredictorGroupsItem
        from ..models.predictor_user import PredictorUser
        from ..models.sharing import Sharing
        from ..models.translation import Translation

        d = src_dict.copy()
        organisation_unit_descendants = PredictorOrganisationUnitDescendants(d.pop("organisationUnitDescendants"))

        _access = d.pop("access", UNSET)
        access: Union[Unset, Access]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        annual_sample_count = d.pop("annualSampleCount", UNSET)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = AttributeValue.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        code = d.pop("code", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, PredictorCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = PredictorCreatedBy.from_dict(_created_by)

        description = d.pop("description", UNSET)

        display_description = d.pop("displayDescription", UNSET)

        display_form_name = d.pop("displayFormName", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_short_name = d.pop("displayShortName", UNSET)

        favorite = d.pop("favorite", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        form_name = d.pop("formName", UNSET)

        _generator = d.pop("generator", UNSET)
        generator: Union[Unset, Expression]
        if isinstance(_generator, Unset):
            generator = UNSET
        else:
            generator = Expression.from_dict(_generator)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_updated_by = d.pop("lastUpdatedBy", UNSET)
        last_updated_by: Union[Unset, PredictorLastUpdatedBy]
        if isinstance(_last_updated_by, Unset):
            last_updated_by = UNSET
        else:
            last_updated_by = PredictorLastUpdatedBy.from_dict(_last_updated_by)

        name = d.pop("name", UNSET)

        organisation_unit_levels = []
        _organisation_unit_levels = d.pop("organisationUnitLevels", UNSET)
        for organisation_unit_levels_item_data in _organisation_unit_levels or []:
            organisation_unit_levels_item = PredictorOrganisationUnitLevelsItem.from_dict(
                organisation_unit_levels_item_data
            )

            organisation_unit_levels.append(organisation_unit_levels_item)

        _output = d.pop("output", UNSET)
        output: Union[Unset, PredictorOutput]
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = PredictorOutput.from_dict(_output)

        _output_combo = d.pop("outputCombo", UNSET)
        output_combo: Union[Unset, PredictorOutputCombo]
        if isinstance(_output_combo, Unset):
            output_combo = UNSET
        else:
            output_combo = PredictorOutputCombo.from_dict(_output_combo)

        _period_type = d.pop("periodType", UNSET)
        period_type: Union[Unset, PredictorPeriodType]
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = PredictorPeriodType(_period_type)

        predictor_groups = []
        _predictor_groups = d.pop("predictorGroups", UNSET)
        for predictor_groups_item_data in _predictor_groups or []:
            predictor_groups_item = PredictorPredictorGroupsItem.from_dict(predictor_groups_item_data)

            predictor_groups.append(predictor_groups_item)

        _sample_skip_test = d.pop("sampleSkipTest", UNSET)
        sample_skip_test: Union[Unset, Expression]
        if isinstance(_sample_skip_test, Unset):
            sample_skip_test = UNSET
        else:
            sample_skip_test = Expression.from_dict(_sample_skip_test)

        sequential_sample_count = d.pop("sequentialSampleCount", UNSET)

        sequential_skip_count = d.pop("sequentialSkipCount", UNSET)

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
        user: Union[Unset, PredictorUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PredictorUser.from_dict(_user)

        predictor = cls(
            organisation_unit_descendants=organisation_unit_descendants,
            access=access,
            annual_sample_count=annual_sample_count,
            attribute_values=attribute_values,
            code=code,
            created=created,
            created_by=created_by,
            description=description,
            display_description=display_description,
            display_form_name=display_form_name,
            display_name=display_name,
            display_short_name=display_short_name,
            favorite=favorite,
            favorites=favorites,
            form_name=form_name,
            generator=generator,
            href=href,
            id=id,
            last_updated=last_updated,
            last_updated_by=last_updated_by,
            name=name,
            organisation_unit_levels=organisation_unit_levels,
            output=output,
            output_combo=output_combo,
            period_type=period_type,
            predictor_groups=predictor_groups,
            sample_skip_test=sample_skip_test,
            sequential_sample_count=sequential_sample_count,
            sequential_skip_count=sequential_skip_count,
            sharing=sharing,
            short_name=short_name,
            translations=translations,
            user=user,
        )

        predictor.additional_properties = d
        return predictor

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
