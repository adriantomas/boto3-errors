# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ApplicationDiscoveryServiceError(Boto3Error):
    _SERVICE = "discovery"


class AuthorizationErrorException(ApplicationDiscoveryServiceError):
    """The user does not have permission to perform the action. Check the IAM policy
    associated with this user.
    """

    _ERROR_CODE = "AuthorizationErrorException"


class ConflictErrorException(ApplicationDiscoveryServiceError):
    """Conflict error."""
    _ERROR_CODE = "ConflictErrorException"


class HomeRegionNotSetException(ApplicationDiscoveryServiceError):
    """The home Region is not set. Set the home Region to continue."""
    _ERROR_CODE = "HomeRegionNotSetException"


class InvalidParameterException(ApplicationDiscoveryServiceError):
    """One or more parameters are not valid. Verify the parameters and try again."""
    _ERROR_CODE = "InvalidParameterException"


class InvalidParameterValueException(ApplicationDiscoveryServiceError):
    """The value of one or more parameters are either invalid or out of range. Verify the
    parameter values and try again.
    """

    _ERROR_CODE = "InvalidParameterValueException"


class LimitExceededException(ApplicationDiscoveryServiceError):
    """The limit of 200 configuration IDs per request has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class OperationNotPermittedException(ApplicationDiscoveryServiceError):
    """This operation is not permitted."""
    _ERROR_CODE = "OperationNotPermittedException"


class ResourceInUseException(ApplicationDiscoveryServiceError):
    """This issue occurs when the same `clientRequestToken` is used with the
    `StartImportTask` action, but with different parameters. For example, you use the
    same request token but have two different import URLs, you can encounter this issue.
    If the import tasks are meant to be different, use a different `clientRequestToken`,
    and try again.
    """

    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(ApplicationDiscoveryServiceError):
    """The specified configuration ID was not located. Verify the configuration ID and try
    again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServerInternalErrorException(ApplicationDiscoveryServiceError):
    """The server experienced an internal error. Try again."""
    _ERROR_CODE = "ServerInternalErrorException"


EXCEPTIONS: dict[str, type[ApplicationDiscoveryServiceError]] = {
    "AuthorizationErrorException": AuthorizationErrorException,
    "ConflictErrorException": ConflictErrorException,
    "HomeRegionNotSetException": HomeRegionNotSetException,
    "InvalidParameterException": InvalidParameterException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "LimitExceededException": LimitExceededException,
    "OperationNotPermittedException": OperationNotPermittedException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServerInternalErrorException": ServerInternalErrorException,
}
