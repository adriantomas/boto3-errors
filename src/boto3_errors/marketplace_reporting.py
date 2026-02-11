# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceReportingError(Boto3Error):
    _SERVICE = "marketplace-reporting"


class AccessDeniedException(MarketplaceReportingError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(MarketplaceReportingError):
    """The request is malformed, or it contains an error such as an invalid parameter.
    Ensure the request has all required parameters.
    """

    _ERROR_CODE = "BadRequestException"


class InternalServerException(MarketplaceReportingError):
    """The operation failed due to a server error."""
    _ERROR_CODE = "InternalServerException"


class UnauthorizedException(MarketplaceReportingError):
    """You do not have permission to perform this action."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[MarketplaceReportingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "InternalServerException": InternalServerException,
    "UnauthorizedException": UnauthorizedException,
}
