# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class SSMQuickSetupError(Boto3Error):
    _SERVICE = "ssm-quicksetup"


class AccessDeniedException(SSMQuickSetupError):
    """The requester has insufficient permissions to perform the operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(SSMQuickSetupError):
    """Another request is being processed. Wait a few minutes and try again."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(SSMQuickSetupError):
    """An error occurred on the server side."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SSMQuickSetupError):
    """The resource couldn't be found. Check the ID or name and try again."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(SSMQuickSetupError):
    """The request or operation exceeds the maximum allowed request rate per Amazon Web
    Services account and Amazon Web Services Region.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(SSMQuickSetupError):
    """The request is invalid. Verify the values provided for the request parameters are
    accurate.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SSMQuickSetupError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
