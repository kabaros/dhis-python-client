from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.datastore_entry import DatastoreEntry
from ...models.web_message import WebMessage
from ...types import Response


def _get_kwargs(
    namespace: str,
    key: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dataStore/{namespace}/{key}/metaData",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DatastoreEntry, WebMessage]]:
    if response.status_code == 200:
        response_200 = DatastoreEntry.from_dict(response.json())

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
) -> Response[Union[DatastoreEntry, WebMessage]]:
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
) -> Response[Union[DatastoreEntry, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatastoreEntry, WebMessage]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        key=key,
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
) -> Optional[Union[DatastoreEntry, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatastoreEntry, WebMessage]
    """

    return sync_detailed(
        namespace=namespace,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DatastoreEntry, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DatastoreEntry, WebMessage]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace: str,
    key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DatastoreEntry, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DatastoreEntry, WebMessage]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            key=key,
            client=client,
        )
    ).parsed
