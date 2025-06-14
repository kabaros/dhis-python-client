from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.i18n_output import I18NOutput
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    package: Union[Unset, str] = "org.hisp.dhis",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["package"] = package

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/i18n/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[I18NOutput]:
    if response.status_code == 200:
        response_200 = I18NOutput.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[I18NOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    package: Union[Unset, str] = "org.hisp.dhis",
) -> Response[I18NOutput]:
    """[no description yet]

    Args:
        package (Union[Unset, str]):  Default: 'org.hisp.dhis'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[I18NOutput]
    """

    kwargs = _get_kwargs(
        package=package,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    package: Union[Unset, str] = "org.hisp.dhis",
) -> Optional[I18NOutput]:
    """[no description yet]

    Args:
        package (Union[Unset, str]):  Default: 'org.hisp.dhis'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        I18NOutput
    """

    return sync_detailed(
        client=client,
        package=package,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    package: Union[Unset, str] = "org.hisp.dhis",
) -> Response[I18NOutput]:
    """[no description yet]

    Args:
        package (Union[Unset, str]):  Default: 'org.hisp.dhis'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[I18NOutput]
    """

    kwargs = _get_kwargs(
        package=package,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    package: Union[Unset, str] = "org.hisp.dhis",
) -> Optional[I18NOutput]:
    """[no description yet]

    Args:
        package (Union[Unset, str]):  Default: 'org.hisp.dhis'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        I18NOutput
    """

    return (
        await asyncio_detailed(
            client=client,
            package=package,
        )
    ).parsed
