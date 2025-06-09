from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_export_params import MetadataExportParams
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    download: Union[Unset, bool] = False,
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["download"] = download

    params["locale"] = locale

    params["translate"] = translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/metadata/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MetadataExportParams]:
    if response.status_code == 200:
        response_200 = MetadataExportParams.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MetadataExportParams]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    download: Union[Unset, bool] = False,
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = False,
) -> Response[MetadataExportParams]:
    """[no description yet]

    Args:
        download (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataExportParams]
    """

    kwargs = _get_kwargs(
        download=download,
        locale=locale,
        translate=translate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    download: Union[Unset, bool] = False,
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = False,
) -> Optional[MetadataExportParams]:
    """[no description yet]

    Args:
        download (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataExportParams
    """

    return sync_detailed(
        client=client,
        download=download,
        locale=locale,
        translate=translate,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    download: Union[Unset, bool] = False,
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = False,
) -> Response[MetadataExportParams]:
    """[no description yet]

    Args:
        download (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataExportParams]
    """

    kwargs = _get_kwargs(
        download=download,
        locale=locale,
        translate=translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    download: Union[Unset, bool] = False,
    locale: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = False,
) -> Optional[MetadataExportParams]:
    """[no description yet]

    Args:
        download (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataExportParams
    """

    return (
        await asyncio_detailed(
            client=client,
            download=download,
            locale=locale,
            translate=translate,
        )
    ).parsed
