# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DataZoneError(Boto3Error):
    _SERVICE = "datazone"


class AccessDeniedException(DataZoneError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(DataZoneError):
    """There is a conflict while performing this action."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(DataZoneError):
    """The request has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(DataZoneError):
    """The specified resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(DataZoneError):
    """The request has exceeded the specified service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(DataZoneError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class UnauthorizedException(DataZoneError):
    """You do not have permission to perform this action."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(DataZoneError):
    """The input fails to satisfy the constraints specified by the Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[DataZoneError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
