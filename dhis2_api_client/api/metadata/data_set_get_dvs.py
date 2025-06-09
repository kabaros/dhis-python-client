from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_set_get_dvs_response_200 import DataSetGetDvsResponse200
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    comment: Union[Unset, bool] = True,
    data_element_id_scheme: Union[Unset, str] = "ID",
    locale: Union[Unset, str] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = "ID",
    period: Union[Unset, str] = "",
    translate: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["comment"] = comment

    params["dataElementIdScheme"] = data_element_id_scheme

    params["locale"] = locale

    json_org_unit: Union[Unset, list[str]] = UNSET
    if not isinstance(org_unit, Unset):
        json_org_unit = org_unit

    params["orgUnit"] = json_org_unit

    params["orgUnitIdScheme"] = org_unit_id_scheme

    params["period"] = period

    params["translate"] = translate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/dataSets/{uid}/dataValueSet",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DataSetGetDvsResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = DataSetGetDvsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = WebMessage.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DataSetGetDvsResponse200, WebMessage]]:
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
    comment: Union[Unset, bool] = True,
    data_element_id_scheme: Union[Unset, str] = "ID",
    locale: Union[Unset, str] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = "ID",
    period: Union[Unset, str] = "",
    translate: Union[Unset, bool] = True,
) -> Response[Union[DataSetGetDvsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        comment (Union[Unset, bool]):  Default: True.
        data_element_id_scheme (Union[Unset, str]):  Default: 'ID'.
        locale (Union[Unset, str]):
        org_unit (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):  Default: 'ID'.
        period (Union[Unset, str]):  Default: ''.
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSetGetDvsResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        comment=comment,
        data_element_id_scheme=data_element_id_scheme,
        locale=locale,
        org_unit=org_unit,
        org_unit_id_scheme=org_unit_id_scheme,
        period=period,
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
    comment: Union[Unset, bool] = True,
    data_element_id_scheme: Union[Unset, str] = "ID",
    locale: Union[Unset, str] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = "ID",
    period: Union[Unset, str] = "",
    translate: Union[Unset, bool] = True,
) -> Optional[Union[DataSetGetDvsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        comment (Union[Unset, bool]):  Default: True.
        data_element_id_scheme (Union[Unset, str]):  Default: 'ID'.
        locale (Union[Unset, str]):
        org_unit (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):  Default: 'ID'.
        period (Union[Unset, str]):  Default: ''.
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataSetGetDvsResponse200, WebMessage]
    """

    return sync_detailed(
        uid=uid,
        client=client,
        comment=comment,
        data_element_id_scheme=data_element_id_scheme,
        locale=locale,
        org_unit=org_unit,
        org_unit_id_scheme=org_unit_id_scheme,
        period=period,
        translate=translate,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    comment: Union[Unset, bool] = True,
    data_element_id_scheme: Union[Unset, str] = "ID",
    locale: Union[Unset, str] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = "ID",
    period: Union[Unset, str] = "",
    translate: Union[Unset, bool] = True,
) -> Response[Union[DataSetGetDvsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        comment (Union[Unset, bool]):  Default: True.
        data_element_id_scheme (Union[Unset, str]):  Default: 'ID'.
        locale (Union[Unset, str]):
        org_unit (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):  Default: 'ID'.
        period (Union[Unset, str]):  Default: ''.
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataSetGetDvsResponse200, WebMessage]]
    """

    kwargs = _get_kwargs(
        uid=uid,
        comment=comment,
        data_element_id_scheme=data_element_id_scheme,
        locale=locale,
        org_unit=org_unit,
        org_unit_id_scheme=org_unit_id_scheme,
        period=period,
        translate=translate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    comment: Union[Unset, bool] = True,
    data_element_id_scheme: Union[Unset, str] = "ID",
    locale: Union[Unset, str] = UNSET,
    org_unit: Union[Unset, list[str]] = UNSET,
    org_unit_id_scheme: Union[Unset, str] = "ID",
    period: Union[Unset, str] = "",
    translate: Union[Unset, bool] = True,
) -> Optional[Union[DataSetGetDvsResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        comment (Union[Unset, bool]):  Default: True.
        data_element_id_scheme (Union[Unset, str]):  Default: 'ID'.
        locale (Union[Unset, str]):
        org_unit (Union[Unset, list[str]]):
        org_unit_id_scheme (Union[Unset, str]):  Default: 'ID'.
        period (Union[Unset, str]):  Default: ''.
        translate (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataSetGetDvsResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            comment=comment,
            data_element_id_scheme=data_element_id_scheme,
            locale=locale,
            org_unit=org_unit,
            org_unit_id_scheme=org_unit_id_scheme,
            period=period,
            translate=translate,
        )
    ).parsed
