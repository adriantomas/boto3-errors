# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SecurityHubError(Boto3Error):
    _SERVICE = "securityhub"


class AccessDeniedException(SecurityHubError):
    """You don't have permission to perform the action specified in the request."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ConflictException(SecurityHubError):
    """The request causes conflict with the current state of the service resource."""
    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class InternalException(SecurityHubError):
    """Internal server error."""
    _ERROR_CODE = "InternalException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class InternalServerException(SecurityHubError):
    """The request has failed due to an internal failure of the service."""
    _ERROR_CODE = "InternalServerException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class InvalidAccessException(SecurityHubError):
    """The account doesn't have permission to perform this action."""
    _ERROR_CODE = "InvalidAccessException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class InvalidInputException(SecurityHubError):
    """The request was rejected because you supplied an invalid or out-of-range value for
    an input parameter.
    """

    _ERROR_CODE = "InvalidInputException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class LimitExceededException(SecurityHubError):
    """The request was rejected because it attempted to create resources beyond the current
    Amazon Web Services account or throttling limits. The error code describes the limit
    exceeded.
    """

    _ERROR_CODE = "LimitExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ResourceConflictException(SecurityHubError):
    """The resource specified in the request conflicts with an existing resource."""
    _ERROR_CODE = "ResourceConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ResourceInUseException(SecurityHubError):
    """The request was rejected because it conflicts with the resource's availability. For
    example, you tried to update a security control that's currently in the `UPDATING`
    state.
    """

    _ERROR_CODE = "ResourceInUseException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ResourceNotFoundException(SecurityHubError):
    """The request was rejected because we can't find the specified resource."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ServiceQuotaExceededException(SecurityHubError):
    """The request was rejected because it would exceed the service quota limit."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ThrottlingException(SecurityHubError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


class ValidationException(SecurityHubError):
    """The request has failed validation because it's missing required fields or has
    invalid inputs.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def code(self) -> str | None:
        return self.response.get("Code")


EXCEPTIONS: dict[str, type[SecurityHubError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalException": InternalException,
    "InternalServerException": InternalServerException,
    "InvalidAccessException": InvalidAccessException,
    "InvalidInputException": InvalidInputException,
    "LimitExceededException": LimitExceededException,
    "ResourceConflictException": ResourceConflictException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
