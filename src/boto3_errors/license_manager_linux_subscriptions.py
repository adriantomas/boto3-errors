# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class LicenseManagerLinuxSubscriptionsError(Boto3Error):
    _SERVICE = "license-manager-linux-subscriptions"


class InternalServerException(LicenseManagerLinuxSubscriptionsError):
    """An exception occurred with the service."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(LicenseManagerLinuxSubscriptionsError):
    """Unable to find the requested Amazon Web Services resource."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(LicenseManagerLinuxSubscriptionsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(LicenseManagerLinuxSubscriptionsError):
    """The provided input is not valid. Try your request again."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[LicenseManagerLinuxSubscriptionsError]] = {
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
