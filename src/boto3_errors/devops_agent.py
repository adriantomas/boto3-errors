# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DevOpsAgentError(Boto3Error):
    _SERVICE = "devops-agent"


class AccessDeniedException(DevOpsAgentError):
    """Access to the requested resource is denied due to insufficient permissions."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(DevOpsAgentError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"


class ContentSizeExceededException(DevOpsAgentError):
    """This exception is thrown when the content size exceeds the allowed limit."""
    _ERROR_CODE = "ContentSizeExceededException"


class IdentityCenterServiceException(DevOpsAgentError):
    """Calls to the customer Identity Center have failed"""
    _ERROR_CODE = "IdentityCenterServiceException"

    @property
    def underlying_error_code(self) -> str | None:
        """The Idc error code"""
        return self.response.get("underlyingErrorCode")


class InternalServerException(DevOpsAgentError):
    """This exception is thrown when an unexpected error occurs in the processing of a
    request.
    """

    _ERROR_CODE = "InternalServerException"


class InvalidParameterException(DevOpsAgentError):
    """One or more parameters provided in the request are invalid."""
    _ERROR_CODE = "InvalidParameterException"


class ResourceNotFoundException(DevOpsAgentError):
    """The requested resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(DevOpsAgentError):
    """The request would exceed the service quota limit."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(DevOpsAgentError):
    """The request was throttled due to too many requests. Please slow down and try again."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(DevOpsAgentError):
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


EXCEPTIONS: dict[str, type[DevOpsAgentError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ContentSizeExceededException": ContentSizeExceededException,
    "IdentityCenterServiceException": IdentityCenterServiceException,
    "InternalServerException": InternalServerException,
    "InvalidParameterException": InvalidParameterException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
