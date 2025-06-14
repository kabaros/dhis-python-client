from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_integrity_details import DataIntegrityDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    check: str,
    *,
    timeout: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["timeout"] = timeout

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dataIntegrity/{check}/details",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DataIntegrityDetails]:
    if response.status_code == 200:
        response_200 = DataIntegrityDetails.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DataIntegrityDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    check: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timeout: Union[Unset, int] = 0,
) -> Response[DataIntegrityDetails]:
    """[no description yet]

    Args:
        check (str):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrityDetails]
    """

    kwargs = _get_kwargs(
        check=check,
        timeout=timeout,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    check: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timeout: Union[Unset, int] = 0,
) -> Optional[DataIntegrityDetails]:
    """[no description yet]

    Args:
        check (str):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrityDetails
    """

    return sync_detailed(
        check=check,
        client=client,
        timeout=timeout,
    ).parsed


async def asyncio_detailed(
    check: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timeout: Union[Unset, int] = 0,
) -> Response[DataIntegrityDetails]:
    """[no description yet]

    Args:
        check (str):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataIntegrityDetails]
    """

    kwargs = _get_kwargs(
        check=check,
        timeout=timeout,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    check: str,
    *,
    client: Union[AuthenticatedClient, Client],
    timeout: Union[Unset, int] = 0,
) -> Optional[DataIntegrityDetails]:
    """[no description yet]

    Args:
        check (str):
        timeout (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataIntegrityDetails
    """

    return (
        await asyncio_detailed(
            check=check,
            client=client,
            timeout=timeout,
        )
    ).parsed
