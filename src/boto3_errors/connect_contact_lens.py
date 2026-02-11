# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ConnectContactLensError(Boto3Error):
    _SERVICE = "connect-contact-lens"


class AccessDeniedException(ConnectContactLensError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServiceException(ConnectContactLensError):
    """Request processing failed due to an error or failure with the service."""
    _ERROR_CODE = "InternalServiceException"


class InvalidRequestException(ConnectContactLensError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"


class ResourceNotFoundException(ConnectContactLensError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(ConnectContactLensError):
    """The throttling limit has been exceeded."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[ConnectContactLensError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServiceException": InternalServiceException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
