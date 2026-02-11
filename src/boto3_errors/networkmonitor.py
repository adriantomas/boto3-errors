# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class NetworkMonitorError(Boto3Error):
    _SERVICE = "networkmonitor"


class AccessDeniedException(NetworkMonitorError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(NetworkMonitorError):
    """This operation attempted to create a resource that already exists."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(NetworkMonitorError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(NetworkMonitorError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(NetworkMonitorError):
    """This request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(NetworkMonitorError):
    """The request was denied due to request throttling"""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(NetworkMonitorError):
    """One of the parameters for the request is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[NetworkMonitorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
