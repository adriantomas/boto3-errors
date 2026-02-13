# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BraketError(Boto3Error):
    _SERVICE = "braket"


class AccessDeniedException(BraketError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(BraketError):
    """An error occurred due to a conflict."""
    _ERROR_CODE = "ConflictException"


class DeviceOfflineException(BraketError):
    """The specified device is currently offline."""
    _ERROR_CODE = "DeviceOfflineException"


class DeviceRetiredException(BraketError):
    """The specified device has been retired."""
    _ERROR_CODE = "DeviceRetiredException"


class InternalServiceException(BraketError):
    """The request failed because of an unknown error."""
    _ERROR_CODE = "InternalServiceException"


class ResourceNotFoundException(BraketError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BraketError):
    """The request failed because a service quota is exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BraketError):
    """The API throttling rate limit is exceeded."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BraketError):
    """The input request failed to satisfy constraints expected by Amazon Braket."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for validation failure."""
        return self.response.get("reason")

    @property
    def program_set_validation_failures(self) -> list[Any] | None:
        """The validation failures in the program set submitted in the request."""
        return self.response.get("programSetValidationFailures")


EXCEPTIONS: dict[str, type[BraketError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DeviceOfflineException": DeviceOfflineException,
    "DeviceRetiredException": DeviceRetiredException,
    "InternalServiceException": InternalServiceException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
