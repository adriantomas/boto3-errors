# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PIError(Boto3Error):
    _SERVICE = "pi"


class InternalServiceError(PIError):
    """The request failed due to an unknown error."""
    _ERROR_CODE = "InternalServiceError"


class InvalidArgumentException(PIError):
    """One of the arguments provided is invalid for this request."""
    _ERROR_CODE = "InvalidArgumentException"


class NotAuthorizedException(PIError):
    """The user is not authorized to perform this request."""
    _ERROR_CODE = "NotAuthorizedException"


EXCEPTIONS: dict[str, type[PIError]] = {
    "InternalServiceError": InternalServiceError,
    "InvalidArgumentException": InvalidArgumentException,
    "NotAuthorizedException": NotAuthorizedException,
}
