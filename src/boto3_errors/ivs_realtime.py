# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IVSRealTimeError(Boto3Error):
    _SERVICE = "ivs-realtime"


class AccessDeniedException(IVSRealTimeError):
    _ERROR_CODE = "AccessDeniedException"

    @property
    def exception_message(self) -> str | None:
        """User does not have sufficient access to perform this action."""
        return self.response.get("exceptionMessage")


class ConflictException(IVSRealTimeError):
    _ERROR_CODE = "ConflictException"

    @property
    def exception_message(self) -> str | None:
        """Updating or deleting a resource can cause an inconsistent state."""
        return self.response.get("exceptionMessage")


class InternalServerException(IVSRealTimeError):
    _ERROR_CODE = "InternalServerException"

    @property
    def exception_message(self) -> str | None:
        """Unexpected error during processing of request."""
        return self.response.get("exceptionMessage")


class PendingVerification(IVSRealTimeError):
    _ERROR_CODE = "PendingVerification"

    @property
    def exception_message(self) -> str | None:
        """Your account is pending verification."""
        return self.response.get("exceptionMessage")


class ResourceNotFoundException(IVSRealTimeError):
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def exception_message(self) -> str | None:
        """Request references a resource which does not exist."""
        return self.response.get("exceptionMessage")


class ServiceQuotaExceededException(IVSRealTimeError):
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def exception_message(self) -> str | None:
        """Request would cause a service quota to be exceeded."""
        return self.response.get("exceptionMessage")


class ValidationException(IVSRealTimeError):
    _ERROR_CODE = "ValidationException"

    @property
    def exception_message(self) -> str | None:
        """The input fails to satisfy the constraints specified by an Amazon Web Services
        service.
        """
        return self.response.get("exceptionMessage")


EXCEPTIONS: dict[str, type[IVSRealTimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "PendingVerification": PendingVerification,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
