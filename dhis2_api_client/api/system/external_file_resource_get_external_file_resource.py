from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_resource import FileResource
from ...types import Response


def _get_kwargs(
    access_token: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/externalFileResources/{access_token}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[FileResource]:
    if response.status_code == 200:
        response_200 = FileResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[FileResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    access_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[FileResource]:
    """[no description yet]

    Args:
        access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileResource]
    """

    kwargs = _get_kwargs(
        access_token=access_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    access_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[FileResource]:
    """[no description yet]

    Args:
        access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileResource
    """

    return sync_detailed(
        access_token=access_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    access_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[FileResource]:
    """[no description yet]

    Args:
        access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileResource]
    """

    kwargs = _get_kwargs(
        access_token=access_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    access_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[FileResource]:
    """[no description yet]

    Args:
        access_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileResource
    """

    return (
        await asyncio_detailed(
            access_token=access_token,
            client=client,
        )
    ).parsed
