from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    criteria: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    var: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_criteria: Union[Unset, list[str]] = UNSET
    if not isinstance(criteria, Unset):
        json_criteria = criteria

    params["criteria"] = json_criteria

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["skipPaging"] = skip_paging

    params["total"] = total

    json_var: Union[Unset, list[str]] = UNSET
    if not isinstance(var, Unset):
        json_var = var

    params["var"] = json_var

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sqlViews/{uid}/data.xml",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WebMessage]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    criteria: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    var: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        criteria (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        var (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        criteria=criteria,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
        var=var,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    criteria: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    var: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        criteria (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        var (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        client=client,
        criteria=criteria,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
        var=var,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    criteria: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    var: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        criteria (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        var (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        criteria=criteria,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
        var=var,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    criteria: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    var: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        criteria (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        var (Union[Unset, list[str]]):

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
            criteria=criteria,
            page=page,
            page_size=page_size,
            paging=paging,
            skip_paging=skip_paging,
            total=total,
            var=var,
        )
    ).parsed
