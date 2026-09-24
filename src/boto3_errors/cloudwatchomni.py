# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CloudWatchOmniError(Boto3Error):
    _SERVICE = "cloudwatchomni"


class AccessDeniedException(CloudWatchOmniError):
    """The caller is not authorized to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(CloudWatchOmniError):
    """The operation could not be completed because of a conflict with the current state of
    the resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def conflict_type(self) -> str | None:
        """The type of conflict that caused the request to fail. Not always present."""
        return self.response.get("conflictType")

    @property
    def error_code(self) -> str | None:
        """The error code associated with the conflict. Not always present."""
        return self.response.get("errorCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that is in conflict. Not always present."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is in conflict. Not always present."""
        return self.response.get("resourceType")


class InternalServerException(CloudWatchOmniError):
    """An unexpected error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the internal error."""
        return self.response.get("errorCode")


class ResourceNotFoundException(CloudWatchOmniError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the failure."""
        return self.response.get("errorCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that could not be found. Not always present."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that could not be found. Not always present."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(CloudWatchOmniError):
    """A service quota was exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(CloudWatchOmniError):
    """The request was throttled due to exceeding the allowed request rate."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request. Not always present."""
        return self.response.get("retryAfterSeconds")


class ValidationException(CloudWatchOmniError):
    """A parameter is specified incorrectly."""
    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        """The error code associated with the validation failure."""
        return self.response.get("errorCode")


EXCEPTIONS: dict[str, type[CloudWatchOmniError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
