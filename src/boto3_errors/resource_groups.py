# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ResourceGroupsError(Boto3Error):
    _SERVICE = "resource-groups"


class BadRequestException(ResourceGroupsError):
    """The request includes one or more parameters that violate validation rules."""
    _ERROR_CODE = "BadRequestException"


class ForbiddenException(ResourceGroupsError):
    """The caller isn't authorized to make the request. Check permissions."""
    _ERROR_CODE = "ForbiddenException"


class InternalServerErrorException(ResourceGroupsError):
    """An internal error occurred while processing the request. Try again later."""
    _ERROR_CODE = "InternalServerErrorException"


class MethodNotAllowedException(ResourceGroupsError):
    """The request uses an HTTP method that isn't allowed for the specified resource."""
    _ERROR_CODE = "MethodNotAllowedException"


class NotFoundException(ResourceGroupsError):
    """One or more of the specified resources don't exist."""
    _ERROR_CODE = "NotFoundException"


class TooManyRequestsException(ResourceGroupsError):
    """You've exceeded throttling limits by making too many requests in a period of time."""
    _ERROR_CODE = "TooManyRequestsException"


class UnauthorizedException(ResourceGroupsError):
    """The request was rejected because it doesn't have valid credentials for the target
    resource.
    """

    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[ResourceGroupsError]] = {
    "BadRequestException": BadRequestException,
    "ForbiddenException": ForbiddenException,
    "InternalServerErrorException": InternalServerErrorException,
    "MethodNotAllowedException": MethodNotAllowedException,
    "NotFoundException": NotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
