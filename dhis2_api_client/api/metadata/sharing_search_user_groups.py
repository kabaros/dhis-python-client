from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sharing_search_user_groups_response_200 import SharingSearchUserGroupsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key: str,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["key"] = key

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sharing/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SharingSearchUserGroupsResponse200]:
    if response.status_code == 200:
        response_200 = SharingSearchUserGroupsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SharingSearchUserGroupsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key: str,
    page_size: Union[Unset, int] = UNSET,
) -> Response[SharingSearchUserGroupsResponse200]:
    """[no description yet]

    Args:
        key (str):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharingSearchUserGroupsResponse200]
    """

    kwargs = _get_kwargs(
        key=key,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    key: str,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[SharingSearchUserGroupsResponse200]:
    """[no description yet]

    Args:
        key (str):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharingSearchUserGroupsResponse200
    """

    return sync_detailed(
        client=client,
        key=key,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    key: str,
    page_size: Union[Unset, int] = UNSET,
) -> Response[SharingSearchUserGroupsResponse200]:
    """[no description yet]

    Args:
        key (str):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SharingSearchUserGroupsResponse200]
    """

    kwargs = _get_kwargs(
        key=key,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    key: str,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[SharingSearchUserGroupsResponse200]:
    """[no description yet]

    Args:
        key (str):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SharingSearchUserGroupsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            key=key,
            page_size=page_size,
        )
    ).parsed
