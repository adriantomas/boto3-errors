# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MigrationHubConfigError(Boto3Error):
    _SERVICE = "migrationhub-config"


class AccessDeniedException(MigrationHubConfigError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class DryRunOperation(MigrationHubConfigError):
    """Exception raised to indicate that authorization of an action was successful, when
    the `DryRun` flag is set to true.
    """

    _ERROR_CODE = "DryRunOperation"


class InternalServerError(MigrationHubConfigError):
    """Exception raised when an internal, configuration, or dependency error is
    encountered.
    """

    _ERROR_CODE = "InternalServerError"


class InvalidInputException(MigrationHubConfigError):
    """Exception raised when the provided input violates a policy constraint or is entered
    in the wrong format or data type.
    """

    _ERROR_CODE = "InvalidInputException"


class ServiceUnavailableException(MigrationHubConfigError):
    """Exception raised when a request fails due to temporary unavailability of the
    service.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(MigrationHubConfigError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds the caller should wait before retrying."""
        return self.response.get("RetryAfterSeconds")


EXCEPTIONS: dict[str, type[MigrationHubConfigError]] = {
    "AccessDeniedException": AccessDeniedException,
    "DryRunOperation": DryRunOperation,
    "InternalServerError": InternalServerError,
    "InvalidInputException": InvalidInputException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
