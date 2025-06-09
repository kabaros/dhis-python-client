from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_version import MetadataVersion
from ...models.metadata_version_create_system_version_type import MetadataVersionCreateSystemVersionType
from ...models.web_message import WebMessage
from ...types import UNSET, Response


def _get_kwargs(
    *,
    type_: MetadataVersionCreateSystemVersionType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/metadata/version/create",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[MetadataVersion, WebMessage]]:
    if response.status_code == 200:
        response_200 = MetadataVersion.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[MetadataVersion, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: MetadataVersionCreateSystemVersionType,
) -> Response[Union[MetadataVersion, WebMessage]]:
    """[no description yet]

    Args:
        type_ (MetadataVersionCreateSystemVersionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MetadataVersion, WebMessage]]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: MetadataVersionCreateSystemVersionType,
) -> Optional[Union[MetadataVersion, WebMessage]]:
    """[no description yet]

    Args:
        type_ (MetadataVersionCreateSystemVersionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MetadataVersion, WebMessage]
    """

    return sync_detailed(
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: MetadataVersionCreateSystemVersionType,
) -> Response[Union[MetadataVersion, WebMessage]]:
    """[no description yet]

    Args:
        type_ (MetadataVersionCreateSystemVersionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MetadataVersion, WebMessage]]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: MetadataVersionCreateSystemVersionType,
) -> Optional[Union[MetadataVersion, WebMessage]]:
    """[no description yet]

    Args:
        type_ (MetadataVersionCreateSystemVersionType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MetadataVersion, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
        )
    ).parsed
