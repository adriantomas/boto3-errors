# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class resiliencehubv2Error(Boto3Error):
    _SERVICE = "resiliencehubv2"


class AccessDeniedException(resiliencehubv2Error):
    """Access denied — caller lacks required permissions."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(resiliencehubv2Error):
    """Conflict — resource already exists."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(resiliencehubv2Error):
    """Internal service error."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(resiliencehubv2Error):
    """Resource not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(resiliencehubv2Error):
    """Service quota exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(resiliencehubv2Error):
    """Too many requests — rate limit exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(resiliencehubv2Error):
    """Validation error — invalid input parameters."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that failed validation."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[resiliencehubv2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
