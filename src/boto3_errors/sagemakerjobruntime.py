# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SagemakerJobRuntimeError(Boto3Error):
    _SERVICE = "sagemakerjobruntime"


class AccessDeniedException(SagemakerJobRuntimeError):
    """You do not have permission to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SagemakerJobRuntimeError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"


class InternalServiceError(SagemakerJobRuntimeError):
    """An internal service error occurred. Retry the request."""
    _ERROR_CODE = "InternalServiceError"


class ResourceNotFoundException(SagemakerJobRuntimeError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SagemakerJobRuntimeError):
    """You have exceeded a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(SagemakerJobRuntimeError):
    """The request was throttled. Retry the request after a brief wait."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(SagemakerJobRuntimeError):
    """The request is not valid. Check the request syntax and parameters"""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SagemakerJobRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServiceError": InternalServiceError,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
