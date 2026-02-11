# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class LicenseManagerError(Boto3Error):
    _SERVICE = "license-manager"


class AccessDeniedException(LicenseManagerError):
    """Access to resource denied."""
    _ERROR_CODE = "AccessDeniedException"


class AuthorizationException(LicenseManagerError):
    """The Amazon Web Services user account does not have permission to perform the action.
    Check the IAM policy associated with this account.
    """

    _ERROR_CODE = "AuthorizationException"


class ConflictException(LicenseManagerError):
    """There was a conflict processing the request. Try your request again."""
    _ERROR_CODE = "ConflictException"


class EntitlementNotAllowedException(LicenseManagerError):
    """The entitlement is not allowed."""
    _ERROR_CODE = "EntitlementNotAllowedException"


class FailedDependencyException(LicenseManagerError):
    """A dependency required to run the API is missing."""
    _ERROR_CODE = "FailedDependencyException"

    @property
    def error_code(self) -> str | None:
        return self.response.get("ErrorCode")


class FilterLimitExceededException(LicenseManagerError):
    """The request uses too many filters or too many filter values."""
    _ERROR_CODE = "FilterLimitExceededException"


class InvalidParameterValueException(LicenseManagerError):
    """One or more parameter values are not valid."""
    _ERROR_CODE = "InvalidParameterValueException"


class InvalidResourceStateException(LicenseManagerError):
    """License Manager cannot allocate a license to a resource because of its state.

    For example, you cannot allocate a license to an instance in the process of shutting
    down.
    """

    _ERROR_CODE = "InvalidResourceStateException"


class LicenseUsageException(LicenseManagerError):
    """You do not have enough licenses available to support a new resource launch."""
    _ERROR_CODE = "LicenseUsageException"


class NoEntitlementsAllowedException(LicenseManagerError):
    """There are no entitlements found for this license, or the entitlement maximum count
    is reached.
    """

    _ERROR_CODE = "NoEntitlementsAllowedException"


class RateLimitExceededException(LicenseManagerError):
    """Too many requests have been submitted. Try again after a brief wait."""
    _ERROR_CODE = "RateLimitExceededException"


class RedirectException(LicenseManagerError):
    """This is not the correct Region for the resource. Try again."""
    _ERROR_CODE = "RedirectException"

    @property
    def location(self) -> str | None:
        return self.response.get("Location")


class ResourceLimitExceededException(LicenseManagerError):
    """Your resource limits have been exceeded."""
    _ERROR_CODE = "ResourceLimitExceededException"


class ResourceNotFoundException(LicenseManagerError):
    """The resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServerInternalException(LicenseManagerError):
    """The server experienced an internal error. Try again."""
    _ERROR_CODE = "ServerInternalException"


class UnsupportedDigitalSignatureMethodException(LicenseManagerError):
    """The digital signature method is unsupported. Try your request again."""
    _ERROR_CODE = "UnsupportedDigitalSignatureMethodException"


class ValidationException(LicenseManagerError):
    """The provided input is not valid. Try your request again."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LicenseManagerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "AuthorizationException": AuthorizationException,
    "ConflictException": ConflictException,
    "EntitlementNotAllowedException": EntitlementNotAllowedException,
    "FailedDependencyException": FailedDependencyException,
    "FilterLimitExceededException": FilterLimitExceededException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "InvalidResourceStateException": InvalidResourceStateException,
    "LicenseUsageException": LicenseUsageException,
    "NoEntitlementsAllowedException": NoEntitlementsAllowedException,
    "RateLimitExceededException": RateLimitExceededException,
    "RedirectException": RedirectException,
    "ResourceLimitExceededException": ResourceLimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServerInternalException": ServerInternalException,
    "UnsupportedDigitalSignatureMethodException": UnsupportedDigitalSignatureMethodException,
    "ValidationException": ValidationException,
}
