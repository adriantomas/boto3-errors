# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class Cloud9Error(Boto3Error):
    _SERVICE = "cloud9"


class BadRequestException(Cloud9Error):
    """The target request is invalid."""
    _ERROR_CODE = "BadRequestException"


class ConcurrentAccessException(Cloud9Error):
    """A concurrent access issue occurred."""
    _ERROR_CODE = "ConcurrentAccessException"


class ConflictException(Cloud9Error):
    """A conflict occurred."""
    _ERROR_CODE = "ConflictException"


class ForbiddenException(Cloud9Error):
    """An access permissions issue occurred."""
    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(Cloud9Error):
    """An internal server error occurred."""
    _ERROR_CODE = "InternalServerErrorException"


class LimitExceededException(Cloud9Error):
    """A service limit was exceeded."""
    _ERROR_CODE = "LimitExceededException"


class NotFoundException(Cloud9Error):
    """The target resource cannot be found."""
    _ERROR_CODE = "NotFoundException"


class TooManyRequestsException(Cloud9Error):
    """Too many service requests were made over the given time period."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[Cloud9Error]] = {
    "BadRequestException": BadRequestException,
    "ConcurrentAccessException": ConcurrentAccessException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
