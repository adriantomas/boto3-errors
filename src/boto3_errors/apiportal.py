# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class APIPortalError(Boto3Error):
    _SERVICE = "apiportal"


class AccessDeniedException(APIPortalError):
    """You do not have permission to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class BadRequestException(APIPortalError):
    """The request is not valid. The message identifies the field or value that failed
    validation.
    """

    _ERROR_CODE = "BadRequestException"


class ConflictException(APIPortalError):
    """The request conflicts with the current state of the resource, for example because
    another operation on it is still in progress.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(APIPortalError):
    """The service encountered an internal error. Try the request again."""
    _ERROR_CODE = "InternalServerException"


class LimitExceededException(APIPortalError):
    """The request rate or a service quota was exceeded. Reduce the request rate or the
    number of resources and try again.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(APIPortalError):
    """The requested resource does not exist, or you do not have access to it."""
    _ERROR_CODE = "ResourceNotFoundException"


EXCEPTIONS: dict[str, type[APIPortalError]] = {
    "AccessDeniedException": AccessDeniedException,
    "BadRequestException": BadRequestException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
}
