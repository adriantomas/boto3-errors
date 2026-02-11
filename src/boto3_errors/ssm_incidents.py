# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SSMIncidentsError(Boto3Error):
    _SERVICE = "ssm-incidents"


class AccessDeniedException(SSMIncidentsError):
    """You don't have sufficient access to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SSMIncidentsError):
    """Updating or deleting a resource causes an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_identifier(self) -> str | None:
        """The identifier of the requested resource"""
        return self.response.get("resourceIdentifier")

    @property
    def resource_type(self) -> str | None:
        """The resource type"""
        return self.response.get("resourceType")

    @property
    def retry_after(self) -> str | None:
        """If present in the output, the operation can be retried after this time"""
        return self.response.get("retryAfter")


class InternalServerException(SSMIncidentsError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SSMIncidentsError):
    """Request references a resource which doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_identifier(self) -> str | None:
        """The identifier for the requested resource"""
        return self.response.get("resourceIdentifier")

    @property
    def resource_type(self) -> str | None:
        """The resource type"""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(SSMIncidentsError):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """Originating quota code"""
        return self.response.get("quotaCode")

    @property
    def resource_identifier(self) -> str | None:
        """The identifier for the requested resource"""
        return self.response.get("resourceIdentifier")

    @property
    def resource_type(self) -> str | None:
        """The resource type"""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """Originating service code"""
        return self.response.get("serviceCode")


class ThrottlingException(SSMIncidentsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """Originating quota code"""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """Originating service code"""
        return self.response.get("serviceCode")


class ValidationException(SSMIncidentsError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SSMIncidentsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
