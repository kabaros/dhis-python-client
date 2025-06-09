from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_conversation_remove_user_from_message_conversation_response_200 import (
    MessageConversationRemoveUserFromMessageConversationResponse200,
)
from ...types import Response


def _get_kwargs(
    mc_uid: str,
    user_uid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/messageConversations/{mc_uid}/{user_uid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MessageConversationRemoveUserFromMessageConversationResponse200]:
    if response.status_code == 200:
        response_200 = MessageConversationRemoveUserFromMessageConversationResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MessageConversationRemoveUserFromMessageConversationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mc_uid: str,
    user_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MessageConversationRemoveUserFromMessageConversationResponse200]:
    """[no description yet]

    Args:
        mc_uid (str):
        user_uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationRemoveUserFromMessageConversationResponse200]
    """

    kwargs = _get_kwargs(
        mc_uid=mc_uid,
        user_uid=user_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mc_uid: str,
    user_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MessageConversationRemoveUserFromMessageConversationResponse200]:
    """[no description yet]

    Args:
        mc_uid (str):
        user_uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationRemoveUserFromMessageConversationResponse200
    """

    return sync_detailed(
        mc_uid=mc_uid,
        user_uid=user_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    mc_uid: str,
    user_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MessageConversationRemoveUserFromMessageConversationResponse200]:
    """[no description yet]

    Args:
        mc_uid (str):
        user_uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageConversationRemoveUserFromMessageConversationResponse200]
    """

    kwargs = _get_kwargs(
        mc_uid=mc_uid,
        user_uid=user_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mc_uid: str,
    user_uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MessageConversationRemoveUserFromMessageConversationResponse200]:
    """[no description yet]

    Args:
        mc_uid (str):
        user_uid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageConversationRemoveUserFromMessageConversationResponse200
    """

    return (
        await asyncio_detailed(
            mc_uid=mc_uid,
            user_uid=user_uid,
            client=client,
        )
    ).parsed
