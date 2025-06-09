import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
    scheduled_at: Union[Unset, datetime.datetime] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["enrollment"] = enrollment

    params["event"] = event

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["programInstance"] = program_instance

    params["programStageInstance"] = program_stage_instance

    json_scheduled_at: Union[Unset, str] = UNSET
    if not isinstance(scheduled_at, Unset):
        json_scheduled_at = scheduled_at.isoformat()
    params["scheduledAt"] = json_scheduled_at

    params["skipPaging"] = skip_paging

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/programNotificationInstances/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WebMessage]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
    scheduled_at: Union[Unset, datetime.datetime] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):
        scheduled_at (Union[Unset, datetime.datetime]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        event=event,
        page=page,
        page_size=page_size,
        paging=paging,
        program_instance=program_instance,
        program_stage_instance=program_stage_instance,
        scheduled_at=scheduled_at,
        skip_paging=skip_paging,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
    scheduled_at: Union[Unset, datetime.datetime] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):
        scheduled_at (Union[Unset, datetime.datetime]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return sync_detailed(
        client=client,
        enrollment=enrollment,
        event=event,
        page=page,
        page_size=page_size,
        paging=paging,
        program_instance=program_instance,
        program_stage_instance=program_stage_instance,
        scheduled_at=scheduled_at,
        skip_paging=skip_paging,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
    scheduled_at: Union[Unset, datetime.datetime] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):
        scheduled_at (Union[Unset, datetime.datetime]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        enrollment=enrollment,
        event=event,
        page=page,
        page_size=page_size,
        paging=paging,
        program_instance=program_instance,
        program_stage_instance=program_stage_instance,
        scheduled_at=scheduled_at,
        skip_paging=skip_paging,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
    scheduled_at: Union[Unset, datetime.datetime] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):
        scheduled_at (Union[Unset, datetime.datetime]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            enrollment=enrollment,
            event=event,
            page=page,
            page_size=page_size,
            paging=paging,
            program_instance=program_instance,
            program_stage_instance=program_stage_instance,
            scheduled_at=scheduled_at,
            skip_paging=skip_paging,
        )
    ).parsed
