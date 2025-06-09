from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.program_rule import ProgramRule
from ...models.program_rule_put_json_objectput_xml_object_atomic_mode import (
    ProgramRulePutJsonObjectputXmlObjectAtomicMode,
)
from ...models.program_rule_put_json_objectput_xml_object_flush_mode import (
    ProgramRulePutJsonObjectputXmlObjectFlushMode,
)
from ...models.program_rule_put_json_objectput_xml_object_identifier import (
    ProgramRulePutJsonObjectputXmlObjectIdentifier,
)
from ...models.program_rule_put_json_objectput_xml_object_import_mode import (
    ProgramRulePutJsonObjectputXmlObjectImportMode,
)
from ...models.program_rule_put_json_objectput_xml_object_import_report_mode import (
    ProgramRulePutJsonObjectputXmlObjectImportReportMode,
)
from ...models.program_rule_put_json_objectput_xml_object_import_strategy import (
    ProgramRulePutJsonObjectputXmlObjectImportStrategy,
)
from ...models.program_rule_put_json_objectput_xml_object_preheat_mode import (
    ProgramRulePutJsonObjectputXmlObjectPreheatMode,
)
from ...models.program_rule_put_json_objectput_xml_object_user_override_mode import (
    ProgramRulePutJsonObjectputXmlObjectUserOverrideMode,
)
from ...models.web_message import WebMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uid: str,
    *,
    body: ProgramRule,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode
    ] = ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL,
    flush_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode
    ] = ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO,
    identifier: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier
    ] = ProgramRulePutJsonObjectputXmlObjectIdentifier.UID,
    import_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy
    ] = ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    preheat_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode
    ] = ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode
    ] = ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE,
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

    json_preheat_mode: Union[Unset, str] = UNSET
    if not isinstance(preheat_mode, Unset):
        json_preheat_mode = preheat_mode.value

    params["preheatMode"] = json_preheat_mode

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
        "method": "put",
        "url": f"/programRules/{uid}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WebMessage]:
    if response.status_code == 200:
        response_200 = WebMessage.from_dict(response.json())

        return response_200
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
    body: ProgramRule,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode
    ] = ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL,
    flush_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode
    ] = ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO,
    identifier: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier
    ] = ProgramRulePutJsonObjectputXmlObjectIdentifier.UID,
    import_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy
    ] = ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    preheat_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode
    ] = ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode
    ] = ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an ProgramRule object
            (Java name `org.hisp.dhis.programrule.ProgramRule`) Example: te7tR6cY5OU.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL.
        flush_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO.
        identifier (Union[Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier]):  Default:
            ProgramRulePutJsonObjectputXmlObjectIdentifier.UID.
        import_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        preheat_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE.
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE.
        body (ProgramRule):

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
        preheat_mode=preheat_mode,
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
    body: ProgramRule,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode
    ] = ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL,
    flush_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode
    ] = ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO,
    identifier: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier
    ] = ProgramRulePutJsonObjectputXmlObjectIdentifier.UID,
    import_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy
    ] = ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    preheat_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode
    ] = ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode
    ] = ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an ProgramRule object
            (Java name `org.hisp.dhis.programrule.ProgramRule`) Example: te7tR6cY5OU.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL.
        flush_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO.
        identifier (Union[Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier]):  Default:
            ProgramRulePutJsonObjectputXmlObjectIdentifier.UID.
        import_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        preheat_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE.
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE.
        body (ProgramRule):

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
        preheat_mode=preheat_mode,
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
    body: ProgramRule,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode
    ] = ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL,
    flush_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode
    ] = ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO,
    identifier: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier
    ] = ProgramRulePutJsonObjectputXmlObjectIdentifier.UID,
    import_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy
    ] = ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    preheat_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode
    ] = ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode
    ] = ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE,
) -> Response[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an ProgramRule object
            (Java name `org.hisp.dhis.programrule.ProgramRule`) Example: te7tR6cY5OU.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL.
        flush_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO.
        identifier (Union[Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier]):  Default:
            ProgramRulePutJsonObjectputXmlObjectIdentifier.UID.
        import_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        preheat_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE.
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE.
        body (ProgramRule):

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
        preheat_mode=preheat_mode,
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
    body: ProgramRule,
    async_: Union[Unset, bool] = False,
    atomic_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode
    ] = ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL,
    flush_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode
    ] = ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO,
    identifier: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier
    ] = ProgramRulePutJsonObjectputXmlObjectIdentifier.UID,
    import_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT,
    import_report_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode
    ] = ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS,
    import_strategy: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy
    ] = ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE,
    metadata_sync_import: Union[Unset, bool] = False,
    override_user: Union[Unset, str] = UNSET,
    preheat_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode
    ] = ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE,
    skip_sharing: Union[Unset, bool] = False,
    skip_translation: Union[Unset, bool] = False,
    skip_validation: Union[Unset, bool] = False,
    user: Union[Unset, str] = UNSET,
    user_override_mode: Union[
        Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode
    ] = ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE,
) -> Optional[WebMessage]:
    """[no description yet]

    Args:
        uid (str): A UID for an ProgramRule object
            (Java name `org.hisp.dhis.programrule.ProgramRule`) Example: te7tR6cY5OU.
        async_ (Union[Unset, bool]):  Default: False.
        atomic_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectAtomicMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectAtomicMode.ALL.
        flush_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectFlushMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectFlushMode.AUTO.
        identifier (Union[Unset, ProgramRulePutJsonObjectputXmlObjectIdentifier]):  Default:
            ProgramRulePutJsonObjectputXmlObjectIdentifier.UID.
        import_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectImportMode.COMMIT.
        import_report_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportReportMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportReportMode.ERRORS.
        import_strategy (Union[Unset, ProgramRulePutJsonObjectputXmlObjectImportStrategy]):
            Default: ProgramRulePutJsonObjectputXmlObjectImportStrategy.CREATE_AND_UPDATE.
        metadata_sync_import (Union[Unset, bool]):  Default: False.
        override_user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        preheat_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectPreheatMode]):  Default:
            ProgramRulePutJsonObjectputXmlObjectPreheatMode.REFERENCE.
        skip_sharing (Union[Unset, bool]):  Default: False.
        skip_translation (Union[Unset, bool]):  Default: False.
        skip_validation (Union[Unset, bool]):  Default: False.
        user (Union[Unset, str]): A UID for an User object
            (Java name `org.hisp.dhis.user.User`) Example: r87xh9Xn8ON.
        user_override_mode (Union[Unset, ProgramRulePutJsonObjectputXmlObjectUserOverrideMode]):
            Default: ProgramRulePutJsonObjectputXmlObjectUserOverrideMode.NONE.
        body (ProgramRule):

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
            preheat_mode=preheat_mode,
            skip_sharing=skip_sharing,
            skip_translation=skip_translation,
            skip_validation=skip_validation,
            user=user,
            user_override_mode=user_override_mode,
        )
    ).parsed
