from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.field_path import FieldPath
from ...models.trigram_summary import TrigramSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.to_dict()
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/trigramSummary/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TrigramSummary]:
    if response.status_code == 200:
        response_200 = TrigramSummary.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TrigramSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Response[TrigramSummary]:
    """[no description yet]

    Args:
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrigramSummary]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Optional[TrigramSummary]:
    """[no description yet]

    Args:
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrigramSummary
    """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Response[TrigramSummary]:
    """[no description yet]

    Args:
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrigramSummary]
    """

    kwargs = _get_kwargs(
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Optional[TrigramSummary]:
    """[no description yet]

    Args:
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TrigramSummary
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
