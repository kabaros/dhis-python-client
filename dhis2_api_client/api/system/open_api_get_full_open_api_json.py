from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fail_on_inconsistency: Union[Unset, bool] = False,
    fail_on_name_clash: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["failOnInconsistency"] = fail_on_inconsistency

    params["failOnNameClash"] = fail_on_name_clash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/openapi.json",
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
    fail_on_inconsistency: Union[Unset, bool] = False,
    fail_on_name_clash: Union[Unset, bool] = False,
) -> Response[Any]:
    """[no description yet]

    Args:
        fail_on_inconsistency (Union[Unset, bool]):  Default: False.
        fail_on_name_clash (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fail_on_inconsistency=fail_on_inconsistency,
        fail_on_name_clash=fail_on_name_clash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fail_on_inconsistency: Union[Unset, bool] = False,
    fail_on_name_clash: Union[Unset, bool] = False,
) -> Response[Any]:
    """[no description yet]

    Args:
        fail_on_inconsistency (Union[Unset, bool]):  Default: False.
        fail_on_name_clash (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fail_on_inconsistency=fail_on_inconsistency,
        fail_on_name_clash=fail_on_name_clash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
