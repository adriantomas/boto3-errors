# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AgentRegistryControlError(Boto3Error):
    _SERVICE = "agent-registry-control"


class AccessDeniedException(AgentRegistryControlError):
    """The caller is not authorized to perform the requested action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(AgentRegistryControlError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(AgentRegistryControlError):
    """The request failed due to an unexpected internal error; the caller may retry."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(AgentRegistryControlError):
    """The requested resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(AgentRegistryControlError):
    """The request would exceed a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(AgentRegistryControlError):
    """The request was denied due to request throttling; the caller may retry after a
    delay.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(AgentRegistryControlError):
    """The request failed validation of one or more input fields."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of input fields that failed validation."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason the request failed validation."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[AgentRegistryControlError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
