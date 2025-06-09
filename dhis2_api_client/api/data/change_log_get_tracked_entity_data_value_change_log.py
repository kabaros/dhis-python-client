import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_log_get_tracked_entity_data_value_change_log_audit_type_item import (
    ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem,
)
from ...models.change_log_get_tracked_entity_data_value_change_log_ou_mode import (
    ChangeLogGetTrackedEntityDataValueChangeLogOuMode,
)
from ...models.change_log_get_tracked_entity_data_value_change_log_response_200 import (
    ChangeLogGetTrackedEntityDataValueChangeLogResponse200,
)
from ...models.data_element import DataElement
from ...models.event import Event
from ...models.organisation_unit import OrganisationUnit
from ...models.program_stage import ProgramStage
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    audit_type: Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    events: Union["Event", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    ps: Union["ProgramStage", Unset, list[str]] = UNSET,
    psi: Union["Event", Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_audit_type: Union[Unset, list[str]] = UNSET
    if not isinstance(audit_type, Unset):
        json_audit_type = []
        for audit_type_item_data in audit_type:
            audit_type_item = audit_type_item_data.value
            json_audit_type.append(audit_type_item)

    params["auditType"] = json_audit_type

    json_de: Union[Unset, dict[str, Any], list[str]]
    if isinstance(de, Unset):
        json_de = UNSET
    elif isinstance(de, list):
        json_de = de

    else:
        json_de = de.to_dict()

    params["de"] = json_de

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_events: Union[Unset, dict[str, Any], list[str]]
    if isinstance(events, Unset):
        json_events = UNSET
    elif isinstance(events, list):
        json_events = events

    else:
        json_events = events.to_dict()

    params["events"] = json_events

    json_ou: Union[Unset, dict[str, Any], list[str]]
    if isinstance(ou, Unset):
        json_ou = UNSET
    elif isinstance(ou, list):
        json_ou = ou

    else:
        json_ou = ou.to_dict()

    params["ou"] = json_ou

    json_ou_mode: Union[Unset, str] = UNSET
    if not isinstance(ou_mode, Unset):
        json_ou_mode = ou_mode.value

    params["ouMode"] = json_ou_mode

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_ps: Union[Unset, dict[str, Any], list[str]]
    if isinstance(ps, Unset):
        json_ps = UNSET
    elif isinstance(ps, list):
        json_ps = ps

    else:
        json_ps = ps.to_dict()

    params["ps"] = json_ps

    json_psi: Union[Unset, dict[str, Any], list[str]]
    if isinstance(psi, Unset):
        json_psi = UNSET
    elif isinstance(psi, list):
        json_psi = psi

    else:
        json_psi = psi.to_dict()

    params["psi"] = json_psi

    params["skipPaging"] = skip_paging

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audits/trackedEntityDataValue",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = ChangeLogGetTrackedEntityDataValueChangeLogResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    events: Union["Event", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    ps: Union["ProgramStage", Unset, list[str]] = UNSET,
    psi: Union["Event", Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]]):
        de (Union['DataElement', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        events (Union['Event', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        ou_mode (Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        ps (Union['ProgramStage', Unset, list[str]]):
        psi (Union['Event', Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        audit_type=audit_type,
        de=de,
        end_date=end_date,
        events=events,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        ps=ps,
        psi=psi,
        skip_paging=skip_paging,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    events: Union["Event", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    ps: Union["ProgramStage", Unset, list[str]] = UNSET,
    psi: Union["Event", Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]]):
        de (Union['DataElement', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        events (Union['Event', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        ou_mode (Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        ps (Union['ProgramStage', Unset, list[str]]):
        psi (Union['Event', Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]
    """

    return sync_detailed(
        client=client,
        audit_type=audit_type,
        de=de,
        end_date=end_date,
        events=events,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        ps=ps,
        psi=psi,
        skip_paging=skip_paging,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    events: Union["Event", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    ps: Union["ProgramStage", Unset, list[str]] = UNSET,
    psi: Union["Event", Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]]):
        de (Union['DataElement', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        events (Union['Event', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        ou_mode (Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        ps (Union['ProgramStage', Unset, list[str]]):
        psi (Union['Event', Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        audit_type=audit_type,
        de=de,
        end_date=end_date,
        events=events,
        ou=ou,
        ou_mode=ou_mode,
        page=page,
        page_size=page_size,
        paging=paging,
        ps=ps,
        psi=psi,
        skip_paging=skip_paging,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    events: Union["Event", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    ou_mode: Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    ps: Union["ProgramStage", Unset, list[str]] = UNSET,
    psi: Union["Event", Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEntityDataValueChangeLogAuditTypeItem]]):
        de (Union['DataElement', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        events (Union['Event', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        ou_mode (Union[Unset, ChangeLogGetTrackedEntityDataValueChangeLogOuMode]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        ps (Union['ProgramStage', Unset, list[str]]):
        psi (Union['Event', Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChangeLogGetTrackedEntityDataValueChangeLogResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            audit_type=audit_type,
            de=de,
            end_date=end_date,
            events=events,
            ou=ou,
            ou_mode=ou_mode,
            page=page,
            page_size=page_size,
            paging=paging,
            ps=ps,
            psi=psi,
            skip_paging=skip_paging,
            start_date=start_date,
        )
    ).parsed
