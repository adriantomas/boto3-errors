# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class QAppsError(Boto3Error):
    _SERVICE = "qapps"


class AccessDeniedException(QAppsError):
    """The client is not authorized to perform the requested operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(QAppsError):
    """The requested operation could not be completed due to a conflict with the current
    state of the resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource"""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource"""
        return self.response.get("resourceType")


class ContentTooLargeException(QAppsError):
    """The requested operation could not be completed because the content exceeds the
    maximum allowed size.
    """

    _ERROR_CODE = "ContentTooLargeException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource"""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource"""
        return self.response.get("resourceType")


class InternalServerException(QAppsError):
    """An internal service error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the operation"""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(QAppsError):
    """The requested resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource"""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource"""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(QAppsError):
    """The requested operation could not be completed because it would exceed the service's
    quota or limit.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The unique identifier of the resource"""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource"""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the service where the quota was exceeded"""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The code of the quota that was exceeded"""
        return self.response.get("quotaCode")


class ThrottlingException(QAppsError):
    """The requested operation could not be completed because too many requests were sent
    at once. Wait a bit and try again later.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The code for the service where the quota was exceeded"""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The code of the quota that was exceeded"""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the operation"""
        return self.response.get("retryAfterSeconds")


class UnauthorizedException(QAppsError):
    """The client is not authenticated or authorized to perform the requested operation."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(QAppsError):
    """The input failed to satisfy the constraints specified by the service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[QAppsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ContentTooLargeException": ContentTooLargeException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
