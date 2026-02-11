# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SchedulerError(Boto3Error):
    _SERVICE = "scheduler"


class ConflictException(SchedulerError):
    """Updating or deleting the resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(SchedulerError):
    """Unexpected error encountered while processing the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SchedulerError):
    """The request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SchedulerError):
    """The request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(SchedulerError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(SchedulerError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SchedulerError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
