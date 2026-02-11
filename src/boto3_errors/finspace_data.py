# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class finspacedataError(Boto3Error):
    _SERVICE = "finspace-data"


class AccessDeniedException(finspacedataError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(finspacedataError):
    """The request conflicts with an existing resource."""
    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


class InternalServerException(finspacedataError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class LimitExceededException(finspacedataError):
    """A limit has exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(finspacedataError):
    """One or more resources can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


class ThrottlingException(finspacedataError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(finspacedataError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[finspacedataError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
