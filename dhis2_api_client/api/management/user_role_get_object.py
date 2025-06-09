from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_role import UserRole
from ...models.user_role_get_object_root_junction import UserRoleGetObjectRootJunction
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
    root_junction: Union[Unset, UserRoleGetObjectRootJunction] = UNSET,
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
        "url": f"/userRoles/{uid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[UserRole, WebMessage]]:
    if response.status_code == 200:
        response_200 = UserRole.from_dict(response.json())

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
) -> Response[Union[UserRole, WebMessage]]:
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
    root_junction: Union[Unset, UserRoleGetObjectRootJunction] = UNSET,
) -> Response[Union[UserRole, WebMessage]]:
    """View a UserRole

    Args:
        uid (str): A UID for an UserRole object
            (Java name `org.hisp.dhis.user.UserRole`) Example: vc4Bi38eb5R.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, UserRoleGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UserRole, WebMessage]]
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
    root_junction: Union[Unset, UserRoleGetObjectRootJunction] = UNSET,
) -> Optional[Union[UserRole, WebMessage]]:
    """View a UserRole

    Args:
        uid (str): A UID for an UserRole object
            (Java name `org.hisp.dhis.user.UserRole`) Example: vc4Bi38eb5R.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, UserRoleGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UserRole, WebMessage]
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
    root_junction: Union[Unset, UserRoleGetObjectRootJunction] = UNSET,
) -> Response[Union[UserRole, WebMessage]]:
    """View a UserRole

    Args:
        uid (str): A UID for an UserRole object
            (Java name `org.hisp.dhis.user.UserRole`) Example: vc4Bi38eb5R.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, UserRoleGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UserRole, WebMessage]]
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
    root_junction: Union[Unset, UserRoleGetObjectRootJunction] = UNSET,
) -> Optional[Union[UserRole, WebMessage]]:
    """View a UserRole

    Args:
        uid (str): A UID for an UserRole object
            (Java name `org.hisp.dhis.user.UserRole`) Example: vc4Bi38eb5R.
        fields (Union[Unset, list[str]]):
        filter_ (Union[Unset, list[str]]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        root_junction (Union[Unset, UserRoleGetObjectRootJunction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UserRole, WebMessage]
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
