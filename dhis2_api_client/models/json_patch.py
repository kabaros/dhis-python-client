from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_operation import AddOperation
    from ..models.remove_by_id_operation import RemoveByIdOperation
    from ..models.remove_operation import RemoveOperation
    from ..models.replace_operation import ReplaceOperation


T = TypeVar("T", bound="JsonPatch")


@_attrs_define
class JsonPatch:
    """
    Attributes:
        operations (Union[Unset, list[Union['AddOperation', 'RemoveByIdOperation', 'RemoveOperation',
            'ReplaceOperation']]]):
    """

    operations: Union[
        Unset, list[Union["AddOperation", "RemoveByIdOperation", "RemoveOperation", "ReplaceOperation"]]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_operation import AddOperation
        from ..models.remove_by_id_operation import RemoveByIdOperation
        from ..models.remove_operation import RemoveOperation

        operations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item: dict[str, Any]
                if isinstance(operations_item_data, AddOperation):
                    operations_item = operations_item_data.to_dict()
                elif isinstance(operations_item_data, RemoveOperation):
                    operations_item = operations_item_data.to_dict()
                elif isinstance(operations_item_data, RemoveByIdOperation):
                    operations_item = operations_item_data.to_dict()
                else:
                    operations_item = operations_item_data.to_dict()

                operations.append(operations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operations is not UNSET:
            field_dict["operations"] = operations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.add_operation import AddOperation
        from ..models.remove_by_id_operation import RemoveByIdOperation
        from ..models.remove_operation import RemoveOperation
        from ..models.replace_operation import ReplaceOperation

        d = src_dict.copy()
        operations = []
        _operations = d.pop("operations", UNSET)
        for operations_item_data in _operations or []:

            def _parse_operations_item(
                data: object,
            ) -> Union["AddOperation", "RemoveByIdOperation", "RemoveOperation", "ReplaceOperation"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_0 = AddOperation.from_dict(data)

                    return operations_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_1 = RemoveOperation.from_dict(data)

                    return operations_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    operations_item_type_2 = RemoveByIdOperation.from_dict(data)

                    return operations_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                operations_item_type_3 = ReplaceOperation.from_dict(data)

                return operations_item_type_3

            operations_item = _parse_operations_item(operations_item_data)

            operations.append(operations_item)

        json_patch = cls(
            operations=operations,
        )

        json_patch.additional_properties = d
        return json_patch

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
