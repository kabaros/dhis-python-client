from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, str] = UNSET,
    notification_sent: Union[Unset, bool] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    unconstrained: Union[Unset, bool] = UNSET,
    vr: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["created"] = created

    params["notificationSent"] = notification_sent

    json_ou: Union[Unset, list[str]] = UNSET
    if not isinstance(ou, Unset):
        json_ou = ou

    params["ou"] = json_ou

    params["pe"] = pe

    params["unconstrained"] = unconstrained

    json_vr: Union[Unset, list[str]] = UNSET
    if not isinstance(vr, Unset):
        json_vr = vr

    params["vr"] = json_vr

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/validationResults/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
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
    created: Union[Unset, str] = UNSET,
    notification_sent: Union[Unset, bool] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    unconstrained: Union[Unset, bool] = UNSET,
    vr: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        created (Union[Unset, str]):
        notification_sent (Union[Unset, bool]):
        ou (Union[Unset, list[str]]):
        pe (Union[Unset, str]):
        unconstrained (Union[Unset, bool]):
        vr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        notification_sent=notification_sent,
        ou=ou,
        pe=pe,
        unconstrained=unconstrained,
        vr=vr,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    created: Union[Unset, str] = UNSET,
    notification_sent: Union[Unset, bool] = UNSET,
    ou: Union[Unset, list[str]] = UNSET,
    pe: Union[Unset, str] = UNSET,
    unconstrained: Union[Unset, bool] = UNSET,
    vr: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        created (Union[Unset, str]):
        notification_sent (Union[Unset, bool]):
        ou (Union[Unset, list[str]]):
        pe (Union[Unset, str]):
        unconstrained (Union[Unset, bool]):
        vr (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        created=created,
        notification_sent=notification_sent,
        ou=ou,
        pe=pe,
        unconstrained=unconstrained,
        vr=vr,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
