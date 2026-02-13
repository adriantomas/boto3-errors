# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class InternetMonitorError(Boto3Error):
    _SERVICE = "internetmonitor"


class AccessDeniedException(InternetMonitorError):
    """You don't have sufficient permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(InternetMonitorError):
    """A bad request was received."""
    _ERROR_CODE = "BadRequestException"


class ConflictException(InternetMonitorError):
    """The requested resource is in use."""
    _ERROR_CODE = "ConflictException"


class InternalServerErrorException(InternetMonitorError):
    """There was an internal server error."""
    _ERROR_CODE = "InternalServerErrorException"


class InternalServerException(InternetMonitorError):
    """An internal error occurred."""
    _ERROR_CODE = "InternalServerException"


class LimitExceededException(InternetMonitorError):
    """The request exceeded a service quota."""
    _ERROR_CODE = "LimitExceededException"


class NotFoundException(InternetMonitorError):
    """The request specifies something that doesn't exist."""
    _ERROR_CODE = "NotFoundException"


class ResourceNotFoundException(InternetMonitorError):
    """The request specifies a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(InternetMonitorError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class TooManyRequestsException(InternetMonitorError):
    """There were too many requests."""
    _ERROR_CODE = "TooManyRequestsException"


class ValidationException(InternetMonitorError):
    """Invalid request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[InternetMonitorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServerErrorException": InternalServerErrorException,
    "InternalServerException": InternalServerException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "TooManyRequestsException": TooManyRequestsException,
    "ValidationException": ValidationException,
}
