from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key: str,
    *,
    body: str,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["user"] = user

    params["userId"] = user_id

    params["value"] = value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/userSettings/{key}",
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
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        key (str):
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        value (Union[Unset, str]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        key=key,
        body=body,
        user=user,
        user_id=user_id,
        value=value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        key (str):
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        value (Union[Unset, str]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        key=key,
        client=client,
        body=body,
        user=user,
        user_id=user_id,
        value=value,
    ).parsed


async def asyncio_detailed(
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        key (str):
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        value (Union[Unset, str]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        key=key,
        body=body,
        user=user,
        user_id=user_id,
        value=value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: str,
    user: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        key (str):
        user (Union[Unset, str]):
        user_id (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        value (Union[Unset, str]):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            key=key,
            client=client,
            body=body,
            user=user,
            user_id=user_id,
            value=value,
        )
    ).parsed
