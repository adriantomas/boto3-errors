# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class PanoramaError(Boto3Error):
    _SERVICE = "panorama"


class AccessDeniedException(PanoramaError):
    """The requestor does not have permission to access the target action or resource."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(PanoramaError):
    """The target resource is in use."""
    _ERROR_CODE = "ConflictException"

    @property
    def error_arguments(self) -> list[Any] | None:
        """A list of attributes that led to the exception and their values."""
        return self.response.get("ErrorArguments")

    @property
    def error_id(self) -> str | None:
        """A unique ID for the error."""
        return self.response.get("ErrorId")

    @property
    def resource_id(self) -> str | None:
        """The resource's ID."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource's type."""
        return self.response.get("ResourceType")


class InternalServerException(PanoramaError):
    """An internal error occurred."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds a client should wait before retrying the call."""
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(PanoramaError):
    """The target resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The resource's ID."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource's type."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(PanoramaError):
    """The request would cause a limit to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The name of the limit."""
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The target resource's ID."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The target resource's type."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The name of the service."""
        return self.response.get("ServiceCode")


class ValidationException(PanoramaError):
    """The request contains an invalid parameter value."""
    _ERROR_CODE = "ValidationException"

    @property
    def error_arguments(self) -> list[Any] | None:
        """A list of attributes that led to the exception and their values."""
        return self.response.get("ErrorArguments")

    @property
    def error_id(self) -> str | None:
        """A unique ID for the error."""
        return self.response.get("ErrorId")

    @property
    def fields(self) -> list[Any] | None:
        """A list of request parameters that failed validation."""
        return self.response.get("Fields")

    @property
    def reason(self) -> str | None:
        """The reason that validation failed."""
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[PanoramaError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
