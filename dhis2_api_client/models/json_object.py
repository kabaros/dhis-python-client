from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_typed_access_store import JsonTypedAccessStore


T = TypeVar("T", bound="JsonObject")


@_attrs_define
class JsonObject:
    """
    Attributes:
        access_cached (Union[Unset, bool]):
        access_store (Union[Unset, JsonTypedAccessStore]): The actual type is unknown.
            (Java type was: `interface org.hisp.dhis.jsontree.JsonTypedAccessStore`)
        array (Union[Unset, bool]):
        boolean (Union[Unset, bool]):
        empty (Union[Unset, bool]):
        integer (Union[Unset, bool]):
        null (Union[Unset, bool]):
        number (Union[Unset, bool]):
        object_ (Union[Unset, bool]):
        string (Union[Unset, bool]):
        undefined (Union[Unset, bool]):
    """

    access_cached: Union[Unset, bool] = UNSET
    access_store: Union[Unset, "JsonTypedAccessStore"] = UNSET
    array: Union[Unset, bool] = UNSET
    boolean: Union[Unset, bool] = UNSET
    empty: Union[Unset, bool] = UNSET
    integer: Union[Unset, bool] = UNSET
    null: Union[Unset, bool] = UNSET
    number: Union[Unset, bool] = UNSET
    object_: Union[Unset, bool] = UNSET
    string: Union[Unset, bool] = UNSET
    undefined: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_cached = self.access_cached

        access_store: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.access_store, Unset):
            access_store = self.access_store.to_dict()

        array = self.array

        boolean = self.boolean

        empty = self.empty

        integer = self.integer

        null = self.null

        number = self.number

        object_ = self.object_

        string = self.string

        undefined = self.undefined

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_cached is not UNSET:
            field_dict["accessCached"] = access_cached
        if access_store is not UNSET:
            field_dict["accessStore"] = access_store
        if array is not UNSET:
            field_dict["array"] = array
        if boolean is not UNSET:
            field_dict["boolean"] = boolean
        if empty is not UNSET:
            field_dict["empty"] = empty
        if integer is not UNSET:
            field_dict["integer"] = integer
        if null is not UNSET:
            field_dict["null"] = null
        if number is not UNSET:
            field_dict["number"] = number
        if object_ is not UNSET:
            field_dict["object"] = object_
        if string is not UNSET:
            field_dict["string"] = string
        if undefined is not UNSET:
            field_dict["undefined"] = undefined

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.json_typed_access_store import JsonTypedAccessStore

        d = src_dict.copy()
        access_cached = d.pop("accessCached", UNSET)

        _access_store = d.pop("accessStore", UNSET)
        access_store: Union[Unset, JsonTypedAccessStore]
        if isinstance(_access_store, Unset):
            access_store = UNSET
        else:
            access_store = JsonTypedAccessStore.from_dict(_access_store)

        array = d.pop("array", UNSET)

        boolean = d.pop("boolean", UNSET)

        empty = d.pop("empty", UNSET)

        integer = d.pop("integer", UNSET)

        null = d.pop("null", UNSET)

        number = d.pop("number", UNSET)

        object_ = d.pop("object", UNSET)

        string = d.pop("string", UNSET)

        undefined = d.pop("undefined", UNSET)

        json_object = cls(
            access_cached=access_cached,
            access_store=access_store,
            array=array,
            boolean=boolean,
            empty=empty,
            integer=integer,
            null=null,
            number=number,
            object_=object_,
            string=string,
            undefined=undefined,
        )

        json_object.additional_properties = d
        return json_object

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
