# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SSMGuiConnectError(Boto3Error):
    _SERVICE = "ssm-guiconnect"


class AccessDeniedException(SSMGuiConnectError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SSMGuiConnectError):
    """An error occurred due to a conflict."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(SSMGuiConnectError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SSMGuiConnectError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SSMGuiConnectError):
    """Your request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(SSMGuiConnectError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(SSMGuiConnectError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SSMGuiConnectError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
