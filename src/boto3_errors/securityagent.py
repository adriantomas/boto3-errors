# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SecurityAgentError(Boto3Error):
    _SERVICE = "securityagent"


class AccessDeniedException(SecurityAgentError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SecurityAgentError):
    """The request could not be completed due to a conflict with the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(SecurityAgentError):
    """An unexpected error occurred during the processing of your request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SecurityAgentError):
    """The specified resource was not found. Verify that the resource identifier is correct
    and that the resource exists in the specified agent space or account.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(SecurityAgentError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """Quota code for throttling limit."""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """Service code for throttling limit."""
        return self.response.get("serviceCode")


class ValidationException(SecurityAgentError):
    """The input fails to satisfy the constraints specified by the service."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of specific failures encountered during validation."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[SecurityAgentError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
