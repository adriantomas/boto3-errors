# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ArtifactError(Boto3Error):
    _SERVICE = "artifact"


class AccessDeniedException(ArtifactError):
    """User does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ArtifactError):
    """Request to create/modify content would result in a conflict."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the affected resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the affected resource."""
        return self.response.get("resourceType")


class InternalServerException(ArtifactError):
    """An unknown server exception has occurred."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Number of seconds in which the caller can retry the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(ArtifactError):
    """Request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the affected resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the affected resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(ArtifactError):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the affected resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the affected resource."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """Code for the affected service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Code for the affected quota."""
        return self.response.get("quotaCode")


class ThrottlingException(ArtifactError):
    """Request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """Code for the affected service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Code for the affected quota."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Number of seconds in which the caller can retry the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(ArtifactError):
    """Request fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """Reason the request failed validation."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The field that caused the error, if applicable."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[ArtifactError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
