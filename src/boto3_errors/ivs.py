# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ivsError(Boto3Error):
    _SERVICE = "ivs"


class AccessDeniedException(ivsError):
    _ERROR_CODE = "AccessDeniedException"

    @property
    def exception_message(self) -> str | None:
        """User does not have sufficient access to perform this action."""
        return self.response.get("exceptionMessage")


class ChannelNotBroadcasting(ivsError):
    _ERROR_CODE = "ChannelNotBroadcasting"

    @property
    def exception_message(self) -> str | None:
        """The stream is offline for the given channel ARN."""
        return self.response.get("exceptionMessage")


class ConflictException(ivsError):
    _ERROR_CODE = "ConflictException"

    @property
    def exception_message(self) -> str | None:
        """Updating or deleting a resource can cause an inconsistent state."""
        return self.response.get("exceptionMessage")


class InternalServerException(ivsError):
    _ERROR_CODE = "InternalServerException"

    @property
    def exception_message(self) -> str | None:
        """Unexpected error during processing of request."""
        return self.response.get("exceptionMessage")


class PendingVerification(ivsError):
    _ERROR_CODE = "PendingVerification"

    @property
    def exception_message(self) -> str | None:
        """Your account is pending verification."""
        return self.response.get("exceptionMessage")


class ResourceNotFoundException(ivsError):
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def exception_message(self) -> str | None:
        """Request references a resource which does not exist."""
        return self.response.get("exceptionMessage")


class ServiceQuotaExceededException(ivsError):
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def exception_message(self) -> str | None:
        """Request would cause a service quota to be exceeded."""
        return self.response.get("exceptionMessage")


class StreamUnavailable(ivsError):
    _ERROR_CODE = "StreamUnavailable"

    @property
    def exception_message(self) -> str | None:
        """The stream is temporarily unavailable."""
        return self.response.get("exceptionMessage")


class ThrottlingException(ivsError):
    _ERROR_CODE = "ThrottlingException"

    @property
    def exception_message(self) -> str | None:
        """Request was denied due to request throttling."""
        return self.response.get("exceptionMessage")


class ValidationException(ivsError):
    _ERROR_CODE = "ValidationException"

    @property
    def exception_message(self) -> str | None:
        """The input fails to satisfy the constraints specified by an Amazon Web Services
        service.
        """
        return self.response.get("exceptionMessage")


EXCEPTIONS: dict[str, type[ivsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ChannelNotBroadcasting": ChannelNotBroadcasting,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "PendingVerification": PendingVerification,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "StreamUnavailable": StreamUnavailable,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
