from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification import Notification
from ...types import Response


def _get_kwargs(
    job_type: str,
    job_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/system/tasks/{job_type}/{job_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Notification"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Notification.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Notification"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_type: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["Notification"]]:
    """[no description yet]

    Args:
        job_type (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Notification']]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_type: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["Notification"]]:
    """[no description yet]

    Args:
        job_type (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Notification']
    """

    return sync_detailed(
        job_type=job_type,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_type: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[list["Notification"]]:
    """[no description yet]

    Args:
        job_type (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Notification']]
    """

    kwargs = _get_kwargs(
        job_type=job_type,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_type: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[list["Notification"]]:
    """[no description yet]

    Args:
        job_type (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Notification']
    """

    return (
        await asyncio_detailed(
            job_type=job_type,
            job_id=job_id,
            client=client,
        )
    ).parsed
