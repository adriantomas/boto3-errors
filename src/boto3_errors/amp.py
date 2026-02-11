# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ampError(Boto3Error):
    _SERVICE = "amp"


class AccessDeniedException(ampError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ampError):
    """The request would cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")


class InternalServerException(ampError):
    """An unexpected error occurred during the processing of the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(ampError):
    """The request references a resources that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(ampError):
    """Completing the request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """Service quotas code for the originating service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Service quotas code of the originating quota."""
        return self.response.get("quotaCode")


class ThrottlingException(ampError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """Service quotas code for the originating service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Service quotas code for the originating quota."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")


class ValidationException(ampError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """Reason the request failed validation."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The field that caused the error, if applicable."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[ampError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
