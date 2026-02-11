# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SnowDeviceManagementError(Boto3Error):
    _SERVICE = "snow-device-management"


class AccessDeniedException(SnowDeviceManagementError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(SnowDeviceManagementError):
    """An unexpected error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SnowDeviceManagementError):
    """The request references a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SnowDeviceManagementError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(SnowDeviceManagementError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(SnowDeviceManagementError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SnowDeviceManagementError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
