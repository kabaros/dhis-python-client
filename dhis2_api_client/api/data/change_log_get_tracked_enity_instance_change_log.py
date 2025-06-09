import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_log_get_tracked_enity_instance_change_log_audit_type_item import (
    ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem,
)
from ...models.change_log_get_tracked_enity_instance_change_log_response_200 import (
    ChangeLogGetTrackedEnityInstanceChangeLogResponse200,
)
from ...models.tracked_entity import TrackedEntity
from ...models.user import User
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    audit_type: Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tei: Union["TrackedEntity", Unset, list[str]] = UNSET,
    tracked_entities: Union["TrackedEntity", Unset, list[str]] = UNSET,
    user: Union["User", Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_audit_type: Union[Unset, list[str]] = UNSET
    if not isinstance(audit_type, Unset):
        json_audit_type = []
        for audit_type_item_data in audit_type:
            audit_type_item = audit_type_item_data.value
            json_audit_type.append(audit_type_item)

    params["auditType"] = json_audit_type

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["skipPaging"] = skip_paging

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_tei: Union[Unset, dict[str, Any], list[str]]
    if isinstance(tei, Unset):
        json_tei = UNSET
    elif isinstance(tei, list):
        json_tei = tei

    else:
        json_tei = tei.to_dict()

    params["tei"] = json_tei

    json_tracked_entities: Union[Unset, dict[str, Any], list[str]]
    if isinstance(tracked_entities, Unset):
        json_tracked_entities = UNSET
    elif isinstance(tracked_entities, list):
        json_tracked_entities = tracked_entities

    else:
        json_tracked_entities = tracked_entities.to_dict()

    params["trackedEntities"] = json_tracked_entities

    json_user: Union[Unset, dict[str, Any], list[str]]
    if isinstance(user, Unset):
        json_user = UNSET
    elif isinstance(user, list):
        json_user = user

    else:
        json_user = user.to_dict()

    params["user"] = json_user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audits/trackedEntityInstance",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = ChangeLogGetTrackedEnityInstanceChangeLogResponse200.from_dict(response.json())

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
) -> Response[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tei: Union["TrackedEntity", Unset, list[str]] = UNSET,
    tracked_entities: Union["TrackedEntity", Unset, list[str]] = UNSET,
    user: Union["User", Unset, list[str]] = UNSET,
) -> Response[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]]):
        end_date (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        tei (Union['TrackedEntity', Unset, list[str]]):
        tracked_entities (Union['TrackedEntity', Unset, list[str]]):
        user (Union['User', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        audit_type=audit_type,
        end_date=end_date,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        start_date=start_date,
        tei=tei,
        tracked_entities=tracked_entities,
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tei: Union["TrackedEntity", Unset, list[str]] = UNSET,
    tracked_entities: Union["TrackedEntity", Unset, list[str]] = UNSET,
    user: Union["User", Unset, list[str]] = UNSET,
) -> Optional[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]]):
        end_date (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        tei (Union['TrackedEntity', Unset, list[str]]):
        tracked_entities (Union['TrackedEntity', Unset, list[str]]):
        user (Union['User', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]
    """

    return sync_detailed(
        client=client,
        audit_type=audit_type,
        end_date=end_date,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        start_date=start_date,
        tei=tei,
        tracked_entities=tracked_entities,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tei: Union["TrackedEntity", Unset, list[str]] = UNSET,
    tracked_entities: Union["TrackedEntity", Unset, list[str]] = UNSET,
    user: Union["User", Unset, list[str]] = UNSET,
) -> Response[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]]):
        end_date (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        tei (Union['TrackedEntity', Unset, list[str]]):
        tracked_entities (Union['TrackedEntity', Unset, list[str]]):
        user (Union['User', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        audit_type=audit_type,
        end_date=end_date,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        start_date=start_date,
        tei=tei,
        tracked_entities=tracked_entities,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    tei: Union["TrackedEntity", Unset, list[str]] = UNSET,
    tracked_entities: Union["TrackedEntity", Unset, list[str]] = UNSET,
    user: Union["User", Unset, list[str]] = UNSET,
) -> Optional[Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetTrackedEnityInstanceChangeLogAuditTypeItem]]):
        end_date (Union[Unset, datetime.datetime]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        tei (Union['TrackedEntity', Unset, list[str]]):
        tracked_entities (Union['TrackedEntity', Unset, list[str]]):
        user (Union['User', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChangeLogGetTrackedEnityInstanceChangeLogResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            audit_type=audit_type,
            end_date=end_date,
            page=page,
            page_size=page_size,
            paging=paging,
            skip_paging=skip_paging,
            start_date=start_date,
            tei=tei,
            tracked_entities=tracked_entities,
            user=user,
        )
    ).parsed
