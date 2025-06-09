from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_set_get_object_list_gistget_object_list_gist_as_csv_auto import (
    DataSetGetObjectListGistgetObjectListGistAsCsvAuto,
)
from ...models.data_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_0 import (
    DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0,
)
from ...models.data_set_get_object_list_gistget_object_list_gist_as_csv_response_200_type_1_item import (
    DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item,
)
from ...models.data_set_get_object_list_gistget_object_list_gist_as_csv_root_junction import (
    DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto] = UNSET,
    describe: Union[Unset, bool] = False,
    fields: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    inverse: Union[Unset, bool] = False,
    locale: Union[Unset, str] = "",
    order: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_list_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    references: Union[Unset, bool] = True,
    root_junction: Union[
        Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction
    ] = DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["absoluteUrls"] = absolute_urls

    json_auto: Union[Unset, str] = UNSET
    if not isinstance(auto, Unset):
        json_auto = auto.value

    params["auto"] = json_auto

    params["describe"] = describe

    params["fields"] = fields

    params["filter"] = filter_

    params["headless"] = headless

    params["inverse"] = inverse

    params["locale"] = locale

    params["order"] = order

    params["page"] = page

    params["pageListName"] = page_list_name

    params["pageSize"] = page_size

    params["references"] = references

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params["total"] = total

    params["totalPages"] = total_pages

    params["translate"] = translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataSets/gist",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Union[
            "DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0",
            list["DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item"],
        ],
        WebMessage,
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0",
            list["DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item"],
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = []
            _response_200_type_1 = data
            for response_200_type_1_item_data in _response_200_type_1:
                response_200_type_1_item = DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item.from_dict(
                    response_200_type_1_item_data
                )

                response_200_type_1.append(response_200_type_1_item)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Union[
            "DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0",
            list["DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item"],
        ],
        WebMessage,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto] = UNSET,
    describe: Union[Unset, bool] = False,
    fields: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    inverse: Union[Unset, bool] = False,
    locale: Union[Unset, str] = "",
    order: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_list_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    references: Union[Unset, bool] = True,
    root_junction: Union[
        Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction
    ] = DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[
    Union[
        Union[
            "DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0",
            list["DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item"],
        ],
        WebMessage,
    ]
]:
    """[no description yet]

    Args:
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto]):
        describe (Union[Unset, bool]):  Default: False.
        fields (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        inverse (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):  Default: ''.
        order (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_list_name (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        references (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction]):
            Default: DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Union['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0', list['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item']], WebMessage]]
    """

    kwargs = _get_kwargs(
        absolute_urls=absolute_urls,
        auto=auto,
        describe=describe,
        fields=fields,
        filter_=filter_,
        headless=headless,
        inverse=inverse,
        locale=locale,
        order=order,
        page=page,
        page_list_name=page_list_name,
        page_size=page_size,
        references=references,
        root_junction=root_junction,
        total=total,
        total_pages=total_pages,
        translate=translate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto] = UNSET,
    describe: Union[Unset, bool] = False,
    fields: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    inverse: Union[Unset, bool] = False,
    locale: Union[Unset, str] = "",
    order: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_list_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    references: Union[Unset, bool] = True,
    root_junction: Union[
        Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction
    ] = DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[
    Union[
        Union[
            "DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0",
            list["DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item"],
        ],
        WebMessage,
    ]
]:
    """[no description yet]

    Args:
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto]):
        describe (Union[Unset, bool]):  Default: False.
        fields (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        inverse (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):  Default: ''.
        order (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_list_name (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        references (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction]):
            Default: DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Union['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0', list['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item']], WebMessage]
    """

    return sync_detailed(
        client=client,
        absolute_urls=absolute_urls,
        auto=auto,
        describe=describe,
        fields=fields,
        filter_=filter_,
        headless=headless,
        inverse=inverse,
        locale=locale,
        order=order,
        page=page,
        page_list_name=page_list_name,
        page_size=page_size,
        references=references,
        root_junction=root_junction,
        total=total,
        total_pages=total_pages,
        translate=translate,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto] = UNSET,
    describe: Union[Unset, bool] = False,
    fields: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    inverse: Union[Unset, bool] = False,
    locale: Union[Unset, str] = "",
    order: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_list_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    references: Union[Unset, bool] = True,
    root_junction: Union[
        Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction
    ] = DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[
    Union[
        Union[
            "DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0",
            list["DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item"],
        ],
        WebMessage,
    ]
]:
    """[no description yet]

    Args:
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto]):
        describe (Union[Unset, bool]):  Default: False.
        fields (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        inverse (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):  Default: ''.
        order (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_list_name (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        references (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction]):
            Default: DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Union['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0', list['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item']], WebMessage]]
    """

    kwargs = _get_kwargs(
        absolute_urls=absolute_urls,
        auto=auto,
        describe=describe,
        fields=fields,
        filter_=filter_,
        headless=headless,
        inverse=inverse,
        locale=locale,
        order=order,
        page=page,
        page_list_name=page_list_name,
        page_size=page_size,
        references=references,
        root_junction=root_junction,
        total=total,
        total_pages=total_pages,
        translate=translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto] = UNSET,
    describe: Union[Unset, bool] = False,
    fields: Union[Unset, str] = UNSET,
    filter_: Union[Unset, str] = UNSET,
    headless: Union[Unset, bool] = False,
    inverse: Union[Unset, bool] = False,
    locale: Union[Unset, str] = "",
    order: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    page_list_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = 50,
    references: Union[Unset, bool] = True,
    root_junction: Union[
        Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction
    ] = DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[
    Union[
        Union[
            "DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0",
            list["DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item"],
        ],
        WebMessage,
    ]
]:
    """[no description yet]

    Args:
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvAuto]):
        describe (Union[Unset, bool]):  Default: False.
        fields (Union[Unset, str]):
        filter_ (Union[Unset, str]):
        headless (Union[Unset, bool]):  Default: False.
        inverse (Union[Unset, bool]):  Default: False.
        locale (Union[Unset, str]):  Default: ''.
        order (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        page_list_name (Union[Unset, str]):
        page_size (Union[Unset, int]):  Default: 50.
        references (Union[Unset, bool]):  Default: True.
        root_junction (Union[Unset, DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction]):
            Default: DataSetGetObjectListGistgetObjectListGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Union['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type0', list['DataSetGetObjectListGistgetObjectListGistAsCsvResponse200Type1Item']], WebMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            absolute_urls=absolute_urls,
            auto=auto,
            describe=describe,
            fields=fields,
            filter_=filter_,
            headless=headless,
            inverse=inverse,
            locale=locale,
            order=order,
            page=page,
            page_list_name=page_list_name,
            page_size=page_size,
            references=references,
            root_junction=root_junction,
            total=total,
            total_pages=total_pages,
            translate=translate,
        )
    ).parsed
