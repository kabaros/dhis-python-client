from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_resource_owner import FileResourceOwner
from ...types import UNSET, Response


def _get_kwargs(
    *,
    storage_key: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["storageKey"] = storage_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fileResources/owners",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["FileResourceOwner"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FileResourceOwner.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["FileResourceOwner"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    storage_key: str,
) -> Response[list["FileResourceOwner"]]:
    """[no description yet]

    Args:
        storage_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FileResourceOwner']]
    """

    kwargs = _get_kwargs(
        storage_key=storage_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    storage_key: str,
) -> Optional[list["FileResourceOwner"]]:
    """[no description yet]

    Args:
        storage_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FileResourceOwner']
    """

    return sync_detailed(
        client=client,
        storage_key=storage_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    storage_key: str,
) -> Response[list["FileResourceOwner"]]:
    """[no description yet]

    Args:
        storage_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FileResourceOwner']]
    """

    kwargs = _get_kwargs(
        storage_key=storage_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    storage_key: str,
) -> Optional[list["FileResourceOwner"]]:
    """[no description yet]

    Args:
        storage_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FileResourceOwner']
    """

    return (
        await asyncio_detailed(
            client=client,
            storage_key=storage_key,
        )
    ).parsed
