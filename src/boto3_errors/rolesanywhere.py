# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class RolesAnywhereError(Boto3Error):
    _SERVICE = "rolesanywhere"


class AccessDeniedException(RolesAnywhereError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ResourceNotFoundException(RolesAnywhereError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyTagsException(RolesAnywhereError):
    """Too many tags."""
    _ERROR_CODE = "TooManyTagsException"


class ValidationException(RolesAnywhereError):
    """Validation exception error."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[RolesAnywhereError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
