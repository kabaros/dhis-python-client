from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_dto import ApprovalDto


T = TypeVar("T", bound="ApprovalsDto")


@_attrs_define
class ApprovalsDto:
    """
    Attributes:
        approvals (Union[Unset, list['ApprovalDto']]):
        ds (Union[Unset, list[str]]):
        pe (Union[Unset, list[str]]):
        wf (Union[Unset, list[str]]):
    """

    approvals: Union[Unset, list["ApprovalDto"]] = UNSET
    ds: Union[Unset, list[str]] = UNSET
    pe: Union[Unset, list[str]] = UNSET
    wf: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approvals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.approvals, Unset):
            approvals = []
            for approvals_item_data in self.approvals:
                approvals_item = approvals_item_data.to_dict()
                approvals.append(approvals_item)

        ds: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ds, Unset):
            ds = self.ds

        pe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pe, Unset):
            pe = self.pe

        wf: Union[Unset, list[str]] = UNSET
        if not isinstance(self.wf, Unset):
            wf = self.wf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approvals is not UNSET:
            field_dict["approvals"] = approvals
        if ds is not UNSET:
            field_dict["ds"] = ds
        if pe is not UNSET:
            field_dict["pe"] = pe
        if wf is not UNSET:
            field_dict["wf"] = wf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.approval_dto import ApprovalDto

        d = src_dict.copy()
        approvals = []
        _approvals = d.pop("approvals", UNSET)
        for approvals_item_data in _approvals or []:
            approvals_item = ApprovalDto.from_dict(approvals_item_data)

            approvals.append(approvals_item)

        ds = cast(list[str], d.pop("ds", UNSET))

        pe = cast(list[str], d.pop("pe", UNSET))

        wf = cast(list[str], d.pop("wf", UNSET))

        approvals_dto = cls(
            approvals=approvals,
            ds=ds,
            pe=pe,
            wf=wf,
        )

        approvals_dto.additional_properties = d
        return approvals_dto

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
