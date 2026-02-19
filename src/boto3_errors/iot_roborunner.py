# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTRoboRunnerError(Boto3Error):
    _SERVICE = "iot-roborunner"


class AccessDeniedException(IoTRoboRunnerError):
    """User does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(IoTRoboRunnerError):
    """Exception thrown if a resource in a create request already exists."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(IoTRoboRunnerError):
    """Exception thrown if something goes wrong within the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(IoTRoboRunnerError):
    """Exception thrown if a resource referenced in the request doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(IoTRoboRunnerError):
    """Exception thrown if the user's AWS account has reached a service limit and the
    operation cannot proceed.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(IoTRoboRunnerError):
    """Exception thrown if the api has been called too quickly be the client."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(IoTRoboRunnerError):
    """Exception thrown if an invalid parameter is provided to an API."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IoTRoboRunnerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
