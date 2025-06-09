from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_account_register_user_response_201 import UserAccountRegisterUserResponse201
from ...models.user_registration_params import UserRegistrationParams
from ...models.web_message import WebMessage
from ...types import Response


def _get_kwargs(
    *,
    body: UserRegistrationParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/registration",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[UserAccountRegisterUserResponse201, WebMessage]]:
    if response.status_code == 201:
        response_201 = UserAccountRegisterUserResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[UserAccountRegisterUserResponse201, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserRegistrationParams,
) -> Response[Union[UserAccountRegisterUserResponse201, WebMessage]]:
    """[no description yet]

    Args:
        body (UserRegistrationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UserAccountRegisterUserResponse201, WebMessage]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserRegistrationParams,
) -> Optional[Union[UserAccountRegisterUserResponse201, WebMessage]]:
    """[no description yet]

    Args:
        body (UserRegistrationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UserAccountRegisterUserResponse201, WebMessage]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserRegistrationParams,
) -> Response[Union[UserAccountRegisterUserResponse201, WebMessage]]:
    """[no description yet]

    Args:
        body (UserRegistrationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UserAccountRegisterUserResponse201, WebMessage]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UserRegistrationParams,
) -> Optional[Union[UserAccountRegisterUserResponse201, WebMessage]]:
    """[no description yet]

    Args:
        body (UserRegistrationParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UserAccountRegisterUserResponse201, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
