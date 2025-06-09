import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    attachment: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
    height: Union[Unset, int] = UNSET,
    ou: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["attachment"] = attachment

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["height"] = height

    params["ou"] = ou

    params["width"] = width

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/maps/{uid}/data",
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    attachment: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
    height: Union[Unset, int] = UNSET,
    ou: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        uid (str):
        attachment (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):
        height (Union[Unset, int]):
        ou (Union[Unset, str]):
        width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uid=uid,
        attachment=attachment,
        date=date,
        height=height,
        ou=ou,
        width=width,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    attachment: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
    height: Union[Unset, int] = UNSET,
    ou: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        uid (str):
        attachment (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):
        height (Union[Unset, int]):
        ou (Union[Unset, str]):
        width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uid=uid,
        attachment=attachment,
        date=date,
        height=height,
        ou=ou,
        width=width,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
