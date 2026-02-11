# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SocialMessagingError(Boto3Error):
    _SERVICE = "socialmessaging"


class AccessDeniedByMetaException(SocialMessagingError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedByMetaException"


class AccessDeniedException(SocialMessagingError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class DependencyException(SocialMessagingError):
    """Thrown when performing an action because a dependency would be broken."""
    _ERROR_CODE = "DependencyException"


class InternalServiceException(SocialMessagingError):
    """The request processing has failed because of an unknown error, exception, or
    failure.
    """

    _ERROR_CODE = "InternalServiceException"


class InvalidParametersException(SocialMessagingError):
    """One or more parameters provided to the action are not valid."""
    _ERROR_CODE = "InvalidParametersException"


class LimitExceededException(SocialMessagingError):
    """The request was denied because it would exceed one or more service quotas or limits."""
    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(SocialMessagingError):
    """The resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottledRequestException(SocialMessagingError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottledRequestException"


class ValidationException(SocialMessagingError):
    """The request contains an invalid parameter value."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SocialMessagingError]] = {
    "AccessDeniedByMetaException": AccessDeniedByMetaException,
    "AccessDeniedException": AccessDeniedException,
    "DependencyException": DependencyException,
    "InternalServiceException": InternalServiceException,
    "InvalidParametersException": InvalidParametersException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottledRequestException": ThrottledRequestException,
    "ValidationException": ValidationException,
}
