from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tracked_entity_instance_get_attribute_image_dimension import (
    TrackedEntityInstanceGetAttributeImageDimension,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tei_id: str,
    attribute_id: str,
    *,
    dimension: Union[Unset, TrackedEntityInstanceGetAttributeImageDimension] = UNSET,
    height: Union[Unset, int] = UNSET,
    program_id: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_dimension: Union[Unset, str] = UNSET
    if not isinstance(dimension, Unset):
        json_dimension = dimension.value

    params["dimension"] = json_dimension

    params["height"] = height

    params["programId"] = program_id

    params["width"] = width

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/trackedEntityInstances/{tei_id}/{attribute_id}/image",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WebMessage]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tei_id: str,
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntityInstanceGetAttributeImageDimension] = UNSET,
    height: Union[Unset, int] = UNSET,
    program_id: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        tei_id (str):
        attribute_id (str):
        dimension (Union[Unset, TrackedEntityInstanceGetAttributeImageDimension]):
        height (Union[Unset, int]):
        program_id (Union[Unset, str]):
        width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        tei_id=tei_id,
        attribute_id=attribute_id,
        dimension=dimension,
        height=height,
        program_id=program_id,
        width=width,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tei_id: str,
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntityInstanceGetAttributeImageDimension] = UNSET,
    height: Union[Unset, int] = UNSET,
    program_id: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        tei_id (str):
        attribute_id (str):
        dimension (Union[Unset, TrackedEntityInstanceGetAttributeImageDimension]):
        height (Union[Unset, int]):
        program_id (Union[Unset, str]):
        width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return sync_detailed(
        tei_id=tei_id,
        attribute_id=attribute_id,
        client=client,
        dimension=dimension,
        height=height,
        program_id=program_id,
        width=width,
    ).parsed


async def asyncio_detailed(
    tei_id: str,
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntityInstanceGetAttributeImageDimension] = UNSET,
    height: Union[Unset, int] = UNSET,
    program_id: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> Response[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        tei_id (str):
        attribute_id (str):
        dimension (Union[Unset, TrackedEntityInstanceGetAttributeImageDimension]):
        height (Union[Unset, int]):
        program_id (Union[Unset, str]):
        width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        tei_id=tei_id,
        attribute_id=attribute_id,
        dimension=dimension,
        height=height,
        program_id=program_id,
        width=width,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tei_id: str,
    attribute_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntityInstanceGetAttributeImageDimension] = UNSET,
    height: Union[Unset, int] = UNSET,
    program_id: Union[Unset, str] = UNSET,
    width: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, WebMessage]]:
    """[no description yet]

    Args:
        tei_id (str):
        attribute_id (str):
        dimension (Union[Unset, TrackedEntityInstanceGetAttributeImageDimension]):
        height (Union[Unset, int]):
        program_id (Union[Unset, str]):
        width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return (
        await asyncio_detailed(
            tei_id=tei_id,
            attribute_id=attribute_id,
            client=client,
            dimension=dimension,
            height=height,
            program_id=program_id,
            width=width,
        )
    ).parsed
