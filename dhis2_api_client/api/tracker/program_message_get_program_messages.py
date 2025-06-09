import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.program_message import ProgramMessage
from ...models.program_message_get_program_messages_message_status import ProgramMessageGetProgramMessagesMessageStatus
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after_date: Union[Unset, datetime.datetime] = UNSET,
    before_date: Union[Unset, datetime.datetime] = UNSET,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    message_status: Union[Unset, ProgramMessageGetProgramMessagesMessageStatus] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_after_date: Union[Unset, str] = UNSET
    if not isinstance(after_date, Unset):
        json_after_date = after_date.isoformat()
    params["afterDate"] = json_after_date

    json_before_date: Union[Unset, str] = UNSET
    if not isinstance(before_date, Unset):
        json_before_date = before_date.isoformat()
    params["beforeDate"] = json_before_date

    params["enrollment"] = enrollment

    params["event"] = event

    json_message_status: Union[Unset, str] = UNSET
    if not isinstance(message_status, Unset):
        json_message_status = message_status.value

    params["messageStatus"] = json_message_status

    json_ou: Union[Unset, list[str]] = UNSET
    if not isinstance(ou, Unset):
        json_ou = ou

    params["ou"] = json_ou

    params["page"] = page

    params["pageSize"] = page_size

    params["programInstance"] = program_instance

    params["programStageInstance"] = program_stage_instance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[WebMessage, list["ProgramMessage"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProgramMessage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[WebMessage, list["ProgramMessage"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    after_date: Union[Unset, datetime.datetime] = UNSET,
    before_date: Union[Unset, datetime.datetime] = UNSET,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    message_status: Union[Unset, ProgramMessageGetProgramMessagesMessageStatus] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
) -> Response[Union[WebMessage, list["ProgramMessage"]]]:
    """Get program messages matching given query criteria.

    Args:
        after_date (Union[Unset, datetime.datetime]):
        before_date (Union[Unset, datetime.datetime]):
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        message_status (Union[Unset, ProgramMessageGetProgramMessagesMessageStatus]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, list['ProgramMessage']]]
    """

    kwargs = _get_kwargs(
        after_date=after_date,
        before_date=before_date,
        enrollment=enrollment,
        event=event,
        message_status=message_status,
        ou=ou,
        page=page,
        page_size=page_size,
        program_instance=program_instance,
        program_stage_instance=program_stage_instance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    after_date: Union[Unset, datetime.datetime] = UNSET,
    before_date: Union[Unset, datetime.datetime] = UNSET,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    message_status: Union[Unset, ProgramMessageGetProgramMessagesMessageStatus] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
) -> Optional[Union[WebMessage, list["ProgramMessage"]]]:
    """Get program messages matching given query criteria.

    Args:
        after_date (Union[Unset, datetime.datetime]):
        before_date (Union[Unset, datetime.datetime]):
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        message_status (Union[Unset, ProgramMessageGetProgramMessagesMessageStatus]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, list['ProgramMessage']]
    """

    return sync_detailed(
        client=client,
        after_date=after_date,
        before_date=before_date,
        enrollment=enrollment,
        event=event,
        message_status=message_status,
        ou=ou,
        page=page,
        page_size=page_size,
        program_instance=program_instance,
        program_stage_instance=program_stage_instance,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    after_date: Union[Unset, datetime.datetime] = UNSET,
    before_date: Union[Unset, datetime.datetime] = UNSET,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    message_status: Union[Unset, ProgramMessageGetProgramMessagesMessageStatus] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
) -> Response[Union[WebMessage, list["ProgramMessage"]]]:
    """Get program messages matching given query criteria.

    Args:
        after_date (Union[Unset, datetime.datetime]):
        before_date (Union[Unset, datetime.datetime]):
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        message_status (Union[Unset, ProgramMessageGetProgramMessagesMessageStatus]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, list['ProgramMessage']]]
    """

    kwargs = _get_kwargs(
        after_date=after_date,
        before_date=before_date,
        enrollment=enrollment,
        event=event,
        message_status=message_status,
        ou=ou,
        page=page,
        page_size=page_size,
        program_instance=program_instance,
        program_stage_instance=program_stage_instance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    after_date: Union[Unset, datetime.datetime] = UNSET,
    before_date: Union[Unset, datetime.datetime] = UNSET,
    enrollment: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    message_status: Union[Unset, ProgramMessageGetProgramMessagesMessageStatus] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    program_instance: Union[Unset, str] = UNSET,
    program_stage_instance: Union[Unset, str] = UNSET,
) -> Optional[Union[WebMessage, list["ProgramMessage"]]]:
    """Get program messages matching given query criteria.

    Args:
        after_date (Union[Unset, datetime.datetime]):
        before_date (Union[Unset, datetime.datetime]):
        enrollment (Union[Unset, str]):
        event (Union[Unset, str]):
        message_status (Union[Unset, ProgramMessageGetProgramMessagesMessageStatus]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        program_instance (Union[Unset, str]):
        program_stage_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, list['ProgramMessage']]
    """

    return (
        await asyncio_detailed(
            client=client,
            after_date=after_date,
            before_date=before_date,
            enrollment=enrollment,
            event=event,
            message_status=message_status,
            ou=ou,
            page=page,
            page_size=page_size,
            program_instance=program_instance,
            program_stage_instance=program_stage_instance,
        )
    ).parsed
