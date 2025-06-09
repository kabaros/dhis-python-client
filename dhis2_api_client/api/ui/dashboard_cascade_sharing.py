from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cascade_sharing_report import CascadeSharingReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    atomic: Union[Unset, bool] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["atomic"] = atomic

    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/dashboards/cascadeSharing/{uid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CascadeSharingReport]:
    if response.status_code == 200:
        response_200 = CascadeSharingReport.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CascadeSharingReport]:
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
    atomic: Union[Unset, bool] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Response[CascadeSharingReport]:
    """[no description yet]

    Args:
        uid (str):
        atomic (Union[Unset, bool]):
        dry_run (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CascadeSharingReport]
    """

    kwargs = _get_kwargs(
        uid=uid,
        atomic=atomic,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    atomic: Union[Unset, bool] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Optional[CascadeSharingReport]:
    """[no description yet]

    Args:
        uid (str):
        atomic (Union[Unset, bool]):
        dry_run (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CascadeSharingReport
    """

    return sync_detailed(
        uid=uid,
        client=client,
        atomic=atomic,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    atomic: Union[Unset, bool] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Response[CascadeSharingReport]:
    """[no description yet]

    Args:
        uid (str):
        atomic (Union[Unset, bool]):
        dry_run (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CascadeSharingReport]
    """

    kwargs = _get_kwargs(
        uid=uid,
        atomic=atomic,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    atomic: Union[Unset, bool] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Optional[CascadeSharingReport]:
    """[no description yet]

    Args:
        uid (str):
        atomic (Union[Unset, bool]):
        dry_run (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CascadeSharingReport
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            atomic=atomic,
            dry_run=dry_run,
        )
    ).parsed
