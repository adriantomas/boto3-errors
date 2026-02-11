# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MigrationHubOrchestratorError(Boto3Error):
    _SERVICE = "migrationhuborchestrator"


class AccessDeniedException(MigrationHubOrchestratorError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MigrationHubOrchestratorError):
    """This exception is thrown when an attempt to update or delete a resource would cause
    an inconsistent state.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(MigrationHubOrchestratorError):
    """An internal error has occurred."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MigrationHubOrchestratorError):
    """The resource is not available."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(MigrationHubOrchestratorError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(MigrationHubOrchestratorError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MigrationHubOrchestratorError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
