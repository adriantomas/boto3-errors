# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WorkLinkError(Boto3Error):
    _SERVICE = "worklink"


class InternalServerErrorException(WorkLinkError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "InternalServerErrorException"


class InvalidRequestException(WorkLinkError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"


class ResourceAlreadyExistsException(WorkLinkError):
    """The resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(WorkLinkError):
    """The requested resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class TooManyRequestsException(WorkLinkError):
    """The number of requests exceeds the limit."""
    _ERROR_CODE = "TooManyRequestsException"


class UnauthorizedException(WorkLinkError):
    """You are not authorized to perform this action."""
    _ERROR_CODE = "UnauthorizedException"


EXCEPTIONS: dict[str, type[WorkLinkError]] = {
    "InternalServerErrorException": InternalServerErrorException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "TooManyRequestsException": TooManyRequestsException,
    "UnauthorizedException": UnauthorizedException,
}
