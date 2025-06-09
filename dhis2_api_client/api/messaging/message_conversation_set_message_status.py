from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_conversation_set_message_status_message_conversation_status import (
    MessageConversationSetMessageStatusMessageConversationStatus,
)
from ...models.message_conversation_set_message_status_response_200 import (
    MessageConversationSetMessageStatusResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    uid: str,
    *,
    message_conversation_status: MessageConversationSetMessageStatusMessageConversationStatus,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_message_conversation_status = message_conversation_status.value
    params["messageConversationStatus"] = json_message_conversation_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/messageConversations/{uid}/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MessageConversationSetMessageStatusResponse200]:
    if response.status_code == 200:
        response_200 = MessageConversationSetMessageStatusResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MessageConversationSetMessageStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    message_conversation_status: MessageConversationSetMessageStatusMessageConversationStatus,
) -> Response[MessageConversationSetMessageStatusResponse200]:
    """[no description yet]

    Args:
        uid (str):
        message_conversation_status
            (MessageConversationSetMessageStatusMessageConversationStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationSetMessageStatusResponse200]
    """

    kwargs = _get_kwargs(
        uid=uid,
        message_conversation_status=message_conversation_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    message_conversation_status: MessageConversationSetMessageStatusMessageConversationStatus,
) -> Optional[MessageConversationSetMessageStatusResponse200]:
    """[no description yet]

    Args:
        uid (str):
        message_conversation_status
            (MessageConversationSetMessageStatusMessageConversationStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationSetMessageStatusResponse200
    """

    return sync_detailed(
        uid=uid,
        client=client,
        message_conversation_status=message_conversation_status,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    message_conversation_status: MessageConversationSetMessageStatusMessageConversationStatus,
) -> Response[MessageConversationSetMessageStatusResponse200]:
    """[no description yet]

    Args:
        uid (str):
        message_conversation_status
            (MessageConversationSetMessageStatusMessageConversationStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationSetMessageStatusResponse200]
    """

    kwargs = _get_kwargs(
        uid=uid,
        message_conversation_status=message_conversation_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    message_conversation_status: MessageConversationSetMessageStatusMessageConversationStatus,
) -> Optional[MessageConversationSetMessageStatusResponse200]:
    """[no description yet]

    Args:
        uid (str):
        message_conversation_status
            (MessageConversationSetMessageStatusMessageConversationStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationSetMessageStatusResponse200
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            message_conversation_status=message_conversation_status,
        )
    ).parsed
