# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AccessAnalyzerError(Boto3Error):
    _SERVICE = "accessanalyzer"


class AccessDeniedException(AccessAnalyzerError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(AccessAnalyzerError):
    """A conflict exception error."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")


class InternalServerException(AccessAnalyzerError):
    """Internal server error."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The seconds to wait to retry."""
        return self.response.get("retryAfterSeconds")


class InvalidParameterException(AccessAnalyzerError):
    """The specified parameter is invalid."""
    _ERROR_CODE = "InvalidParameterException"


class ResourceNotFoundException(AccessAnalyzerError):
    """The specified resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(AccessAnalyzerError):
    """Service quote met error."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")


class ThrottlingException(AccessAnalyzerError):
    """Throttling limit exceeded error."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The seconds to wait to retry."""
        return self.response.get("retryAfterSeconds")


class UnprocessableEntityException(AccessAnalyzerError):
    """The specified entity could not be processed."""
    _ERROR_CODE = "UnprocessableEntityException"


class ValidationException(AccessAnalyzerError):
    """Validation exception error."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that didn't validate."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[AccessAnalyzerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidParameterException": InvalidParameterException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnprocessableEntityException": UnprocessableEntityException,
    "ValidationException": ValidationException,
}
