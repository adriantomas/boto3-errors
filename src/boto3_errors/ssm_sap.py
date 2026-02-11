# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SsmSapError(Boto3Error):
    _SERVICE = "ssm-sap"


class ConflictException(SsmSapError):
    """A conflict has occurred."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(SsmSapError):
    """An internal error has occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SsmSapError):
    """The resource is not available."""
    _ERROR_CODE = "ResourceNotFoundException"


class UnauthorizedException(SsmSapError):
    """The request is not authorized."""
    _ERROR_CODE = "UnauthorizedException"


class ValidationException(SsmSapError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SsmSapError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "UnauthorizedException": UnauthorizedException,
    "ValidationException": ValidationException,
}
