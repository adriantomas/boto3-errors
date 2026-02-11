# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class S3OutpostsError(Boto3Error):
    _SERVICE = "s3outposts"


class AccessDeniedException(S3OutpostsError):
    """Access was denied for this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(S3OutpostsError):
    """There was a conflict with this action, and it could not be completed."""
    _ERROR_CODE = "ConflictException"


class InternalServerException(S3OutpostsError):
    """There was an exception with the internal server."""
    _ERROR_CODE = "InternalServerException"


class OutpostOfflineException(S3OutpostsError):
    """The service link connection to your Outposts home Region is down. Check your
    connection and try again.
    """

    _ERROR_CODE = "OutpostOfflineException"


class ResourceNotFoundException(S3OutpostsError):
    """The requested resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(S3OutpostsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(S3OutpostsError):
    """There was an exception validating this data."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[S3OutpostsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "OutpostOfflineException": OutpostOfflineException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
