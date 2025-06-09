from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email: str,
    first_name: str,
    g_recaptcha_response: Union[Unset, str] = UNSET,
    invite_token: Union[Unset, str] = UNSET,
    invite_username: Union[Unset, str] = UNSET,
    password: str,
    phone_number: str,
    surname: str,
    username: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["email"] = email

    params["firstName"] = first_name

    params["g-recaptcha-response"] = g_recaptcha_response

    params["inviteToken"] = invite_token

    params["inviteUsername"] = invite_username

    params["password"] = password

    params["phoneNumber"] = phone_number

    params["surname"] = surname

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/account/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    email: str,
    first_name: str,
    g_recaptcha_response: Union[Unset, str] = UNSET,
    invite_token: Union[Unset, str] = UNSET,
    invite_username: Union[Unset, str] = UNSET,
    password: str,
    phone_number: str,
    surname: str,
    username: str,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        email (str):
        first_name (str):
        g_recaptcha_response (Union[Unset, str]):
        invite_token (Union[Unset, str]):
        invite_username (Union[Unset, str]):
        password (str):
        phone_number (str):
        surname (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        email=email,
        first_name=first_name,
        g_recaptcha_response=g_recaptcha_response,
        invite_token=invite_token,
        invite_username=invite_username,
        password=password,
        phone_number=phone_number,
        surname=surname,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    email: str,
    first_name: str,
    g_recaptcha_response: Union[Unset, str] = UNSET,
    invite_token: Union[Unset, str] = UNSET,
    invite_username: Union[Unset, str] = UNSET,
    password: str,
    phone_number: str,
    surname: str,
    username: str,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        email (str):
        first_name (str):
        g_recaptcha_response (Union[Unset, str]):
        invite_token (Union[Unset, str]):
        invite_username (Union[Unset, str]):
        password (str):
        phone_number (str):
        surname (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        email=email,
        first_name=first_name,
        g_recaptcha_response=g_recaptcha_response,
        invite_token=invite_token,
        invite_username=invite_username,
        password=password,
        phone_number=phone_number,
        surname=surname,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    email: str,
    first_name: str,
    g_recaptcha_response: Union[Unset, str] = UNSET,
    invite_token: Union[Unset, str] = UNSET,
    invite_username: Union[Unset, str] = UNSET,
    password: str,
    phone_number: str,
    surname: str,
    username: str,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        email (str):
        first_name (str):
        g_recaptcha_response (Union[Unset, str]):
        invite_token (Union[Unset, str]):
        invite_username (Union[Unset, str]):
        password (str):
        phone_number (str):
        surname (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        email=email,
        first_name=first_name,
        g_recaptcha_response=g_recaptcha_response,
        invite_token=invite_token,
        invite_username=invite_username,
        password=password,
        phone_number=phone_number,
        surname=surname,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    email: str,
    first_name: str,
    g_recaptcha_response: Union[Unset, str] = UNSET,
    invite_token: Union[Unset, str] = UNSET,
    invite_username: Union[Unset, str] = UNSET,
    password: str,
    phone_number: str,
    surname: str,
    username: str,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        email (str):
        first_name (str):
        g_recaptcha_response (Union[Unset, str]):
        invite_token (Union[Unset, str]):
        invite_username (Union[Unset, str]):
        password (str):
        phone_number (str):
        surname (str):
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            first_name=first_name,
            g_recaptcha_response=g_recaptcha_response,
            invite_token=invite_token,
            invite_username=invite_username,
            password=password,
            phone_number=phone_number,
            surname=surname,
            username=username,
        )
    ).parsed
