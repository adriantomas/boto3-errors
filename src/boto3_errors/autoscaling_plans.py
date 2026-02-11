# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AutoScalingPlansError(Boto3Error):
    _SERVICE = "autoscaling-plans"


class ConcurrentUpdateException(AutoScalingPlansError):
    """Concurrent updates caused an exception, for example, if you request an update to a
    scaling plan that already has a pending update.
    """

    _ERROR_CODE = "ConcurrentUpdateException"


class InternalServiceException(AutoScalingPlansError):
    """The service encountered an internal error."""
    _ERROR_CODE = "InternalServiceException"


class InvalidNextTokenException(AutoScalingPlansError):
    """The token provided is not valid."""
    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(AutoScalingPlansError):
    """Your account exceeded a limit. This exception is thrown when a per-account resource
    limit is exceeded.
    """

    _ERROR_CODE = "LimitExceededException"


class ObjectNotFoundException(AutoScalingPlansError):
    """The specified object could not be found."""
    _ERROR_CODE = "ObjectNotFoundException"


class ValidationException(AutoScalingPlansError):
    """An exception was thrown for a validation issue. Review the parameters provided."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[AutoScalingPlansError]] = {
    "ConcurrentUpdateException": ConcurrentUpdateException,
    "InternalServiceException": InternalServiceException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "ObjectNotFoundException": ObjectNotFoundException,
    "ValidationException": ValidationException,
}
