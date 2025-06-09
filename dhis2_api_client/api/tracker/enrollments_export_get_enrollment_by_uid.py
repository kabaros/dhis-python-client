from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tracker_enrollment import TrackerEnrollment
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tracker/enrollments/{uid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[TrackerEnrollment, WebMessage]]:
    if response.status_code == 200:
        response_200 = TrackerEnrollment.from_dict(response.json())

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
) -> Response[Union[TrackerEnrollment, WebMessage]]:
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
) -> Response[Union[TrackerEnrollment, WebMessage]]:
    """Get an enrollment with given UID.

    Args:
        uid (str): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TrackerEnrollment, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        fields=fields,
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
) -> Optional[Union[TrackerEnrollment, WebMessage]]:
    """Get an enrollment with given UID.

    Args:
        uid (str): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrackerEnrollment, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[TrackerEnrollment, WebMessage]]:
    """Get an enrollment with given UID.

    Args:
        uid (str): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TrackerEnrollment, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[TrackerEnrollment, WebMessage]]:
    """Get an enrollment with given UID.

    Args:
        uid (str): A UID for an TrackerEnrollment object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Enrollment`) Example:
            h9qA2Xb1CV0.
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TrackerEnrollment, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            fields=fields,
        )
    ).parsed
