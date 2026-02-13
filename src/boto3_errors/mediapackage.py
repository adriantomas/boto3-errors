# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class MediaPackageError(Boto3Error):
    _SERVICE = "mediapackage"


class ForbiddenException(MediaPackageError):
    """The client is not authorized to access the requested resource."""
    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(MediaPackageError):
    """An unexpected error occurred."""
    _ERROR_CODE = "InternalServerErrorException"


class NotFoundException(MediaPackageError):
    """The requested resource does not exist."""
    _ERROR_CODE = "NotFoundException"


class ServiceUnavailableException(MediaPackageError):
    """An unexpected error occurred."""
    _ERROR_CODE = "ServiceUnavailableException"


class TooManyRequestsException(MediaPackageError):
    """The client has exceeded their resource or throttling limits."""
    _ERROR_CODE = "TooManyRequestsException"


class UnprocessableEntityException(MediaPackageError):
    """The parameters sent in the request are not valid."""
    _ERROR_CODE = "UnprocessableEntityException"


EXCEPTIONS: dict[str, type[MediaPackageError]] = {
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "NotFoundException": NotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnprocessableEntityException": UnprocessableEntityException,
}
