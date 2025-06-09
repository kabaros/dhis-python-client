from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_approval_permissions import DataApprovalPermissions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aoc: Union[Unset, str] = UNSET,
    ds: Union[Unset, str] = UNSET,
    ou: str,
    pe: str,
    wf: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["aoc"] = aoc

    params["ds"] = ds

    params["ou"] = ou

    params["pe"] = pe

    params["wf"] = wf

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataApprovals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DataApprovalPermissions]:
    if response.status_code == 200:
        response_200 = DataApprovalPermissions.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DataApprovalPermissions]:
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
    ds: Union[Unset, str] = UNSET,
    ou: str,
    pe: str,
    wf: Union[Unset, str] = UNSET,
) -> Response[DataApprovalPermissions]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union[Unset, str]): A UID for an DataApprovalWorkflow object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalWorkflow`) Example: q6Cw2bo1N7Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataApprovalPermissions]
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


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union[Unset, str] = UNSET,
    ou: str,
    pe: str,
    wf: Union[Unset, str] = UNSET,
) -> Optional[DataApprovalPermissions]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union[Unset, str]): A UID for an DataApprovalWorkflow object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalWorkflow`) Example: q6Cw2bo1N7Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataApprovalPermissions
    """

    return sync_detailed(
        client=client,
        aoc=aoc,
        ds=ds,
        ou=ou,
        pe=pe,
        wf=wf,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union[Unset, str] = UNSET,
    ou: str,
    pe: str,
    wf: Union[Unset, str] = UNSET,
) -> Response[DataApprovalPermissions]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union[Unset, str]): A UID for an DataApprovalWorkflow object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalWorkflow`) Example: q6Cw2bo1N7Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataApprovalPermissions]
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


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    aoc: Union[Unset, str] = UNSET,
    ds: Union[Unset, str] = UNSET,
    ou: str,
    pe: str,
    wf: Union[Unset, str] = UNSET,
) -> Optional[DataApprovalPermissions]:
    """[no description yet]

    Args:
        aoc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):
        wf (Union[Unset, str]): A UID for an DataApprovalWorkflow object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalWorkflow`) Example: q6Cw2bo1N7Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataApprovalPermissions
    """

    return (
        await asyncio_detailed(
            client=client,
            aoc=aoc,
            ds=ds,
            ou=ou,
            pe=pe,
            wf=wf,
        )
    ).parsed
