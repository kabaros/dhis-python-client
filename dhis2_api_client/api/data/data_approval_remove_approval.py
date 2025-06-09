from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_approval_workflow import DataApprovalWorkflow
from ...models.data_set import DataSet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: str,
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
        "method": "delete",
        "url": "/dataApprovals",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
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
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: str,
    pe: str,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union['DataSet', Unset, list[str]]):
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        ds=ds,
        ou=ou,
        pe=pe,
        wf=wf,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: str,
    pe: str,
    wf: Union["DataApprovalWorkflow", Unset, list[str]] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union['DataSet', Unset, list[str]]):
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union['DataApprovalWorkflow', Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        aoc=aoc,
        ds=ds,
        ou=ou,
        pe=pe,
        wf=wf,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
