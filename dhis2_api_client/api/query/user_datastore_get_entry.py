from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    key: str,
    *,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/userDataStore/{namespace}/{key}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[WebMessage, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[WebMessage, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    namespace: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        key=key,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespace: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return sync_detailed(
        namespace=namespace,
        key=key,
        client=client,
        username=username,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        key=key,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            key=key,
            client=client,
            username=username,
        )
    ).parsed
