from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.field_path import FieldPath
from ...models.sms_gateway_get_gateway_configuration_response_200 import SmsGatewayGetGatewayConfigurationResponse200
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[dict[str, Any]]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.to_dict()
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/gateways/{uid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]:
    if response.status_code == 200:
        response_200 = SmsGatewayGetGatewayConfigurationResponse200.from_dict(response.json())

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
) -> Response[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]:
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
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Response[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]
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
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Optional[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]
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
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Response[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]
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
    fields: Union[Unset, list["FieldPath"]] = UNSET,
) -> Optional[Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]]:
    """[no description yet]

    Args:
        uid (str):
        fields (Union[Unset, list['FieldPath']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SmsGatewayGetGatewayConfigurationResponse200, WebMessage]
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            fields=fields,
        )
    ).parsed
