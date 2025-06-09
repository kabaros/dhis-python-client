from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_query_criteria_assigned_user_mode import EntityQueryCriteriaAssignedUserMode
from ..models.entity_query_criteria_enrollment_status import EntityQueryCriteriaEnrollmentStatus
from ..models.entity_query_criteria_event_status import EntityQueryCriteriaEventStatus
from ..models.entity_query_criteria_ou_mode import EntityQueryCriteriaOuMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute_value_filter import AttributeValueFilter
    from ..models.date_filter_period import DateFilterPeriod


T = TypeVar("T", bound="EntityQueryCriteria")


@_attrs_define
class EntityQueryCriteria:
    """
    Attributes:
        assigned_user_mode (EntityQueryCriteriaAssignedUserMode):
        enrollment_status (EntityQueryCriteriaEnrollmentStatus):
        event_status (EntityQueryCriteriaEventStatus):
        ou_mode (EntityQueryCriteriaOuMode):
        assigned_users (Union[Unset, list[str]]):
        attribute_value_filters (Union[Unset, list['AttributeValueFilter']]):
        display_column_order (Union[Unset, list[str]]):
        enrollment_created_date (Union[Unset, DateFilterPeriod]):
        enrollment_incident_date (Union[Unset, DateFilterPeriod]):
        event_date (Union[Unset, DateFilterPeriod]):
        follow_up (Union[Unset, bool]):
        last_updated_date (Union[Unset, DateFilterPeriod]):
        order (Union[Unset, str]):
        organisation_unit (Union[Unset, str]):
        program_stage (Union[Unset, str]):
        tracked_entity_instances (Union[Unset, list[str]]):
        tracked_entity_type (Union[Unset, str]):
    """

    assigned_user_mode: EntityQueryCriteriaAssignedUserMode
    enrollment_status: EntityQueryCriteriaEnrollmentStatus
    event_status: EntityQueryCriteriaEventStatus
    ou_mode: EntityQueryCriteriaOuMode
    assigned_users: Union[Unset, list[str]] = UNSET
    attribute_value_filters: Union[Unset, list["AttributeValueFilter"]] = UNSET
    display_column_order: Union[Unset, list[str]] = UNSET
    enrollment_created_date: Union[Unset, "DateFilterPeriod"] = UNSET
    enrollment_incident_date: Union[Unset, "DateFilterPeriod"] = UNSET
    event_date: Union[Unset, "DateFilterPeriod"] = UNSET
    follow_up: Union[Unset, bool] = UNSET
    last_updated_date: Union[Unset, "DateFilterPeriod"] = UNSET
    order: Union[Unset, str] = UNSET
    organisation_unit: Union[Unset, str] = UNSET
    program_stage: Union[Unset, str] = UNSET
    tracked_entity_instances: Union[Unset, list[str]] = UNSET
    tracked_entity_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_user_mode = self.assigned_user_mode.value

        enrollment_status = self.enrollment_status.value

        event_status = self.event_status.value

        ou_mode = self.ou_mode.value

        assigned_users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigned_users, Unset):
            assigned_users = self.assigned_users

        attribute_value_filters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_value_filters, Unset):
            attribute_value_filters = []
            for attribute_value_filters_item_data in self.attribute_value_filters:
                attribute_value_filters_item = attribute_value_filters_item_data.to_dict()
                attribute_value_filters.append(attribute_value_filters_item)

        display_column_order: Union[Unset, list[str]] = UNSET
        if not isinstance(self.display_column_order, Unset):
            display_column_order = self.display_column_order

        enrollment_created_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_created_date, Unset):
            enrollment_created_date = self.enrollment_created_date.to_dict()

        enrollment_incident_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_incident_date, Unset):
            enrollment_incident_date = self.enrollment_incident_date.to_dict()

        event_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_date, Unset):
            event_date = self.event_date.to_dict()

        follow_up = self.follow_up

        last_updated_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.to_dict()

        order = self.order

        organisation_unit = self.organisation_unit

        program_stage = self.program_stage

        tracked_entity_instances: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tracked_entity_instances, Unset):
            tracked_entity_instances = self.tracked_entity_instances

        tracked_entity_type = self.tracked_entity_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignedUserMode": assigned_user_mode,
                "enrollmentStatus": enrollment_status,
                "eventStatus": event_status,
                "ouMode": ou_mode,
            }
        )
        if assigned_users is not UNSET:
            field_dict["assignedUsers"] = assigned_users
        if attribute_value_filters is not UNSET:
            field_dict["attributeValueFilters"] = attribute_value_filters
        if display_column_order is not UNSET:
            field_dict["displayColumnOrder"] = display_column_order
        if enrollment_created_date is not UNSET:
            field_dict["enrollmentCreatedDate"] = enrollment_created_date
        if enrollment_incident_date is not UNSET:
            field_dict["enrollmentIncidentDate"] = enrollment_incident_date
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date
        if follow_up is not UNSET:
            field_dict["followUp"] = follow_up
        if last_updated_date is not UNSET:
            field_dict["lastUpdatedDate"] = last_updated_date
        if order is not UNSET:
            field_dict["order"] = order
        if organisation_unit is not UNSET:
            field_dict["organisationUnit"] = organisation_unit
        if program_stage is not UNSET:
            field_dict["programStage"] = program_stage
        if tracked_entity_instances is not UNSET:
            field_dict["trackedEntityInstances"] = tracked_entity_instances
        if tracked_entity_type is not UNSET:
            field_dict["trackedEntityType"] = tracked_entity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.attribute_value_filter import AttributeValueFilter
        from ..models.date_filter_period import DateFilterPeriod

        d = src_dict.copy()
        assigned_user_mode = EntityQueryCriteriaAssignedUserMode(d.pop("assignedUserMode"))

        enrollment_status = EntityQueryCriteriaEnrollmentStatus(d.pop("enrollmentStatus"))

        event_status = EntityQueryCriteriaEventStatus(d.pop("eventStatus"))

        ou_mode = EntityQueryCriteriaOuMode(d.pop("ouMode"))

        assigned_users = cast(list[str], d.pop("assignedUsers", UNSET))

        attribute_value_filters = []
        _attribute_value_filters = d.pop("attributeValueFilters", UNSET)
        for attribute_value_filters_item_data in _attribute_value_filters or []:
            attribute_value_filters_item = AttributeValueFilter.from_dict(attribute_value_filters_item_data)

            attribute_value_filters.append(attribute_value_filters_item)

        display_column_order = cast(list[str], d.pop("displayColumnOrder", UNSET))

        _enrollment_created_date = d.pop("enrollmentCreatedDate", UNSET)
        enrollment_created_date: Union[Unset, DateFilterPeriod]
        if isinstance(_enrollment_created_date, Unset):
            enrollment_created_date = UNSET
        else:
            enrollment_created_date = DateFilterPeriod.from_dict(_enrollment_created_date)

        _enrollment_incident_date = d.pop("enrollmentIncidentDate", UNSET)
        enrollment_incident_date: Union[Unset, DateFilterPeriod]
        if isinstance(_enrollment_incident_date, Unset):
            enrollment_incident_date = UNSET
        else:
            enrollment_incident_date = DateFilterPeriod.from_dict(_enrollment_incident_date)

        _event_date = d.pop("eventDate", UNSET)
        event_date: Union[Unset, DateFilterPeriod]
        if isinstance(_event_date, Unset):
            event_date = UNSET
        else:
            event_date = DateFilterPeriod.from_dict(_event_date)

        follow_up = d.pop("followUp", UNSET)

        _last_updated_date = d.pop("lastUpdatedDate", UNSET)
        last_updated_date: Union[Unset, DateFilterPeriod]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = DateFilterPeriod.from_dict(_last_updated_date)

        order = d.pop("order", UNSET)

        organisation_unit = d.pop("organisationUnit", UNSET)

        program_stage = d.pop("programStage", UNSET)

        tracked_entity_instances = cast(list[str], d.pop("trackedEntityInstances", UNSET))

        tracked_entity_type = d.pop("trackedEntityType", UNSET)

        entity_query_criteria = cls(
            assigned_user_mode=assigned_user_mode,
            enrollment_status=enrollment_status,
            event_status=event_status,
            ou_mode=ou_mode,
            assigned_users=assigned_users,
            attribute_value_filters=attribute_value_filters,
            display_column_order=display_column_order,
            enrollment_created_date=enrollment_created_date,
            enrollment_incident_date=enrollment_incident_date,
            event_date=event_date,
            follow_up=follow_up,
            last_updated_date=last_updated_date,
            order=order,
            organisation_unit=organisation_unit,
            program_stage=program_stage,
            tracked_entity_instances=tracked_entity_instances,
            tracked_entity_type=tracked_entity_type,
        )

        entity_query_criteria.additional_properties = d
        return entity_query_criteria

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
