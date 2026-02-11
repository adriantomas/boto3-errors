# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CustomerProfilesError(Boto3Error):
    _SERVICE = "customer-profiles"


class AccessDeniedException(CustomerProfilesError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(CustomerProfilesError):
    """The input you provided is invalid."""
    _ERROR_CODE = "BadRequestException"


class InternalServerException(CustomerProfilesError):
    """An internal service error occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(CustomerProfilesError):
    """The requested resource does not exist, or access was denied."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(CustomerProfilesError):
    """You exceeded the maximum number of requests."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[CustomerProfilesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
