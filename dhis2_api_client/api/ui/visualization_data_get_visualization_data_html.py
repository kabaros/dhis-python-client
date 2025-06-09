import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.grid import Grid
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params["ou"] = ou

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/visualizations/{uid}/data.html",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Grid]:
    if response.status_code == 200:
        response_200 = Grid.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Grid]:
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
    date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, str] = UNSET,
) -> Response[Grid]:
    """[no description yet]

    Args:
        uid (str):
        date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Grid]
    """

    kwargs = _get_kwargs(
        uid=uid,
        date=date,
        ou=ou,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, str] = UNSET,
) -> Optional[Grid]:
    """[no description yet]

    Args:
        uid (str):
        date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Grid
    """

    return sync_detailed(
        uid=uid,
        client=client,
        date=date,
        ou=ou,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, str] = UNSET,
) -> Response[Grid]:
    """[no description yet]

    Args:
        uid (str):
        date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Grid]
    """

    kwargs = _get_kwargs(
        uid=uid,
        date=date,
        ou=ou,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union[Unset, str] = UNSET,
) -> Optional[Grid]:
    """[no description yet]

    Args:
        uid (str):
        date (Union[Unset, datetime.datetime]):
        ou (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Grid
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            date=date,
            ou=ou,
        )
    ).parsed
