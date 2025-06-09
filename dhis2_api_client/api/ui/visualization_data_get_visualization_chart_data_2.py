from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    attachment: Union[Unset, bool] = UNSET,
    height: Union[Unset, int] = 500,
    in_: str,
    ou: str,
    periods: Union[Unset, bool] = UNSET,
    skip_title: Union[Unset, bool] = UNSET,
    width: Union[Unset, int] = 800,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["attachment"] = attachment

    params["height"] = height

    params["in"] = in_

    params["ou"] = ou

    params["periods"] = periods

    params["skipTitle"] = skip_title

    params["width"] = width

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/visualizations/data.png",
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
    attachment: Union[Unset, bool] = UNSET,
    height: Union[Unset, int] = 500,
    in_: str,
    ou: str,
    periods: Union[Unset, bool] = UNSET,
    skip_title: Union[Unset, bool] = UNSET,
    width: Union[Unset, int] = 800,
) -> Response[Any]:
    """[no description yet]

    Args:
        attachment (Union[Unset, bool]):
        height (Union[Unset, int]):  Default: 500.
        in_ (str):
        ou (str):
        periods (Union[Unset, bool]):
        skip_title (Union[Unset, bool]):
        width (Union[Unset, int]):  Default: 800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attachment=attachment,
        height=height,
        in_=in_,
        ou=ou,
        periods=periods,
        skip_title=skip_title,
        width=width,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attachment: Union[Unset, bool] = UNSET,
    height: Union[Unset, int] = 500,
    in_: str,
    ou: str,
    periods: Union[Unset, bool] = UNSET,
    skip_title: Union[Unset, bool] = UNSET,
    width: Union[Unset, int] = 800,
) -> Response[Any]:
    """[no description yet]

    Args:
        attachment (Union[Unset, bool]):
        height (Union[Unset, int]):  Default: 500.
        in_ (str):
        ou (str):
        periods (Union[Unset, bool]):
        skip_title (Union[Unset, bool]):
        width (Union[Unset, int]):  Default: 800.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        attachment=attachment,
        height=height,
        in_=in_,
        ou=ou,
        periods=periods,
        skip_title=skip_title,
        width=width,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
