import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deleted_object import DeletedObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    code: Union[Unset, list[str]] = UNSET,
    deleted_at: Union[Unset, datetime.datetime] = UNSET,
    klass: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    uid: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_code: Union[Unset, list[str]] = UNSET
    if not isinstance(code, Unset):
        json_code = code

    params["code"] = json_code

    json_deleted_at: Union[Unset, str] = UNSET
    if not isinstance(deleted_at, Unset):
        json_deleted_at = deleted_at.isoformat()
    params["deletedAt"] = json_deleted_at

    json_klass: Union[Unset, list[str]] = UNSET
    if not isinstance(klass, Unset):
        json_klass = klass

    params["klass"] = json_klass

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["skipPaging"] = skip_paging

    params["total"] = total

    json_uid: Union[Unset, list[str]] = UNSET
    if not isinstance(uid, Unset):
        json_uid = uid

    params["uid"] = json_uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deletedObjects/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["DeletedObject"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DeletedObject.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["DeletedObject"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, list[str]] = UNSET,
    deleted_at: Union[Unset, datetime.datetime] = UNSET,
    klass: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    uid: Union[Unset, list[str]] = UNSET,
) -> Response[list["DeletedObject"]]:
    """[no description yet]

    Args:
        code (Union[Unset, list[str]]):
        deleted_at (Union[Unset, datetime.datetime]):
        klass (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        uid (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DeletedObject']]
    """

    kwargs = _get_kwargs(
        code=code,
        deleted_at=deleted_at,
        klass=klass,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
        uid=uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, list[str]] = UNSET,
    deleted_at: Union[Unset, datetime.datetime] = UNSET,
    klass: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    uid: Union[Unset, list[str]] = UNSET,
) -> Optional[list["DeletedObject"]]:
    """[no description yet]

    Args:
        code (Union[Unset, list[str]]):
        deleted_at (Union[Unset, datetime.datetime]):
        klass (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        uid (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DeletedObject']
    """

    return sync_detailed(
        client=client,
        code=code,
        deleted_at=deleted_at,
        klass=klass,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
        uid=uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, list[str]] = UNSET,
    deleted_at: Union[Unset, datetime.datetime] = UNSET,
    klass: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    uid: Union[Unset, list[str]] = UNSET,
) -> Response[list["DeletedObject"]]:
    """[no description yet]

    Args:
        code (Union[Unset, list[str]]):
        deleted_at (Union[Unset, datetime.datetime]):
        klass (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        uid (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DeletedObject']]
    """

    kwargs = _get_kwargs(
        code=code,
        deleted_at=deleted_at,
        klass=klass,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        total=total,
        uid=uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, list[str]] = UNSET,
    deleted_at: Union[Unset, datetime.datetime] = UNSET,
    klass: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    uid: Union[Unset, list[str]] = UNSET,
) -> Optional[list["DeletedObject"]]:
    """[no description yet]

    Args:
        code (Union[Unset, list[str]]):
        deleted_at (Union[Unset, datetime.datetime]):
        klass (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        uid (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DeletedObject']
    """

    return (
        await asyncio_detailed(
            client=client,
            code=code,
            deleted_at=deleted_at,
            klass=klass,
            page=page,
            page_size=page_size,
            paging=paging,
            skip_paging=skip_paging,
            total=total,
            uid=uid,
        )
    ).parsed
