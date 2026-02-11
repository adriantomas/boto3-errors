# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class Macie2Error(Boto3Error):
    _SERVICE = "macie2"


class AccessDeniedException(Macie2Error):
    """Provides information about an error that occurred due to insufficient access to a
    specified resource.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(Macie2Error):
    """Provides information about an error that occurred due to a versioning conflict for a
    specified resource.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(Macie2Error):
    """Provides information about an error that occurred due to an unknown internal server
    error, exception, or failure.
    """

    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(Macie2Error):
    """Provides information about an error that occurred because a specified resource
    wasn't found.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(Macie2Error):
    """Provides information about an error that occurred due to one or more service quotas
    for an account.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(Macie2Error):
    """Provides information about an error that occurred because too many requests were
    sent during a certain amount of time.
    """

    _ERROR_CODE = "ThrottlingException"


class UnprocessableEntityException(Macie2Error):
    """Provides information about an error that occurred due to an unprocessable entity."""
    _ERROR_CODE = "UnprocessableEntityException"


class ValidationException(Macie2Error):
    """Provides information about an error that occurred due to a syntax error in a
    request.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[Macie2Error]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UnprocessableEntityException": UnprocessableEntityException,
    "ValidationException": ValidationException,
}
