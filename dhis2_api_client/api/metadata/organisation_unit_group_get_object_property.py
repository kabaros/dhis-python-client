from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organisation_unit_group_get_object_property_property import (
    OrganisationUnitGroupGetObjectPropertyProperty,
)
from ...models.organisation_unit_group_get_object_property_response_200 import (
    OrganisationUnitGroupGetObjectPropertyResponse200,
)
from ...models.organisation_unit_group_get_object_property_root_junction import (
    OrganisationUnitGroupGetObjectPropertyRootJunction,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    property_: OrganisationUnitGroupGetObjectPropertyProperty,
    *,
    fields: Union[Unset, list[str]] = UNSET,
    locale: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction] = UNSET,
    translate: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["locale"] = locale

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params["translate"] = translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/organisationUnitGroups/{uid}/{property_}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = OrganisationUnitGroupGetObjectPropertyResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uid: str,
    property_: OrganisationUnitGroupGetObjectPropertyProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    locale: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_ (OrganisationUnitGroupGetObjectPropertyProperty):
        fields (Union[Unset, list[str]]):
        locale (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        property_=property_,
        fields=fields,
        locale=locale,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        translate=translate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    property_: OrganisationUnitGroupGetObjectPropertyProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    locale: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_ (OrganisationUnitGroupGetObjectPropertyProperty):
        fields (Union[Unset, list[str]]):
        locale (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        property_=property_,
        client=client,
        fields=fields,
        locale=locale,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        translate=translate,
    ).parsed


async def asyncio_detailed(
    uid: str,
    property_: OrganisationUnitGroupGetObjectPropertyProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    locale: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_ (OrganisationUnitGroupGetObjectPropertyProperty):
        fields (Union[Unset, list[str]]):
        locale (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        property_=property_,
        fields=fields,
        locale=locale,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        translate=translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    property_: OrganisationUnitGroupGetObjectPropertyProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    locale: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_ (OrganisationUnitGroupGetObjectPropertyProperty):
        fields (Union[Unset, list[str]]):
        locale (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, OrganisationUnitGroupGetObjectPropertyRootJunction]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganisationUnitGroupGetObjectPropertyResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            property_=property_,
            client=client,
            fields=fields,
            locale=locale,
            page=page,
            page_size=page_size,
            paging=paging,
            root_junction=root_junction,
            translate=translate,
        )
    ).parsed
