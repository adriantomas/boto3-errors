# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class MediaPackageVodError(Boto3Error):
    _SERVICE = "mediapackage-vod"


class ForbiddenException(MediaPackageVodError):
    """The client is not authorized to access the requested resource."""
    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(MediaPackageVodError):
    """An unexpected error occurred."""
    _ERROR_CODE = "InternalServerErrorException"


class NotFoundException(MediaPackageVodError):
    """The requested resource does not exist."""
    _ERROR_CODE = "NotFoundException"


class ServiceUnavailableException(MediaPackageVodError):
    """An unexpected error occurred."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(MediaPackageVodError):
    """The client has exceeded their resource or throttling limits."""
    _ERROR_CODE = "TooManyRequestsException"


class UnprocessableEntityException(MediaPackageVodError):
    """The parameters sent in the request are not valid."""
    _ERROR_CODE = "UnprocessableEntityException"


EXCEPTIONS: dict[str, type[MediaPackageVodError]] = {
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnprocessableEntityException": UnprocessableEntityException,
}
