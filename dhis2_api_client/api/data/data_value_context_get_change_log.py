from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_value_context_dto import DataValueContextDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: Union[Unset, str] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cc"] = cc

    params["co"] = co

    params["cp"] = cp

    params["de"] = de

    params["ou"] = ou

    params["pe"] = pe

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataEntry/dataValueContext",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DataValueContextDto]:
    if response.status_code == 200:
        response_200 = DataValueContextDto.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DataValueContextDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: Union[Unset, str] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
) -> Response[DataValueContextDto]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataValueContextDto]
    """

    kwargs = _get_kwargs(
        cc=cc,
        co=co,
        cp=cp,
        de=de,
        ou=ou,
        pe=pe,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: Union[Unset, str] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
) -> Optional[DataValueContextDto]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataValueContextDto
    """

    return sync_detailed(
        client=client,
        cc=cc,
        co=co,
        cp=cp,
        de=de,
        ou=ou,
        pe=pe,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: Union[Unset, str] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
) -> Response[DataValueContextDto]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataValueContextDto]
    """

    kwargs = _get_kwargs(
        cc=cc,
        co=co,
        cp=cp,
        de=de,
        ou=ou,
        pe=pe,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: Union[Unset, str] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
) -> Optional[DataValueContextDto]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (Union[Unset, str]): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ou (Union[Unset, str]): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataValueContextDto
    """

    return (
        await asyncio_detailed(
            client=client,
            cc=cc,
            co=co,
            cp=cp,
            de=de,
            ou=ou,
            pe=pe,
        )
    ).parsed
