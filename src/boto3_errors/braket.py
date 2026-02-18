# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class BraketError(Boto3Error):
    _SERVICE = "braket"


class AccessDeniedException(BraketError):
    """You do not have sufficient access to perform this action."""
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
    """The request processing has failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServiceException"


class ResourceNotFoundException(BraketError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BraketError):
    """The request failed because a service quota is exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(BraketError):
    """The throttling rate limit is met."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BraketError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


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
