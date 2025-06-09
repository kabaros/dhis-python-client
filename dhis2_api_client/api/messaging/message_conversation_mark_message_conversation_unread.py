from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_conversation_mark_message_conversation_unread_response_200 import (
    MessageConversationMarkMessageConversationUnreadResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    user_uid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userUid"] = user_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/messageConversations/{uid}/unread",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MessageConversationMarkMessageConversationUnreadResponse200]:
    if response.status_code == 200:
        response_200 = MessageConversationMarkMessageConversationUnreadResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MessageConversationMarkMessageConversationUnreadResponse200]:
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
    user_uid: Union[Unset, str] = UNSET,
) -> Response[MessageConversationMarkMessageConversationUnreadResponse200]:
    """[no description yet]

    Args:
        uid (str):
        user_uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationMarkMessageConversationUnreadResponse200]
    """

    kwargs = _get_kwargs(
        uid=uid,
        user_uid=user_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    user_uid: Union[Unset, str] = UNSET,
) -> Optional[MessageConversationMarkMessageConversationUnreadResponse200]:
    """[no description yet]

    Args:
        uid (str):
        user_uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationMarkMessageConversationUnreadResponse200
    """

    return sync_detailed(
        uid=uid,
        client=client,
        user_uid=user_uid,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    user_uid: Union[Unset, str] = UNSET,
) -> Response[MessageConversationMarkMessageConversationUnreadResponse200]:
    """[no description yet]

    Args:
        uid (str):
        user_uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationMarkMessageConversationUnreadResponse200]
    """

    kwargs = _get_kwargs(
        uid=uid,
        user_uid=user_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    user_uid: Union[Unset, str] = UNSET,
) -> Optional[MessageConversationMarkMessageConversationUnreadResponse200]:
    """[no description yet]

    Args:
        uid (str):
        user_uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationMarkMessageConversationUnreadResponse200
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            user_uid=user_uid,
        )
    ).parsed
