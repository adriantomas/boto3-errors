# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class codestarnotificationsError(Boto3Error):
    _SERVICE = "codestar-notifications"


class AccessDeniedException(codestarnotificationsError):
    """CodeStar Notifications can't create the notification rule because you do not have
    sufficient permissions.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConcurrentModificationException(codestarnotificationsError):
    """CodeStar Notifications can't complete the request because the resource is being
    modified by another process. Wait a few minutes and try again.
    """

    _ERROR_CODE = "ConcurrentModificationException"


class ConfigurationException(codestarnotificationsError):
    """Some or all of the configuration is incomplete, missing, or not valid."""
    _ERROR_CODE = "ConfigurationException"


class InvalidNextTokenException(codestarnotificationsError):
    """The value for the enumeration token used in the request to return the next batch of
    the results is not valid.
    """

    _ERROR_CODE = "InvalidNextTokenException"


class LimitExceededException(codestarnotificationsError):
    """One of the CodeStar Notifications limits has been exceeded. Limits apply to
    accounts, notification rules, notifications, resources, and targets. For more
    information, see Limits.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(codestarnotificationsError):
    """A resource with the same name or ID already exists. Notification rule names must be
    unique in your Amazon Web Services account.
    """

    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(codestarnotificationsError):
    """CodeStar Notifications can't find a resource that matches the provided ARN."""
    _ERROR_CODE = "ResourceNotFoundException"


class ValidationException(codestarnotificationsError):
    """One or more parameter values are not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[codestarnotificationsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConcurrentModificationException": ConcurrentModificationException,
    "ConfigurationException": ConfigurationException,
    "InvalidNextTokenException": InvalidNextTokenException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ValidationException": ValidationException,
}
