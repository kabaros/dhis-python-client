from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_get_object_gist_as_csv_auto import DashboardGetObjectGistAsCsvAuto
from ...models.dashboard_get_object_gist_as_csv_root_junction import DashboardGetObjectGistAsCsvRootJunction
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DashboardGetObjectGistAsCsvAuto] = UNSET,
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
    root_junction: Union[Unset, DashboardGetObjectGistAsCsvRootJunction] = DashboardGetObjectGistAsCsvRootJunction.AND,
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
        "url": f"/dashboards/{uid}/gist.csv",
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DashboardGetObjectGistAsCsvAuto] = UNSET,
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
    root_junction: Union[Unset, DashboardGetObjectGistAsCsvRootJunction] = DashboardGetObjectGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str): A UID for an Dashboard object
            (Java name `org.hisp.dhis.dashboard.Dashboard`) Example: fV5sz4Ys38O.
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DashboardGetObjectGistAsCsvAuto]):
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
        root_junction (Union[Unset, DashboardGetObjectGistAsCsvRootJunction]):  Default:
            DashboardGetObjectGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        uid=uid,
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DashboardGetObjectGistAsCsvAuto] = UNSET,
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
    root_junction: Union[Unset, DashboardGetObjectGistAsCsvRootJunction] = DashboardGetObjectGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str): A UID for an Dashboard object
            (Java name `org.hisp.dhis.dashboard.Dashboard`) Example: fV5sz4Ys38O.
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DashboardGetObjectGistAsCsvAuto]):
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
        root_junction (Union[Unset, DashboardGetObjectGistAsCsvRootJunction]):  Default:
            DashboardGetObjectGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return sync_detailed(
        uid=uid,
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DashboardGetObjectGistAsCsvAuto] = UNSET,
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
    root_junction: Union[Unset, DashboardGetObjectGistAsCsvRootJunction] = DashboardGetObjectGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Response[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str): A UID for an Dashboard object
            (Java name `org.hisp.dhis.dashboard.Dashboard`) Example: fV5sz4Ys38O.
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DashboardGetObjectGistAsCsvAuto]):
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
        root_junction (Union[Unset, DashboardGetObjectGistAsCsvRootJunction]):  Default:
            DashboardGetObjectGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WebMessage, str]]
    """

    kwargs = _get_kwargs(
        uid=uid,
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    absolute_urls: Union[Unset, bool] = False,
    auto: Union[Unset, DashboardGetObjectGistAsCsvAuto] = UNSET,
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
    root_junction: Union[Unset, DashboardGetObjectGistAsCsvRootJunction] = DashboardGetObjectGistAsCsvRootJunction.AND,
    total: Union[Unset, bool] = UNSET,
    total_pages: Union[Unset, bool] = UNSET,
    translate: Union[Unset, bool] = True,
) -> Optional[Union[WebMessage, str]]:
    """[no description yet]

    Args:
        uid (str): A UID for an Dashboard object
            (Java name `org.hisp.dhis.dashboard.Dashboard`) Example: fV5sz4Ys38O.
        absolute_urls (Union[Unset, bool]):  Default: False.
        auto (Union[Unset, DashboardGetObjectGistAsCsvAuto]):
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
        root_junction (Union[Unset, DashboardGetObjectGistAsCsvRootJunction]):  Default:
            DashboardGetObjectGistAsCsvRootJunction.AND.
        total (Union[Unset, bool]):
        total_pages (Union[Unset, bool]):
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WebMessage, str]
    """

    return (
        await asyncio_detailed(
            uid=uid,
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
