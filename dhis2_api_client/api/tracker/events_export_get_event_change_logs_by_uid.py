from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.field_path import FieldPath
from ...models.order_criteria import OrderCriteria
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event: str,
    *,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.to_dict()
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_order: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(order, Unset):
        json_order = []
        for order_item_data in order:
            order_item = order_item_data.to_dict()
            json_order.append(order_item)

    params["order"] = json_order

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tracker/events/{event}/changeLogs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, WebMessage]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
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
    event: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
) -> Response[Union[Any, WebMessage]]:
    """Get the change logs of all data elements related to that particular event UID.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list['FieldPath']]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        event=event,
        fields=fields,
        order=order,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
) -> Optional[Union[Any, WebMessage]]:
    """Get the change logs of all data elements related to that particular event UID.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list['FieldPath']]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return sync_detailed(
        event=event,
        client=client,
        fields=fields,
        order=order,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    event: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
) -> Response[Union[Any, WebMessage]]:
    """Get the change logs of all data elements related to that particular event UID.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list['FieldPath']]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WebMessage]]
    """

    kwargs = _get_kwargs(
        event=event,
        fields=fields,
        order=order,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list["FieldPath"]] = UNSET,
    order: Union[Unset, list["OrderCriteria"]] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 50,
) -> Optional[Union[Any, WebMessage]]:
    """Get the change logs of all data elements related to that particular event UID.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        fields (Union[Unset, list['FieldPath']]):
        order (Union[Unset, list['OrderCriteria']]):
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WebMessage]
    """

    return (
        await asyncio_detailed(
            event=event,
            client=client,
            fields=fields,
            order=order,
            page=page,
            page_size=page_size,
        )
    ).parsed
