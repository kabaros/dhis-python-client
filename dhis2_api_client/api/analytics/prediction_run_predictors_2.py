import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    async_: Union[Unset, bool] = False,
    end_date: datetime.datetime,
    predictor: Union[Unset, list[str]] = UNSET,
    predictor_group: Union[Unset, list[str]] = UNSET,
    start_date: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["async"] = async_

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_predictor: Union[Unset, list[str]] = UNSET
    if not isinstance(predictor, Unset):
        json_predictor = predictor

    params["predictor"] = json_predictor

    json_predictor_group: Union[Unset, list[str]] = UNSET
    if not isinstance(predictor_group, Unset):
        json_predictor_group = predictor_group

    params["predictorGroup"] = json_predictor_group

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/predictions/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
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
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    end_date: datetime.datetime,
    predictor: Union[Unset, list[str]] = UNSET,
    predictor_group: Union[Unset, list[str]] = UNSET,
    start_date: datetime.datetime,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        end_date (datetime.datetime):
        predictor (Union[Unset, list[str]]):
        predictor_group (Union[Unset, list[str]]):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        async_=async_,
        end_date=end_date,
        predictor=predictor,
        predictor_group=predictor_group,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    end_date: datetime.datetime,
    predictor: Union[Unset, list[str]] = UNSET,
    predictor_group: Union[Unset, list[str]] = UNSET,
    start_date: datetime.datetime,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        end_date (datetime.datetime):
        predictor (Union[Unset, list[str]]):
        predictor_group (Union[Unset, list[str]]):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        async_=async_,
        end_date=end_date,
        predictor=predictor,
        predictor_group=predictor_group,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    end_date: datetime.datetime,
    predictor: Union[Unset, list[str]] = UNSET,
    predictor_group: Union[Unset, list[str]] = UNSET,
    start_date: datetime.datetime,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        end_date (datetime.datetime):
        predictor (Union[Unset, list[str]]):
        predictor_group (Union[Unset, list[str]]):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        async_=async_,
        end_date=end_date,
        predictor=predictor,
        predictor_group=predictor_group,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    end_date: datetime.datetime,
    predictor: Union[Unset, list[str]] = UNSET,
    predictor_group: Union[Unset, list[str]] = UNSET,
    start_date: datetime.datetime,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        end_date (datetime.datetime):
        predictor (Union[Unset, list[str]]):
        predictor_group (Union[Unset, list[str]]):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            async_=async_,
            end_date=end_date,
            predictor=predictor,
            predictor_group=predictor_group,
            start_date=start_date,
        )
    ).parsed
