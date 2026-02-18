# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CostExplorerError(Boto3Error):
    _SERVICE = "ce"


class BillExpirationException(CostExplorerError):
    """The requested report expired. Update the date interval and try again."""
    _ERROR_CODE = "BillExpirationException"


class DataUnavailableException(CostExplorerError):
    """The requested data is unavailable."""
    _ERROR_CODE = "DataUnavailableException"


class GenerationExistsException(CostExplorerError):
    """A request to generate a recommendation is already in progress."""
    _ERROR_CODE = "GenerationExistsException"


class InvalidNextTokenException(CostExplorerError):
    """The pagination token is invalid. Try again without a pagination token."""
    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(CostExplorerError):
    """You made too many calls in a short period of time. Try again later."""
    _ERROR_CODE = "LimitExceededException"


class RequestChangedException(CostExplorerError):
    """Your request parameters changed between pages. Try again with the old parameters or
    without a pagination token.
    """

    _ERROR_CODE = "RequestChangedException"


class ResourceNotFoundException(CostExplorerError):
    """The specified ARN in the request doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("ResourceName")


class ServiceQuotaExceededException(CostExplorerError):
    """You've reached the limit on the number of resources you can create, or exceeded the
    size of an individual resource.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class TooManyTagsException(CostExplorerError):
    """Can occur if you specify a number of tags for a resource greater than the maximum 50
    user tags per resource.
    """

    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        return self.response.get("ResourceName")


class UnknownMonitorException(CostExplorerError):
    """The cost anomaly monitor does not exist for the account."""
    _ERROR_CODE = "UnknownMonitorException"


class UnknownSubscriptionException(CostExplorerError):
    """The cost anomaly subscription does not exist for the account."""
    _ERROR_CODE = "UnknownSubscriptionException"


class UnresolvableUsageUnitException(CostExplorerError):
    """Cost Explorer was unable to identify the usage unit. Provide
    `UsageType/UsageTypeGroup` filter selections that contain matching units, for
    example: `hours`.
    """

    _ERROR_CODE = "UnresolvableUsageUnitException"


EXCEPTIONS: dict[str, type[CostExplorerError]] = {
    "BillExpirationException": BillExpirationException,
    "DataUnavailableException": DataUnavailableException,
    "GenerationExistsException": GenerationExistsException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "RequestChangedException": RequestChangedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyTagsException": TooManyTagsException,
    "UnknownMonitorException": UnknownMonitorException,
    "UnknownSubscriptionException": UnknownSubscriptionException,
    "UnresolvableUsageUnitException": UnresolvableUsageUnitException,
}
