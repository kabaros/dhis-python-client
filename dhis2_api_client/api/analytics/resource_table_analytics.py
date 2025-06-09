from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    last_years: Union[Unset, int] = UNSET,
    skip_aggregate: Union[Unset, bool] = False,
    skip_enrollment: Union[Unset, bool] = False,
    skip_events: Union[Unset, bool] = False,
    skip_org_unit_ownership: Union[Unset, bool] = False,
    skip_outliers: Union[Unset, bool] = False,
    skip_resource_tables: Union[Unset, bool] = False,
    skip_tracked_entities: Union[Unset, bool] = False,
    skip_validation_result: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["lastYears"] = last_years

    params["skipAggregate"] = skip_aggregate

    params["skipEnrollment"] = skip_enrollment

    params["skipEvents"] = skip_events

    params["skipOrgUnitOwnership"] = skip_org_unit_ownership

    params["skipOutliers"] = skip_outliers

    params["skipResourceTables"] = skip_resource_tables

    params["skipTrackedEntities"] = skip_tracked_entities

    params["skipValidationResult"] = skip_validation_result

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/resourceTables/analytics",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WebMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    last_years: Union[Unset, int] = UNSET,
    skip_aggregate: Union[Unset, bool] = False,
    skip_enrollment: Union[Unset, bool] = False,
    skip_events: Union[Unset, bool] = False,
    skip_org_unit_ownership: Union[Unset, bool] = False,
    skip_outliers: Union[Unset, bool] = False,
    skip_resource_tables: Union[Unset, bool] = False,
    skip_tracked_entities: Union[Unset, bool] = False,
    skip_validation_result: Union[Unset, bool] = False,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        last_years (Union[Unset, int]):
        skip_aggregate (Union[Unset, bool]):  Default: False.
        skip_enrollment (Union[Unset, bool]):  Default: False.
        skip_events (Union[Unset, bool]):  Default: False.
        skip_org_unit_ownership (Union[Unset, bool]):  Default: False.
        skip_outliers (Union[Unset, bool]):  Default: False.
        skip_resource_tables (Union[Unset, bool]):  Default: False.
        skip_tracked_entities (Union[Unset, bool]):  Default: False.
        skip_validation_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        last_years=last_years,
        skip_aggregate=skip_aggregate,
        skip_enrollment=skip_enrollment,
        skip_events=skip_events,
        skip_org_unit_ownership=skip_org_unit_ownership,
        skip_outliers=skip_outliers,
        skip_resource_tables=skip_resource_tables,
        skip_tracked_entities=skip_tracked_entities,
        skip_validation_result=skip_validation_result,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    last_years: Union[Unset, int] = UNSET,
    skip_aggregate: Union[Unset, bool] = False,
    skip_enrollment: Union[Unset, bool] = False,
    skip_events: Union[Unset, bool] = False,
    skip_org_unit_ownership: Union[Unset, bool] = False,
    skip_outliers: Union[Unset, bool] = False,
    skip_resource_tables: Union[Unset, bool] = False,
    skip_tracked_entities: Union[Unset, bool] = False,
    skip_validation_result: Union[Unset, bool] = False,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        last_years (Union[Unset, int]):
        skip_aggregate (Union[Unset, bool]):  Default: False.
        skip_enrollment (Union[Unset, bool]):  Default: False.
        skip_events (Union[Unset, bool]):  Default: False.
        skip_org_unit_ownership (Union[Unset, bool]):  Default: False.
        skip_outliers (Union[Unset, bool]):  Default: False.
        skip_resource_tables (Union[Unset, bool]):  Default: False.
        skip_tracked_entities (Union[Unset, bool]):  Default: False.
        skip_validation_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        client=client,
        last_years=last_years,
        skip_aggregate=skip_aggregate,
        skip_enrollment=skip_enrollment,
        skip_events=skip_events,
        skip_org_unit_ownership=skip_org_unit_ownership,
        skip_outliers=skip_outliers,
        skip_resource_tables=skip_resource_tables,
        skip_tracked_entities=skip_tracked_entities,
        skip_validation_result=skip_validation_result,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    last_years: Union[Unset, int] = UNSET,
    skip_aggregate: Union[Unset, bool] = False,
    skip_enrollment: Union[Unset, bool] = False,
    skip_events: Union[Unset, bool] = False,
    skip_org_unit_ownership: Union[Unset, bool] = False,
    skip_outliers: Union[Unset, bool] = False,
    skip_resource_tables: Union[Unset, bool] = False,
    skip_tracked_entities: Union[Unset, bool] = False,
    skip_validation_result: Union[Unset, bool] = False,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        last_years (Union[Unset, int]):
        skip_aggregate (Union[Unset, bool]):  Default: False.
        skip_enrollment (Union[Unset, bool]):  Default: False.
        skip_events (Union[Unset, bool]):  Default: False.
        skip_org_unit_ownership (Union[Unset, bool]):  Default: False.
        skip_outliers (Union[Unset, bool]):  Default: False.
        skip_resource_tables (Union[Unset, bool]):  Default: False.
        skip_tracked_entities (Union[Unset, bool]):  Default: False.
        skip_validation_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        last_years=last_years,
        skip_aggregate=skip_aggregate,
        skip_enrollment=skip_enrollment,
        skip_events=skip_events,
        skip_org_unit_ownership=skip_org_unit_ownership,
        skip_outliers=skip_outliers,
        skip_resource_tables=skip_resource_tables,
        skip_tracked_entities=skip_tracked_entities,
        skip_validation_result=skip_validation_result,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    last_years: Union[Unset, int] = UNSET,
    skip_aggregate: Union[Unset, bool] = False,
    skip_enrollment: Union[Unset, bool] = False,
    skip_events: Union[Unset, bool] = False,
    skip_org_unit_ownership: Union[Unset, bool] = False,
    skip_outliers: Union[Unset, bool] = False,
    skip_resource_tables: Union[Unset, bool] = False,
    skip_tracked_entities: Union[Unset, bool] = False,
    skip_validation_result: Union[Unset, bool] = False,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        last_years (Union[Unset, int]):
        skip_aggregate (Union[Unset, bool]):  Default: False.
        skip_enrollment (Union[Unset, bool]):  Default: False.
        skip_events (Union[Unset, bool]):  Default: False.
        skip_org_unit_ownership (Union[Unset, bool]):  Default: False.
        skip_outliers (Union[Unset, bool]):  Default: False.
        skip_resource_tables (Union[Unset, bool]):  Default: False.
        skip_tracked_entities (Union[Unset, bool]):  Default: False.
        skip_validation_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            last_years=last_years,
            skip_aggregate=skip_aggregate,
            skip_enrollment=skip_enrollment,
            skip_events=skip_events,
            skip_org_unit_ownership=skip_org_unit_ownership,
            skip_outliers=skip_outliers,
            skip_resource_tables=skip_resource_tables,
            skip_tracked_entities=skip_tracked_entities,
            skip_validation_result=skip_validation_result,
        )
    ).parsed
