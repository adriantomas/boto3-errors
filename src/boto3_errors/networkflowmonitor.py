# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class NetworkFlowMonitorError(Boto3Error):
    _SERVICE = "networkflowmonitor"


class AccessDeniedException(NetworkFlowMonitorError):
    """You don't have sufficient permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(NetworkFlowMonitorError):
    """The requested resource is in use."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(NetworkFlowMonitorError):
    """An internal error occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(NetworkFlowMonitorError):
    """The request specifies a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(NetworkFlowMonitorError):
    """The request exceeded a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(NetworkFlowMonitorError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(NetworkFlowMonitorError):
    """Invalid request."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[NetworkFlowMonitorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
