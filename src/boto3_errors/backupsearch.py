# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BackupSearchError(Boto3Error):
    _SERVICE = "backupsearch"


class AccessDeniedException(BackupSearchError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BackupSearchError):
    """This exception occurs when a conflict with a previous successful operation is
    detected. This generally occurs when the previous operation did not have time to
    propagate to the host serving the current request.

    A retry (with appropriate backoff logic) is the recommended response to this
    exception.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")


class InternalServerException(BackupSearchError):
    """An internal server error occurred. Retry your request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Retry the call after number of seconds."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(BackupSearchError):
    """The resource was not found for this request.

    Confirm the resource information, such as the ARN or type is correct and exists,
    then retry the request.
    """

    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Hypothetical identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Hypothetical type of the resource affected."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(BackupSearchError):
    """The request denied due to exceeding the quota limits permitted."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """This is the code specific to the quota type."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of resource."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """This is the code unique to the originating service with the quota."""
        return self.response.get("serviceCode")


class ThrottlingException(BackupSearchError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """This is the code unique to the originating service with the quota."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Retry the call after number of seconds."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """This is the code unique to the originating service."""
        return self.response.get("serviceCode")


class ValidationException(BackupSearchError):
    """The input fails to satisfy the constraints specified by a service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BackupSearchError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
