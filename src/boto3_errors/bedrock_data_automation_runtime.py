# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class BedrockDataAutomationRuntimeError(Boto3Error):
    _SERVICE = "bedrock-data-automation-runtime"


class AccessDeniedException(BedrockDataAutomationRuntimeError):
    """This exception will be thrown when customer does not have access to API."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(BedrockDataAutomationRuntimeError):
    """This exception is for any internal un-expected service errors."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(BedrockDataAutomationRuntimeError):
    """This exception will be thrown when resource provided from customer not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(BedrockDataAutomationRuntimeError):
    """This exception will be thrown when service quota is exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ServiceUnavailableException(BedrockDataAutomationRuntimeError):
    """This exception will be thrown when service is temporarily unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(BedrockDataAutomationRuntimeError):
    """This exception will be thrown when customer reached API TPS limit."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(BedrockDataAutomationRuntimeError):
    """This exception will be thrown when customer provided invalid parameters."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[BedrockDataAutomationRuntimeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
