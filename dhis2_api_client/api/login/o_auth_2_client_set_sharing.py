from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sharing import Sharing
from ...models.web_message import WebMessage
from ...types import Response


def _get_kwargs(
    uid: str,
    *,
    body: Sharing,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/oAuth2Clients/{uid}/sharing",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WebMessage]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Sharing,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OAuth2Client object
            (Java name `org.hisp.dhis.security.oauth2.OAuth2Client`) Example: ts8HI7xp6I4.
        body (Sharing):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Sharing,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OAuth2Client object
            (Java name `org.hisp.dhis.security.oauth2.OAuth2Client`) Example: ts8HI7xp6I4.
        body (Sharing):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Sharing,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OAuth2Client object
            (Java name `org.hisp.dhis.security.oauth2.OAuth2Client`) Example: ts8HI7xp6I4.
        body (Sharing):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Sharing,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OAuth2Client object
            (Java name `org.hisp.dhis.security.oauth2.OAuth2Client`) Example: ts8HI7xp6I4.
        body (Sharing):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            body=body,
        )
    ).parsed
