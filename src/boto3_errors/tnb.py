# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class tnbError(Boto3Error):
    _SERVICE = "tnb"


class AccessDeniedException(tnbError):
    """Insufficient permissions to make request."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(tnbError):
    """Unexpected error occurred. Problem on the server."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(tnbError):
    """Request references a resource that doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(tnbError):
    """Service quotas have been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(tnbError):
    """Exception caused by throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(tnbError):
    """Unable to process the request because the client provided input failed to satisfy
    request constraints.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[tnbError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
