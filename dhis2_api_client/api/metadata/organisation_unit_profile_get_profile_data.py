from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.org_unit_profile_data import OrgUnitProfileData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    period: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/organisationUnitProfile/{uid}/data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OrgUnitProfileData]:
    if response.status_code == 200:
        response_200 = OrgUnitProfileData.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OrgUnitProfileData]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Response[OrgUnitProfileData]:
    """[no description yet]

    Args:
        uid (str):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgUnitProfileData]
    """

    kwargs = _get_kwargs(
        uid=uid,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Optional[OrgUnitProfileData]:
    """[no description yet]

    Args:
        uid (str):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgUnitProfileData
    """

    return sync_detailed(
        uid=uid,
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Response[OrgUnitProfileData]:
    """[no description yet]

    Args:
        uid (str):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgUnitProfileData]
    """

    kwargs = _get_kwargs(
        uid=uid,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    period: Union[Unset, str] = UNSET,
) -> Optional[OrgUnitProfileData]:
    """[no description yet]

    Args:
        uid (str):
        period (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgUnitProfileData
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            period=period,
        )
    ).parsed
