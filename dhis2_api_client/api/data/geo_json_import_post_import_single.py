from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    body: Union[
        str,
        str,
    ],
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["attributeId"] = attribute_id

    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/organisationUnits/{uid}/geometry",
        "params": params,
    }

    if isinstance(body, str):
        _json_body = body

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/geo+json"
    if isinstance(body, str):
        _json_body = body

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        str,
        str,
    ],
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        body (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
        attribute_id=attribute_id,
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
    body: Union[
        str,
        str,
    ],
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        body (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        uid=uid,
        client=client,
        body=body,
        attribute_id=attribute_id,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        str,
        str,
    ],
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        body (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
        attribute_id=attribute_id,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        str,
        str,
    ],
    attribute_id: Union[Unset, str] = UNSET,
    dry_run: Union[Unset, bool] = UNSET,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str):
        attribute_id (Union[Unset, str]):
        dry_run (Union[Unset, bool]):
        body (str):
        body (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            body=body,
            attribute_id=attribute_id,
            dry_run=dry_run,
        )
    ).parsed
