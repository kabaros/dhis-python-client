from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entries_response import EntriesResponse
from ...models.user_datastore_get_entries_root_junction import UserDatastoreGetEntriesRootJunction
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: str,
    *,
    fields: str,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    include_all: Union[Unset, bool] = False,
    order: Union[Unset, str] = "_",
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    root_junction: Union[Unset, UserDatastoreGetEntriesRootJunction] = UserDatastoreGetEntriesRootJunction.AND,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["fields"] = fields

    params["filter"] = filter_

    params["headless"] = headless

    params["includeAll"] = include_all

    params["order"] = order

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/userDataStore/{namespace}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EntriesResponse, WebMessage]]:
    if response.status_code == 200:
        response_200 = EntriesResponse.from_dict(response.json())

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
) -> Response[Union[EntriesResponse, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: str,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    include_all: Union[Unset, bool] = False,
    order: Union[Unset, str] = "_",
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    root_junction: Union[Unset, UserDatastoreGetEntriesRootJunction] = UserDatastoreGetEntriesRootJunction.AND,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[EntriesResponse, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        fields (str):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        include_all (Union[Unset, bool]):  Default: False.
        order (Union[Unset, str]):  Default: '_'.
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, UserDatastoreGetEntriesRootJunction]):  Default:
            UserDatastoreGetEntriesRootJunction.AND.
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntriesResponse, WebMessage]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        fields=fields,
        filter_=filter_,
        headless=headless,
        include_all=include_all,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: str,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    include_all: Union[Unset, bool] = False,
    order: Union[Unset, str] = "_",
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    root_junction: Union[Unset, UserDatastoreGetEntriesRootJunction] = UserDatastoreGetEntriesRootJunction.AND,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[EntriesResponse, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        fields (str):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        include_all (Union[Unset, bool]):  Default: False.
        order (Union[Unset, str]):  Default: '_'.
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, UserDatastoreGetEntriesRootJunction]):  Default:
            UserDatastoreGetEntriesRootJunction.AND.
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntriesResponse, WebMessage]
    """

    return sync_detailed(
        namespace=namespace,
        client=client,
        fields=fields,
        filter_=filter_,
        headless=headless,
        include_all=include_all,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        username=username,
    ).parsed


async def asyncio_detailed(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: str,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    include_all: Union[Unset, bool] = False,
    order: Union[Unset, str] = "_",
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    root_junction: Union[Unset, UserDatastoreGetEntriesRootJunction] = UserDatastoreGetEntriesRootJunction.AND,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[EntriesResponse, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        fields (str):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        include_all (Union[Unset, bool]):  Default: False.
        order (Union[Unset, str]):  Default: '_'.
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, UserDatastoreGetEntriesRootJunction]):  Default:
            UserDatastoreGetEntriesRootJunction.AND.
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntriesResponse, WebMessage]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        fields=fields,
        filter_=filter_,
        headless=headless,
        include_all=include_all,
        order=order,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    namespace: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: str,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    include_all: Union[Unset, bool] = False,
    order: Union[Unset, str] = "_",
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
    paging: Union[Unset, bool] = True,
    root_junction: Union[Unset, UserDatastoreGetEntriesRootJunction] = UserDatastoreGetEntriesRootJunction.AND,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[EntriesResponse, WebMessage]]:
    """[no description yet]

    Args:
        namespace (str):
        fields (str):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        include_all (Union[Unset, bool]):  Default: False.
        order (Union[Unset, str]):  Default: '_'.
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.
        paging (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, UserDatastoreGetEntriesRootJunction]):  Default:
            UserDatastoreGetEntriesRootJunction.AND.
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntriesResponse, WebMessage]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            client=client,
            fields=fields,
            filter_=filter_,
            headless=headless,
            include_all=include_all,
            order=order,
            page=page,
            page_size=page_size,
            paging=paging,
            root_junction=root_junction,
            username=username,
        )
    ).parsed
