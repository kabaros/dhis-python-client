from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, File, FileJsonType, Response, Unset


def _get_kwargs(
    *,
    blank: Union[Unset, bool] = UNSET,
    bytes_: Union[Unset, File] = UNSET,
    empty: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["blank"] = blank

    json_bytes_: Union[Unset, FileJsonType] = UNSET
    if not isinstance(bytes_, Unset):
        json_bytes_ = bytes_.to_tuple()

    params["bytes"] = json_bytes_

    params["empty"] = empty

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/routes/addCollectionItem__disabled",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if response.status_code == 405:
        response_405 = WebMessage.from_dict(response.json())

        return response_405
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
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
    blank: Union[Unset, bool] = UNSET,
    bytes_: Union[Unset, File] = UNSET,
    empty: Union[Unset, bool] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        blank (Union[Unset, bool]):
        bytes_ (Union[Unset, File]):
        empty (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        blank=blank,
        bytes_=bytes_,
        empty=empty,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    blank: Union[Unset, bool] = UNSET,
    bytes_: Union[Unset, File] = UNSET,
    empty: Union[Unset, bool] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        blank (Union[Unset, bool]):
        bytes_ (Union[Unset, File]):
        empty (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        blank=blank,
        bytes_=bytes_,
        empty=empty,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    blank: Union[Unset, bool] = UNSET,
    bytes_: Union[Unset, File] = UNSET,
    empty: Union[Unset, bool] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        blank (Union[Unset, bool]):
        bytes_ (Union[Unset, File]):
        empty (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        blank=blank,
        bytes_=bytes_,
        empty=empty,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    blank: Union[Unset, bool] = UNSET,
    bytes_: Union[Unset, File] = UNSET,
    empty: Union[Unset, bool] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        blank (Union[Unset, bool]):
        bytes_ (Union[Unset, File]):
        empty (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            blank=blank,
            bytes_=bytes_,
            empty=empty,
        )
    ).parsed
