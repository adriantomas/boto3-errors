# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SecurityAgentError(Boto3Error):
    _SERVICE = "securityagent"


class AccessDeniedException(SecurityAgentError):
    """Request denied due to insufficient permissions"""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SecurityAgentError):
    """Request conflicts with current resource state"""
    _ERROR_CODE = "ConflictException"


class InternalServerException(SecurityAgentError):
    """Unexpected server error occurred"""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SecurityAgentError):
    """Specified resource was not found"""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(SecurityAgentError):
    """Request denied due to throttling"""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """Quota code for throttling limit"""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """Service code for throttling limit"""
        return self.response.get("serviceCode")


class ValidationException(SecurityAgentError):
    """A standard error for input validation failures. This should be thrown by services
    when a member of the input structure falls outside of the modeled or documented
    constraints.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of specific failures encountered while validating the input. A member can
        appear in this list more than once if it failed to satisfy multiple constraints.
        """
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[SecurityAgentError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
