from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.input_stream_resource import InputStreamResource
from ...models.tracked_entities_export_get_attribute_value_image_dimension import (
    TrackedEntitiesExportGetAttributeValueImageDimension,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tracked_entity: str,
    attribute: str,
    *,
    dimension: Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension] = UNSET,
    program: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_dimension: Union[Unset, str] = UNSET
    if not isinstance(dimension, Unset):
        json_dimension = dimension.value

    params["dimension"] = json_dimension

    params["program"] = program

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tracker/trackedEntities/{tracked_entity}/attributes/{attribute}/image",
        "params": params,
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
    tracked_entity: str,
    attribute: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension] = UNSET,
    program: Union[Unset, str] = UNSET,
) -> Response[Union[InputStreamResource, WebMessage]]:
    """Get an event data value image for given event and data element UID. Images are returned in their
    original dimension by default. This endpoint is only supported for data elements of value type
    image.

    Args:
        tracked_entity (str): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        attribute (str): A UID for an TrackerAttribute object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Attribute`) Example: ce5CG4iu357.
        dimension (Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InputStreamResource, WebMessage]]
    """

    kwargs = _get_kwargs(
        tracked_entity=tracked_entity,
        attribute=attribute,
        dimension=dimension,
        program=program,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tracked_entity: str,
    attribute: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension] = UNSET,
    program: Union[Unset, str] = UNSET,
) -> Optional[Union[InputStreamResource, WebMessage]]:
    """Get an event data value image for given event and data element UID. Images are returned in their
    original dimension by default. This endpoint is only supported for data elements of value type
    image.

    Args:
        tracked_entity (str): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        attribute (str): A UID for an TrackerAttribute object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Attribute`) Example: ce5CG4iu357.
        dimension (Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InputStreamResource, WebMessage]
    """

    return sync_detailed(
        tracked_entity=tracked_entity,
        attribute=attribute,
        client=client,
        dimension=dimension,
        program=program,
    ).parsed


async def asyncio_detailed(
    tracked_entity: str,
    attribute: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension] = UNSET,
    program: Union[Unset, str] = UNSET,
) -> Response[Union[InputStreamResource, WebMessage]]:
    """Get an event data value image for given event and data element UID. Images are returned in their
    original dimension by default. This endpoint is only supported for data elements of value type
    image.

    Args:
        tracked_entity (str): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        attribute (str): A UID for an TrackerAttribute object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Attribute`) Example: ce5CG4iu357.
        dimension (Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InputStreamResource, WebMessage]]
    """

    kwargs = _get_kwargs(
        tracked_entity=tracked_entity,
        attribute=attribute,
        dimension=dimension,
        program=program,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tracked_entity: str,
    attribute: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dimension: Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension] = UNSET,
    program: Union[Unset, str] = UNSET,
) -> Optional[Union[InputStreamResource, WebMessage]]:
    """Get an event data value image for given event and data element UID. Images are returned in their
    original dimension by default. This endpoint is only supported for data elements of value type
    image.

    Args:
        tracked_entity (str): A UID for an TrackerTrackedEntity object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.TrackedEntity`) Example:
            zg9rM85NF00.
        attribute (str): A UID for an TrackerAttribute object
            (Java name `org.hisp.dhis.webapi.controller.tracker.view.Attribute`) Example: ce5CG4iu357.
        dimension (Union[Unset, TrackedEntitiesExportGetAttributeValueImageDimension]):
        program (Union[Unset, str]): A UID for an Program object
            (Java name `org.hisp.dhis.program.Program`) Example: pa3pN28SD4S.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InputStreamResource, WebMessage]
    """

    return (
        await asyncio_detailed(
            tracked_entity=tracked_entity,
            attribute=attribute,
            client=client,
            dimension=dimension,
            program=program,
        )
    ).parsed
