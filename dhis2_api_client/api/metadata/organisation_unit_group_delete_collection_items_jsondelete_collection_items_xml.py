from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identifiable_objects import IdentifiableObjects
from ...models.organisation_unit_group_delete_collection_items_jsondelete_collection_items_xml_property import (
    OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty,
)
from ...models.web_message import WebMessage
from ...types import Response


def _get_kwargs(
    uid: str,
    property_: OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty,
    *,
    body: IdentifiableObjects,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/organisationUnitGroups/{uid}/{property_}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
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
    uid: str,
    property_: OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentifiableObjects,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_
            (OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty):
        body (IdentifiableObjects):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        property_=property_,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    property_: OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentifiableObjects,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_
            (OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty):
        body (IdentifiableObjects):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        uid=uid,
        property_=property_,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uid: str,
    property_: OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentifiableObjects,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_
            (OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty):
        body (IdentifiableObjects):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        property_=property_,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    property_: OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IdentifiableObjects,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an OrganisationUnitGroup object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnitGroup`) Example: Co7xX6sn5Ve.
        property_
            (OrganisationUnitGroupDeleteCollectionItemsJsondeleteCollectionItemsXmlProperty):
        body (IdentifiableObjects):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            uid=uid,
            property_=property_,
            client=client,
            body=body,
        )
    ).parsed
