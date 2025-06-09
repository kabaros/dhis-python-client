from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_conversation_mark_message_conversations_read_response_200 import (
    MessageConversationMarkMessageConversationsReadResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[str],
    user: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["user"] = user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messageConversations/read",
        "params": params,
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MessageConversationMarkMessageConversationsReadResponse200]:
    if response.status_code == 200:
        response_200 = MessageConversationMarkMessageConversationsReadResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MessageConversationMarkMessageConversationsReadResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    user: Union[Unset, str] = UNSET,
) -> Response[MessageConversationMarkMessageConversationsReadResponse200]:
    """[no description yet]

    Args:
        user (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationMarkMessageConversationsReadResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        user=user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    user: Union[Unset, str] = UNSET,
) -> Optional[MessageConversationMarkMessageConversationsReadResponse200]:
    """[no description yet]

    Args:
        user (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationMarkMessageConversationsReadResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
        user=user,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    user: Union[Unset, str] = UNSET,
) -> Response[MessageConversationMarkMessageConversationsReadResponse200]:
    """[no description yet]

    Args:
        user (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationMarkMessageConversationsReadResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
        user=user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: list[str],
    user: Union[Unset, str] = UNSET,
) -> Optional[MessageConversationMarkMessageConversationsReadResponse200]:
    """[no description yet]

    Args:
        user (Union[Unset, str]):
        body (list[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationMarkMessageConversationsReadResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            user=user,
        )
    ).parsed
