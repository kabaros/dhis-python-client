from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deduplication_update_potential_duplicate_status import DeduplicationUpdatePotentialDuplicateStatus
from ...models.web_message import WebMessage
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    status: DeduplicationUpdatePotentialDuplicateStatus,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status = status.value
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/potentialDuplicates/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WebMessage]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: DeduplicationUpdatePotentialDuplicateStatus,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        id (str):
        status (DeduplicationUpdatePotentialDuplicateStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: DeduplicationUpdatePotentialDuplicateStatus,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        id (str):
        status (DeduplicationUpdatePotentialDuplicateStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return sync_detailed(
        id=id,
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: DeduplicationUpdatePotentialDuplicateStatus,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        id (str):
        status (DeduplicationUpdatePotentialDuplicateStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: DeduplicationUpdatePotentialDuplicateStatus,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        id (str):
        status (DeduplicationUpdatePotentialDuplicateStatus):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            status=status,
        )
    ).parsed
