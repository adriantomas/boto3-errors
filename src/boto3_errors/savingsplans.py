# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class savingsplansError(Boto3Error):
    _SERVICE = "savingsplans"


class InternalServerException(savingsplansError):
    """An unexpected error occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(savingsplansError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(savingsplansError):
    """A service quota has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(savingsplansError):
    """One of the input parameters is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[savingsplansError]] = {
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
