# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class GameLiftStreamsError(Boto3Error):
    _SERVICE = "gameliftstreams"


class AccessDeniedException(GameLiftStreamsError):
    """You don't have the required permissions to access this Amazon GameLift Streams
    resource. Correct the permissions before you try again.
    """

    _ERROR_CODE = "AccessDeniedException"


class ConflictException(GameLiftStreamsError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(GameLiftStreamsError):
    """The service encountered an internal error and is unable to complete the request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(GameLiftStreamsError):
    """The resource specified in the request was not found. Correct the request before you
    try again.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ServiceQuotaExceededException(GameLiftStreamsError):
    """The request would cause the resource to exceed an allowed service quota. Resolve the
    issue before you try again.
    """

    _ERROR_CODE = "ServiceQuotaExceededException"


class ThrottlingException(GameLiftStreamsError):
    """The request was denied due to request throttling. Retry the request after the
    suggested wait time.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(GameLiftStreamsError):
    """One or more parameter values in the request fail to satisfy the specified
    constraints. Correct the invalid parameter values before retrying the request.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[GameLiftStreamsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
