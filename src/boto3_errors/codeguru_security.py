# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CodeGuruSecurityError(Boto3Error):
    _SERVICE = "codeguru-security"


class AccessDeniedException(CodeGuruSecurityError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def error_code(self) -> str | None:
        """The identifier for the error."""
        return self.response.get("errorCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier for the resource you don't have access to."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource you don't have access to."""
        return self.response.get("resourceType")


class ConflictException(CodeGuruSecurityError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def error_code(self) -> str | None:
        """The identifier for the error."""
        return self.response.get("errorCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier for the service resource associated with the request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource associated with the request."""
        return self.response.get("resourceType")


class InternalServerException(CodeGuruSecurityError):
    """The server encountered an internal error and is unable to complete the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def error(self) -> str | None:
        """The internal error encountered by the server."""
        return self.response.get("error")


class ResourceNotFoundException(CodeGuruSecurityError):
    """The resource specified in the request was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def error_code(self) -> str | None:
        """The identifier for the error."""
        return self.response.get("errorCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier for the resource that was not found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that was not found."""
        return self.response.get("resourceType")


class ThrottlingException(CodeGuruSecurityError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def error_code(self) -> str | None:
        """The identifier for the error."""
        return self.response.get("errorCode")

    @property
    def service_code(self) -> str | None:
        """The identifier for the originating service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The identifier for the originating quota."""
        return self.response.get("quotaCode")


class ValidationException(CodeGuruSecurityError):
    """The input fails to satisfy the specified constraints."""
    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        """The identifier for the error."""
        return self.response.get("errorCode")

    @property
    def reason(self) -> str | None:
        """The reason the request failed validation."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The field that caused the error, if applicable."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[CodeGuruSecurityError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
