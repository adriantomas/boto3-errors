# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceEntitlementServiceError(Boto3Error):
    _SERVICE = "marketplace-entitlement"


class InternalServiceErrorException(MarketplaceEntitlementServiceError):
    """An internal error has occurred. Retry your request. If the problem persists, post a
    message with details on the AWS forums.
    """

    _ERROR_CODE = "InternalServiceErrorException"


class InvalidParameterException(MarketplaceEntitlementServiceError):
    """One or more parameters in your request was invalid."""
    _ERROR_CODE = "InvalidParameterException"


class ThrottlingException(MarketplaceEntitlementServiceError):
    """The calls to the GetEntitlements API are throttled."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[MarketplaceEntitlementServiceError]] = {
    "InternalServiceErrorException": InternalServiceErrorException,
    "InvalidParameterException": InvalidParameterException,
    "ThrottlingException": ThrottlingException,
}
