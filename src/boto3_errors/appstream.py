# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class AppStreamError(Boto3Error):
    _SERVICE = "appstream"


class ConcurrentModificationException(AppStreamError):
    """An API error occurred. Wait a few minutes and try again."""
    _ERROR_CODE = "ConcurrentModificationException"


class DryRunOperationException(AppStreamError):
    """The exception that is thrown when a dry run operation is requested. This indicates
    that the validation checks have been performed successfully, but no actual resources
    were created or modified.
    """

    _ERROR_CODE = "DryRunOperationException"


class EntitlementAlreadyExistsException(AppStreamError):
    """The entitlement already exists."""
    _ERROR_CODE = "EntitlementAlreadyExistsException"


class EntitlementNotFoundException(AppStreamError):
    """The entitlement can't be found."""
    _ERROR_CODE = "EntitlementNotFoundException"


class IncompatibleImageException(AppStreamError):
    """The image can't be updated because it's not compatible for updates."""
    _ERROR_CODE = "IncompatibleImageException"


class InvalidAccountStatusException(AppStreamError):
    """The resource cannot be created because your AWS account is suspended. For
    assistance, contact AWS Support.
    """

    _ERROR_CODE = "InvalidAccountStatusException"


class InvalidParameterCombinationException(AppStreamError):
    """Indicates an incorrect combination of parameters, or a missing parameter."""
    _ERROR_CODE = "InvalidParameterCombinationException"


class InvalidRoleException(AppStreamError):
    """The specified role is invalid."""
    _ERROR_CODE = "InvalidRoleException"


class LimitExceededException(AppStreamError):
    """The requested limit exceeds the permitted limit for an account."""
    _ERROR_CODE = "LimitExceededException"


class OperationNotPermittedException(AppStreamError):
    """The attempted operation is not permitted."""
    _ERROR_CODE = "OperationNotPermittedException"


class RequestLimitExceededException(AppStreamError):
    """WorkSpaces Applications can’t process the request right now because the Describe
    calls from your AWS account are being throttled by Amazon EC2. Try again later.
    """

    _ERROR_CODE = "RequestLimitExceededException"


class ResourceAlreadyExistsException(AppStreamError):
    """The specified resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceInUseException(AppStreamError):
    """The specified resource is in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotAvailableException(AppStreamError):
    """The specified resource exists and is not in use, but isn't available."""
    _ERROR_CODE = "ResourceNotAvailableException"


class ResourceNotFoundException(AppStreamError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[AppStreamError]] = {
    "ConcurrentModificationException": ConcurrentModificationException,
    "DryRunOperationException": DryRunOperationException,
    "EntitlementAlreadyExistsException": EntitlementAlreadyExistsException,
    "EntitlementNotFoundException": EntitlementNotFoundException,
    "IncompatibleImageException": IncompatibleImageException,
    "InvalidAccountStatusException": InvalidAccountStatusException,
    "InvalidParameterCombinationException": InvalidParameterCombinationException,
    "InvalidRoleException": InvalidRoleException,
    "LimitExceededException": LimitExceededException,
    "OperationNotPermittedException": OperationNotPermittedException,
    "RequestLimitExceededException": RequestLimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotAvailableException": ResourceNotAvailableException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
