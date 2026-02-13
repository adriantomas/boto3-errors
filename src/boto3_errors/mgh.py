# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MigrationHubError(Boto3Error):
    _SERVICE = "mgh"


class AccessDeniedException(MigrationHubError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class DryRunOperation(MigrationHubError):
    """Exception raised to indicate a successfully authorized action when the `DryRun` flag
    is set to "true".
    """

    _ERROR_CODE = "DryRunOperation"


class HomeRegionNotSetException(MigrationHubError):
    """The home region is not set. Set the home region to continue."""
    _ERROR_CODE = "HomeRegionNotSetException"


class InternalServerError(MigrationHubError):
    """Exception raised when an internal, configuration, or dependency error is
    encountered.
    """

    _ERROR_CODE = "InternalServerError"


class InvalidInputException(MigrationHubError):
    """Exception raised when the provided input violates a policy constraint or is entered
    in the wrong format or data type.
    """

    _ERROR_CODE = "InvalidInputException"


class PolicyErrorException(MigrationHubError):
    """Exception raised when there are problems accessing Application Discovery Service
    (Application Discovery Service); most likely due to a misconfigured policy or the
    `migrationhub-discovery` role is missing or not configured correctly.
    """

    _ERROR_CODE = "PolicyErrorException"


class ResourceNotFoundException(MigrationHubError):
    """Exception raised when the request references a resource (Application Discovery
    Service configuration, update stream, migration task, etc.) that does not exist in
    Application Discovery Service (Application Discovery Service) or in Migration Hub's
    repository.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(MigrationHubError):
    """Exception raised when there is an internal, configuration, or dependency error
    encountered.
    """

    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(MigrationHubError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds the caller should wait before retrying."""
        return self.response.get("RetryAfterSeconds")


class UnauthorizedOperation(MigrationHubError):
    """Exception raised to indicate a request was not authorized when the `DryRun` flag is
    set to "true".
    """

    _ERROR_CODE = "UnauthorizedOperation"


EXCEPTIONS: dict[str, type[MigrationHubError]] = {
    "AccessDeniedException": AccessDeniedException,
    "DryRunOperation": DryRunOperation,
    "HomeRegionNotSetException": HomeRegionNotSetException,
    "InternalServerError": InternalServerError,
    "InvalidInputException": InvalidInputException,
    "PolicyErrorException": PolicyErrorException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "UnauthorizedOperation": UnauthorizedOperation,
}
