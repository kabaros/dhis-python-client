import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    end_date: datetime.datetime,
    locale: Union[Unset, str] = UNSET,
    start_date: datetime.datetime,
    translate: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["locale"] = locale

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params["translate"] = translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/predictors/{uid}/run",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebMessage]:
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
    end_date: datetime.datetime,
    locale: Union[Unset, str] = UNSET,
    start_date: datetime.datetime,
    translate: Union[Unset, bool] = True,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        end_date (datetime.datetime):
        locale (Union[Unset, str]):
        start_date (datetime.datetime):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        end_date=end_date,
        locale=locale,
        start_date=start_date,
        translate=translate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    end_date: datetime.datetime,
    locale: Union[Unset, str] = UNSET,
    start_date: datetime.datetime,
    translate: Union[Unset, bool] = True,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        end_date (datetime.datetime):
        locale (Union[Unset, str]):
        start_date (datetime.datetime):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        uid=uid,
        client=client,
        end_date=end_date,
        locale=locale,
        start_date=start_date,
        translate=translate,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    end_date: datetime.datetime,
    locale: Union[Unset, str] = UNSET,
    start_date: datetime.datetime,
    translate: Union[Unset, bool] = True,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        end_date (datetime.datetime):
        locale (Union[Unset, str]):
        start_date (datetime.datetime):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        end_date=end_date,
        locale=locale,
        start_date=start_date,
        translate=translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    end_date: datetime.datetime,
    locale: Union[Unset, str] = UNSET,
    start_date: datetime.datetime,
    translate: Union[Unset, bool] = True,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        end_date (datetime.datetime):
        locale (Union[Unset, str]):
        start_date (datetime.datetime):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            end_date=end_date,
            locale=locale,
            start_date=start_date,
            translate=translate,
        )
    ).parsed
