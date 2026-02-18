# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WorkspacesInstancesError(Boto3Error):
    _SERVICE = "workspaces-instances"


class AccessDeniedException(WorkspacesInstancesError):
    """Indicates insufficient permissions to perform the requested action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(WorkspacesInstancesError):
    """Signals a conflict with the current state of the resource."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the conflicting resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the conflicting resource."""
        return self.response.get("ResourceType")


class InternalServerException(WorkspacesInstancesError):
    """Indicates an unexpected server-side error occurred."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Recommended wait time before retrying the request."""
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(WorkspacesInstancesError):
    """Indicates the requested resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource that was not found."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource that was not found."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(WorkspacesInstancesError):
    """Indicates that a service quota has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """Specific code for the exceeded quota."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource related to the quota."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of resource related to the quota."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """Code identifying the service with the quota limitation."""
        return self.response.get("ServiceCode")


class ThrottlingException(WorkspacesInstancesError):
    """Indicates the request rate has exceeded limits."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """Specific code for the throttling quota."""
        return self.response.get("QuotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Recommended wait time before retrying the request."""
        return self.response.get("RetryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """Code identifying the service experiencing throttling."""
        return self.response.get("ServiceCode")


class ValidationException(WorkspacesInstancesError):
    """Indicates invalid input parameters in the request."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """List of fields that failed validation."""
        return self.response.get("FieldList")

    @property
    def reason(self) -> str | None:
        """Specific reason for the validation failure."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[WorkspacesInstancesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
