# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MarketplaceDiscoveryError(Boto3Error):
    _SERVICE = "marketplace-discovery"


class AccessDeniedException(MarketplaceDiscoveryError):
    """You don't have sufficient access to perform this action. Verify that you have the
    required permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(MarketplaceDiscoveryError):
    """Unexpected error during processing of the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MarketplaceDiscoveryError):
    """The specified resource doesn't exist. Verify that the identifier is correct."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(MarketplaceDiscoveryError):
    """The request was denied due to request throttling. Reduce the frequency of your
    requests and retry.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(MarketplaceDiscoveryError):
    """The input fails to satisfy the constraints specified by the service. Check the
    `reason` field for the constraint that failed.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason that the input fails to satisfy the constraints that the Discovery
        API specifies. This field has one of the following values:
        INVALID_PAGINATION_TOKEN

        The `nextToken` value is malformed, expired, or belongs to a different request.
        Start the pagination again from the first page. MALFORMED_REQUEST_PARAMETERS

        One or more request parameters have an invalid value. Correct the parameters
        that you specified, and then resubmit your request. PAGINATION_LIMIT_EXCEEDED

        The request asks for results beyond the deepest page that the operation returns.
        Narrow your request with filters or a more specific search.
        """
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[MarketplaceDiscoveryError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
