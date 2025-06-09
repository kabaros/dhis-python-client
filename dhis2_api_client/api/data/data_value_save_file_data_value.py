from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, File, FileJsonType, Response, Unset


def _get_kwargs(
    *,
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    comment: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: str,
    ds: Union[Unset, str] = UNSET,
    file: Union[Unset, File] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cc"] = cc

    params["co"] = co

    params["comment"] = comment

    params["cp"] = cp

    params["de"] = de

    params["ds"] = ds

    json_file: Union[Unset, FileJsonType] = UNSET
    if not isinstance(file, Unset):
        json_file = file.to_tuple()

    params["file"] = json_file

    params["followUp"] = follow_up

    params["force"] = force

    params["ou"] = ou

    params["pe"] = pe

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/dataValues/file",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebMessage]:
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
    comment: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: str,
    ds: Union[Unset, str] = UNSET,
    file: Union[Unset, File] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        comment (Union[Unset, str]):
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        file (Union[Unset, File]):
        follow_up (Union[Unset, bool]):
        force (Union[Unset, bool]):
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        cc=cc,
        co=co,
        comment=comment,
        cp=cp,
        de=de,
        ds=ds,
        file=file,
        follow_up=follow_up,
        force=force,
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
    comment: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: str,
    ds: Union[Unset, str] = UNSET,
    file: Union[Unset, File] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        comment (Union[Unset, str]):
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        file (Union[Unset, File]):
        follow_up (Union[Unset, bool]):
        force (Union[Unset, bool]):
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        cc=cc,
        co=co,
        comment=comment,
        cp=cp,
        de=de,
        ds=ds,
        file=file,
        follow_up=follow_up,
        force=force,
        ou=ou,
        pe=pe,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cc: Union[Unset, str] = UNSET,
    co: Union[Unset, str] = UNSET,
    comment: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: str,
    ds: Union[Unset, str] = UNSET,
    file: Union[Unset, File] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        comment (Union[Unset, str]):
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        file (Union[Unset, File]):
        follow_up (Union[Unset, bool]):
        force (Union[Unset, bool]):
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        cc=cc,
        co=co,
        comment=comment,
        cp=cp,
        de=de,
        ds=ds,
        file=file,
        follow_up=follow_up,
        force=force,
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
    comment: Union[Unset, str] = UNSET,
    cp: Union[Unset, str] = UNSET,
    de: str,
    ds: Union[Unset, str] = UNSET,
    file: Union[Unset, File] = UNSET,
    follow_up: Union[Unset, bool] = UNSET,
    force: Union[Unset, bool] = UNSET,
    ou: str,
    pe: str,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        cc (Union[Unset, str]): A UID for an CategoryCombo object
            (Java name `org.hisp.dhis.category.CategoryCombo`) Example: iZ9tI8jD7T4.
        co (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        comment (Union[Unset, str]):
        cp (Union[Unset, str]): A UID for an CategoryOption object
            (Java name `org.hisp.dhis.category.CategoryOption`) Example: j0wu64kE8Vc.
        de (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.
        ds (Union[Unset, str]): A UID for an DataSet object
            (Java name `org.hisp.dhis.dataset.DataSet`) Example: dT3ji2fG1SM.
        file (Union[Unset, File]):
        follow_up (Union[Unset, bool]):
        force (Union[Unset, bool]):
        ou (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        pe (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            cc=cc,
            co=co,
            comment=comment,
            cp=cp,
            de=de,
            ds=ds,
            file=file,
            follow_up=follow_up,
            force=force,
            ou=ou,
            pe=pe,
        )
    ).parsed
