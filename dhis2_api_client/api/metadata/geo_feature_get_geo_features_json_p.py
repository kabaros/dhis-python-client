import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.geo_feature_get_geo_features_json_p_display_property import GeoFeatureGetGeoFeaturesJsonPDisplayProperty
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    callback: Union[Unset, str] = "callback",
    coordinate_field: Union[Unset, str] = UNSET,
    display_property: Union[Unset, GeoFeatureGetGeoFeaturesJsonPDisplayProperty] = UNSET,
    include_group_sets: Union[Unset, bool] = False,
    ou: Union[Unset, str] = UNSET,
    oug: Union[Unset, str] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    user_org_unit: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["callback"] = callback

    params["coordinateField"] = coordinate_field

    json_display_property: Union[Unset, str] = UNSET
    if not isinstance(display_property, Unset):
        json_display_property = display_property.value

    params["displayProperty"] = json_display_property

    params["includeGroupSets"] = include_group_sets

    params["ou"] = ou

    params["oug"] = oug

    json_relative_period_date: Union[Unset, str] = UNSET
    if not isinstance(relative_period_date, Unset):
        json_relative_period_date = relative_period_date.isoformat()
    params["relativePeriodDate"] = json_relative_period_date

    params["userOrgUnit"] = user_org_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/geoFeatures/#getGeoFeaturesJsonP",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
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
    callback: Union[Unset, str] = "callback",
    coordinate_field: Union[Unset, str] = UNSET,
    display_property: Union[Unset, GeoFeatureGetGeoFeaturesJsonPDisplayProperty] = UNSET,
    include_group_sets: Union[Unset, bool] = False,
    ou: Union[Unset, str] = UNSET,
    oug: Union[Unset, str] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        callback (Union[Unset, str]):  Default: 'callback'.
        coordinate_field (Union[Unset, str]):
        display_property (Union[Unset, GeoFeatureGetGeoFeaturesJsonPDisplayProperty]):
        include_group_sets (Union[Unset, bool]):  Default: False.
        ou (Union[Unset, str]):
        oug (Union[Unset, str]):
        relative_period_date (Union[Unset, datetime.datetime]):
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        callback=callback,
        coordinate_field=coordinate_field,
        display_property=display_property,
        include_group_sets=include_group_sets,
        ou=ou,
        oug=oug,
        relative_period_date=relative_period_date,
        user_org_unit=user_org_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    callback: Union[Unset, str] = "callback",
    coordinate_field: Union[Unset, str] = UNSET,
    display_property: Union[Unset, GeoFeatureGetGeoFeaturesJsonPDisplayProperty] = UNSET,
    include_group_sets: Union[Unset, bool] = False,
    ou: Union[Unset, str] = UNSET,
    oug: Union[Unset, str] = UNSET,
    relative_period_date: Union[Unset, datetime.datetime] = UNSET,
    user_org_unit: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """[no description yet]

    Args:
        callback (Union[Unset, str]):  Default: 'callback'.
        coordinate_field (Union[Unset, str]):
        display_property (Union[Unset, GeoFeatureGetGeoFeaturesJsonPDisplayProperty]):
        include_group_sets (Union[Unset, bool]):  Default: False.
        ou (Union[Unset, str]):
        oug (Union[Unset, str]):
        relative_period_date (Union[Unset, datetime.datetime]):
        user_org_unit (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        callback=callback,
        coordinate_field=coordinate_field,
        display_property=display_property,
        include_group_sets=include_group_sets,
        ou=ou,
        oug=oug,
        relative_period_date=relative_period_date,
        user_org_unit=user_org_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
