import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_status_dto import ApprovalStatusDto
from ...models.category_option_combo import CategoryOptionCombo
from ...models.data_approval_workflow import DataApprovalWorkflow
from ...models.organisation_unit import OrganisationUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", list[str]],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_aoc: Union[Unset, dict[str, Any], list[str]]
    if isinstance(aoc, Unset):
        json_aoc = UNSET
    elif isinstance(aoc, list):
        json_aoc = aoc

    else:
        json_aoc = aoc.to_dict()

    params["aoc"] = json_aoc

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

    json_pe: Union[Unset, list[str]] = UNSET
    if not isinstance(pe, Unset):
        json_pe = pe

    params["pe"] = json_pe

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_wf: Union[dict[str, Any], list[str]]
    if isinstance(wf, list):
        json_wf = wf

    else:
        json_wf = wf.to_dict()

    params["wf"] = json_wf

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataApprovals/multiple",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ApprovalStatusDto"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApprovalStatusDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ApprovalStatusDto"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", list[str]],
) -> Response[list["ApprovalStatusDto"]]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ApprovalStatusDto']]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        end_date=end_date,
        ou=ou,
        pe=pe,
        start_date=start_date,
        wf=wf,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", list[str]],
) -> Optional[list["ApprovalStatusDto"]]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ApprovalStatusDto']
    """

    return sync_detailed(
        client=client,
        aoc=aoc,
        end_date=end_date,
        ou=ou,
        pe=pe,
        start_date=start_date,
        wf=wf,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", list[str]],
) -> Response[list["ApprovalStatusDto"]]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ApprovalStatusDto']]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        end_date=end_date,
        ou=ou,
        pe=pe,
        start_date=start_date,
        wf=wf,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", list[str]],
    pe: Union[Unset, list[str]] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", list[str]],
) -> Optional[list["ApprovalStatusDto"]]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', list[str]]):
        pe (Union[Unset, list[str]]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ApprovalStatusDto']
    """

    return (
        await asyncio_detailed(
            client=client,
            aoc=aoc,
            end_date=end_date,
            ou=ou,
            pe=pe,
            start_date=start_date,
            wf=wf,
        )
    ).parsed
