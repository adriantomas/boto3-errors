# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class WickrError(Boto3Error):
    _SERVICE = "wickr"


class BadRequestError(WickrError):
    """The request was invalid or malformed. This error occurs when the request parameters
    do not meet the API requirements, such as invalid field values, missing required
    parameters, or improperly formatted data.
    """

    _ERROR_CODE = "BadRequestError"


class ForbiddenError(WickrError):
    """Access to the requested resource is forbidden. This error occurs when the
    authenticated user does not have the necessary permissions to perform the requested
    operation, even though they are authenticated.
    """

    _ERROR_CODE = "ForbiddenError"


class InternalServerError(WickrError):
    """An unexpected error occurred on the server while processing the request. This
    indicates a problem with the Wickr service itself rather than with the request. If
    this error persists, contact Amazon Web Services Support.
    """

    _ERROR_CODE = "InternalServerError"


class RateLimitError(WickrError):
    """The request was throttled because too many requests were sent in a short period of
    time. Wait a moment and retry the request. Consider implementing exponential backoff
    in your application.
    """

    _ERROR_CODE = "RateLimitError"


class ResourceNotFoundError(WickrError):
    """The requested resource could not be found. This error occurs when you try to access
    or modify a network, user, bot, security group, or other resource that doesn't exist
    or has been deleted.
    """

    _ERROR_CODE = "ResourceNotFoundError"


class UnauthorizedError(WickrError):
    """The request was not authenticated or the authentication credentials were invalid.
    This error occurs when the request lacks valid authentication credentials or the
    credentials have expired.
    """

    _ERROR_CODE = "UnauthorizedError"


class ValidationError(WickrError):
    """One or more fields in the request failed validation. This error provides detailed
    information about which fields were invalid and why, allowing you to correct the
    request and retry.
    """

    _ERROR_CODE = "ValidationError"

    @property
    def reasons(self) -> list[Any] | None:
        """A list of validation error details, where each item identifies a specific field
        that failed validation and explains the reason for the failure.
        """
        return self.response.get("reasons")


EXCEPTIONS: dict[str, type[WickrError]] = {
    "BadRequestError": BadRequestError,
    "ForbiddenError": ForbiddenError,
    "InternalServerError": InternalServerError,
    "RateLimitError": RateLimitError,
    "ResourceNotFoundError": ResourceNotFoundError,
    "UnauthorizedError": UnauthorizedError,
    "ValidationError": ValidationError,
}
