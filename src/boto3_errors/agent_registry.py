# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AgentRegistryError(Boto3Error):
    _SERVICE = "agent-registry"


class AccessDeniedException(AgentRegistryError):
    """The caller is not authorized to perform the requested action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(AgentRegistryError):
    """The request failed due to an unexpected internal error; the caller may retry."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(AgentRegistryError):
    """The requested resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(AgentRegistryError):
    """The request was denied due to request throttling; the caller may retry after a
    delay.
    """

    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(AgentRegistryError):
    """The request could not be authenticated."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(AgentRegistryError):
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


EXCEPTIONS: dict[str, type[AgentRegistryError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
