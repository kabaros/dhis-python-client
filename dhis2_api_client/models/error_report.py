from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_report_error_code import ErrorReportErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_report_value import ErrorReportValue


T = TypeVar("T", bound="ErrorReport")


@_attrs_define
class ErrorReport:
    """
    Attributes:
        error_code (ErrorReportErrorCode):
        args (Union[Unset, list[str]]):
        error_klass (Union[Unset, str]):
        error_properties (Union[Unset, list[Any]]):
        error_property (Union[Unset, str]):
        main_id (Union[Unset, str]):
        main_klass (Union[Unset, str]):
        message (Union[Unset, str]):
        value (Union[Unset, ErrorReportValue]): The actual type is unknown.
            (Java type was: `class java.lang.Object`)
    """

    error_code: ErrorReportErrorCode
    args: Union[Unset, list[str]] = UNSET
    error_klass: Union[Unset, str] = UNSET
    error_properties: Union[Unset, list[Any]] = UNSET
    error_property: Union[Unset, str] = UNSET
    main_id: Union[Unset, str] = UNSET
    main_klass: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    value: Union[Unset, "ErrorReportValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code.value

        args: Union[Unset, list[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        error_klass = self.error_klass

        error_properties: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.error_properties, Unset):
            error_properties = self.error_properties

        error_property = self.error_property

        main_id = self.main_id

        main_klass = self.main_klass

        message = self.message

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorCode": error_code,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if error_klass is not UNSET:
            field_dict["errorKlass"] = error_klass
        if error_properties is not UNSET:
            field_dict["errorProperties"] = error_properties
        if error_property is not UNSET:
            field_dict["errorProperty"] = error_property
        if main_id is not UNSET:
            field_dict["mainId"] = main_id
        if main_klass is not UNSET:
            field_dict["mainKlass"] = main_klass
        if message is not UNSET:
            field_dict["message"] = message
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.error_report_value import ErrorReportValue

        d = src_dict.copy()
        error_code = ErrorReportErrorCode(d.pop("errorCode"))

        args = cast(list[str], d.pop("args", UNSET))

        error_klass = d.pop("errorKlass", UNSET)

        error_properties = cast(list[Any], d.pop("errorProperties", UNSET))

        error_property = d.pop("errorProperty", UNSET)

        main_id = d.pop("mainId", UNSET)

        main_klass = d.pop("mainKlass", UNSET)

        message = d.pop("message", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, ErrorReportValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ErrorReportValue.from_dict(_value)

        error_report = cls(
            error_code=error_code,
            args=args,
            error_klass=error_klass,
            error_properties=error_properties,
            error_property=error_property,
            main_id=main_id,
            main_klass=main_klass,
            message=message,
            value=value,
        )

        error_report.additional_properties = d
        return error_report

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
