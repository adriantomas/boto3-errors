# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class HealthLakeError(Boto3Error):
    _SERVICE = "healthlake"


class AccessDeniedException(HealthLakeError):
    """Access is denied. Your account is not authorized to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(HealthLakeError):
    """The data store is in a transition state and the user requested action cannot be
    performed.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(HealthLakeError):
    """An unknown internal error occurred in the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(HealthLakeError):
    """The requested data store was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(HealthLakeError):
    """The user has exceeded their maximum number of allowed calls to the given API."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(HealthLakeError):
    """The user input parameter was invalid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[HealthLakeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
