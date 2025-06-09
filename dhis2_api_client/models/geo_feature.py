from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.geo_feature_dimensions import GeoFeatureDimensions


T = TypeVar("T", bound="GeoFeature")


@_attrs_define
class GeoFeature:
    """
    Attributes:
        le (int):
        ty (int):
        co (Union[Unset, str]):
        code (Union[Unset, str]):
        dimensions (Union[Unset, GeoFeatureDimensions]):
        hcd (Union[Unset, bool]):
        hcu (Union[Unset, bool]):
        id (Union[Unset, str]):
        na (Union[Unset, str]):
        pg (Union[Unset, str]):
        pi (Union[Unset, str]):
        pn (Union[Unset, str]):
    """

    le: int
    ty: int
    co: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    dimensions: Union[Unset, "GeoFeatureDimensions"] = UNSET
    hcd: Union[Unset, bool] = UNSET
    hcu: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    na: Union[Unset, str] = UNSET
    pg: Union[Unset, str] = UNSET
    pi: Union[Unset, str] = UNSET
    pn: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        le = self.le

        ty = self.ty

        co = self.co

        code = self.code

        dimensions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = self.dimensions.to_dict()

        hcd = self.hcd

        hcu = self.hcu

        id = self.id

        na = self.na

        pg = self.pg

        pi = self.pi

        pn = self.pn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "le": le,
                "ty": ty,
            }
        )
        if co is not UNSET:
            field_dict["co"] = co
        if code is not UNSET:
            field_dict["code"] = code
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if hcd is not UNSET:
            field_dict["hcd"] = hcd
        if hcu is not UNSET:
            field_dict["hcu"] = hcu
        if id is not UNSET:
            field_dict["id"] = id
        if na is not UNSET:
            field_dict["na"] = na
        if pg is not UNSET:
            field_dict["pg"] = pg
        if pi is not UNSET:
            field_dict["pi"] = pi
        if pn is not UNSET:
            field_dict["pn"] = pn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.geo_feature_dimensions import GeoFeatureDimensions

        d = src_dict.copy()
        le = d.pop("le")

        ty = d.pop("ty")

        co = d.pop("co", UNSET)

        code = d.pop("code", UNSET)

        _dimensions = d.pop("dimensions", UNSET)
        dimensions: Union[Unset, GeoFeatureDimensions]
        if isinstance(_dimensions, Unset):
            dimensions = UNSET
        else:
            dimensions = GeoFeatureDimensions.from_dict(_dimensions)

        hcd = d.pop("hcd", UNSET)

        hcu = d.pop("hcu", UNSET)

        id = d.pop("id", UNSET)

        na = d.pop("na", UNSET)

        pg = d.pop("pg", UNSET)

        pi = d.pop("pi", UNSET)

        pn = d.pop("pn", UNSET)

        geo_feature = cls(
            le=le,
            ty=ty,
            co=co,
            code=code,
            dimensions=dimensions,
            hcd=hcd,
            hcu=hcu,
            id=id,
            na=na,
            pg=pg,
            pi=pi,
            pn=pn,
        )

        geo_feature.additional_properties = d
        return geo_feature

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
