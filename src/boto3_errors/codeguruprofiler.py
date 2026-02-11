# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CodeGuruProfilerError(Boto3Error):
    _SERVICE = "codeguruprofiler"


class ConflictException(CodeGuruProfilerError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(CodeGuruProfilerError):
    """The server encountered an internal error and is unable to complete the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(CodeGuruProfilerError):
    """The resource specified in the request does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(CodeGuruProfilerError):
    """You have exceeded your service quota. To perform the requested action, remove some
    of the relevant resources, or use Service Quotas to request a service quota
    increase.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(CodeGuruProfilerError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(CodeGuruProfilerError):
    """The parameter is not valid."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[CodeGuruProfilerError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
