# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MailManagerError(Boto3Error):
    _SERVICE = "mailmanager"


class AccessDeniedException(MailManagerError):
    """Occurs when a user is denied access to a specific resource or action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(MailManagerError):
    """The request configuration has conflicts. For details, see the accompanying error
    message.
    """

    _ERROR_CODE = "ConflictException"


class ResourceNotFoundException(MailManagerError):
    """Occurs when a requested resource is not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(MailManagerError):
    """Occurs when an operation exceeds a predefined service quota or limit."""
    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(MailManagerError):
    """Occurs when a service's request rate limit is exceeded, resulting in throttling of
    further requests.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(MailManagerError):
    """The request validation has failed. For details, see the accompanying error message."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[MailManagerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
