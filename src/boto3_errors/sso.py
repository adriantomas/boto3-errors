# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SSOError(Boto3Error):
    _SERVICE = "sso"


class InvalidRequestException(SSOError):
    """Indicates that a problem occurred with the input to the request. For example, a
    required parameter might be missing or out of range.
    """

    _ERROR_CODE = "InvalidRequestException"


class ResourceNotFoundException(SSOError):
    """The specified resource doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyRequestsException(SSOError):
    """Indicates that the request is being made too frequently and is more than what the
    server can handle.
    """

    _ERROR_CODE = "TooManyRequestsException"


class UnauthorizedException(SSOError):
    """Indicates that the request is not authorized. This can happen due to an invalid
    access token in the request.
    """

    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[SSOError]] = {
    "InvalidRequestException": InvalidRequestException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
