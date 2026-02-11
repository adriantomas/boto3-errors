# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class finspaceError(Boto3Error):
    _SERVICE = "finspace"


class AccessDeniedException(finspaceError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(finspaceError):
    """There was a conflict with this action, and it could not be completed."""
    _ERROR_CODE = "ConflictException"

    @property
    def reason(self) -> str | None:
        """The reason for the conflict exception."""
        return self.response.get("reason")


class InternalServerException(finspaceError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"


class InvalidRequestException(finspaceError):
    """The request is invalid. Something is wrong with the input to the request."""
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(finspaceError):
    """A service limit or quota is exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(finspaceError):
    """The specified resource group already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(finspaceError):
    """One or more resources can't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(finspaceError):
    """You have exceeded your service quota. To perform the requested action, remove some
    of the relevant resources, or use Service Quotas to request a service quota
    increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(finspaceError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(finspaceError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[finspaceError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
