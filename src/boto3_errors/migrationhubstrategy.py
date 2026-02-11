# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MigrationHubStrategyError(Boto3Error):
    _SERVICE = "migrationhubstrategy"


class AccessDeniedException(MigrationHubStrategyError):
    """The user does not have permission to perform the action. Check the AWS Identity and
    Access Management (IAM) policy associated with this user.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MigrationHubStrategyError):
    """Exception to indicate that there is an ongoing task when a new task is created.
    Return when once the existing tasks are complete.
    """

    _ERROR_CODE = "ConflictException"


class DependencyException(MigrationHubStrategyError):
    """Dependency encountered an error."""
    _ERROR_CODE = "DependencyException"


class InternalServerException(MigrationHubStrategyError):
    """The server experienced an internal error. Try again."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(MigrationHubStrategyError):
    """The specified ID in the request is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceLinkedRoleLockClientException(MigrationHubStrategyError):
    """Exception to indicate that the service-linked role (SLR) is locked."""
    _ERROR_CODE = "ServiceLinkedRoleLockClientException"


class ServiceQuotaExceededException(MigrationHubStrategyError):
    """The AWS account has reached its quota of imports. Contact AWS Support to increase
    the quota for this account.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(MigrationHubStrategyError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(MigrationHubStrategyError):
    """The request body isn't valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MigrationHubStrategyError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DependencyException": DependencyException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceLinkedRoleLockClientException": ServiceLinkedRoleLockClientException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
