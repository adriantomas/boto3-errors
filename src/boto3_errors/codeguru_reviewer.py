# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class CodeGuruReviewerError(Boto3Error):
    _SERVICE = "codeguru-reviewer"


class AccessDeniedException(CodeGuruReviewerError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(CodeGuruReviewerError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(CodeGuruReviewerError):
    """The server encountered an internal error and is unable to complete the request."""
    _ERROR_CODE = "InternalServerException"


class NotFoundException(CodeGuruReviewerError):
    """The resource specified in the request was not found."""
    _ERROR_CODE = "NotFoundException"


class ResourceNotFoundException(CodeGuruReviewerError):
    """The resource specified in the request was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(CodeGuruReviewerError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(CodeGuruReviewerError):
    """The input fails to satisfy the specified constraints."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CodeGuruReviewerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "NotFoundException": NotFoundException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
