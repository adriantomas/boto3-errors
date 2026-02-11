# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class deadlineError(Boto3Error):
    _SERVICE = "deadline"


class AccessDeniedException(deadlineError):
    """You don't have permission to perform the action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def context(self) -> dict[str, Any] | None:
        """Information about the resources in use when the exception was thrown."""
        return self.response.get("context")


class ConflictException(deadlineError):
    """Your request has conflicting operations. This can occur if you're trying to perform
    more than one operation on the same resource at the same time.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """A description of the error."""
        return self.response.get("reason")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource in use."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource in use."""
        return self.response.get("resourceType")

    @property
    def context(self) -> dict[str, Any] | None:
        """Information about the resources in use when the exception was thrown."""
        return self.response.get("context")


class InternalServerErrorException(deadlineError):
    """Deadline Cloud can't process your request right now. Try again later."""
    _ERROR_CODE = "InternalServerErrorException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds a client should wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(deadlineError):
    """The requested resource can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that couldn't be found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that couldn't be found."""
        return self.response.get("resourceType")

    @property
    def context(self) -> dict[str, Any] | None:
        """Information about the resources in use when the exception was thrown."""
        return self.response.get("context")


class ServiceQuotaExceededException(deadlineError):
    """You exceeded your service quota. Service quotas, also referred to as limits, are the
    maximum number of service resources or operations for your Amazon Web Services
    account.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def reason(self) -> str | None:
        """A string that describes the reason the quota was exceeded."""
        return self.response.get("reason")

    @property
    def resource_type(self) -> str | None:
        """The type of the affected resource"""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """Identifies the service that exceeded the quota."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Identifies the quota that has been exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the affected resource."""
        return self.response.get("resourceId")

    @property
    def context(self) -> dict[str, Any] | None:
        """Information about the resources in use when the exception was thrown."""
        return self.response.get("context")


class ThrottlingException(deadlineError):
    """Your request exceeded a request rate quota."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """Identifies the service that is being throttled."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Identifies the quota that is being throttled."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds a client should wait before retrying the request."""
        return self.response.get("retryAfterSeconds")

    @property
    def context(self) -> dict[str, Any] | None:
        """Information about the resources in use when the exception was thrown."""
        return self.response.get("context")


class ValidationException(deadlineError):
    """The request isn't valid. This can occur if your request contains malformed JSON or
    unsupported characters.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason that the request failed validation."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that failed validation."""
        return self.response.get("fieldList")

    @property
    def context(self) -> dict[str, Any] | None:
        """Information about the resources in use when the exception was thrown."""
        return self.response.get("context")


EXCEPTIONS: dict[str, type[deadlineError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerErrorException": InternalServerErrorException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
