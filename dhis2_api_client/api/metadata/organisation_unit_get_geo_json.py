from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organisation_unit import OrganisationUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    level: Union[Unset, list[int]] = UNSET,
    parent: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    properties: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_level: Union[Unset, list[int]] = UNSET
    if not isinstance(level, Unset):
        json_level = level

    params["level"] = json_level

    json_parent: Union[Unset, dict[str, Any], list[str]]
    if isinstance(parent, Unset):
        json_parent = UNSET
    elif isinstance(parent, list):
        json_parent = parent

    else:
        json_parent = parent.to_dict()

    params["parent"] = json_parent

    params["properties"] = properties

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/organisationUnits/#getGeoJson",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
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
    level: Union[Unset, list[int]] = UNSET,
    parent: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    properties: Union[Unset, bool] = True,
) -> Response[Any]:
    """[no description yet]

    Args:
        level (Union[Unset, list[int]]):
        parent (Union['OrganisationUnit', Unset, list[str]]):
        properties (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        level=level,
        parent=parent,
        properties=properties,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    level: Union[Unset, list[int]] = UNSET,
    parent: Union["OrganisationUnit", Unset, list[str]] = UNSET,
    properties: Union[Unset, bool] = True,
) -> Response[Any]:
    """[no description yet]

    Args:
        level (Union[Unset, list[int]]):
        parent (Union['OrganisationUnit', Unset, list[str]]):
        properties (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        level=level,
        parent=parent,
        properties=properties,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
