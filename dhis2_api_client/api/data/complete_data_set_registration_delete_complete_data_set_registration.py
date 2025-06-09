from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cc: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    ds: list[str],
    multi_ou: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cc"] = cc

    params["cp"] = cp

    json_ds = ds

    params["ds"] = json_ds

    params["multiOu"] = multi_ou

    params["ou"] = ou

    params["pe"] = pe

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/completeDataSetRegistrations/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
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
    cc: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    ds: list[str],
    multi_ou: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> Response[Any]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]):
        cp (Union[Unset, str]):
        ds (list[str]):
        multi_ou (Union[Unset, bool]):
        ou (str):
        pe (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        cc=cc,
        cp=cp,
        ds=ds,
        multi_ou=multi_ou,
        ou=ou,
        pe=pe,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cc: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    ds: list[str],
    multi_ou: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> Response[Any]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]):
        cp (Union[Unset, str]):
        ds (list[str]):
        multi_ou (Union[Unset, bool]):
        ou (str):
        pe (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        cc=cc,
        cp=cp,
        ds=ds,
        multi_ou=multi_ou,
        ou=ou,
        pe=pe,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
