from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    async_: Union[Unset, bool] = False,
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
    geo_json_id: Union[Unset, bool] = True,
    geo_json_property: Union[Unset, str] = UNSET,
    org_unit_property: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["async"] = async_

    params["attributeId"] = attribute_id

    params["dryRun"] = dry_run

    params["geoJsonId"] = geo_json_id

    params["geoJsonProperty"] = geo_json_property

    params["orgUnitProperty"] = org_unit_property

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/organisationUnits/geometry",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
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
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
    geo_json_id: Union[Unset, bool] = True,
    geo_json_property: Union[Unset, str] = UNSET,
    org_unit_property: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        geo_json_id (Union[Unset, bool]):  Default: True.
        geo_json_property (Union[Unset, str]):
        org_unit_property (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        async_=async_,
        attribute_id=attribute_id,
        dry_run=dry_run,
        geo_json_id=geo_json_id,
        geo_json_property=geo_json_property,
        org_unit_property=org_unit_property,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
    geo_json_id: Union[Unset, bool] = True,
    geo_json_property: Union[Unset, str] = UNSET,
    org_unit_property: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        geo_json_id (Union[Unset, bool]):  Default: True.
        geo_json_property (Union[Unset, str]):
        org_unit_property (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        async_=async_,
        attribute_id=attribute_id,
        dry_run=dry_run,
        geo_json_id=geo_json_id,
        geo_json_property=geo_json_property,
        org_unit_property=org_unit_property,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
    geo_json_id: Union[Unset, bool] = True,
    geo_json_property: Union[Unset, str] = UNSET,
    org_unit_property: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        geo_json_id (Union[Unset, bool]):  Default: True.
        geo_json_property (Union[Unset, str]):
        org_unit_property (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        async_=async_,
        attribute_id=attribute_id,
        dry_run=dry_run,
        geo_json_id=geo_json_id,
        geo_json_property=geo_json_property,
        org_unit_property=org_unit_property,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    async_: Union[Unset, bool] = False,
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
    geo_json_id: Union[Unset, bool] = True,
    geo_json_property: Union[Unset, str] = UNSET,
    org_unit_property: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        async_ (Union[Unset, bool]):  Default: False.
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        geo_json_id (Union[Unset, bool]):  Default: True.
        geo_json_property (Union[Unset, str]):
        org_unit_property (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            async_=async_,
            attribute_id=attribute_id,
            dry_run=dry_run,
            geo_json_id=geo_json_id,
            geo_json_property=geo_json_property,
            org_unit_property=org_unit_property,
        )
    ).parsed
