from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_status_dto_state import ApprovalStatusDtoState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_approval_permissions import DataApprovalPermissions


T = TypeVar("T", bound="ApprovalStatusDto")


@_attrs_define
class ApprovalStatusDto:
    """
    Attributes:
        state (ApprovalStatusDtoState):
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        level (Union[Unset, str]):
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        ou_name (Union[Unset, str]):
        pe (Union[Unset, str]):
        permissions (Union[Unset, DataApprovalPermissions]):
        wf (Union[Unset, str]): A UID for an DataApprovalWorkflow object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalWorkflow`) Example: q6Cw2bo1N7Z.
    """

    state: ApprovalStatusDtoState
    aoc: Union[Unset, str] = UNSET
    level: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    ou_name: Union[Unset, str] = UNSET
    pe: Union[Unset, str] = UNSET
    permissions: Union[Unset, "DataApprovalPermissions"] = UNSET
    wf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        aoc = self.aoc

        level = self.level

        ou = self.ou

        ou_name = self.ou_name

        pe = self.pe

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        wf = self.wf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
            }
        )
        if aoc is not UNSET:
            field_dict["aoc"] = aoc
        if level is not UNSET:
            field_dict["level"] = level
        if ou is not UNSET:
            field_dict["ou"] = ou
        if ou_name is not UNSET:
            field_dict["ouName"] = ou_name
        if pe is not UNSET:
            field_dict["pe"] = pe
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if wf is not UNSET:
            field_dict["wf"] = wf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.data_approval_permissions import DataApprovalPermissions

        d = src_dict.copy()
        state = ApprovalStatusDtoState(d.pop("state"))

        aoc = d.pop("aoc", UNSET)

        level = d.pop("level", UNSET)

        ou = d.pop("ou", UNSET)

        ou_name = d.pop("ouName", UNSET)

        pe = d.pop("pe", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, DataApprovalPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = DataApprovalPermissions.from_dict(_permissions)

        wf = d.pop("wf", UNSET)

        approval_status_dto = cls(
            state=state,
            aoc=aoc,
            level=level,
            ou=ou,
            ou_name=ou_name,
            pe=pe,
            permissions=permissions,
            wf=wf,
        )

        approval_status_dto.additional_properties = d
        return approval_status_dto

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
