from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.form import Form
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    category_options: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    meta_data: Union[Unset, bool] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["categoryOptions"] = category_options

    params["locale"] = locale

    params["metaData"] = meta_data

    params["ou"] = ou

    params["pe"] = pe

    params["translate"] = translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dataSets/{uid}/form",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Form, WebMessage]]:
    if response.status_code == 200:
        response_200 = Form.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Form, WebMessage]]:
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
    category_options: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    meta_data: Union[Unset, bool] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[Form, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        category_options (Union[Unset, str]):
        locale (Union[Unset, str]):
        meta_data (Union[Unset, bool]):
        ou (Union[Unset, str]):
        pe (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Form, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        category_options=category_options,
        locale=locale,
        meta_data=meta_data,
        ou=ou,
        pe=pe,
        translate=translate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category_options: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    meta_data: Union[Unset, bool] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[Form, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        category_options (Union[Unset, str]):
        locale (Union[Unset, str]):
        meta_data (Union[Unset, bool]):
        ou (Union[Unset, str]):
        pe (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Form, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        client=client,
        category_options=category_options,
        locale=locale,
        meta_data=meta_data,
        ou=ou,
        pe=pe,
        translate=translate,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category_options: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    meta_data: Union[Unset, bool] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[Form, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        category_options (Union[Unset, str]):
        locale (Union[Unset, str]):
        meta_data (Union[Unset, bool]):
        ou (Union[Unset, str]):
        pe (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Form, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        category_options=category_options,
        locale=locale,
        meta_data=meta_data,
        ou=ou,
        pe=pe,
        translate=translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category_options: Union[Unset, str] = UNSET,
    locale: Union[Unset, str] = UNSET,
    meta_data: Union[Unset, bool] = UNSET,
    ou: Union[Unset, str] = UNSET,
    pe: Union[Unset, str] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[Form, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        category_options (Union[Unset, str]):
        locale (Union[Unset, str]):
        meta_data (Union[Unset, bool]):
        ou (Union[Unset, str]):
        pe (Union[Unset, str]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Form, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            category_options=category_options,
            locale=locale,
            meta_data=meta_data,
            ou=ou,
            pe=pe,
            translate=translate,
        )
    ).parsed
