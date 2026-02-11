# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class EntityResolutionError(Boto3Error):
    _SERVICE = "entityresolution"


class AccessDeniedException(EntityResolutionError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(EntityResolutionError):
    """The request couldn't be processed because of conflict in the current state of the
    resource. Example: Workflow already exists, Schema already exists, Workflow is
    currently running, etc.
    """

    _ERROR_CODE = "ConflictException"


class ExceedsLimitException(EntityResolutionError):
    """The request was rejected because it attempted to create resources beyond the current
    Entity Resolution account limits. The error message describes the limit exceeded.
    """

    _ERROR_CODE = "ExceedsLimitException"

    @property
    def quota_name(self) -> str | None:
        """The name of the quota that has been breached."""
        return self.response.get("quotaName")

    @property
    def quota_value(self) -> int | None:
        """The current quota value for the customers."""
        return self.response.get("quotaValue")


class InternalServerException(EntityResolutionError):
    """This exception occurs when there is an internal failure in the Entity Resolution
    service.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(EntityResolutionError):
    """The resource couldn't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(EntityResolutionError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(EntityResolutionError):
    """The input fails to satisfy the constraints specified by Entity Resolution."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[EntityResolutionError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ExceedsLimitException": ExceedsLimitException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
