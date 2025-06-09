from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_statistics_save_event_event_type import DataStatisticsSaveEventEventType
from ...types import UNSET, File, FileJsonType, Response, Unset


def _get_kwargs(
    *,
    blank: Union[Unset, bool] = UNSET,
    bytes_: Union[Unset, File] = UNSET,
    empty: Union[Unset, bool] = UNSET,
    event_type: DataStatisticsSaveEventEventType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["blank"] = blank

    json_bytes_: Union[Unset, FileJsonType] = UNSET
    if not isinstance(bytes_, Unset):
        json_bytes_ = bytes_.to_tuple()

    params["bytes"] = json_bytes_

    params["empty"] = empty

    json_event_type = event_type.value
    params["eventType"] = json_event_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dataStatistics/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 201:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    event_type: DataStatisticsSaveEventEventType,
) -> Response[Any]:
    """[no description yet]

    Args:
        blank (Union[Unset, bool]):
        bytes_ (Union[Unset, File]):
        empty (Union[Unset, bool]):
        event_type (DataStatisticsSaveEventEventType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        blank=blank,
        bytes_=bytes_,
        empty=empty,
        event_type=event_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    blank: Union[Unset, bool] = UNSET,
    bytes_: Union[Unset, File] = UNSET,
    empty: Union[Unset, bool] = UNSET,
    event_type: DataStatisticsSaveEventEventType,
) -> Response[Any]:
    """[no description yet]

    Args:
        blank (Union[Unset, bool]):
        bytes_ (Union[Unset, File]):
        empty (Union[Unset, bool]):
        event_type (DataStatisticsSaveEventEventType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        blank=blank,
        bytes_=bytes_,
        empty=empty,
        event_type=event_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
