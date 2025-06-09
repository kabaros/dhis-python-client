from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.section_get_object_list_csv_root_junction import SectionGetObjectListCsvRootJunction
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    array_separator: Union[Unset, str] = ";",
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, SectionGetObjectListCsvRootJunction] = UNSET,
    separator: Union[Unset, str] = ",",
    skip_header: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["arraySeparator"] = array_separator

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    json_orders: Union[Unset, list[str]] = UNSET
    if not isinstance(orders, Unset):
        json_orders = orders

    params["orders"] = json_orders

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params["separator"] = separator

    params["skipHeader"] = skip_header

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sections/#getObjectListCsv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[WebMessage, str]]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.text)

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.text)

        return response_403
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.text)

        return response_404
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.text)

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[WebMessage, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    array_separator: Union[Unset, str] = ";",
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, SectionGetObjectListCsvRootJunction] = UNSET,
    separator: Union[Unset, str] = ",",
    skip_header: Union[Unset, bool] = False,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        array_separator (Union[Unset, str]):  Default: ';'.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, SectionGetObjectListCsvRootJunction]):
        separator (Union[Unset, str]):  Default: ','.
        skip_header (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        array_separator=array_separator,
        fields=fields,
        filter_=filter_,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        separator=separator,
        skip_header=skip_header,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    array_separator: Union[Unset, str] = ";",
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, SectionGetObjectListCsvRootJunction] = UNSET,
    separator: Union[Unset, str] = ",",
    skip_header: Union[Unset, bool] = False,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        array_separator (Union[Unset, str]):  Default: ';'.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, SectionGetObjectListCsvRootJunction]):
        separator (Union[Unset, str]):  Default: ','.
        skip_header (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return sync_detailed(
        client=client,
        array_separator=array_separator,
        fields=fields,
        filter_=filter_,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        separator=separator,
        skip_header=skip_header,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    array_separator: Union[Unset, str] = ";",
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, SectionGetObjectListCsvRootJunction] = UNSET,
    separator: Union[Unset, str] = ",",
    skip_header: Union[Unset, bool] = False,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        array_separator (Union[Unset, str]):  Default: ';'.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, SectionGetObjectListCsvRootJunction]):
        separator (Union[Unset, str]):  Default: ','.
        skip_header (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        array_separator=array_separator,
        fields=fields,
        filter_=filter_,
        orders=orders,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
        separator=separator,
        skip_header=skip_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    array_separator: Union[Unset, str] = ";",
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    orders: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, SectionGetObjectListCsvRootJunction] = UNSET,
    separator: Union[Unset, str] = ",",
    skip_header: Union[Unset, bool] = False,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        array_separator (Union[Unset, str]):  Default: ';'.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        orders (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, SectionGetObjectListCsvRootJunction]):
        separator (Union[Unset, str]):  Default: ','.
        skip_header (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            array_separator=array_separator,
            fields=fields,
            filter_=filter_,
            orders=orders,
            page=page,
            page_size=page_size,
            paging=paging,
            root_junction=root_junction,
            separator=separator,
            skip_header=skip_header,
        )
    ).parsed
