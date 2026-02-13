# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ApplicationSignalsError(Boto3Error):
    _SERVICE = "application-signals"


class AccessDeniedException(ApplicationSignalsError):
    """You don't have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ApplicationSignalsError):
    """This operation attempted to create a resource that already exists."""
    _ERROR_CODE = "ConflictException"


class ResourceNotFoundException(ApplicationSignalsError):
    """Resource not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_type(self) -> str | None:
        """The resource type is not valid."""
        return self.response.get("ResourceType")

    @property
    def resource_id(self) -> str | None:
        """Can't find the resource id."""
        return self.response.get("ResourceId")


class ServiceQuotaExceededException(ApplicationSignalsError):
    """This request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ApplicationSignalsError):
    """The request was throttled because of quota limits."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ApplicationSignalsError):
    """The resource is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ApplicationSignalsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
