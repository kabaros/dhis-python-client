from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ds: str,
    filter_: Union[Unset, list[str]] = UNSET,
    ou: str,
    pe: list[str],
    selected_unit_only: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ds"] = ds

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    params["ou"] = ou

    json_pe = pe

    params["pe"] = json_pe

    params["selectedUnitOnly"] = selected_unit_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataSetReport.pdf",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
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
    ds: str,
    filter_: Union[Unset, list[str]] = UNSET,
    ou: str,
    pe: list[str],
    selected_unit_only: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        ds (str):
        filter_ (Union[Unset, list[str]]):
        ou (str):
        pe (list[str]):
        selected_unit_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ds=ds,
        filter_=filter_,
        ou=ou,
        pe=pe,
        selected_unit_only=selected_unit_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ds: str,
    filter_: Union[Unset, list[str]] = UNSET,
    ou: str,
    pe: list[str],
    selected_unit_only: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        ds (str):
        filter_ (Union[Unset, list[str]]):
        ou (str):
        pe (list[str]):
        selected_unit_only (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ds=ds,
        filter_=filter_,
        ou=ou,
        pe=pe,
        selected_unit_only=selected_unit_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
