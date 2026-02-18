# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CleanRoomsMLError(Boto3Error):
    _SERVICE = "cleanroomsml"


class AccessDeniedException(CleanRoomsMLError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(CleanRoomsMLError):
    """A resource with that name already exists in this region."""
    _ERROR_CODE = "ConflictException"


class ResourceNotFoundException(CleanRoomsMLError):
    """The resource you are requesting does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(CleanRoomsMLError):
    """You have exceeded your service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ValidationException(CleanRoomsMLError):
    """The request parameters for this request are incorrect."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CleanRoomsMLError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ValidationException": ValidationException,
}
