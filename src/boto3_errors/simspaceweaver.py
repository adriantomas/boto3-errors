# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SimSpaceWeaverError(Boto3Error):
    _SERVICE = "simspaceweaver"


class AccessDeniedException(SimSpaceWeaverError):
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SimSpaceWeaverError):
    _ERROR_CODE = "ConflictException"


class InternalServerException(SimSpaceWeaverError):
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SimSpaceWeaverError):
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(SimSpaceWeaverError):
    _ERROR_CODE = "ServiceQuotaExceededException"


class TooManyTagsException(SimSpaceWeaverError):
    _ERROR_CODE = "TooManyTagsException"


class ValidationException(SimSpaceWeaverError):
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SimSpaceWeaverError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
