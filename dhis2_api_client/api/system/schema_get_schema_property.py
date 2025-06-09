from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.property_ import Property
from ...models.web_message import WebMessage
from ...types import Response


def _get_kwargs(
    type_: str,
    property_: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/schemas/{type_}/{property_}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Property, WebMessage]]:
    if response.status_code == 200:
        response_200 = Property.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Property, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type_: str,
    property_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Property, WebMessage]]:
    """[no description yet]

    Args:
        type_ (str):
        property_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Property, WebMessage]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        property_=property_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type_: str,
    property_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Property, WebMessage]]:
    """[no description yet]

    Args:
        type_ (str):
        property_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Property, WebMessage]
    """

    return sync_detailed(
        type_=type_,
        property_=property_,
        client=client,
    ).parsed


async def asyncio_detailed(
    type_: str,
    property_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Property, WebMessage]]:
    """[no description yet]

    Args:
        type_ (str):
        property_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Property, WebMessage]]
    """

    kwargs = _get_kwargs(
        type_=type_,
        property_=property_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type_: str,
    property_: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Property, WebMessage]]:
    """[no description yet]

    Args:
        type_ (str):
        property_ (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Property, WebMessage]
    """

    return (
        await asyncio_detailed(
            type_=type_,
            property_=property_,
            client=client,
        )
    ).parsed
