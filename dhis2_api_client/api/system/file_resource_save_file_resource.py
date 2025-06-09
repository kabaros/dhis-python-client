from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_resource_save_file_resource_domain import FileResourceSaveFileResourceDomain
from ...models.web_message import WebMessage
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    *,
    domain: Union[Unset, FileResourceSaveFileResourceDomain] = FileResourceSaveFileResourceDomain.DATA_VALUE,
    file: File,
    uid: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_domain: Union[Unset, str] = UNSET
    if not isinstance(domain, Unset):
        json_domain = domain.value

    params["domain"] = json_domain

    json_file = file.to_tuple()

    params["file"] = json_file

    params["uid"] = uid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fileResources/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
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
    domain: Union[Unset, FileResourceSaveFileResourceDomain] = FileResourceSaveFileResourceDomain.DATA_VALUE,
    file: File,
    uid: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        domain (Union[Unset, FileResourceSaveFileResourceDomain]):  Default:
            FileResourceSaveFileResourceDomain.DATA_VALUE.
        file (File):
        uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        domain=domain,
        file=file,
        uid=uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    domain: Union[Unset, FileResourceSaveFileResourceDomain] = FileResourceSaveFileResourceDomain.DATA_VALUE,
    file: File,
    uid: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        domain (Union[Unset, FileResourceSaveFileResourceDomain]):  Default:
            FileResourceSaveFileResourceDomain.DATA_VALUE.
        file (File):
        uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        domain=domain,
        file=file,
        uid=uid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    domain: Union[Unset, FileResourceSaveFileResourceDomain] = FileResourceSaveFileResourceDomain.DATA_VALUE,
    file: File,
    uid: Union[Unset, str] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        domain (Union[Unset, FileResourceSaveFileResourceDomain]):  Default:
            FileResourceSaveFileResourceDomain.DATA_VALUE.
        file (File):
        uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        domain=domain,
        file=file,
        uid=uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    domain: Union[Unset, FileResourceSaveFileResourceDomain] = FileResourceSaveFileResourceDomain.DATA_VALUE,
    file: File,
    uid: Union[Unset, str] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        domain (Union[Unset, FileResourceSaveFileResourceDomain]):  Default:
            FileResourceSaveFileResourceDomain.DATA_VALUE.
        file (File):
        uid (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            domain=domain,
            file=file,
            uid=uid,
        )
    ).parsed
