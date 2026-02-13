# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DataBrewError(Boto3Error):
    _SERVICE = "databrew"


class AccessDeniedException(DataBrewError):
    """Access to the specified resource was denied."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(DataBrewError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(DataBrewError):
    """An internal service failure occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(DataBrewError):
    """One or more resources can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(DataBrewError):
    """A service quota is exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(DataBrewError):
    """The input parameters for this request failed validation."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[DataBrewError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
