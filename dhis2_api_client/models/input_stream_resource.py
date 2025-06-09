from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.input_stream import InputStream


T = TypeVar("T", bound="InputStreamResource")


@_attrs_define
class InputStreamResource:
    """
    Attributes:
        description (Union[Unset, str]):
        file (Union[Unset, File]): The actual type is unknown.
            (Java type was: `class java.io.File`)
        filename (Union[Unset, str]):
        input_stream (Union[Unset, InputStream]): The actual type is unknown.
            (Java type was: `class java.io.InputStream`)
        open_ (Union[Unset, bool]):
        readable (Union[Unset, bool]):
        u_ri (Union[Unset, str]):
        u_rl (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    file: Union[Unset, "File"] = UNSET
    filename: Union[Unset, str] = UNSET
    input_stream: Union[Unset, "InputStream"] = UNSET
    open_: Union[Unset, bool] = UNSET
    readable: Union[Unset, bool] = UNSET
    u_ri: Union[Unset, str] = UNSET
    u_rl: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        file: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        filename = self.filename

        input_stream: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.input_stream, Unset):
            input_stream = self.input_stream.to_dict()

        open_ = self.open_

        readable = self.readable

        u_ri = self.u_ri

        u_rl = self.u_rl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if file is not UNSET:
            field_dict["file"] = file
        if filename is not UNSET:
            field_dict["filename"] = filename
        if input_stream is not UNSET:
            field_dict["inputStream"] = input_stream
        if open_ is not UNSET:
            field_dict["open"] = open_
        if readable is not UNSET:
            field_dict["readable"] = readable
        if u_ri is not UNSET:
            field_dict["uRI"] = u_ri
        if u_rl is not UNSET:
            field_dict["uRL"] = u_rl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file import File
        from ..models.input_stream import InputStream

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _file = d.pop("file", UNSET)
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File.from_dict(_file)

        filename = d.pop("filename", UNSET)

        _input_stream = d.pop("inputStream", UNSET)
        input_stream: Union[Unset, InputStream]
        if isinstance(_input_stream, Unset):
            input_stream = UNSET
        else:
            input_stream = InputStream.from_dict(_input_stream)

        open_ = d.pop("open", UNSET)

        readable = d.pop("readable", UNSET)

        u_ri = d.pop("uRI", UNSET)

        u_rl = d.pop("uRL", UNSET)

        input_stream_resource = cls(
            description=description,
            file=file,
            filename=filename,
            input_stream=input_stream,
            open_=open_,
            readable=readable,
            u_ri=u_ri,
            u_rl=u_rl,
        )

        input_stream_resource.additional_properties = d
        return input_stream_resource

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
