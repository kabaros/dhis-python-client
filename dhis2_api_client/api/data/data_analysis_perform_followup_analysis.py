import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.followup_analysis_response import FollowupAnalysisResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    coc: Union[Unset, list[str]] = UNSET,
    de: Union[Unset, list[str]] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    max_results: Union[Unset, int] = 50,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_coc: Union[Unset, list[str]] = UNSET
    if not isinstance(coc, Unset):
        json_coc = coc

    params["coc"] = json_coc

    json_de: Union[Unset, list[str]] = UNSET
    if not isinstance(de, Unset):
        json_de = de

    params["de"] = json_de

    json_ds: Union[Unset, list[str]] = UNSET
    if not isinstance(ds, Unset):
        json_ds = ds

    params["ds"] = json_ds

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["maxResults"] = max_results

    json_ou: Union[Unset, list[str]] = UNSET
    if not isinstance(ou, Unset):
        json_ou = ou

    params["ou"] = json_ou

    params["pe"] = pe

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataAnalysis/followup",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FollowupAnalysisResponse]:
    if response.status_code == 200:
        response_200 = FollowupAnalysisResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FollowupAnalysisResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    coc: Union[Unset, list[str]] = UNSET,
    de: Union[Unset, list[str]] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    max_results: Union[Unset, int] = 50,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[FollowupAnalysisResponse]:
    """[no description yet]

    Args:
        coc (Union[Unset, list[str]]):
        de (Union[Unset, list[str]]):
        ds (Union[Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        max_results (Union[Unset, int]):  Default: 50.
        ou (Union[Unset, list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowupAnalysisResponse]
    """

    kwargs = _get_kwargs(
        coc=coc,
        de=de,
        ds=ds,
        end_date=end_date,
        max_results=max_results,
        ou=ou,
        pe=pe,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    coc: Union[Unset, list[str]] = UNSET,
    de: Union[Unset, list[str]] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    max_results: Union[Unset, int] = 50,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[FollowupAnalysisResponse]:
    """[no description yet]

    Args:
        coc (Union[Unset, list[str]]):
        de (Union[Unset, list[str]]):
        ds (Union[Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        max_results (Union[Unset, int]):  Default: 50.
        ou (Union[Unset, list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowupAnalysisResponse
    """

    return sync_detailed(
        client=client,
        coc=coc,
        de=de,
        ds=ds,
        end_date=end_date,
        max_results=max_results,
        ou=ou,
        pe=pe,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    coc: Union[Unset, list[str]] = UNSET,
    de: Union[Unset, list[str]] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    max_results: Union[Unset, int] = 50,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[FollowupAnalysisResponse]:
    """[no description yet]

    Args:
        coc (Union[Unset, list[str]]):
        de (Union[Unset, list[str]]):
        ds (Union[Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        max_results (Union[Unset, int]):  Default: 50.
        ou (Union[Unset, list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FollowupAnalysisResponse]
    """

    kwargs = _get_kwargs(
        coc=coc,
        de=de,
        ds=ds,
        end_date=end_date,
        max_results=max_results,
        ou=ou,
        pe=pe,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    coc: Union[Unset, list[str]] = UNSET,
    de: Union[Unset, list[str]] = UNSET,
    ds: Union[Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    max_results: Union[Unset, int] = 50,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[FollowupAnalysisResponse]:
    """[no description yet]

    Args:
        coc (Union[Unset, list[str]]):
        de (Union[Unset, list[str]]):
        ds (Union[Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        max_results (Union[Unset, int]):  Default: 50.
        ou (Union[Unset, list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FollowupAnalysisResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            coc=coc,
            de=de,
            ds=ds,
            end_date=end_date,
            max_results=max_results,
            ou=ou,
            pe=pe,
            start_date=start_date,
        )
    ).parsed
