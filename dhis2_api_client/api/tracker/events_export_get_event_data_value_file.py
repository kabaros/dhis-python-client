from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.input_stream_resource import InputStreamResource
from ...models.web_message import WebMessage
from ...types import Response


def _get_kwargs(
    event: str,
    data_element: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tracker/events/{event}/dataValues/{data_element}/file",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[InputStreamResource, WebMessage]]:
    if response.status_code == 200:
        response_200 = InputStreamResource.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = WebMessage.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[InputStreamResource, WebMessage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event: str,
    data_element: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[InputStreamResource, WebMessage]]:
    """Get an event data value file or image for given event and data element UID. Images are returned in
    their original dimension.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        data_element (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InputStreamResource, WebMessage]]
    """

    kwargs = _get_kwargs(
        event=event,
        data_element=data_element,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event: str,
    data_element: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[InputStreamResource, WebMessage]]:
    """Get an event data value file or image for given event and data element UID. Images are returned in
    their original dimension.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        data_element (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InputStreamResource, WebMessage]
    """

    return sync_detailed(
        event=event,
        data_element=data_element,
        client=client,
    ).parsed


async def asyncio_detailed(
    event: str,
    data_element: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[InputStreamResource, WebMessage]]:
    """Get an event data value file or image for given event and data element UID. Images are returned in
    their original dimension.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        data_element (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InputStreamResource, WebMessage]]
    """

    kwargs = _get_kwargs(
        event=event,
        data_element=data_element,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event: str,
    data_element: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[InputStreamResource, WebMessage]]:
    """Get an event data value file or image for given event and data element UID. Images are returned in
    their original dimension.

    Args:
        event (str): A UID for an TrackerEvent object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Event`) Example: cc1uN0fb9Qi.
        data_element (str): A UID for an DataElement object
            (Java name `org.hisp.dhis.dataelement.DataElement`) Example: hX7n8Y4pu89.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InputStreamResource, WebMessage]
    """

    return (
        await asyncio_detailed(
            event=event,
            data_element=data_element,
            client=client,
        )
    ).parsed
