# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class BackupGatewayError(Boto3Error):
    _SERVICE = "backup-gateway"


class AccessDeniedException(BackupGatewayError):
    """The operation cannot proceed because you have insufficient permissions."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def error_code(self) -> str | None:
        """A description of why you have insufficient permissions."""
        return self.response.get("ErrorCode")


class ConflictException(BackupGatewayError):
    """The operation cannot proceed because it is not supported."""
    _ERROR_CODE = "ConflictException"

    @property
    def error_code(self) -> str | None:
        """A description of why the operation is not supported."""
        return self.response.get("ErrorCode")


class InternalServerException(BackupGatewayError):
    """The operation did not succeed because an internal error occurred. Try again later."""
    _ERROR_CODE = "InternalServerException"

    @property
    def error_code(self) -> str | None:
        """A description of which internal error occured."""
        return self.response.get("ErrorCode")


class ResourceNotFoundException(BackupGatewayError):
    """A resource that is required for the action wasn't found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def error_code(self) -> str | None:
        """A description of which resource wasn't found."""
        return self.response.get("ErrorCode")


class ThrottlingException(BackupGatewayError):
    """TPS has been limited to protect against intentional or unintentional high request
    volumes.
    """

    _ERROR_CODE = "ThrottlingException"

    @property
    def error_code(self) -> str | None:
        """Error: TPS has been limited to protect against intentional or unintentional high
        request volumes.
        """
        return self.response.get("ErrorCode")


class ValidationException(BackupGatewayError):
    """The operation did not succeed because a validation error occurred."""
    _ERROR_CODE = "ValidationException"

    @property
    def error_code(self) -> str | None:
        """A description of what caused the validation error."""
        return self.response.get("ErrorCode")


EXCEPTIONS: dict[str, type[BackupGatewayError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
