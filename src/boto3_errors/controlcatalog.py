# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ControlCatalogError(Boto3Error):
    _SERVICE = "controlcatalog"


class AccessDeniedException(ControlCatalogError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(ControlCatalogError):
    """An internal service error occurred during the processing of your request. Try again
    later.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ControlCatalogError):
    """The requested resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(ControlCatalogError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ControlCatalogError):
    """The request has invalid or missing parameters."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ControlCatalogError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
