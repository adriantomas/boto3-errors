# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudWatchError(Boto3Error):
    _SERVICE = "cloudwatch"


class ConcurrentModificationException(CloudWatchError):
    """More than one process tried to modify a resource at the same time."""
    _ERROR_CODE = "ConcurrentModificationException"


class ConflictException(CloudWatchError):
    """This operation attempted to create a resource that already exists."""
    _ERROR_CODE = "ConflictException"


class DashboardInvalidInputError(CloudWatchError):
    """Some part of the dashboard data is invalid."""
    _ERROR_CODE = "InvalidParameterInput"

    @property
    def dashboard_validation_messages(self) -> list[Any] | None:
        return self.response.get("dashboardValidationMessages")


class DashboardNotFoundError(CloudWatchError):
    """The specified dashboard does not exist."""
    _ERROR_CODE = "ResourceNotFound"


class InternalServiceFault(CloudWatchError):
    """Request processing has failed due to some unknown error, exception, or failure."""
    _ERROR_CODE = "InternalServiceError"


class InvalidFormatFault(CloudWatchError):
    """Data was not syntactically valid JSON."""
    _ERROR_CODE = "InvalidFormat"


class InvalidNextToken(CloudWatchError):
    """The next token specified is invalid."""
    _ERROR_CODE = "InvalidNextToken"


class InvalidParameterCombinationException(CloudWatchError):
    """Parameters were used together that cannot be used together."""
    _ERROR_CODE = "InvalidParameterCombination"


class InvalidParameterValueException(CloudWatchError):
    """The value of an input parameter is bad or out-of-range."""
    _ERROR_CODE = "InvalidParameterValue"


class LimitExceededException(CloudWatchError):
    """The operation exceeded one or more limits."""
    _ERROR_CODE = "LimitExceededException"


class LimitExceededFault(CloudWatchError):
    """The quota for alarms for this customer has already been reached."""
    _ERROR_CODE = "LimitExceeded"


class MissingRequiredParameterException(CloudWatchError):
    """An input parameter that is required is missing."""
    _ERROR_CODE = "MissingParameter"


class ResourceNotFound(CloudWatchError):
    """The named resource does not exist."""
    _ERROR_CODE = "ResourceNotFound"


class ResourceNotFoundException(CloudWatchError):
    """The named resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        return self.response.get("ResourceType")


EXCEPTIONS: dict[str, type[CloudWatchError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConflictException": ConflictException,
    "InvalidParameterInput": DashboardInvalidInputError,
    "ResourceNotFound": DashboardNotFoundError,
    "InternalServiceError": InternalServiceFault,
    "InvalidFormat": InvalidFormatFault,
    "InvalidNextToken": InvalidNextToken,
    "InvalidParameterCombination": InvalidParameterCombinationException,
    "InvalidParameterValue": InvalidParameterValueException,
    "LimitExceededException": LimitExceededException,
    "LimitExceeded": LimitExceededFault,
    "MissingParameter": MissingRequiredParameterException,
    "ResourceNotFound": ResourceNotFound,
    "ResourceNotFoundException": ResourceNotFoundException,
}
