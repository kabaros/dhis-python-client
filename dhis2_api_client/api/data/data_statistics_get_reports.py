import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_statistics_get_reports_interval import DataStatisticsGetReportsInterval
from ...models.data_statistics_get_reports_response_200_item import DataStatisticsGetReportsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    end_date: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
    interval: DataStatisticsGetReportsInterval,
    start_date: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_interval = interval.value
    params["interval"] = json_interval

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataStatistics/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["DataStatisticsGetReportsResponse200Item"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataStatisticsGetReportsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["DataStatisticsGetReportsResponse200Item"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    end_date: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
    interval: DataStatisticsGetReportsInterval,
    start_date: datetime.datetime,
) -> Response[list["DataStatisticsGetReportsResponse200Item"]]:
    """[no description yet]

    Args:
        end_date (datetime.datetime):
        fields (Union[Unset, list[str]]):
        interval (DataStatisticsGetReportsInterval):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DataStatisticsGetReportsResponse200Item']]
    """

    kwargs = _get_kwargs(
        end_date=end_date,
        fields=fields,
        interval=interval,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    end_date: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
    interval: DataStatisticsGetReportsInterval,
    start_date: datetime.datetime,
) -> Optional[list["DataStatisticsGetReportsResponse200Item"]]:
    """[no description yet]

    Args:
        end_date (datetime.datetime):
        fields (Union[Unset, list[str]]):
        interval (DataStatisticsGetReportsInterval):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DataStatisticsGetReportsResponse200Item']
    """

    return sync_detailed(
        client=client,
        end_date=end_date,
        fields=fields,
        interval=interval,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    end_date: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
    interval: DataStatisticsGetReportsInterval,
    start_date: datetime.datetime,
) -> Response[list["DataStatisticsGetReportsResponse200Item"]]:
    """[no description yet]

    Args:
        end_date (datetime.datetime):
        fields (Union[Unset, list[str]]):
        interval (DataStatisticsGetReportsInterval):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DataStatisticsGetReportsResponse200Item']]
    """

    kwargs = _get_kwargs(
        end_date=end_date,
        fields=fields,
        interval=interval,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    end_date: datetime.datetime,
    fields: Union[Unset, list[str]] = UNSET,
    interval: DataStatisticsGetReportsInterval,
    start_date: datetime.datetime,
) -> Optional[list["DataStatisticsGetReportsResponse200Item"]]:
    """[no description yet]

    Args:
        end_date (datetime.datetime):
        fields (Union[Unset, list[str]]):
        interval (DataStatisticsGetReportsInterval):
        start_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DataStatisticsGetReportsResponse200Item']
    """

    return (
        await asyncio_detailed(
            client=client,
            end_date=end_date,
            fields=fields,
            interval=interval,
            start_date=start_date,
        )
    ).parsed
