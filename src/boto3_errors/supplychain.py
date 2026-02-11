# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SupplyChainError(Boto3Error):
    _SERVICE = "supplychain"


class AccessDeniedException(SupplyChainError):
    """You do not have the required privileges to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SupplyChainError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(SupplyChainError):
    """Unexpected error during processing of request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SupplyChainError):
    """Request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SupplyChainError):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(SupplyChainError):
    """Request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(SupplyChainError):
    """The input does not satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SupplyChainError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
