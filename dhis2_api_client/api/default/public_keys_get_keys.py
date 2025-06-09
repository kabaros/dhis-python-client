from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.public_keys_get_keys_response_200 import PublicKeysGetKeysResponse200
from ...types import Response


def _get_kwargs(
    client_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/publicKeys/{client_id}/jwks.json",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PublicKeysGetKeysResponse200]:
    if response.status_code == 200:
        response_200 = PublicKeysGetKeysResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PublicKeysGetKeysResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PublicKeysGetKeysResponse200]:
    """[no description yet]

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublicKeysGetKeysResponse200]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PublicKeysGetKeysResponse200]:
    """[no description yet]

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublicKeysGetKeysResponse200
    """

    return sync_detailed(
        client_id=client_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PublicKeysGetKeysResponse200]:
    """[no description yet]

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublicKeysGetKeysResponse200]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    client_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PublicKeysGetKeysResponse200]:
    """[no description yet]

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublicKeysGetKeysResponse200
    """

    return (
        await asyncio_detailed(
            client_id=client_id,
            client=client,
        )
    ).parsed
