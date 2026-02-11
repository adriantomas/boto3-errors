# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class S3TablesError(Boto3Error):
    _SERVICE = "s3tables"


class AccessDeniedException(S3TablesError):
    """The action cannot be performed because you do not have the required permission."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(S3TablesError):
    """The request is invalid or malformed."""
    _ERROR_CODE = "BadRequestException"


class ConflictException(S3TablesError):
    """The request failed because there is a conflict with a previous write. You can retry
    the request.
    """

    _ERROR_CODE = "ConflictException"


class ForbiddenException(S3TablesError):
    """The caller isn't authorized to make the request."""
    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(S3TablesError):
    """The request failed due to an internal server error."""
    _ERROR_CODE = "InternalServerErrorException"


class MethodNotAllowedException(S3TablesError):
    """The requested operation is not allowed on this resource. This may occur when
    attempting to modify a resource that is managed by a service or has restrictions
    that prevent the operation.
    """

    _ERROR_CODE = "MethodNotAllowedException"


class NotFoundException(S3TablesError):
    """The request was rejected because the specified resource could not be found."""
    _ERROR_CODE = "NotFoundException"


class TooManyRequestsException(S3TablesError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[S3TablesError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "MethodNotAllowedException": MethodNotAllowedException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
}
