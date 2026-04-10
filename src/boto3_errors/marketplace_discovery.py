# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceDiscoveryError(Boto3Error):
    _SERVICE = "marketplace-discovery"


class AccessDeniedException(MarketplaceDiscoveryError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(MarketplaceDiscoveryError):
    """Unexpected error during processing of the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MarketplaceDiscoveryError):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(MarketplaceDiscoveryError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(MarketplaceDiscoveryError):
    """The input fails to satisfy the constraints specified by the service."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason that the input fails to satisfy the constraints specified by the
        service.
        """
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[MarketplaceDiscoveryError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
