# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class LexRuntimeV2Error(Boto3Error):
    _SERVICE = "lexv2-runtime"


class AccessDeniedException(LexRuntimeV2Error):
    _ERROR_CODE = "AccessDeniedException"


class BadGatewayException(LexRuntimeV2Error):
    _ERROR_CODE = "BadGatewayException"


class ConflictException(LexRuntimeV2Error):
    _ERROR_CODE = "ConflictException"


class DependencyFailedException(LexRuntimeV2Error):
    _ERROR_CODE = "DependencyFailedException"


class InternalServerException(LexRuntimeV2Error):
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LexRuntimeV2Error):
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(LexRuntimeV2Error):
    _ERROR_CODE = "ThrottlingException"


class ValidationException(LexRuntimeV2Error):
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LexRuntimeV2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadGatewayException": BadGatewayException,
    "ConflictException": ConflictException,
    "DependencyFailedException": DependencyFailedException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
