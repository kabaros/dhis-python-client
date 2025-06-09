from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ou: str,
    program: str,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ou"] = ou

    params["program"] = program

    params["trackedEntity"] = tracked_entity

    params["trackedEntityInstance"] = tracked_entity_instance

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/tracker/ownership/transfer",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ou: str,
    program: str,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        ou (str):
        program (str):
        tracked_entity (Union[Unset, str]):
        tracked_entity_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        ou=ou,
        program=program,
        tracked_entity=tracked_entity,
        tracked_entity_instance=tracked_entity_instance,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ou: str,
    program: str,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        ou (str):
        program (str):
        tracked_entity (Union[Unset, str]):
        tracked_entity_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        ou=ou,
        program=program,
        tracked_entity=tracked_entity,
        tracked_entity_instance=tracked_entity_instance,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ou: str,
    program: str,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        ou (str):
        program (str):
        tracked_entity (Union[Unset, str]):
        tracked_entity_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        ou=ou,
        program=program,
        tracked_entity=tracked_entity,
        tracked_entity_instance=tracked_entity_instance,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ou: str,
    program: str,
    tracked_entity: Union[Unset, str] = UNSET,
    tracked_entity_instance: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        ou (str):
        program (str):
        tracked_entity (Union[Unset, str]):
        tracked_entity_instance (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            ou=ou,
            program=program,
            tracked_entity=tracked_entity,
            tracked_entity_instance=tracked_entity_instance,
        )
    ).parsed
