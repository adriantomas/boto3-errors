# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AppIntegrationsError(Boto3Error):
    _SERVICE = "appintegrations"


class AccessDeniedException(AppIntegrationsError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class DuplicateResourceException(AppIntegrationsError):
    """A resource with the specified name already exists."""
    _ERROR_CODE = "DuplicateResourceException"


class InternalServiceError(AppIntegrationsError):
    """Request processing failed due to an error or failure with the service."""
    _ERROR_CODE = "InternalServiceError"


class InvalidRequestException(AppIntegrationsError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"


class ResourceNotFoundException(AppIntegrationsError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ResourceQuotaExceededException(AppIntegrationsError):
    """The allowed quota for the resource has been exceeded."""
    _ERROR_CODE = "ResourceQuotaExceededException"


class ThrottlingException(AppIntegrationsError):
    """The throttling limit has been exceeded."""
    _ERROR_CODE = "ThrottlingException"


class UnsupportedOperationException(AppIntegrationsError):
    """The operation is not supported."""
    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[AppIntegrationsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "DuplicateResourceException": DuplicateResourceException,
    "InternalServiceError": InternalServiceError,
    "InvalidRequestException": InvalidRequestException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ResourceQuotaExceededException": ResourceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
