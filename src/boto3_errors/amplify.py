# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AmplifyError(Boto3Error):
    _SERVICE = "amplify"


class BadRequestException(AmplifyError):
    """A request contains unexpected data."""
    _ERROR_CODE = "BadRequestException"


class DependentServiceFailureException(AmplifyError):
    """An operation failed because a dependent service threw an exception."""
    _ERROR_CODE = "DependentServiceFailureException"


class InternalFailureException(AmplifyError):
    """The service failed to perform an operation due to an internal issue."""
    _ERROR_CODE = "InternalFailureException"


class LimitExceededException(AmplifyError):
    """A resource could not be created because service quotas were exceeded."""
    _ERROR_CODE = "LimitExceededException"


class NotFoundException(AmplifyError):
    """An entity was not found during an operation."""
    _ERROR_CODE = "NotFoundException"


class ResourceNotFoundException(AmplifyError):
    """An operation failed due to a non-existent resource."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class UnauthorizedException(AmplifyError):
    """An operation failed due to a lack of access."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[AmplifyError]] = {
    "BadRequestException": BadRequestException,
    "DependentServiceFailureException": DependentServiceFailureException,
    "InternalFailureException": InternalFailureException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "UnauthorizedException": UnauthorizedException,
}
