import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.outlier_detection_get_outliers_csv_algorithm import OutlierDetectionGetOutliersCsvAlgorithm
from ...models.outlier_detection_get_outliers_csv_order_by import OutlierDetectionGetOutliersCsvOrderBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    algorithm: Union[Unset, OutlierDetectionGetOutliersCsvAlgorithm] = OutlierDetectionGetOutliersCsvAlgorithm.Z_SCORE,
    data_end_date: Union[Unset, datetime.datetime] = UNSET,
    data_start_date: Union[Unset, datetime.datetime] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    dx: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    max_results: Union[Unset, int] = UNSET,
    order_by: Union[Unset, OutlierDetectionGetOutliersCsvOrderBy] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    threshold: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_algorithm: Union[Unset, str] = UNSET
    if not isinstance(algorithm, Unset):
        json_algorithm = algorithm.value

    params["algorithm"] = json_algorithm

    json_data_end_date: Union[Unset, str] = UNSET
    if not isinstance(data_end_date, Unset):
        json_data_end_date = data_end_date.isoformat()
    params["dataEndDate"] = json_data_end_date

    json_data_start_date: Union[Unset, str] = UNSET
    if not isinstance(data_start_date, Unset):
        json_data_start_date = data_start_date.isoformat()
    params["dataStartDate"] = json_data_start_date

    json_ds: Union[Unset, list[str]] = UNSET
    if not isinstance(ds, Unset):
        json_ds = ds

    params["ds"] = json_ds

    json_dx: Union[Unset, list[str]] = UNSET
    if not isinstance(dx, Unset):
        json_dx = dx

    params["dx"] = json_dx

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_headers: Union[Unset, list[str]] = UNSET
    if not isinstance(headers, Unset):
        json_headers = headers

    params["headers"] = json_headers

    params["maxResults"] = max_results

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    json_ou: Union[Unset, list[str]] = UNSET
    if not isinstance(ou, Unset):
        json_ou = ou

    params["ou"] = json_ou

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params["threshold"] = threshold

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/outlierDetection.csv",
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
    algorithm: Union[Unset, OutlierDetectionGetOutliersCsvAlgorithm] = OutlierDetectionGetOutliersCsvAlgorithm.Z_SCORE,
    data_end_date: Union[Unset, datetime.datetime] = UNSET,
    data_start_date: Union[Unset, datetime.datetime] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    dx: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    max_results: Union[Unset, int] = UNSET,
    order_by: Union[Unset, OutlierDetectionGetOutliersCsvOrderBy] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    threshold: Union[Unset, float] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        algorithm (Union[Unset, OutlierDetectionGetOutliersCsvAlgorithm]):  Default:
            OutlierDetectionGetOutliersCsvAlgorithm.Z_SCORE.
        data_end_date (Union[Unset, datetime.datetime]):
        data_start_date (Union[Unset, datetime.datetime]):
        ds (Union[Unset, list[str]]):
        dx (Union[Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        headers (Union[Unset, list[str]]):
        max_results (Union[Unset, int]):
        order_by (Union[Unset, OutlierDetectionGetOutliersCsvOrderBy]):
        ou (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        threshold (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        algorithm=algorithm,
        data_end_date=data_end_date,
        data_start_date=data_start_date,
        ds=ds,
        dx=dx,
        end_date=end_date,
        headers=headers,
        max_results=max_results,
        order_by=order_by,
        ou=ou,
        start_date=start_date,
        threshold=threshold,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    algorithm: Union[Unset, OutlierDetectionGetOutliersCsvAlgorithm] = OutlierDetectionGetOutliersCsvAlgorithm.Z_SCORE,
    data_end_date: Union[Unset, datetime.datetime] = UNSET,
    data_start_date: Union[Unset, datetime.datetime] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    dx: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    headers: Union[Unset, list[str]] = UNSET,
    max_results: Union[Unset, int] = UNSET,
    order_by: Union[Unset, OutlierDetectionGetOutliersCsvOrderBy] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    threshold: Union[Unset, float] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        algorithm (Union[Unset, OutlierDetectionGetOutliersCsvAlgorithm]):  Default:
            OutlierDetectionGetOutliersCsvAlgorithm.Z_SCORE.
        data_end_date (Union[Unset, datetime.datetime]):
        data_start_date (Union[Unset, datetime.datetime]):
        ds (Union[Unset, list[str]]):
        dx (Union[Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        headers (Union[Unset, list[str]]):
        max_results (Union[Unset, int]):
        order_by (Union[Unset, OutlierDetectionGetOutliersCsvOrderBy]):
        ou (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        threshold (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        algorithm=algorithm,
        data_end_date=data_end_date,
        data_start_date=data_start_date,
        ds=ds,
        dx=dx,
        end_date=end_date,
        headers=headers,
        max_results=max_results,
        order_by=order_by,
        ou=ou,
        start_date=start_date,
        threshold=threshold,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
