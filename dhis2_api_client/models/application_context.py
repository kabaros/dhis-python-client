from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_context_class_loader import ApplicationContextClassLoader
    from ..models.autowire_capable_bean_factory import AutowireCapableBeanFactory
    from ..models.bean_factory import BeanFactory
    from ..models.environment import Environment


T = TypeVar("T", bound="ApplicationContext")


@_attrs_define
class ApplicationContext:
    """
    Attributes:
        bean_definition_count (int):
        startup_date (int):
        application_name (Union[Unset, str]):
        autowire_capable_bean_factory (Union[Unset, AutowireCapableBeanFactory]): The actual type is unknown.
            (Java type was: `interface org.springframework.beans.factory.config.AutowireCapableBeanFactory`)
        bean_definition_names (Union[Unset, list[str]]):
        class_loader (Union[Unset, ApplicationContextClassLoader]): The actual type is unknown.
            (Java type was: `class java.lang.ClassLoader`)
        display_name (Union[Unset, str]):
        environment (Union[Unset, Environment]):
        id (Union[Unset, str]):
        parent (Union[Unset, ApplicationContext]):
        parent_bean_factory (Union[Unset, BeanFactory]): The actual type is unknown.
            (Java type was: `interface org.springframework.beans.factory.BeanFactory`)
    """

    bean_definition_count: int
    startup_date: int
    application_name: Union[Unset, str] = UNSET
    autowire_capable_bean_factory: Union[Unset, "AutowireCapableBeanFactory"] = UNSET
    bean_definition_names: Union[Unset, list[str]] = UNSET
    class_loader: Union[Unset, "ApplicationContextClassLoader"] = UNSET
    display_name: Union[Unset, str] = UNSET
    environment: Union[Unset, "Environment"] = UNSET
    id: Union[Unset, str] = UNSET
    parent: Union[Unset, "ApplicationContext"] = UNSET
    parent_bean_factory: Union[Unset, "BeanFactory"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bean_definition_count = self.bean_definition_count

        startup_date = self.startup_date

        application_name = self.application_name

        autowire_capable_bean_factory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.autowire_capable_bean_factory, Unset):
            autowire_capable_bean_factory = self.autowire_capable_bean_factory.to_dict()

        bean_definition_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.bean_definition_names, Unset):
            bean_definition_names = self.bean_definition_names

        class_loader: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.class_loader, Unset):
            class_loader = self.class_loader.to_dict()

        display_name = self.display_name

        environment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        id = self.id

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        parent_bean_factory: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_bean_factory, Unset):
            parent_bean_factory = self.parent_bean_factory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "beanDefinitionCount": bean_definition_count,
                "startupDate": startup_date,
            }
        )
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if autowire_capable_bean_factory is not UNSET:
            field_dict["autowireCapableBeanFactory"] = autowire_capable_bean_factory
        if bean_definition_names is not UNSET:
            field_dict["beanDefinitionNames"] = bean_definition_names
        if class_loader is not UNSET:
            field_dict["classLoader"] = class_loader
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if id is not UNSET:
            field_dict["id"] = id
        if parent is not UNSET:
            field_dict["parent"] = parent
        if parent_bean_factory is not UNSET:
            field_dict["parentBeanFactory"] = parent_bean_factory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.application_context_class_loader import ApplicationContextClassLoader
        from ..models.autowire_capable_bean_factory import AutowireCapableBeanFactory
        from ..models.bean_factory import BeanFactory
        from ..models.environment import Environment

        d = src_dict.copy()
        bean_definition_count = d.pop("beanDefinitionCount")

        startup_date = d.pop("startupDate")

        application_name = d.pop("applicationName", UNSET)

        _autowire_capable_bean_factory = d.pop("autowireCapableBeanFactory", UNSET)
        autowire_capable_bean_factory: Union[Unset, AutowireCapableBeanFactory]
        if isinstance(_autowire_capable_bean_factory, Unset):
            autowire_capable_bean_factory = UNSET
        else:
            autowire_capable_bean_factory = AutowireCapableBeanFactory.from_dict(_autowire_capable_bean_factory)

        bean_definition_names = cast(list[str], d.pop("beanDefinitionNames", UNSET))

        _class_loader = d.pop("classLoader", UNSET)
        class_loader: Union[Unset, ApplicationContextClassLoader]
        if isinstance(_class_loader, Unset):
            class_loader = UNSET
        else:
            class_loader = ApplicationContextClassLoader.from_dict(_class_loader)

        display_name = d.pop("displayName", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, Environment]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = Environment.from_dict(_environment)

        id = d.pop("id", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, ApplicationContext]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = ApplicationContext.from_dict(_parent)

        _parent_bean_factory = d.pop("parentBeanFactory", UNSET)
        parent_bean_factory: Union[Unset, BeanFactory]
        if isinstance(_parent_bean_factory, Unset):
            parent_bean_factory = UNSET
        else:
            parent_bean_factory = BeanFactory.from_dict(_parent_bean_factory)

        application_context = cls(
            bean_definition_count=bean_definition_count,
            startup_date=startup_date,
            application_name=application_name,
            autowire_capable_bean_factory=autowire_capable_bean_factory,
            bean_definition_names=bean_definition_names,
            class_loader=class_loader,
            display_name=display_name,
            environment=environment,
            id=id,
            parent=parent,
            parent_bean_factory=parent_bean_factory,
        )

        application_context.additional_properties = d
        return application_context

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
