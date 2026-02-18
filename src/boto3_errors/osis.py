# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class OSISError(Boto3Error):
    _SERVICE = "osis"


class AccessDeniedException(OSISError):
    """You don't have permissions to access the resource."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(OSISError):
    """The client attempted to remove a resource that is currently in use."""
    _ERROR_CODE = "ConflictException"


class InternalException(OSISError):
    """The request failed because of an unknown error, exception, or failure (the failure
    is internal to the service).
    """

    _ERROR_CODE = "InternalException"


class InvalidPaginationTokenException(OSISError):
    """An invalid pagination token provided in the request."""
    _ERROR_CODE = "InvalidPaginationTokenException"


class LimitExceededException(OSISError):
    """You attempted to create more than the allowed number of tags."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(OSISError):
    """You attempted to create a resource that already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(OSISError):
    """You attempted to access or delete a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(OSISError):
    """An exception for missing or invalid input fields."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[OSISError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalException": InternalException,
    "InvalidPaginationTokenException": InvalidPaginationTokenException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
