# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IotDeviceAdvisorError(Boto3Error):
    _SERVICE = "iotdeviceadvisor"


class ConflictException(IotDeviceAdvisorError):
    """Sends a Conflict Exception."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(IotDeviceAdvisorError):
    """Sends an Internal Failure exception."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(IotDeviceAdvisorError):
    """Sends a Resource Not Found exception."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(IotDeviceAdvisorError):
    """Sends a validation exception."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IotDeviceAdvisorError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
