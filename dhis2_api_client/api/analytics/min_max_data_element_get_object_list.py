from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.min_max_data_element_get_object_list_response_200 import MinMaxDataElementGetObjectListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filters: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_filters: Union[Unset, list[str]] = UNSET
    if not isinstance(filters, Unset):
        json_filters = filters

    params["filters"] = json_filters

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["skipPaging"] = skip_paging

    params["total"] = total

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/minMaxDataElements/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MinMaxDataElementGetObjectListResponse200]:
    if response.status_code == 200:
        response_200 = MinMaxDataElementGetObjectListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MinMaxDataElementGetObjectListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
) -> Response[MinMaxDataElementGetObjectListResponse200]:
    """[no description yet]

    Args:
        filters (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MinMaxDataElementGetObjectListResponse200]
    """

    kwargs = _get_kwargs(
        filters=filters,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
) -> Optional[MinMaxDataElementGetObjectListResponse200]:
    """[no description yet]

    Args:
        filters (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MinMaxDataElementGetObjectListResponse200
    """

    return sync_detailed(
        client=client,
        filters=filters,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
) -> Response[MinMaxDataElementGetObjectListResponse200]:
    """[no description yet]

    Args:
        filters (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MinMaxDataElementGetObjectListResponse200]
    """

    kwargs = _get_kwargs(
        filters=filters,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    filters: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
) -> Optional[MinMaxDataElementGetObjectListResponse200]:
    """[no description yet]

    Args:
        filters (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MinMaxDataElementGetObjectListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
            page=page,
            page_size=page_size,
            paging=paging,
            skip_paging=skip_paging,
            total=total,
        )
    ).parsed
