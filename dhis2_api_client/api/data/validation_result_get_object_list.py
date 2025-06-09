import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validation_result_get_object_list_response_200 import ValidationResultGetObjectListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    vr: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created_date: Union[Unset, str] = UNSET
    if not isinstance(created_date, Unset):
        json_created_date = created_date.isoformat()
    params["createdDate"] = json_created_date

    json_ou: Union[Unset, list[str]] = UNSET
    if not isinstance(ou, Unset):
        json_ou = ou

    params["ou"] = json_ou

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_pe: Union[Unset, list[str]] = UNSET
    if not isinstance(pe, Unset):
        json_pe = pe

    params["pe"] = json_pe

    params["skipPaging"] = skip_paging

    params["total"] = total

    json_vr: Union[Unset, list[str]] = UNSET
    if not isinstance(vr, Unset):
        json_vr = vr

    params["vr"] = json_vr

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/validationResults/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ValidationResultGetObjectListResponse200]:
    if response.status_code == 200:
        response_200 = ValidationResultGetObjectListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ValidationResultGetObjectListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    vr: Union[Unset, list[str]] = UNSET,
) -> Response[ValidationResultGetObjectListResponse200]:
    """[no description yet]

    Args:
        created_date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        vr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidationResultGetObjectListResponse200]
    """

    kwargs = _get_kwargs(
        created_date=created_date,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        pe=pe,
        skip_paging=skip_paging,
        total=total,
        vr=vr,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    created_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    vr: Union[Unset, list[str]] = UNSET,
) -> Optional[ValidationResultGetObjectListResponse200]:
    """[no description yet]

    Args:
        created_date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        vr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidationResultGetObjectListResponse200
    """

    return sync_detailed(
        client=client,
        created_date=created_date,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        pe=pe,
        skip_paging=skip_paging,
        total=total,
        vr=vr,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    vr: Union[Unset, list[str]] = UNSET,
) -> Response[ValidationResultGetObjectListResponse200]:
    """[no description yet]

    Args:
        created_date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        vr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidationResultGetObjectListResponse200]
    """

    kwargs = _get_kwargs(
        created_date=created_date,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        pe=pe,
        skip_paging=skip_paging,
        total=total,
        vr=vr,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    created_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    total: Union[Unset, int] = 0,
    vr: Union[Unset, list[str]] = UNSET,
) -> Optional[ValidationResultGetObjectListResponse200]:
    """[no description yet]

    Args:
        created_date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):
        total (Union[Unset, int]):  Default: 0.
        vr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidationResultGetObjectListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            created_date=created_date,
            ou=ou,
            page=page,
            page_size=page_size,
            paging=paging,
            pe=pe,
            skip_paging=skip_paging,
            total=total,
            vr=vr,
        )
    ).parsed
