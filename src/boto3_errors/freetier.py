# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class FreeTierError(Boto3Error):
    _SERVICE = "freetier"


class AccessDeniedException(FreeTierError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(FreeTierError):
    """An unexpected error occurred during the processing of your request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(FreeTierError):
    """This exception is thrown when the requested resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(FreeTierError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(FreeTierError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[FreeTierError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
