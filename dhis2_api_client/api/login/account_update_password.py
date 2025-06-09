from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_update_password_response_200 import AccountUpdatePasswordResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    old_password: str,
    password: str,
    username: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["oldPassword"] = old_password

    params["password"] = password

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/password",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AccountUpdatePasswordResponse200]:
    if response.status_code == 200:
        response_200 = AccountUpdatePasswordResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AccountUpdatePasswordResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    old_password: str,
    password: str,
    username: str,
) -> Response[AccountUpdatePasswordResponse200]:
    """[no description yet]

    Args:
        old_password (str):
        password (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUpdatePasswordResponse200]
    """

    kwargs = _get_kwargs(
        old_password=old_password,
        password=password,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    old_password: str,
    password: str,
    username: str,
) -> Optional[AccountUpdatePasswordResponse200]:
    """[no description yet]

    Args:
        old_password (str):
        password (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUpdatePasswordResponse200
    """

    return sync_detailed(
        client=client,
        old_password=old_password,
        password=password,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    old_password: str,
    password: str,
    username: str,
) -> Response[AccountUpdatePasswordResponse200]:
    """[no description yet]

    Args:
        old_password (str):
        password (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountUpdatePasswordResponse200]
    """

    kwargs = _get_kwargs(
        old_password=old_password,
        password=password,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    old_password: str,
    password: str,
    username: str,
) -> Optional[AccountUpdatePasswordResponse200]:
    """[no description yet]

    Args:
        old_password (str):
        password (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountUpdatePasswordResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            old_password=old_password,
            password=password,
            username=username,
        )
    ).parsed
