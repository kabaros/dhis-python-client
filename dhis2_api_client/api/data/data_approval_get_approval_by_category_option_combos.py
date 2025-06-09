from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_approval_get_approval_by_category_option_combos_response_200_item import (
    DataApprovalGetApprovalByCategoryOptionCombosResponse200Item,
)
from ...models.data_approval_workflow import DataApprovalWorkflow
from ...models.data_set import DataSet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_filter: Union[Unset, str] = UNSET,
    pe: str,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aoc"] = aoc

    json_ds: Union[Unset, dict[str, Any], list[str]]
    if isinstance(ds, Unset):
        json_ds = UNSET
    elif isinstance(ds, list):
        json_ds = ds

    else:
        json_ds = ds.to_dict()

    params["ds"] = json_ds

    params["ou"] = ou

    params["ouFilter"] = ou_filter

    params["pe"] = pe

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
        "url": "/dataApprovals/categoryOptionCombos",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["DataApprovalGetApprovalByCategoryOptionCombosResponse200Item"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataApprovalGetApprovalByCategoryOptionCombosResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["DataApprovalGetApprovalByCategoryOptionCombosResponse200Item"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_filter: Union[Unset, str] = UNSET,
    pe: str,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Response[list["DataApprovalGetApprovalByCategoryOptionCombosResponse200Item"]]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        ou_filter (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DataApprovalGetApprovalByCategoryOptionCombosResponse200Item']]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        ds=ds,
        ou=ou,
        ou_filter=ou_filter,
        pe=pe,
        wf=wf,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_filter: Union[Unset, str] = UNSET,
    pe: str,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Optional[list["DataApprovalGetApprovalByCategoryOptionCombosResponse200Item"]]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        ou_filter (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DataApprovalGetApprovalByCategoryOptionCombosResponse200Item']
    """

    return sync_detailed(
        client=client,
        aoc=aoc,
        ds=ds,
        ou=ou,
        ou_filter=ou_filter,
        pe=pe,
        wf=wf,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_filter: Union[Unset, str] = UNSET,
    pe: str,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Response[list["DataApprovalGetApprovalByCategoryOptionCombosResponse200Item"]]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        ou_filter (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DataApprovalGetApprovalByCategoryOptionCombosResponse200Item']]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        ds=ds,
        ou=ou,
        ou_filter=ou_filter,
        pe=pe,
        wf=wf,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union[Unset, str] = UNSET,
    ou_filter: Union[Unset, str] = UNSET,
    pe: str,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Optional[list["DataApprovalGetApprovalByCategoryOptionCombosResponse200Item"]]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        ou_filter (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DataApprovalGetApprovalByCategoryOptionCombosResponse200Item']
    """

    return (
        await asyncio_detailed(
            client=client,
            aoc=aoc,
            ds=ds,
            ou=ou,
            ou_filter=ou_filter,
            pe=pe,
            wf=wf,
        )
    ).parsed
