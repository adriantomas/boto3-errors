# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class repostspaceError(Boto3Error):
    _SERVICE = "repostspace"


class AccessDeniedException(repostspaceError):
    """User does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(repostspaceError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("resourceType")


class InternalServerException(repostspaceError):
    """Unexpected error during processing of request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(repostspaceError):
    """Request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(repostspaceError):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code to identify the quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The id of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code to identify the service."""
        return self.response.get("serviceCode")


class ThrottlingException(repostspaceError):
    """Request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code to identify the quota."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code to identify the service."""
        return self.response.get("serviceCode")


class ValidationException(repostspaceError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The field that caused the error, if applicable."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason why the request failed validation."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[repostspaceError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
