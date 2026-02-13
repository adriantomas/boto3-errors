# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DirectoryServiceDataError(Boto3Error):
    _SERVICE = "ds-data"


class AccessDeniedException(DirectoryServiceDataError):
    """You don't have permission to perform the request or access the directory. It can
    also occur when the `DirectoryId` doesn't exist or the user, member, or group might
    be outside of your organizational unit (OU).

     Make sure that you have the authentication and authorization to perform the action.
    Review the directory information in the request, and make sure that the object isn't
    outside of your OU.
    """

    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """Reason the request was unauthorized."""
        return self.response.get("Reason")


class ConflictException(DirectoryServiceDataError):
    """This error will occur when you try to create a resource that conflicts with an
    existing object. It can also occur when adding a member to a group that the member
    is already in.

     This error can be caused by a request sent within the 8-hour idempotency window
    with the same client token but different input parameters. Client tokens should not
    be re-used across different requests. After 8 hours, any request with the same
    client token is treated as a new request.
    """

    _ERROR_CODE = "ConflictException"


class DirectoryUnavailableException(DirectoryServiceDataError):
    """The request could not be completed due to a problem in the configuration or current
    state of the specified directory.
    """

    _ERROR_CODE = "DirectoryUnavailableException"

    @property
    def reason(self) -> str | None:
        """Reason the request failed for the specified directory."""
        return self.response.get("Reason")


class InternalServerException(DirectoryServiceDataError):
    """The operation didn't succeed because an internal error occurred. Try again later."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(DirectoryServiceDataError):
    """The resource couldn't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(DirectoryServiceDataError):
    """The limit on the number of requests per second has been exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The recommended amount of seconds to retry after a throttling exception."""
        return self.response.get("RetryAfterSeconds")


class ValidationException(DirectoryServiceDataError):
    """The request isn't valid. Review the details in the error message to update the
    invalid parameters or values in your request.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """Reason the request failed validation."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[DirectoryServiceDataError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DirectoryUnavailableException": DirectoryUnavailableException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
