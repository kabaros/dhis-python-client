from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    analytics_table_analyze: Union[Unset, bool] = UNSET,
    analytics_table_clear: Union[Unset, bool] = UNSET,
    app_reload: Union[Unset, bool] = UNSET,
    cache_clear: Union[Unset, bool] = UNSET,
    category_option_combo_update: Union[Unset, bool] = UNSET,
    expired_invitations_clear: Union[Unset, bool] = UNSET,
    ou_paths_update: Union[Unset, bool] = UNSET,
    period_pruning: Union[Unset, bool] = UNSET,
    resource_table_update: Union[Unset, bool] = UNSET,
    soft_deleted_data_value_removal: Union[Unset, bool] = UNSET,
    soft_deleted_enrollment_removal: Union[Unset, bool] = UNSET,
    soft_deleted_event_removal: Union[Unset, bool] = UNSET,
    soft_deleted_relationship_removal: Union[Unset, bool] = UNSET,
    soft_deleted_tracked_entity_instance_removal: Union[Unset, bool] = UNSET,
    soft_deleted_tracked_entity_removal: Union[Unset, bool] = UNSET,
    sql_views_create: Union[Unset, bool] = UNSET,
    sql_views_drop: Union[Unset, bool] = UNSET,
    zero_data_value_removal: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["analyticsTableAnalyze"] = analytics_table_analyze

    params["analyticsTableClear"] = analytics_table_clear

    params["appReload"] = app_reload

    params["cacheClear"] = cache_clear

    params["categoryOptionComboUpdate"] = category_option_combo_update

    params["expiredInvitationsClear"] = expired_invitations_clear

    params["ouPathsUpdate"] = ou_paths_update

    params["periodPruning"] = period_pruning

    params["resourceTableUpdate"] = resource_table_update

    params["softDeletedDataValueRemoval"] = soft_deleted_data_value_removal

    params["softDeletedEnrollmentRemoval"] = soft_deleted_enrollment_removal

    params["softDeletedEventRemoval"] = soft_deleted_event_removal

    params["softDeletedRelationshipRemoval"] = soft_deleted_relationship_removal

    params["softDeletedTrackedEntityInstanceRemoval"] = soft_deleted_tracked_entity_instance_removal

    params["softDeletedTrackedEntityRemoval"] = soft_deleted_tracked_entity_removal

    params["sqlViewsCreate"] = sql_views_create

    params["sqlViewsDrop"] = sql_views_drop

    params["zeroDataValueRemoval"] = zero_data_value_removal

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/maintenance/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    analytics_table_analyze: Union[Unset, bool] = UNSET,
    analytics_table_clear: Union[Unset, bool] = UNSET,
    app_reload: Union[Unset, bool] = UNSET,
    cache_clear: Union[Unset, bool] = UNSET,
    category_option_combo_update: Union[Unset, bool] = UNSET,
    expired_invitations_clear: Union[Unset, bool] = UNSET,
    ou_paths_update: Union[Unset, bool] = UNSET,
    period_pruning: Union[Unset, bool] = UNSET,
    resource_table_update: Union[Unset, bool] = UNSET,
    soft_deleted_data_value_removal: Union[Unset, bool] = UNSET,
    soft_deleted_enrollment_removal: Union[Unset, bool] = UNSET,
    soft_deleted_event_removal: Union[Unset, bool] = UNSET,
    soft_deleted_relationship_removal: Union[Unset, bool] = UNSET,
    soft_deleted_tracked_entity_instance_removal: Union[Unset, bool] = UNSET,
    soft_deleted_tracked_entity_removal: Union[Unset, bool] = UNSET,
    sql_views_create: Union[Unset, bool] = UNSET,
    sql_views_drop: Union[Unset, bool] = UNSET,
    zero_data_value_removal: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        analytics_table_analyze (Union[Unset, bool]):
        analytics_table_clear (Union[Unset, bool]):
        app_reload (Union[Unset, bool]):
        cache_clear (Union[Unset, bool]):
        category_option_combo_update (Union[Unset, bool]):
        expired_invitations_clear (Union[Unset, bool]):
        ou_paths_update (Union[Unset, bool]):
        period_pruning (Union[Unset, bool]):
        resource_table_update (Union[Unset, bool]):
        soft_deleted_data_value_removal (Union[Unset, bool]):
        soft_deleted_enrollment_removal (Union[Unset, bool]):
        soft_deleted_event_removal (Union[Unset, bool]):
        soft_deleted_relationship_removal (Union[Unset, bool]):
        soft_deleted_tracked_entity_instance_removal (Union[Unset, bool]):
        soft_deleted_tracked_entity_removal (Union[Unset, bool]):
        sql_views_create (Union[Unset, bool]):
        sql_views_drop (Union[Unset, bool]):
        zero_data_value_removal (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        analytics_table_analyze=analytics_table_analyze,
        analytics_table_clear=analytics_table_clear,
        app_reload=app_reload,
        cache_clear=cache_clear,
        category_option_combo_update=category_option_combo_update,
        expired_invitations_clear=expired_invitations_clear,
        ou_paths_update=ou_paths_update,
        period_pruning=period_pruning,
        resource_table_update=resource_table_update,
        soft_deleted_data_value_removal=soft_deleted_data_value_removal,
        soft_deleted_enrollment_removal=soft_deleted_enrollment_removal,
        soft_deleted_event_removal=soft_deleted_event_removal,
        soft_deleted_relationship_removal=soft_deleted_relationship_removal,
        soft_deleted_tracked_entity_instance_removal=soft_deleted_tracked_entity_instance_removal,
        soft_deleted_tracked_entity_removal=soft_deleted_tracked_entity_removal,
        sql_views_create=sql_views_create,
        sql_views_drop=sql_views_drop,
        zero_data_value_removal=zero_data_value_removal,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    analytics_table_analyze: Union[Unset, bool] = UNSET,
    analytics_table_clear: Union[Unset, bool] = UNSET,
    app_reload: Union[Unset, bool] = UNSET,
    cache_clear: Union[Unset, bool] = UNSET,
    category_option_combo_update: Union[Unset, bool] = UNSET,
    expired_invitations_clear: Union[Unset, bool] = UNSET,
    ou_paths_update: Union[Unset, bool] = UNSET,
    period_pruning: Union[Unset, bool] = UNSET,
    resource_table_update: Union[Unset, bool] = UNSET,
    soft_deleted_data_value_removal: Union[Unset, bool] = UNSET,
    soft_deleted_enrollment_removal: Union[Unset, bool] = UNSET,
    soft_deleted_event_removal: Union[Unset, bool] = UNSET,
    soft_deleted_relationship_removal: Union[Unset, bool] = UNSET,
    soft_deleted_tracked_entity_instance_removal: Union[Unset, bool] = UNSET,
    soft_deleted_tracked_entity_removal: Union[Unset, bool] = UNSET,
    sql_views_create: Union[Unset, bool] = UNSET,
    sql_views_drop: Union[Unset, bool] = UNSET,
    zero_data_value_removal: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        analytics_table_analyze (Union[Unset, bool]):
        analytics_table_clear (Union[Unset, bool]):
        app_reload (Union[Unset, bool]):
        cache_clear (Union[Unset, bool]):
        category_option_combo_update (Union[Unset, bool]):
        expired_invitations_clear (Union[Unset, bool]):
        ou_paths_update (Union[Unset, bool]):
        period_pruning (Union[Unset, bool]):
        resource_table_update (Union[Unset, bool]):
        soft_deleted_data_value_removal (Union[Unset, bool]):
        soft_deleted_enrollment_removal (Union[Unset, bool]):
        soft_deleted_event_removal (Union[Unset, bool]):
        soft_deleted_relationship_removal (Union[Unset, bool]):
        soft_deleted_tracked_entity_instance_removal (Union[Unset, bool]):
        soft_deleted_tracked_entity_removal (Union[Unset, bool]):
        sql_views_create (Union[Unset, bool]):
        sql_views_drop (Union[Unset, bool]):
        zero_data_value_removal (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        analytics_table_analyze=analytics_table_analyze,
        analytics_table_clear=analytics_table_clear,
        app_reload=app_reload,
        cache_clear=cache_clear,
        category_option_combo_update=category_option_combo_update,
        expired_invitations_clear=expired_invitations_clear,
        ou_paths_update=ou_paths_update,
        period_pruning=period_pruning,
        resource_table_update=resource_table_update,
        soft_deleted_data_value_removal=soft_deleted_data_value_removal,
        soft_deleted_enrollment_removal=soft_deleted_enrollment_removal,
        soft_deleted_event_removal=soft_deleted_event_removal,
        soft_deleted_relationship_removal=soft_deleted_relationship_removal,
        soft_deleted_tracked_entity_instance_removal=soft_deleted_tracked_entity_instance_removal,
        soft_deleted_tracked_entity_removal=soft_deleted_tracked_entity_removal,
        sql_views_create=sql_views_create,
        sql_views_drop=sql_views_drop,
        zero_data_value_removal=zero_data_value_removal,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
