from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organisation_unit import OrganisationUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    distance: float,
    latitude: float,
    longitude: float,
    org_unit_group_set_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["distance"] = distance

    params["latitude"] = latitude

    params["longitude"] = longitude

    params["orgUnitGroupSetId"] = org_unit_group_set_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organisationUnitLocations/withinRange",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["OrganisationUnit"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OrganisationUnit.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["OrganisationUnit"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    distance: float,
    latitude: float,
    longitude: float,
    org_unit_group_set_id: Union[Unset, str] = UNSET,
) -> Response[list["OrganisationUnit"]]:
    """[no description yet]

    Args:
        distance (float):
        latitude (float):
        longitude (float):
        org_unit_group_set_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OrganisationUnit']]
    """

    kwargs = _get_kwargs(
        distance=distance,
        latitude=latitude,
        longitude=longitude,
        org_unit_group_set_id=org_unit_group_set_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    distance: float,
    latitude: float,
    longitude: float,
    org_unit_group_set_id: Union[Unset, str] = UNSET,
) -> Optional[list["OrganisationUnit"]]:
    """[no description yet]

    Args:
        distance (float):
        latitude (float):
        longitude (float):
        org_unit_group_set_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OrganisationUnit']
    """

    return sync_detailed(
        client=client,
        distance=distance,
        latitude=latitude,
        longitude=longitude,
        org_unit_group_set_id=org_unit_group_set_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    distance: float,
    latitude: float,
    longitude: float,
    org_unit_group_set_id: Union[Unset, str] = UNSET,
) -> Response[list["OrganisationUnit"]]:
    """[no description yet]

    Args:
        distance (float):
        latitude (float):
        longitude (float):
        org_unit_group_set_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['OrganisationUnit']]
    """

    kwargs = _get_kwargs(
        distance=distance,
        latitude=latitude,
        longitude=longitude,
        org_unit_group_set_id=org_unit_group_set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    distance: float,
    latitude: float,
    longitude: float,
    org_unit_group_set_id: Union[Unset, str] = UNSET,
) -> Optional[list["OrganisationUnit"]]:
    """[no description yet]

    Args:
        distance (float):
        latitude (float):
        longitude (float):
        org_unit_group_set_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['OrganisationUnit']
    """

    return (
        await asyncio_detailed(
            client=client,
            distance=distance,
            latitude=latitude,
            longitude=longitude,
            org_unit_group_set_id=org_unit_group_set_id,
        )
    ).parsed
