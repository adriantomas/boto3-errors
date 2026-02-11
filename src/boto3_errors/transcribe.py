# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class TranscribeError(Boto3Error):
    _SERVICE = "transcribe"


class BadRequestException(TranscribeError):
    """Your request didn't pass one or more validation tests. This can occur when the
    entity you're trying to delete doesn't exist or if it's in a non-terminal state
    (such as `IN PROGRESS`). See the exception message field for more information.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(TranscribeError):
    """A resource already exists with this name. Resource names must be unique within an
    Amazon Web Services account.
    """

    _ERROR_CODE = "ConflictException"


class InternalFailureException(TranscribeError):
    """There was an internal error. Check the error message, correct the issue, and try
    your request again.
    """

    _ERROR_CODE = "InternalFailureException"


class LimitExceededException(TranscribeError):
    """You've either sent too many requests or your input file is too long. Wait before
    retrying your request, or use a smaller file and try your request again.
    """

    _ERROR_CODE = "LimitExceededException"


class NotFoundException(TranscribeError):
    """We can't find the requested resource. Check that the specified name is correct and
    try your request again.
    """

    _ERROR_CODE = "NotFoundException"


EXCEPTIONS: dict[str, type[TranscribeError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalFailureException": InternalFailureException,
    "LimitExceededException": LimitExceededException,
    "NotFoundException": NotFoundException,
}
