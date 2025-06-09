from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_log_get_aggregate_data_value_audit_audit_type_item import (
    ChangeLogGetAggregateDataValueAuditAuditTypeItem,
)
from ...models.change_log_get_aggregate_data_value_audit_response_200 import (
    ChangeLogGetAggregateDataValueAuditResponse200,
)
from ...models.data_element import DataElement
from ...models.data_set import DataSet
from ...models.organisation_unit import OrganisationUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    audit_type: Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]] = UNSET,
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_audit_type: Union[Unset, list[str]] = UNSET
    if not isinstance(audit_type, Unset):
        json_audit_type = []
        for audit_type_item_data in audit_type:
            audit_type_item = audit_type_item_data.value
            json_audit_type.append(audit_type_item)

    params["auditType"] = json_audit_type

    params["cc"] = cc

    params["co"] = co

    json_de: Union[Unset, dict[str, Any], list[str]]
    if isinstance(de, Unset):
        json_de = UNSET
    elif isinstance(de, list):
        json_de = de

    else:
        json_de = de.to_dict()

    params["de"] = json_de

    json_ds: Union[Unset, dict[str, Any], list[str]]
    if isinstance(ds, Unset):
        json_ds = UNSET
    elif isinstance(ds, list):
        json_ds = ds

    else:
        json_ds = ds.to_dict()

    params["ds"] = json_ds

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

    json_pe: Union[Unset, list[str]] = UNSET
    if not isinstance(pe, Unset):
        json_pe = pe

    params["pe"] = json_pe

    params["skipPaging"] = skip_paging

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/audits/dataValue",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ChangeLogGetAggregateDataValueAuditResponse200]:
    if response.status_code == 200:
        response_200 = ChangeLogGetAggregateDataValueAuditResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChangeLogGetAggregateDataValueAuditResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]] = UNSET,
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Response[ChangeLogGetAggregateDataValueAuditResponse200]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]]):
        cc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        de (Union['DataElement', Unset, list[str]]):
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeLogGetAggregateDataValueAuditResponse200]
    """

    kwargs = _get_kwargs(
        audit_type=audit_type,
        cc=cc,
        co=co,
        de=de,
        ds=ds,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        pe=pe,
        skip_paging=skip_paging,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]] = UNSET,
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Optional[ChangeLogGetAggregateDataValueAuditResponse200]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]]):
        cc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        de (Union['DataElement', Unset, list[str]]):
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeLogGetAggregateDataValueAuditResponse200
    """

    return sync_detailed(
        client=client,
        audit_type=audit_type,
        cc=cc,
        co=co,
        de=de,
        ds=ds,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        pe=pe,
        skip_paging=skip_paging,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]] = UNSET,
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Response[ChangeLogGetAggregateDataValueAuditResponse200]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]]):
        cc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        de (Union['DataElement', Unset, list[str]]):
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangeLogGetAggregateDataValueAuditResponse200]
    """

    kwargs = _get_kwargs(
        audit_type=audit_type,
        cc=cc,
        co=co,
        de=de,
        ds=ds,
        ou=ou,
        page=page,
        page_size=page_size,
        paging=paging,
        pe=pe,
        skip_paging=skip_paging,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    audit_type: Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]] = UNSET,
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    de: Union["DataElement", Unset, list[str]] = UNSET,
    ds: Union["DataSet", Unset, list[str]] = UNSET,
    ou: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = UNSET,
    pe: Union[Unset, list[str]] = UNSET,
    skip_paging: Union[Unset, bool] = UNSET,
) -> Optional[ChangeLogGetAggregateDataValueAuditResponse200]:
    """[no description yet]

    Args:
        audit_type (Union[Unset, list[ChangeLogGetAggregateDataValueAuditAuditTypeItem]]):
        cc (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        de (Union['DataElement', Unset, list[str]]):
        ds (Union['DataSet', Unset, list[str]]):
        ou (Union['OrganisationUnit', Unset, list[str]]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):
        pe (Union[Unset, list[str]]):
        skip_paging (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangeLogGetAggregateDataValueAuditResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            audit_type=audit_type,
            cc=cc,
            co=co,
            de=de,
            ds=ds,
            ou=ou,
            page=page,
            page_size=page_size,
            paging=paging,
            pe=pe,
            skip_paging=skip_paging,
        )
    ).parsed
