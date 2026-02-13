# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MedicalImagingError(Boto3Error):
    _SERVICE = "medical-imaging"


class AccessDeniedException(MedicalImagingError):
    """The user does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MedicalImagingError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(MedicalImagingError):
    """An unexpected error occurred during processing of the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MedicalImagingError):
    """The request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(MedicalImagingError):
    """The request caused a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(MedicalImagingError):
    """The request was denied due to throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(MedicalImagingError):
    """The input fails to satisfy the constraints set by the service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MedicalImagingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
