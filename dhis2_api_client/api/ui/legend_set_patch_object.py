from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.json_patch import JsonPatch
from ...models.legend_set_patch_object_atomic_mode import LegendSetPatchObjectAtomicMode
from ...models.legend_set_patch_object_flush_mode import LegendSetPatchObjectFlushMode
from ...models.legend_set_patch_object_identifier import LegendSetPatchObjectIdentifier
from ...models.legend_set_patch_object_import_mode import LegendSetPatchObjectImportMode
from ...models.legend_set_patch_object_import_report_mode import LegendSetPatchObjectImportReportMode
from ...models.legend_set_patch_object_import_strategy import LegendSetPatchObjectImportStrategy
from ...models.legend_set_patch_object_preheat_mode import LegendSetPatchObjectPreheatMode
from ...models.legend_set_patch_object_root_junction import LegendSetPatchObjectRootJunction
from ...models.legend_set_patch_object_user_override_mode import LegendSetPatchObjectUserOverrideMode
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    body: JsonPatch,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[Unset, LegendSetPatchObjectAtomicMode] = LegendSetPatchObjectAtomicMode.ALL,
    flush_mode: Union[Unset, LegendSetPatchObjectFlushMode] = LegendSetPatchObjectFlushMode.AUTO,
    identifier: Union[Unset, LegendSetPatchObjectIdentifier] = LegendSetPatchObjectIdentifier.UID,
    import_mode: Union[Unset, LegendSetPatchObjectImportMode] = LegendSetPatchObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, LegendSetPatchObjectImportReportMode
    ] = LegendSetPatchObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, LegendSetPatchObjectImportStrategy
    ] = LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    preheat_mode: Union[Unset, LegendSetPatchObjectPreheatMode] = LegendSetPatchObjectPreheatMode.REFERENCE,
    root_junction: Union[Unset, LegendSetPatchObjectRootJunction] = UNSET,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[Unset, LegendSetPatchObjectUserOverrideMode] = LegendSetPatchObjectUserOverrideMode.NONE,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["async"] = async_

    json_atomic_mode: Union[Unset, str] = UNSET
    if not isinstance(atomic_mode, Unset):
        json_atomic_mode = atomic_mode.value

    params["atomicMode"] = json_atomic_mode

    json_flush_mode: Union[Unset, str] = UNSET
    if not isinstance(flush_mode, Unset):
        json_flush_mode = flush_mode.value

    params["flushMode"] = json_flush_mode

    json_identifier: Union[Unset, str] = UNSET
    if not isinstance(identifier, Unset):
        json_identifier = identifier.value

    params["identifier"] = json_identifier

    json_import_mode: Union[Unset, str] = UNSET
    if not isinstance(import_mode, Unset):
        json_import_mode = import_mode.value

    params["importMode"] = json_import_mode

    json_import_report_mode: Union[Unset, str] = UNSET
    if not isinstance(import_report_mode, Unset):
        json_import_report_mode = import_report_mode.value

    params["importReportMode"] = json_import_report_mode

    json_import_strategy: Union[Unset, str] = UNSET
    if not isinstance(import_strategy, Unset):
        json_import_strategy = import_strategy.value

    params["importStrategy"] = json_import_strategy

    params["metadataSyncImport"] = metadata_sync_import

    params["overrideUser"] = override_user

    params["page"] = page

    params["pageSize"] = page_size

    params["paging"] = paging

    json_preheat_mode: Union[Unset, str] = UNSET
    if not isinstance(preheat_mode, Unset):
        json_preheat_mode = preheat_mode.value

    params["preheatMode"] = json_preheat_mode

    json_root_junction: Union[Unset, str] = UNSET
    if not isinstance(root_junction, Unset):
        json_root_junction = root_junction.value

    params["rootJunction"] = json_root_junction

    params["skipSharing"] = skip_sharing

    params["skipTranslation"] = skip_translation

    params["skipValidation"] = skip_validation

    params["user"] = user

    json_user_override_mode: Union[Unset, str] = UNSET
    if not isinstance(user_override_mode, Unset):
        json_user_override_mode = user_override_mode.value

    params["userOverrideMode"] = json_user_override_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/legendSets/{uid}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = WebMessage.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = WebMessage.from_dict(response.json())

        return response_403
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
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: JsonPatch,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[Unset, LegendSetPatchObjectAtomicMode] = LegendSetPatchObjectAtomicMode.ALL,
    flush_mode: Union[Unset, LegendSetPatchObjectFlushMode] = LegendSetPatchObjectFlushMode.AUTO,
    identifier: Union[Unset, LegendSetPatchObjectIdentifier] = LegendSetPatchObjectIdentifier.UID,
    import_mode: Union[Unset, LegendSetPatchObjectImportMode] = LegendSetPatchObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, LegendSetPatchObjectImportReportMode
    ] = LegendSetPatchObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, LegendSetPatchObjectImportStrategy
    ] = LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    preheat_mode: Union[Unset, LegendSetPatchObjectPreheatMode] = LegendSetPatchObjectPreheatMode.REFERENCE,
    root_junction: Union[Unset, LegendSetPatchObjectRootJunction] = UNSET,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[Unset, LegendSetPatchObjectUserOverrideMode] = LegendSetPatchObjectUserOverrideMode.NONE,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an LegendSet object
            (Java name `org.hisp.dhis.legend.LegendSet`) Example: nZ5pL4Kf3gS.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, LegendSetPatchObjectAtomicMode]):  Default:
            LegendSetPatchObjectAtomicMode.ALL.
        flush_mode (Union[Unset, LegendSetPatchObjectFlushMode]):  Default:
            LegendSetPatchObjectFlushMode.AUTO.
        identifier (Union[Unset, LegendSetPatchObjectIdentifier]):  Default:
            LegendSetPatchObjectIdentifier.UID.
        import_mode (Union[Unset, LegendSetPatchObjectImportMode]):  Default:
            LegendSetPatchObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, LegendSetPatchObjectImportReportMode]):  Default:
            LegendSetPatchObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, LegendSetPatchObjectImportStrategy]):  Default:
            LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        preheat_mode (Union[Unset, LegendSetPatchObjectPreheatMode]):  Default:
            LegendSetPatchObjectPreheatMode.REFERENCE.
        root_junction (Union[Unset, LegendSetPatchObjectRootJunction]):
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, LegendSetPatchObjectUserOverrideMode]):  Default:
            LegendSetPatchObjectUserOverrideMode.NONE.
        body (JsonPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
        async_=async_,
        atomic_mode=atomic_mode,
        flush_mode=flush_mode,
        identifier=identifier,
        import_mode=import_mode,
        import_report_mode=import_report_mode,
        import_strategy=import_strategy,
        metadata_sync_import=metadata_sync_import,
        override_user=override_user,
        page=page,
        page_size=page_size,
        paging=paging,
        preheat_mode=preheat_mode,
        root_junction=root_junction,
        skip_sharing=skip_sharing,
        skip_translation=skip_translation,
        skip_validation=skip_validation,
        user=user,
        user_override_mode=user_override_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: JsonPatch,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[Unset, LegendSetPatchObjectAtomicMode] = LegendSetPatchObjectAtomicMode.ALL,
    flush_mode: Union[Unset, LegendSetPatchObjectFlushMode] = LegendSetPatchObjectFlushMode.AUTO,
    identifier: Union[Unset, LegendSetPatchObjectIdentifier] = LegendSetPatchObjectIdentifier.UID,
    import_mode: Union[Unset, LegendSetPatchObjectImportMode] = LegendSetPatchObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, LegendSetPatchObjectImportReportMode
    ] = LegendSetPatchObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, LegendSetPatchObjectImportStrategy
    ] = LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    preheat_mode: Union[Unset, LegendSetPatchObjectPreheatMode] = LegendSetPatchObjectPreheatMode.REFERENCE,
    root_junction: Union[Unset, LegendSetPatchObjectRootJunction] = UNSET,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[Unset, LegendSetPatchObjectUserOverrideMode] = LegendSetPatchObjectUserOverrideMode.NONE,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an LegendSet object
            (Java name `org.hisp.dhis.legend.LegendSet`) Example: nZ5pL4Kf3gS.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, LegendSetPatchObjectAtomicMode]):  Default:
            LegendSetPatchObjectAtomicMode.ALL.
        flush_mode (Union[Unset, LegendSetPatchObjectFlushMode]):  Default:
            LegendSetPatchObjectFlushMode.AUTO.
        identifier (Union[Unset, LegendSetPatchObjectIdentifier]):  Default:
            LegendSetPatchObjectIdentifier.UID.
        import_mode (Union[Unset, LegendSetPatchObjectImportMode]):  Default:
            LegendSetPatchObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, LegendSetPatchObjectImportReportMode]):  Default:
            LegendSetPatchObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, LegendSetPatchObjectImportStrategy]):  Default:
            LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        preheat_mode (Union[Unset, LegendSetPatchObjectPreheatMode]):  Default:
            LegendSetPatchObjectPreheatMode.REFERENCE.
        root_junction (Union[Unset, LegendSetPatchObjectRootJunction]):
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, LegendSetPatchObjectUserOverrideMode]):  Default:
            LegendSetPatchObjectUserOverrideMode.NONE.
        body (JsonPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return sync_detailed(
        uid=uid,
        client=client,
        body=body,
        async_=async_,
        atomic_mode=atomic_mode,
        flush_mode=flush_mode,
        identifier=identifier,
        import_mode=import_mode,
        import_report_mode=import_report_mode,
        import_strategy=import_strategy,
        metadata_sync_import=metadata_sync_import,
        override_user=override_user,
        page=page,
        page_size=page_size,
        paging=paging,
        preheat_mode=preheat_mode,
        root_junction=root_junction,
        skip_sharing=skip_sharing,
        skip_translation=skip_translation,
        skip_validation=skip_validation,
        user=user,
        user_override_mode=user_override_mode,
    ).parsed


async def asyncio_detailed(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: JsonPatch,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[Unset, LegendSetPatchObjectAtomicMode] = LegendSetPatchObjectAtomicMode.ALL,
    flush_mode: Union[Unset, LegendSetPatchObjectFlushMode] = LegendSetPatchObjectFlushMode.AUTO,
    identifier: Union[Unset, LegendSetPatchObjectIdentifier] = LegendSetPatchObjectIdentifier.UID,
    import_mode: Union[Unset, LegendSetPatchObjectImportMode] = LegendSetPatchObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, LegendSetPatchObjectImportReportMode
    ] = LegendSetPatchObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, LegendSetPatchObjectImportStrategy
    ] = LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    preheat_mode: Union[Unset, LegendSetPatchObjectPreheatMode] = LegendSetPatchObjectPreheatMode.REFERENCE,
    root_junction: Union[Unset, LegendSetPatchObjectRootJunction] = UNSET,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[Unset, LegendSetPatchObjectUserOverrideMode] = LegendSetPatchObjectUserOverrideMode.NONE,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an LegendSet object
            (Java name `org.hisp.dhis.legend.LegendSet`) Example: nZ5pL4Kf3gS.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, LegendSetPatchObjectAtomicMode]):  Default:
            LegendSetPatchObjectAtomicMode.ALL.
        flush_mode (Union[Unset, LegendSetPatchObjectFlushMode]):  Default:
            LegendSetPatchObjectFlushMode.AUTO.
        identifier (Union[Unset, LegendSetPatchObjectIdentifier]):  Default:
            LegendSetPatchObjectIdentifier.UID.
        import_mode (Union[Unset, LegendSetPatchObjectImportMode]):  Default:
            LegendSetPatchObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, LegendSetPatchObjectImportReportMode]):  Default:
            LegendSetPatchObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, LegendSetPatchObjectImportStrategy]):  Default:
            LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        preheat_mode (Union[Unset, LegendSetPatchObjectPreheatMode]):  Default:
            LegendSetPatchObjectPreheatMode.REFERENCE.
        root_junction (Union[Unset, LegendSetPatchObjectRootJunction]):
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, LegendSetPatchObjectUserOverrideMode]):  Default:
            LegendSetPatchObjectUserOverrideMode.NONE.
        body (JsonPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebMessage]
    """

    kwargs = _get_kwargs(
        uid=uid,
        body=body,
        async_=async_,
        atomic_mode=atomic_mode,
        flush_mode=flush_mode,
        identifier=identifier,
        import_mode=import_mode,
        import_report_mode=import_report_mode,
        import_strategy=import_strategy,
        metadata_sync_import=metadata_sync_import,
        override_user=override_user,
        page=page,
        page_size=page_size,
        paging=paging,
        preheat_mode=preheat_mode,
        root_junction=root_junction,
        skip_sharing=skip_sharing,
        skip_translation=skip_translation,
        skip_validation=skip_validation,
        user=user,
        user_override_mode=user_override_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: JsonPatch,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[Unset, LegendSetPatchObjectAtomicMode] = LegendSetPatchObjectAtomicMode.ALL,
    flush_mode: Union[Unset, LegendSetPatchObjectFlushMode] = LegendSetPatchObjectFlushMode.AUTO,
    identifier: Union[Unset, LegendSetPatchObjectIdentifier] = LegendSetPatchObjectIdentifier.UID,
    import_mode: Union[Unset, LegendSetPatchObjectImportMode] = LegendSetPatchObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, LegendSetPatchObjectImportReportMode
    ] = LegendSetPatchObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, LegendSetPatchObjectImportStrategy
    ] = LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    paging: Union[Unset, bool] = UNSET,
    preheat_mode: Union[Unset, LegendSetPatchObjectPreheatMode] = LegendSetPatchObjectPreheatMode.REFERENCE,
    root_junction: Union[Unset, LegendSetPatchObjectRootJunction] = UNSET,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[Unset, LegendSetPatchObjectUserOverrideMode] = LegendSetPatchObjectUserOverrideMode.NONE,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an LegendSet object
            (Java name `org.hisp.dhis.legend.LegendSet`) Example: nZ5pL4Kf3gS.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, LegendSetPatchObjectAtomicMode]):  Default:
            LegendSetPatchObjectAtomicMode.ALL.
        flush_mode (Union[Unset, LegendSetPatchObjectFlushMode]):  Default:
            LegendSetPatchObjectFlushMode.AUTO.
        identifier (Union[Unset, LegendSetPatchObjectIdentifier]):  Default:
            LegendSetPatchObjectIdentifier.UID.
        import_mode (Union[Unset, LegendSetPatchObjectImportMode]):  Default:
            LegendSetPatchObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, LegendSetPatchObjectImportReportMode]):  Default:
            LegendSetPatchObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, LegendSetPatchObjectImportStrategy]):  Default:
            LegendSetPatchObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        paging (Union[Unset, bool]):
        preheat_mode (Union[Unset, LegendSetPatchObjectPreheatMode]):  Default:
            LegendSetPatchObjectPreheatMode.REFERENCE.
        root_junction (Union[Unset, LegendSetPatchObjectRootJunction]):
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, LegendSetPatchObjectUserOverrideMode]):  Default:
            LegendSetPatchObjectUserOverrideMode.NONE.
        body (JsonPatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebMessage
    """

    return (
        await asyncio_detailed(
            uid=uid,
            client=client,
            body=body,
            async_=async_,
            atomic_mode=atomic_mode,
            flush_mode=flush_mode,
            identifier=identifier,
            import_mode=import_mode,
            import_report_mode=import_report_mode,
            import_strategy=import_strategy,
            metadata_sync_import=metadata_sync_import,
            override_user=override_user,
            page=page,
            page_size=page_size,
            paging=paging,
            preheat_mode=preheat_mode,
            root_junction=root_junction,
            skip_sharing=skip_sharing,
            skip_translation=skip_translation,
            skip_validation=skip_validation,
            user=user,
            user_override_mode=user_override_mode,
        )
    ).parsed
