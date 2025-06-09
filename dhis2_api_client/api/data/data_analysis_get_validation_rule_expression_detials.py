from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.validation_rule_expression_details import ValidationRuleExpressionDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    attribute_option_combo_id: Union[Unset, str] = UNSET,
    organisation_unit_id: str,
    period_id: str,
    validation_rule_id: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["attributeOptionComboId"] = attribute_option_combo_id

    params["organisationUnitId"] = organisation_unit_id

    params["periodId"] = period_id

    params["validationRuleId"] = validation_rule_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dataAnalysis/validationRulesExpression",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ValidationRuleExpressionDetails]:
    if response.status_code == 200:
        response_200 = ValidationRuleExpressionDetails.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ValidationRuleExpressionDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute_option_combo_id: Union[Unset, str] = UNSET,
    organisation_unit_id: str,
    period_id: str,
    validation_rule_id: str,
) -> Response[ValidationRuleExpressionDetails]:
    """[no description yet]

    Args:
        attribute_option_combo_id (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        organisation_unit_id (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        period_id (str):
        validation_rule_id (str): A UID for an ValidationRule object
            (Java name `org.hisp.dhis.validation.ValidationRule`) Example: C0oy6Qm5HT4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidationRuleExpressionDetails]
    """

    kwargs = _get_kwargs(
        attribute_option_combo_id=attribute_option_combo_id,
        organisation_unit_id=organisation_unit_id,
        period_id=period_id,
        validation_rule_id=validation_rule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute_option_combo_id: Union[Unset, str] = UNSET,
    organisation_unit_id: str,
    period_id: str,
    validation_rule_id: str,
) -> Optional[ValidationRuleExpressionDetails]:
    """[no description yet]

    Args:
        attribute_option_combo_id (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        organisation_unit_id (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        period_id (str):
        validation_rule_id (str): A UID for an ValidationRule object
            (Java name `org.hisp.dhis.validation.ValidationRule`) Example: C0oy6Qm5HT4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidationRuleExpressionDetails
    """

    return sync_detailed(
        client=client,
        attribute_option_combo_id=attribute_option_combo_id,
        organisation_unit_id=organisation_unit_id,
        period_id=period_id,
        validation_rule_id=validation_rule_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute_option_combo_id: Union[Unset, str] = UNSET,
    organisation_unit_id: str,
    period_id: str,
    validation_rule_id: str,
) -> Response[ValidationRuleExpressionDetails]:
    """[no description yet]

    Args:
        attribute_option_combo_id (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        organisation_unit_id (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        period_id (str):
        validation_rule_id (str): A UID for an ValidationRule object
            (Java name `org.hisp.dhis.validation.ValidationRule`) Example: C0oy6Qm5HT4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ValidationRuleExpressionDetails]
    """

    kwargs = _get_kwargs(
        attribute_option_combo_id=attribute_option_combo_id,
        organisation_unit_id=organisation_unit_id,
        period_id=period_id,
        validation_rule_id=validation_rule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    attribute_option_combo_id: Union[Unset, str] = UNSET,
    organisation_unit_id: str,
    period_id: str,
    validation_rule_id: str,
) -> Optional[ValidationRuleExpressionDetails]:
    """[no description yet]

    Args:
        attribute_option_combo_id (Union[Unset, str]): A UID for an CategoryOptionCombo object
            (Java name `org.hisp.dhis.category.CategoryOptionCombo`) Example: o5Bz19pJ30h.
        organisation_unit_id (str): A UID for an OrganisationUnit object
            (Java name `org.hisp.dhis.organisationunit.OrganisationUnit`) Example: xj2sS1ni0Q9.
        period_id (str):
        validation_rule_id (str): A UID for an ValidationRule object
            (Java name `org.hisp.dhis.validation.ValidationRule`) Example: C0oy6Qm5HT4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ValidationRuleExpressionDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            attribute_option_combo_id=attribute_option_combo_id,
            organisation_unit_id=organisation_unit_id,
            period_id=period_id,
            validation_rule_id=validation_rule_id,
        )
    ).parsed
