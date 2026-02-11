# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class OmicsError(Boto3Error):
    _SERVICE = "omics"


class AccessDeniedException(OmicsError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(OmicsError):
    """The request cannot be applied to the target resource in its current state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(OmicsError):
    """An unexpected error occurred. Try the request again."""
    _ERROR_CODE = "InternalServerException"


class NotSupportedOperationException(OmicsError):
    """The operation is not supported by Amazon Omics, or the API does not exist."""
    _ERROR_CODE = "NotSupportedOperationException"


class RangeNotSatisfiableException(OmicsError):
    """The ranges specified in the request are not valid."""
    _ERROR_CODE = "RangeNotSatisfiableException"


class RequestTimeoutException(OmicsError):
    """The request timed out."""
    _ERROR_CODE = "RequestTimeoutException"


class ResourceNotFoundException(OmicsError):
    """The target resource was not found in the current Region."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(OmicsError):
    """The request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(OmicsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(OmicsError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OmicsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "NotSupportedOperationException": NotSupportedOperationException,
    "RangeNotSatisfiableException": RangeNotSatisfiableException,
    "RequestTimeoutException": RequestTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
