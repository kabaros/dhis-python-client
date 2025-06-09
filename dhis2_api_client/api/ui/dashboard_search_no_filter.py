from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_search_no_filter_max_item import DashboardSearchNoFilterMaxItem
from ...models.dashboard_search_result import DashboardSearchResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    count: Union[Unset, int] = UNSET,
    max_: Union[Unset, list[DashboardSearchNoFilterMaxItem]] = UNSET,
    max_count: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["count"] = count

    json_max_: Union[Unset, list[str]] = UNSET
    if not isinstance(max_, Unset):
        json_max_ = []
        for max_item_data in max_:
            max_item = max_item_data.value
            json_max_.append(max_item)

    params["max"] = json_max_

    params["maxCount"] = max_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dashboards/q",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DashboardSearchResult]:
    if response.status_code == 200:
        response_200 = DashboardSearchResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DashboardSearchResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    count: Union[Unset, int] = UNSET,
    max_: Union[Unset, list[DashboardSearchNoFilterMaxItem]] = UNSET,
    max_count: Union[Unset, int] = UNSET,
) -> Response[DashboardSearchResult]:
    """[no description yet]

    Args:
        count (Union[Unset, int]):
        max_ (Union[Unset, list[DashboardSearchNoFilterMaxItem]]):
        max_count (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardSearchResult]
    """

    kwargs = _get_kwargs(
        count=count,
        max_=max_,
        max_count=max_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    count: Union[Unset, int] = UNSET,
    max_: Union[Unset, list[DashboardSearchNoFilterMaxItem]] = UNSET,
    max_count: Union[Unset, int] = UNSET,
) -> Optional[DashboardSearchResult]:
    """[no description yet]

    Args:
        count (Union[Unset, int]):
        max_ (Union[Unset, list[DashboardSearchNoFilterMaxItem]]):
        max_count (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardSearchResult
    """

    return sync_detailed(
        client=client,
        count=count,
        max_=max_,
        max_count=max_count,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    count: Union[Unset, int] = UNSET,
    max_: Union[Unset, list[DashboardSearchNoFilterMaxItem]] = UNSET,
    max_count: Union[Unset, int] = UNSET,
) -> Response[DashboardSearchResult]:
    """[no description yet]

    Args:
        count (Union[Unset, int]):
        max_ (Union[Unset, list[DashboardSearchNoFilterMaxItem]]):
        max_count (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DashboardSearchResult]
    """

    kwargs = _get_kwargs(
        count=count,
        max_=max_,
        max_count=max_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    count: Union[Unset, int] = UNSET,
    max_: Union[Unset, list[DashboardSearchNoFilterMaxItem]] = UNSET,
    max_count: Union[Unset, int] = UNSET,
) -> Optional[DashboardSearchResult]:
    """[no description yet]

    Args:
        count (Union[Unset, int]):
        max_ (Union[Unset, list[DashboardSearchNoFilterMaxItem]]):
        max_count (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DashboardSearchResult
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            max_=max_,
            max_count=max_count,
        )
    ).parsed
