# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class EvidentlyError(Boto3Error):
    _SERVICE = "evidently"


class AccessDeniedException(EvidentlyError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(EvidentlyError):
    """A resource was in an inconsistent state during an update or a deletion."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")


class InternalServerException(EvidentlyError):
    """Unexpected error while processing the request. Retry the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(EvidentlyError):
    """The request references a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(EvidentlyError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that caused the exception."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The ID of the service that is associated with the error."""
        return self.response.get("serviceCode")


class ServiceUnavailableException(EvidentlyError):
    """The service was unavailable. Retry the request."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(EvidentlyError):
    """The request was denied because of request throttling. Retry the request."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """The ID of the service that is associated with the error."""
        return self.response.get("serviceCode")


class ValidationException(EvidentlyError):
    """The value of a parameter in the request caused an error."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The parameter that caused the exception."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """A reason for the error."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[EvidentlyError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
