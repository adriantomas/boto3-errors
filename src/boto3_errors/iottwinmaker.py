# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTTwinMakerError(Boto3Error):
    _SERVICE = "iottwinmaker"


class AccessDeniedException(IoTTwinMakerError):
    """Access is denied."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(IoTTwinMakerError):
    """A conflict occurred."""
    _ERROR_CODE = "ConflictException"


class ConnectorFailureException(IoTTwinMakerError):
    """The connector failed."""
    _ERROR_CODE = "ConnectorFailureException"


class ConnectorTimeoutException(IoTTwinMakerError):
    """The connector timed out."""
    _ERROR_CODE = "ConnectorTimeoutException"


class InternalServerException(IoTTwinMakerError):
    """An unexpected error has occurred."""
    _ERROR_CODE = "InternalServerException"


class QueryTimeoutException(IoTTwinMakerError):
    """The query timeout exception."""
    _ERROR_CODE = "QueryTimeoutException"


class ResourceNotFoundException(IoTTwinMakerError):
    """The resource wasn't found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(IoTTwinMakerError):
    """The service quota was exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(IoTTwinMakerError):
    """The rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(IoTTwinMakerError):
    """The number of tags exceeds the limit."""
    _ERROR_CODE = "TooManyTagsException"


class ValidationException(IoTTwinMakerError):
    """Failed"""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IoTTwinMakerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ConnectorFailureException": ConnectorFailureException,
    "ConnectorTimeoutException": ConnectorTimeoutException,
    "InternalServerException": InternalServerException,
    "QueryTimeoutException": QueryTimeoutException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
