# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudSearchError(Boto3Error):
    _SERVICE = "cloudsearch"


class BaseException(CloudSearchError):
    """An error occurred while processing the request."""
    _ERROR_CODE = "BaseException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class DisabledOperationException(CloudSearchError):
    """The request was rejected because it attempted an operation which is not enabled."""
    _ERROR_CODE = "DisabledAction"


class InternalException(CloudSearchError):
    """An internal error occurred while processing the request. If this problem persists,
    report an issue from the Service Health Dashboard.
    """

    _ERROR_CODE = "InternalException"


class InvalidTypeException(CloudSearchError):
    """The request was rejected because it specified an invalid type definition."""
    _ERROR_CODE = "InvalidType"


class LimitExceededException(CloudSearchError):
    """The request was rejected because a resource limit has already been met."""
    _ERROR_CODE = "LimitExceeded"


class ResourceAlreadyExistsException(CloudSearchError):
    """The request was rejected because it attempted to create a resource that already
    exists.
    """

    _ERROR_CODE = "ResourceAlreadyExists"


class ResourceNotFoundException(CloudSearchError):
    """The request was rejected because it attempted to reference a resource that does not
    exist.
    """

    _ERROR_CODE = "ResourceNotFound"


class ValidationException(CloudSearchError):
    """The request was rejected because it has invalid parameters."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CloudSearchError]] = {
    "BaseException": BaseException,
    "DisabledAction": DisabledOperationException,
    "InternalException": InternalException,
    "InvalidType": InvalidTypeException,
    "LimitExceeded": LimitExceededException,
    "ResourceAlreadyExists": ResourceAlreadyExistsException,
    "ResourceNotFound": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
