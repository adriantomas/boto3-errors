# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class fisError(Boto3Error):
    _SERVICE = "fis"


class ConflictException(fisError):
    """The request could not be processed because of a conflict."""
    _ERROR_CODE = "ConflictException"


class ResourceNotFoundException(fisError):
    """The specified resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(fisError):
    """You have exceeded your service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(fisError):
    """The specified input is not valid, or fails to satisfy the constraints for the
    request.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[fisError]] = {
    "ConflictException": ConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
