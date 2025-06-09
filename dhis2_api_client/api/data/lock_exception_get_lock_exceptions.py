from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lock_exception_get_lock_exceptions_response_200 import LockExceptionGetLockExceptionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["key"] = key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lockExceptions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LockExceptionGetLockExceptionsResponse200]:
    if response.status_code == 200:
        response_200 = LockExceptionGetLockExceptionsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LockExceptionGetLockExceptionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, str] = UNSET,
) -> Response[LockExceptionGetLockExceptionsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LockExceptionGetLockExceptionsResponse200]
    """

    kwargs = _get_kwargs(
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, str] = UNSET,
) -> Optional[LockExceptionGetLockExceptionsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LockExceptionGetLockExceptionsResponse200
    """

    return sync_detailed(
        client=client,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, str] = UNSET,
) -> Response[LockExceptionGetLockExceptionsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LockExceptionGetLockExceptionsResponse200]
    """

    kwargs = _get_kwargs(
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, str] = UNSET,
) -> Optional[LockExceptionGetLockExceptionsResponse200]:
    """[no description yet]

    Args:
        key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LockExceptionGetLockExceptionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            key=key,
        )
    ).parsed
