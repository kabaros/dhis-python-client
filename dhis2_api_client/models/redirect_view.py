from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_context import ApplicationContext
    from ..models.redirect_view_attributes_map import RedirectViewAttributesMap
    from ..models.redirect_view_static_attributes import RedirectViewStaticAttributes


T = TypeVar("T", bound="RedirectView")


@_attrs_define
class RedirectView:
    """
    Attributes:
        application_context (Union[Unset, ApplicationContext]):
        attributes_map (Union[Unset, RedirectViewAttributesMap]):
        bean_name (Union[Unset, str]):
        content_type (Union[Unset, str]):
        expose_path_variables (Union[Unset, bool]):
        hosts (Union[Unset, list[str]]):
        propagate_query_properties (Union[Unset, bool]):
        redirect_view (Union[Unset, bool]):
        request_context_attribute (Union[Unset, str]):
        static_attributes (Union[Unset, RedirectViewStaticAttributes]):
        url (Union[Unset, str]):
    """

    application_context: Union[Unset, "ApplicationContext"] = UNSET
    attributes_map: Union[Unset, "RedirectViewAttributesMap"] = UNSET
    bean_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    expose_path_variables: Union[Unset, bool] = UNSET
    hosts: Union[Unset, list[str]] = UNSET
    propagate_query_properties: Union[Unset, bool] = UNSET
    redirect_view: Union[Unset, bool] = UNSET
    request_context_attribute: Union[Unset, str] = UNSET
    static_attributes: Union[Unset, "RedirectViewStaticAttributes"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.application_context, Unset):
            application_context = self.application_context.to_dict()

        attributes_map: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attributes_map, Unset):
            attributes_map = self.attributes_map.to_dict()

        bean_name = self.bean_name

        content_type = self.content_type

        expose_path_variables = self.expose_path_variables

        hosts: Union[Unset, list[str]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        propagate_query_properties = self.propagate_query_properties

        redirect_view = self.redirect_view

        request_context_attribute = self.request_context_attribute

        static_attributes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_attributes, Unset):
            static_attributes = self.static_attributes.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_context is not UNSET:
            field_dict["applicationContext"] = application_context
        if attributes_map is not UNSET:
            field_dict["attributesMap"] = attributes_map
        if bean_name is not UNSET:
            field_dict["beanName"] = bean_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if expose_path_variables is not UNSET:
            field_dict["exposePathVariables"] = expose_path_variables
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if propagate_query_properties is not UNSET:
            field_dict["propagateQueryProperties"] = propagate_query_properties
        if redirect_view is not UNSET:
            field_dict["redirectView"] = redirect_view
        if request_context_attribute is not UNSET:
            field_dict["requestContextAttribute"] = request_context_attribute
        if static_attributes is not UNSET:
            field_dict["staticAttributes"] = static_attributes
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.application_context import ApplicationContext
        from ..models.redirect_view_attributes_map import RedirectViewAttributesMap
        from ..models.redirect_view_static_attributes import RedirectViewStaticAttributes

        d = src_dict.copy()
        _application_context = d.pop("applicationContext", UNSET)
        application_context: Union[Unset, ApplicationContext]
        if isinstance(_application_context, Unset):
            application_context = UNSET
        else:
            application_context = ApplicationContext.from_dict(_application_context)

        _attributes_map = d.pop("attributesMap", UNSET)
        attributes_map: Union[Unset, RedirectViewAttributesMap]
        if isinstance(_attributes_map, Unset):
            attributes_map = UNSET
        else:
            attributes_map = RedirectViewAttributesMap.from_dict(_attributes_map)

        bean_name = d.pop("beanName", UNSET)

        content_type = d.pop("contentType", UNSET)

        expose_path_variables = d.pop("exposePathVariables", UNSET)

        hosts = cast(list[str], d.pop("hosts", UNSET))

        propagate_query_properties = d.pop("propagateQueryProperties", UNSET)

        redirect_view = d.pop("redirectView", UNSET)

        request_context_attribute = d.pop("requestContextAttribute", UNSET)

        _static_attributes = d.pop("staticAttributes", UNSET)
        static_attributes: Union[Unset, RedirectViewStaticAttributes]
        if isinstance(_static_attributes, Unset):
            static_attributes = UNSET
        else:
            static_attributes = RedirectViewStaticAttributes.from_dict(_static_attributes)

        url = d.pop("url", UNSET)

        redirect_view = cls(
            application_context=application_context,
            attributes_map=attributes_map,
            bean_name=bean_name,
            content_type=content_type,
            expose_path_variables=expose_path_variables,
            hosts=hosts,
            propagate_query_properties=propagate_query_properties,
            redirect_view=redirect_view,
            request_context_attribute=request_context_attribute,
            static_attributes=static_attributes,
            url=url,
        )

        redirect_view.additional_properties = d
        return redirect_view

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
