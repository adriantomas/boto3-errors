# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MediaConvertError(Boto3Error):
    _SERVICE = "mediaconvert"


class BadRequestException(MediaConvertError):
    """The service can't process your request because of a problem in the request. Please
    check your request form and syntax.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(MediaConvertError):
    """The service couldn't complete your request because there is a conflict with the
    current state of the resource.
    """

    _ERROR_CODE = "ConflictException"


class ForbiddenException(MediaConvertError):
    """You don't have permissions for this action with the credentials you sent."""
    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(MediaConvertError):
    """The service encountered an unexpected condition and can't fulfill your request."""
    _ERROR_CODE = "InternalServerErrorException"


class NotFoundException(MediaConvertError):
    """The resource you requested doesn't exist."""
    _ERROR_CODE = "NotFoundException"


class ServiceQuotaExceededException(MediaConvertError):
    """You attempted to create more resources than the service allows based on service
    quotas.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class TooManyRequestsException(MediaConvertError):
    """Too many requests have been sent in too short of a time. The service limits the rate
    at which it will accept requests.
    """

    _ERROR_CODE = "TooManyRequestsException"


EXCEPTIONS: dict[str, type[MediaConvertError]] = {
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "TooManyRequestsException": TooManyRequestsException,
}
