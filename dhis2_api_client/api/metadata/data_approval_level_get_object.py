from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_approval_level import DataApprovalLevel
from ...models.data_approval_level_get_object_root_junction import DataApprovalLevelGetObjectRootJunction
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, DataApprovalLevelGetObjectRootJunction] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_filter_: Union[Unset, list[str]] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_

    params["filter"] = json_filter_

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dataApprovalLevels/{uid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DataApprovalLevel, WebMessage]]:
    if response.status_code == 200:
        response_200 = DataApprovalLevel.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DataApprovalLevel, WebMessage]]:
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
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, DataApprovalLevelGetObjectRootJunction] = UNSET,
) -> Response[Union[DataApprovalLevel, WebMessage]]:
    """View a DataApprovalLevel

    Args:
        uid (str): A UID for an DataApprovalLevel object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalLevel`) Example: n3zt98lA14W.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, DataApprovalLevelGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataApprovalLevel, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        fields=fields,
        filter_=filter_,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, DataApprovalLevelGetObjectRootJunction] = UNSET,
) -> Optional[Union[DataApprovalLevel, WebMessage]]:
    """View a DataApprovalLevel

    Args:
        uid (str): A UID for an DataApprovalLevel object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalLevel`) Example: n3zt98lA14W.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, DataApprovalLevelGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataApprovalLevel, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        client=client,
        fields=fields,
        filter_=filter_,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, DataApprovalLevelGetObjectRootJunction] = UNSET,
) -> Response[Union[DataApprovalLevel, WebMessage]]:
    """View a DataApprovalLevel

    Args:
        uid (str): A UID for an DataApprovalLevel object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalLevel`) Example: n3zt98lA14W.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, DataApprovalLevelGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataApprovalLevel, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        fields=fields,
        filter_=filter_,
        page=page,
        page_size=page_size,
        paging=paging,
        root_junction=root_junction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
    filter_: Union[Unset, list[str]] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    root_junction: Union[Unset, DataApprovalLevelGetObjectRootJunction] = UNSET,
) -> Optional[Union[DataApprovalLevel, WebMessage]]:
    """View a DataApprovalLevel

    Args:
        uid (str): A UID for an DataApprovalLevel object
            (Java name `org.hisp.dhis.dataapproval.DataApprovalLevel`) Example: n3zt98lA14W.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, DataApprovalLevelGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataApprovalLevel, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            fields=fields,
            filter_=filter_,
            page=page,
            page_size=page_size,
            paging=paging,
            root_junction=root_junction,
        )
    ).parsed
