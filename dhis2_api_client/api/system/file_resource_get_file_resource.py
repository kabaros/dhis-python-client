from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_resource import FileResource
from ...models.file_resource_get_file_resource_dimension import FileResourceGetFileResourceDimension
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    dimension: Union[Unset, FileResourceGetFileResourceDimension] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_dimension: Union[Unset, str] = UNSET
    if not isinstance(dimension, Unset):
        json_dimension = dimension.value

    params["dimension"] = json_dimension

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/fileResources/{uid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FileResource, WebMessage]]:
    if response.status_code == 200:
        response_200 = FileResource.from_dict(response.json())

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
) -> Response[Union[FileResource, WebMessage]]:
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
    dimension: Union[Unset, FileResourceGetFileResourceDimension] = UNSET,
) -> Response[Union[FileResource, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        dimension (Union[Unset, FileResourceGetFileResourceDimension]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResource, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        dimension=dimension,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, FileResourceGetFileResourceDimension] = UNSET,
) -> Optional[Union[FileResource, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        dimension (Union[Unset, FileResourceGetFileResourceDimension]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileResource, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        client=client,
        dimension=dimension,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, FileResourceGetFileResourceDimension] = UNSET,
) -> Response[Union[FileResource, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        dimension (Union[Unset, FileResourceGetFileResourceDimension]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileResource, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        dimension=dimension,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, FileResourceGetFileResourceDimension] = UNSET,
) -> Optional[Union[FileResource, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        dimension (Union[Unset, FileResourceGetFileResourceDimension]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileResource, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            dimension=dimension,
        )
    ).parsed
