from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.property_item_property_type import PropertyItemPropertyType
from ..models.property_property_type import PropertyPropertyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gist_preferences import GistPreferences
    from ..models.property_default_value import PropertyDefaultValue


T = TypeVar("T", bound="Property")


@_attrs_define
class Property:
    """
    Attributes:
        item_property_type (PropertyItemPropertyType):
        property_type (PropertyPropertyType):
        analytical_object (Union[Unset, bool]):
        api_endpoint (Union[Unset, str]):
        attribute (Union[Unset, bool]):
        cascade (Union[Unset, str]):
        collection (Union[Unset, bool]):
        collection_name (Union[Unset, str]):
        collection_wrapping (Union[Unset, bool]):
        constants (Union[Unset, list[str]]):
        default_value (Union[Unset, PropertyDefaultValue]): The actual type is unknown.
            (Java type was: `class java.lang.Object`)
        description (Union[Unset, str]):
        embedded_object (Union[Unset, bool]):
        field_name (Union[Unset, str]):
        gist_preferences (Union[Unset, GistPreferences]):
        href (Union[Unset, str]):
        i_18_n_translation_key (Union[Unset, str]):
        identifiable_object (Union[Unset, bool]):
        inverse_role (Union[Unset, str]):
        item_klass (Union[Unset, str]):
        klass (Union[Unset, str]):
        length (Union[Unset, int]):
        many_to_many (Union[Unset, bool]):
        many_to_one (Union[Unset, bool]):
        max_ (Union[Unset, float]):
        min_ (Union[Unset, float]):
        name (Union[Unset, str]):
        nameable_object (Union[Unset, bool]):
        namespace (Union[Unset, str]):
        one_to_many (Union[Unset, bool]):
        one_to_one (Union[Unset, bool]):
        ordered (Union[Unset, bool]):
        owner (Union[Unset, bool]):
        owning_role (Union[Unset, str]):
        persisted (Union[Unset, bool]):
        property_transformer (Union[Unset, bool]):
        readable (Union[Unset, bool]):
        relative_api_endpoint (Union[Unset, str]):
        required (Union[Unset, bool]):
        simple (Union[Unset, bool]):
        translatable (Union[Unset, bool]):
        translation_key (Union[Unset, str]):
        unique (Union[Unset, bool]):
        writable (Union[Unset, bool]):
    """

    item_property_type: PropertyItemPropertyType
    property_type: PropertyPropertyType
    analytical_object: Union[Unset, bool] = UNSET
    api_endpoint: Union[Unset, str] = UNSET
    attribute: Union[Unset, bool] = UNSET
    cascade: Union[Unset, str] = UNSET
    collection: Union[Unset, bool] = UNSET
    collection_name: Union[Unset, str] = UNSET
    collection_wrapping: Union[Unset, bool] = UNSET
    constants: Union[Unset, list[str]] = UNSET
    default_value: Union[Unset, "PropertyDefaultValue"] = UNSET
    description: Union[Unset, str] = UNSET
    embedded_object: Union[Unset, bool] = UNSET
    field_name: Union[Unset, str] = UNSET
    gist_preferences: Union[Unset, "GistPreferences"] = UNSET
    href: Union[Unset, str] = UNSET
    i_18_n_translation_key: Union[Unset, str] = UNSET
    identifiable_object: Union[Unset, bool] = UNSET
    inverse_role: Union[Unset, str] = UNSET
    item_klass: Union[Unset, str] = UNSET
    klass: Union[Unset, str] = UNSET
    length: Union[Unset, int] = UNSET
    many_to_many: Union[Unset, bool] = UNSET
    many_to_one: Union[Unset, bool] = UNSET
    max_: Union[Unset, float] = UNSET
    min_: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    nameable_object: Union[Unset, bool] = UNSET
    namespace: Union[Unset, str] = UNSET
    one_to_many: Union[Unset, bool] = UNSET
    one_to_one: Union[Unset, bool] = UNSET
    ordered: Union[Unset, bool] = UNSET
    owner: Union[Unset, bool] = UNSET
    owning_role: Union[Unset, str] = UNSET
    persisted: Union[Unset, bool] = UNSET
    property_transformer: Union[Unset, bool] = UNSET
    readable: Union[Unset, bool] = UNSET
    relative_api_endpoint: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    simple: Union[Unset, bool] = UNSET
    translatable: Union[Unset, bool] = UNSET
    translation_key: Union[Unset, str] = UNSET
    unique: Union[Unset, bool] = UNSET
    writable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_property_type = self.item_property_type.value

        property_type = self.property_type.value

        analytical_object = self.analytical_object

        api_endpoint = self.api_endpoint

        attribute = self.attribute

        cascade = self.cascade

        collection = self.collection

        collection_name = self.collection_name

        collection_wrapping = self.collection_wrapping

        constants: Union[Unset, list[str]] = UNSET
        if not isinstance(self.constants, Unset):
            constants = self.constants

        default_value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        description = self.description

        embedded_object = self.embedded_object

        field_name = self.field_name

        gist_preferences: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gist_preferences, Unset):
            gist_preferences = self.gist_preferences.to_dict()

        href = self.href

        i_18_n_translation_key = self.i_18_n_translation_key

        identifiable_object = self.identifiable_object

        inverse_role = self.inverse_role

        item_klass = self.item_klass

        klass = self.klass

        length = self.length

        many_to_many = self.many_to_many

        many_to_one = self.many_to_one

        max_ = self.max_

        min_ = self.min_

        name = self.name

        nameable_object = self.nameable_object

        namespace = self.namespace

        one_to_many = self.one_to_many

        one_to_one = self.one_to_one

        ordered = self.ordered

        owner = self.owner

        owning_role = self.owning_role

        persisted = self.persisted

        property_transformer = self.property_transformer

        readable = self.readable

        relative_api_endpoint = self.relative_api_endpoint

        required = self.required

        simple = self.simple

        translatable = self.translatable

        translation_key = self.translation_key

        unique = self.unique

        writable = self.writable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemPropertyType": item_property_type,
                "propertyType": property_type,
            }
        )
        if analytical_object is not UNSET:
            field_dict["analyticalObject"] = analytical_object
        if api_endpoint is not UNSET:
            field_dict["apiEndpoint"] = api_endpoint
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if cascade is not UNSET:
            field_dict["cascade"] = cascade
        if collection is not UNSET:
            field_dict["collection"] = collection
        if collection_name is not UNSET:
            field_dict["collectionName"] = collection_name
        if collection_wrapping is not UNSET:
            field_dict["collectionWrapping"] = collection_wrapping
        if constants is not UNSET:
            field_dict["constants"] = constants
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if description is not UNSET:
            field_dict["description"] = description
        if embedded_object is not UNSET:
            field_dict["embeddedObject"] = embedded_object
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if gist_preferences is not UNSET:
            field_dict["gistPreferences"] = gist_preferences
        if href is not UNSET:
            field_dict["href"] = href
        if i_18_n_translation_key is not UNSET:
            field_dict["i18nTranslationKey"] = i_18_n_translation_key
        if identifiable_object is not UNSET:
            field_dict["identifiableObject"] = identifiable_object
        if inverse_role is not UNSET:
            field_dict["inverseRole"] = inverse_role
        if item_klass is not UNSET:
            field_dict["itemKlass"] = item_klass
        if klass is not UNSET:
            field_dict["klass"] = klass
        if length is not UNSET:
            field_dict["length"] = length
        if many_to_many is not UNSET:
            field_dict["manyToMany"] = many_to_many
        if many_to_one is not UNSET:
            field_dict["manyToOne"] = many_to_one
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if name is not UNSET:
            field_dict["name"] = name
        if nameable_object is not UNSET:
            field_dict["nameableObject"] = nameable_object
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if one_to_many is not UNSET:
            field_dict["oneToMany"] = one_to_many
        if one_to_one is not UNSET:
            field_dict["oneToOne"] = one_to_one
        if ordered is not UNSET:
            field_dict["ordered"] = ordered
        if owner is not UNSET:
            field_dict["owner"] = owner
        if owning_role is not UNSET:
            field_dict["owningRole"] = owning_role
        if persisted is not UNSET:
            field_dict["persisted"] = persisted
        if property_transformer is not UNSET:
            field_dict["propertyTransformer"] = property_transformer
        if readable is not UNSET:
            field_dict["readable"] = readable
        if relative_api_endpoint is not UNSET:
            field_dict["relativeApiEndpoint"] = relative_api_endpoint
        if required is not UNSET:
            field_dict["required"] = required
        if simple is not UNSET:
            field_dict["simple"] = simple
        if translatable is not UNSET:
            field_dict["translatable"] = translatable
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if unique is not UNSET:
            field_dict["unique"] = unique
        if writable is not UNSET:
            field_dict["writable"] = writable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.gist_preferences import GistPreferences
        from ..models.property_default_value import PropertyDefaultValue

        d = src_dict.copy()
        item_property_type = PropertyItemPropertyType(d.pop("itemPropertyType"))

        property_type = PropertyPropertyType(d.pop("propertyType"))

        analytical_object = d.pop("analyticalObject", UNSET)

        api_endpoint = d.pop("apiEndpoint", UNSET)

        attribute = d.pop("attribute", UNSET)

        cascade = d.pop("cascade", UNSET)

        collection = d.pop("collection", UNSET)

        collection_name = d.pop("collectionName", UNSET)

        collection_wrapping = d.pop("collectionWrapping", UNSET)

        constants = cast(list[str], d.pop("constants", UNSET))

        _default_value = d.pop("defaultValue", UNSET)
        default_value: Union[Unset, PropertyDefaultValue]
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = PropertyDefaultValue.from_dict(_default_value)

        description = d.pop("description", UNSET)

        embedded_object = d.pop("embeddedObject", UNSET)

        field_name = d.pop("fieldName", UNSET)

        _gist_preferences = d.pop("gistPreferences", UNSET)
        gist_preferences: Union[Unset, GistPreferences]
        if isinstance(_gist_preferences, Unset):
            gist_preferences = UNSET
        else:
            gist_preferences = GistPreferences.from_dict(_gist_preferences)

        href = d.pop("href", UNSET)

        i_18_n_translation_key = d.pop("i18nTranslationKey", UNSET)

        identifiable_object = d.pop("identifiableObject", UNSET)

        inverse_role = d.pop("inverseRole", UNSET)

        item_klass = d.pop("itemKlass", UNSET)

        klass = d.pop("klass", UNSET)

        length = d.pop("length", UNSET)

        many_to_many = d.pop("manyToMany", UNSET)

        many_to_one = d.pop("manyToOne", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        name = d.pop("name", UNSET)

        nameable_object = d.pop("nameableObject", UNSET)

        namespace = d.pop("namespace", UNSET)

        one_to_many = d.pop("oneToMany", UNSET)

        one_to_one = d.pop("oneToOne", UNSET)

        ordered = d.pop("ordered", UNSET)

        owner = d.pop("owner", UNSET)

        owning_role = d.pop("owningRole", UNSET)

        persisted = d.pop("persisted", UNSET)

        property_transformer = d.pop("propertyTransformer", UNSET)

        readable = d.pop("readable", UNSET)

        relative_api_endpoint = d.pop("relativeApiEndpoint", UNSET)

        required = d.pop("required", UNSET)

        simple = d.pop("simple", UNSET)

        translatable = d.pop("translatable", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        unique = d.pop("unique", UNSET)

        writable = d.pop("writable", UNSET)

        property_ = cls(
            item_property_type=item_property_type,
            property_type=property_type,
            analytical_object=analytical_object,
            api_endpoint=api_endpoint,
            attribute=attribute,
            cascade=cascade,
            collection=collection,
            collection_name=collection_name,
            collection_wrapping=collection_wrapping,
            constants=constants,
            default_value=default_value,
            description=description,
            embedded_object=embedded_object,
            field_name=field_name,
            gist_preferences=gist_preferences,
            href=href,
            i_18_n_translation_key=i_18_n_translation_key,
            identifiable_object=identifiable_object,
            inverse_role=inverse_role,
            item_klass=item_klass,
            klass=klass,
            length=length,
            many_to_many=many_to_many,
            many_to_one=many_to_one,
            max_=max_,
            min_=min_,
            name=name,
            nameable_object=nameable_object,
            namespace=namespace,
            one_to_many=one_to_many,
            one_to_one=one_to_one,
            ordered=ordered,
            owner=owner,
            owning_role=owning_role,
            persisted=persisted,
            property_transformer=property_transformer,
            readable=readable,
            relative_api_endpoint=relative_api_endpoint,
            required=required,
            simple=simple,
            translatable=translatable,
            translation_key=translation_key,
            unique=unique,
            writable=writable,
        )

        property_.additional_properties = d
        return property_

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
