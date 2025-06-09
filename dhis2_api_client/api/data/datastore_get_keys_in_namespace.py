import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    *,
    last_updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_last_updated: Union[Unset, str] = UNSET
    if not isinstance(last_updated, Unset):
        json_last_updated = last_updated.isoformat()
    params["lastUpdated"] = json_last_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dataStore/{namespace}/keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[WebMessage, list[str]]]:
    if response.status_code == 200:
        response_200 = cast(list[str], response.json())

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
) -> Response[Union[WebMessage, list[str]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    last_updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[WebMessage, list[str]]]:
    """List all keys in a specific namespace.

    Args:
        namespace (str):
        last_updated (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, list[str]]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        last_updated=last_updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    last_updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[WebMessage, list[str]]]:
    """List all keys in a specific namespace.

    Args:
        namespace (str):
        last_updated (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, list[str]]
    """

    return sync_detailed(
        namespace=namespace,
        client=client,
        last_updated=last_updated,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    last_updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[WebMessage, list[str]]]:
    """List all keys in a specific namespace.

    Args:
        namespace (str):
        last_updated (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, list[str]]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        last_updated=last_updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    last_updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[WebMessage, list[str]]]:
    """List all keys in a specific namespace.

    Args:
        namespace (str):
        last_updated (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, list[str]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            client=client,
            last_updated=last_updated,
        )
    ).parsed
