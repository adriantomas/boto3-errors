# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SupportAuthZError(Boto3Error):
    _SERVICE = "supportauthz"


class AccessDeniedException(SupportAuthZError):
    """You don't have sufficient permissions to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SupportAuthZError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(SupportAuthZError):
    """An internal service error occurred. Try again later."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(SupportAuthZError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(SupportAuthZError):
    """The request exceeds a service quota for your account."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The quota code of the exceeded quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded the quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeded the quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code of the originating service."""
        return self.response.get("serviceCode")


class ThrottlingException(SupportAuthZError):
    """The request rate exceeded the allowed limit. Try again later."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(SupportAuthZError):
    """The input fails to satisfy the constraints specified by the service."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that fail validation. Each entry identifies the field and the
        reason for the constraint violation.
        """
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[SupportAuthZError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
