# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LicenseManagerUserSubscriptionsError(Boto3Error):
    _SERVICE = "license-manager-user-subscriptions"


class AccessDeniedException(LicenseManagerUserSubscriptionsError):
    """You don't have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(LicenseManagerUserSubscriptionsError):
    """The request couldn't be completed because it conflicted with the current state of
    the resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(LicenseManagerUserSubscriptionsError):
    """An exception occurred with the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LicenseManagerUserSubscriptionsError):
    """The resource couldn't be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(LicenseManagerUserSubscriptionsError):
    """The request failed because a service quota is exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(LicenseManagerUserSubscriptionsError):
    """The request was denied because of request throttling. Retry the request."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(LicenseManagerUserSubscriptionsError):
    """A parameter is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LicenseManagerUserSubscriptionsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
