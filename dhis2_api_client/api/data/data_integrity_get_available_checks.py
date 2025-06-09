from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_integrity_check import DataIntegrityCheck
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    checks: Union[Unset, list[str]] = UNSET,
    programmatic: Union[Unset, bool] = UNSET,
    section: Union[Unset, str] = UNSET,
    slow: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_checks: Union[Unset, list[str]] = UNSET
    if not isinstance(checks, Unset):
        json_checks = checks

    params["checks"] = json_checks

    params["programmatic"] = programmatic

    params["section"] = section

    params["slow"] = slow

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataIntegrity/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["DataIntegrityCheck"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataIntegrityCheck.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["DataIntegrityCheck"]]:
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
    programmatic: Union[Unset, bool] = UNSET,
    section: Union[Unset, str] = UNSET,
    slow: Union[Unset, bool] = UNSET,
) -> Response[list["DataIntegrityCheck"]]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        programmatic (Union[Unset, bool]):
        section (Union[Unset, str]):
        slow (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DataIntegrityCheck']]
    """

    kwargs = _get_kwargs(
        checks=checks,
        programmatic=programmatic,
        section=section,
        slow=slow,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    checks: Union[Unset, list[str]] = UNSET,
    programmatic: Union[Unset, bool] = UNSET,
    section: Union[Unset, str] = UNSET,
    slow: Union[Unset, bool] = UNSET,
) -> Optional[list["DataIntegrityCheck"]]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        programmatic (Union[Unset, bool]):
        section (Union[Unset, str]):
        slow (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DataIntegrityCheck']
    """

    return sync_detailed(
        client=client,
        checks=checks,
        programmatic=programmatic,
        section=section,
        slow=slow,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    checks: Union[Unset, list[str]] = UNSET,
    programmatic: Union[Unset, bool] = UNSET,
    section: Union[Unset, str] = UNSET,
    slow: Union[Unset, bool] = UNSET,
) -> Response[list["DataIntegrityCheck"]]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        programmatic (Union[Unset, bool]):
        section (Union[Unset, str]):
        slow (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['DataIntegrityCheck']]
    """

    kwargs = _get_kwargs(
        checks=checks,
        programmatic=programmatic,
        section=section,
        slow=slow,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    checks: Union[Unset, list[str]] = UNSET,
    programmatic: Union[Unset, bool] = UNSET,
    section: Union[Unset, str] = UNSET,
    slow: Union[Unset, bool] = UNSET,
) -> Optional[list["DataIntegrityCheck"]]:
    """[no description yet]

    Args:
        checks (Union[Unset, list[str]]):
        programmatic (Union[Unset, bool]):
        section (Union[Unset, str]):
        slow (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['DataIntegrityCheck']
    """

    return (
        await asyncio_detailed(
            client=client,
            checks=checks,
            programmatic=programmatic,
            section=section,
            slow=slow,
        )
    ).parsed
