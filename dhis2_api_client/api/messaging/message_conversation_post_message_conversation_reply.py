from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    body: str,
    attachments: Union[Unset, list[str]] = UNSET,
    internal: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_attachments: Union[Unset, list[str]] = UNSET
    if not isinstance(attachments, Unset):
        json_attachments = attachments

    params["attachments"] = json_attachments

    params["internal"] = internal

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/messageConversations/{uid}",
        "params": params,
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebMessage]:
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
    body: str,
    attachments: Union[Unset, list[str]] = UNSET,
    internal: Union[Unset, bool] = False,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attachments (Union[Unset, list[str]]):
        internal (Union[Unset, bool]):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
        attachments=attachments,
        internal=internal,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    attachments: Union[Unset, list[str]] = UNSET,
    internal: Union[Unset, bool] = False,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attachments (Union[Unset, list[str]]):
        internal (Union[Unset, bool]):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        uid=uid,
        client=client,
        body=body,
        attachments=attachments,
        internal=internal,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    attachments: Union[Unset, list[str]] = UNSET,
    internal: Union[Unset, bool] = False,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attachments (Union[Unset, list[str]]):
        internal (Union[Unset, bool]):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
        attachments=attachments,
        internal=internal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    attachments: Union[Unset, list[str]] = UNSET,
    internal: Union[Unset, bool] = False,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attachments (Union[Unset, list[str]]):
        internal (Union[Unset, bool]):  Default: False.
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            body=body,
            attachments=attachments,
            internal=internal,
        )
    ).parsed
