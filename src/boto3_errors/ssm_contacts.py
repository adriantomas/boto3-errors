# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SSMContactsError(Boto3Error):
    _SERVICE = "ssm-contacts"


class AccessDeniedException(SSMContactsError):
    """You don't have sufficient access to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SSMContactsError):
    """Updating or deleting a resource causes an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource in use"""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource in use"""
        return self.response.get("ResourceType")

    @property
    def dependent_entities(self) -> list[Any] | None:
        """List of dependent entities containing information on relation type and
        resourceArns linked to the resource in use
        """
        return self.response.get("DependentEntities")


class DataEncryptionException(SSMContactsError):
    """The operation failed to due an encryption key error."""
    _ERROR_CODE = "DataEncryptionException"


class InternalServerException(SSMContactsError):
    """Unexpected error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried"""
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(SSMContactsError):
    """Request references a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Hypothetical resource identifier that was not found"""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Hypothetical resource type that was not found"""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(SSMContactsError):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected"""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected"""
        return self.response.get("ResourceType")

    @property
    def quota_code(self) -> str | None:
        """Service Quotas requirement to identify originating service"""
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        """Service Quotas requirement to identify originating quota"""
        return self.response.get("ServiceCode")


class ThrottlingException(SSMContactsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """Service Quotas requirement to identify originating service"""
        return self.response.get("QuotaCode")

    @property
    def service_code(self) -> str | None:
        """Service Quotas requirement to identify originating quota"""
        return self.response.get("ServiceCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried"""
        return self.response.get("RetryAfterSeconds")


class ValidationException(SSMContactsError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """Reason the request failed validation"""
        return self.response.get("Reason")

    @property
    def fields(self) -> list[Any] | None:
        """The fields that caused the error"""
        return self.response.get("Fields")


EXCEPTIONS: dict[str, type[SSMContactsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DataEncryptionException": DataEncryptionException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
