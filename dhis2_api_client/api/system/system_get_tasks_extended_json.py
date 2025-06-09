from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_get_tasks_extended_json_response_200 import SystemGetTasksExtendedJsonResponse200
from ...types import Response


def _get_kwargs(
    job_type: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/system/tasks/{job_type}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SystemGetTasksExtendedJsonResponse200]:
    if response.status_code == 200:
        response_200 = SystemGetTasksExtendedJsonResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SystemGetTasksExtendedJsonResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SystemGetTasksExtendedJsonResponse200]:
    """[no description yet]

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemGetTasksExtendedJsonResponse200]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SystemGetTasksExtendedJsonResponse200]:
    """[no description yet]

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemGetTasksExtendedJsonResponse200
    """

    return sync_detailed(
        job_type=job_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[SystemGetTasksExtendedJsonResponse200]:
    """[no description yet]

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemGetTasksExtendedJsonResponse200]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_type: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[SystemGetTasksExtendedJsonResponse200]:
    """[no description yet]

    Args:
        job_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemGetTasksExtendedJsonResponse200
    """

    return (
        await asyncio_detailed(
            job_type=job_type,
            client=client,
        )
    ).parsed
