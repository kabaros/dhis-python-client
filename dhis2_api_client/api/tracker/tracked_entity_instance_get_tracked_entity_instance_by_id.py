from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tracked_entity_instance_get_tracked_entity_instance_by_id_response_200 import (
    TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    program: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["program"] = program

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/trackedEntityInstances/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]:
    if response.status_code == 200:
        response_200 = TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]:
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
    program: Union[Unset, str] = UNSET,
) -> Response[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]:
    """[no description yet]

    Args:
        id (str):
        program (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        program=program,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    program: Union[Unset, str] = UNSET,
) -> Optional[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]:
    """[no description yet]

    Args:
        id (str):
        program (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        program=program,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    program: Union[Unset, str] = UNSET,
) -> Response[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]:
    """[no description yet]

    Args:
        id (str):
        program (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        program=program,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    program: Union[Unset, str] = UNSET,
) -> Optional[TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200]:
    """[no description yet]

    Args:
        id (str):
        program (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrackedEntityInstanceGetTrackedEntityInstanceByIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            program=program,
        )
    ).parsed
