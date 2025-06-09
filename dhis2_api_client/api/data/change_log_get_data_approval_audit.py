import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_option_combo import CategoryOptionCombo
from ...models.change_log_get_data_approval_audit_response_200 import ChangeLogGetDataApprovalAuditResponse200
from ...models.data_approval_level import DataApprovalLevel
from ...models.data_approval_workflow import DataApprovalWorkflow
from ...models.organisation_unit import OrganisationUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    dal: Union["DataApprovalLevel", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
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

    json_dal: Union[Unset, dict[str, Any], list[str]]
    if isinstance(dal, Unset):
        json_dal = UNSET
    elif isinstance(dal, list):
        json_dal = dal

    else:
        json_dal = dal.to_dict()

    params["dal"] = json_dal

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_ou: Union[Unset, dict[str, Any], list[str]]
    if isinstance(ou, Unset):
        json_ou = UNSET
    elif isinstance(ou, list):
        json_ou = ou

    else:
        json_ou = ou.to_dict()

    params["ou"] = json_ou

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    params["skipPaging"] = skip_paging

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_wf: Union[Unset, dict[str, Any], list[str]]
    if isinstance(wf, Unset):
        json_wf = UNSET
    elif isinstance(wf, list):
        json_wf = wf

    else:
        json_wf = wf.to_dict()

    params["wf"] = json_wf

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audits/dataApproval",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ChangeLogGetDataApprovalAuditResponse200]:
    if response.status_code == 200:
        response_200 = ChangeLogGetDataApprovalAuditResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChangeLogGetDataApprovalAuditResponse200]:
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
    dal: Union["DataApprovalLevel", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Response[ChangeLogGetDataApprovalAuditResponse200]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        dal (Union['DataApprovalLevel', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeLogGetDataApprovalAuditResponse200]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        dal=dal,
        end_date=end_date,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
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
    dal: Union["DataApprovalLevel", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Optional[ChangeLogGetDataApprovalAuditResponse200]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        dal (Union['DataApprovalLevel', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeLogGetDataApprovalAuditResponse200
    """

    return sync_detailed(
        client=client,
        aoc=aoc,
        dal=dal,
        end_date=end_date,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        start_date=start_date,
        wf=wf,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    dal: Union["DataApprovalLevel", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Response[ChangeLogGetDataApprovalAuditResponse200]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        dal (Union['DataApprovalLevel', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeLogGetDataApprovalAuditResponse200]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        dal=dal,
        end_date=end_date,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        skip_paging=skip_paging,
        start_date=start_date,
        wf=wf,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union["CategoryOptionCombo", Unset, list[str]] = UNSET,
    dal: Union["DataApprovalLevel", Unset, list[str]] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Optional[ChangeLogGetDataApprovalAuditResponse200]:
    """[no description yet]

    Args:
        aoc (Union['CategoryOptionCombo', Unset, list[str]]):
        dal (Union['DataApprovalLevel', Unset, list[str]]):
        end_date (Union[Unset, datetime.datetime]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        skip_paging (Union[Unset, bool]):
        start_date (Union[Unset, datetime.datetime]):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeLogGetDataApprovalAuditResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            aoc=aoc,
            dal=dal,
            end_date=end_date,
            ou=ou,
            page=page,
            page_size=page_size,
            paging=paging,
            skip_paging=skip_paging,
            start_date=start_date,
            wf=wf,
        )
    ).parsed
