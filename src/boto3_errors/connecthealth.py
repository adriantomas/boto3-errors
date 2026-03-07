# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ConnectHealthError(Boto3Error):
    _SERVICE = "connecthealth"


class AccessDeniedException(ConnectHealthError):
    """This error is thrown when the client does not supply proper credentials to the API."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ConnectHealthError):
    """This error is thrown when a resource update is no longer valid due to assumptions
    about initial state changing.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(ConnectHealthError):
    """This error is thrown when a transient error causes our API to fail."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(ConnectHealthError):
    """This error is thrown when the requested resource is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(ConnectHealthError):
    """The request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(ConnectHealthError):
    """This error is thrown when the client exceeds the allowed request rate."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(ConnectHealthError):
    """This error is thrown when the client supplies invalid input to the API."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[ConnectHealthError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
