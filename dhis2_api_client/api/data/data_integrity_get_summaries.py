from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_integrity_get_summaries_response_200 import DataIntegrityGetSummariesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    checks: Union[Unset, list[str]] = UNSET,
    timeout: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_checks: Union[Unset, list[str]] = UNSET
    if not isinstance(checks, Unset):
        json_checks = checks

    params["checks"] = json_checks

    params["timeout"] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataIntegrity/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DataIntegrityGetSummariesResponse200]:
    if response.status_code == 200:
        response_200 = DataIntegrityGetSummariesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DataIntegrityGetSummariesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    checks: Union[Unset, list[str]] = UNSET,
    timeout: Union[Unset, int] = 0,
) -> Response[DataIntegrityGetSummariesResponse200]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrityGetSummariesResponse200]
    """

    kwargs = _get_kwargs(
        checks=checks,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    checks: Union[Unset, list[str]] = UNSET,
    timeout: Union[Unset, int] = 0,
) -> Optional[DataIntegrityGetSummariesResponse200]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrityGetSummariesResponse200
    """

    return sync_detailed(
        client=client,
        checks=checks,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    checks: Union[Unset, list[str]] = UNSET,
    timeout: Union[Unset, int] = 0,
) -> Response[DataIntegrityGetSummariesResponse200]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrityGetSummariesResponse200]
    """

    kwargs = _get_kwargs(
        checks=checks,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    checks: Union[Unset, list[str]] = UNSET,
    timeout: Union[Unset, int] = 0,
) -> Optional[DataIntegrityGetSummariesResponse200]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrityGetSummariesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            checks=checks,
            timeout=timeout,
        )
    ).parsed
