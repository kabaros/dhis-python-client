import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_approval_get_approval_response_200 import DataApprovalGetApprovalResponse200
from ...models.data_set import DataSet
from ...models.organisation_unit import OrganisationUnit
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    children: Union[Unset, bool] = UNSET,
    ds: Union["DataSet", list[str]],
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["children"] = children

    json_ds: Union[dict[str, Any], list[str]]
    if isinstance(ds, list):
        json_ds = ds

    else:
        json_ds = ds.to_dict()

    params["ds"] = json_ds

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_ou: Union[dict[str, Any], list[str]]
    if isinstance(ou, list):
        json_ou = ou

    else:
        json_ou = ou.to_dict()

    params["ou"] = json_ou

    params["pe"] = pe

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataApprovals/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DataApprovalGetApprovalResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = DataApprovalGetApprovalResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DataApprovalGetApprovalResponse200, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    children: Union[Unset, bool] = UNSET,
    ds: Union["DataSet", list[str]],
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[DataApprovalGetApprovalResponse200, WebMessage]]:
    """[no description yet]

    Args:
        children (Union[Unset, bool]):
        ds (Union['DataSet', list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataApprovalGetApprovalResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        children=children,
        ds=ds,
        end_date=end_date,
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
    children: Union[Unset, bool] = UNSET,
    ds: Union["DataSet", list[str]],
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[DataApprovalGetApprovalResponse200, WebMessage]]:
    """[no description yet]

    Args:
        children (Union[Unset, bool]):
        ds (Union['DataSet', list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataApprovalGetApprovalResponse200, WebMessage]
    """

    return sync_detailed(
        client=client,
        children=children,
        ds=ds,
        end_date=end_date,
        ou=ou,
        pe=pe,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    children: Union[Unset, bool] = UNSET,
    ds: Union["DataSet", list[str]],
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[DataApprovalGetApprovalResponse200, WebMessage]]:
    """[no description yet]

    Args:
        children (Union[Unset, bool]):
        ds (Union['DataSet', list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataApprovalGetApprovalResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        children=children,
        ds=ds,
        end_date=end_date,
        ou=ou,
        pe=pe,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    children: Union[Unset, bool] = UNSET,
    ds: Union["DataSet", list[str]],
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, str] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[DataApprovalGetApprovalResponse200, WebMessage]]:
    """[no description yet]

    Args:
        children (Union[Unset, bool]):
        ds (Union['DataSet', list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataApprovalGetApprovalResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            children=children,
            ds=ds,
            end_date=end_date,
            ou=ou,
            pe=pe,
            start_date=start_date,
        )
    ).parsed
