from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_statistics_get_top_favorites_event_type import DataStatisticsGetTopFavoritesEventType
from ...models.data_statistics_get_top_favorites_sort_order import DataStatisticsGetTopFavoritesSortOrder
from ...models.favorite_statistics import FavoriteStatistics
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    event_type: DataStatisticsGetTopFavoritesEventType,
    page_size: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, DataStatisticsGetTopFavoritesSortOrder] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_event_type = event_type.value
    params["eventType"] = json_event_type

    params["pageSize"] = page_size

    json_sort_order: Union[Unset, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataStatistics/favorites",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["FavoriteStatistics"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FavoriteStatistics.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["FavoriteStatistics"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: DataStatisticsGetTopFavoritesEventType,
    page_size: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, DataStatisticsGetTopFavoritesSortOrder] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["FavoriteStatistics"]]:
    """[no description yet]

    Args:
        event_type (DataStatisticsGetTopFavoritesEventType):
        page_size (Union[Unset, int]):
        sort_order (Union[Unset, DataStatisticsGetTopFavoritesSortOrder]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FavoriteStatistics']]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        page_size=page_size,
        sort_order=sort_order,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: DataStatisticsGetTopFavoritesEventType,
    page_size: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, DataStatisticsGetTopFavoritesSortOrder] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["FavoriteStatistics"]]:
    """[no description yet]

    Args:
        event_type (DataStatisticsGetTopFavoritesEventType):
        page_size (Union[Unset, int]):
        sort_order (Union[Unset, DataStatisticsGetTopFavoritesSortOrder]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FavoriteStatistics']
    """

    return sync_detailed(
        client=client,
        event_type=event_type,
        page_size=page_size,
        sort_order=sort_order,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: DataStatisticsGetTopFavoritesEventType,
    page_size: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, DataStatisticsGetTopFavoritesSortOrder] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[list["FavoriteStatistics"]]:
    """[no description yet]

    Args:
        event_type (DataStatisticsGetTopFavoritesEventType):
        page_size (Union[Unset, int]):
        sort_order (Union[Unset, DataStatisticsGetTopFavoritesSortOrder]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FavoriteStatistics']]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        page_size=page_size,
        sort_order=sort_order,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    event_type: DataStatisticsGetTopFavoritesEventType,
    page_size: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, DataStatisticsGetTopFavoritesSortOrder] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[list["FavoriteStatistics"]]:
    """[no description yet]

    Args:
        event_type (DataStatisticsGetTopFavoritesEventType):
        page_size (Union[Unset, int]):
        sort_order (Union[Unset, DataStatisticsGetTopFavoritesSortOrder]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FavoriteStatistics']
    """

    return (
        await asyncio_detailed(
            client=client,
            event_type=event_type,
            page_size=page_size,
            sort_order=sort_order,
            username=username,
        )
    ).parsed
