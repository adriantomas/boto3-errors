# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class RoboMakerError(Boto3Error):
    _SERVICE = "robomaker"


class ConcurrentDeploymentException(RoboMakerError):
    """The failure percentage threshold percentage was met."""
    _ERROR_CODE = "ConcurrentDeploymentException"


class IdempotentParameterMismatchException(RoboMakerError):
    """The request uses the same client token as a previous, but non-identical request. Do
    not reuse a client token with different requests, unless the requests are identical.
    """

    _ERROR_CODE = "IdempotentParameterMismatchException"


class InternalServerException(RoboMakerError):
    """AWS RoboMaker experienced a service issue. Try your call again."""
    _ERROR_CODE = "InternalServerException"


class InvalidParameterException(RoboMakerError):
    """A parameter specified in a request is not valid, is unsupported, or cannot be used.
    The returned message provides an explanation of the error value.
    """

    _ERROR_CODE = "InvalidParameterException"


class LimitExceededException(RoboMakerError):
    """The requested resource exceeds the maximum number allowed, or the number of
    concurrent stream requests exceeds the maximum number allowed.
    """

    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(RoboMakerError):
    """The specified resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceNotFoundException(RoboMakerError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(RoboMakerError):
    """The request has failed due to a temporary failure of the server."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(RoboMakerError):
    """AWS RoboMaker is temporarily unable to process the request. Try your call again."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[RoboMakerError]] = {
    "ConcurrentDeploymentException": ConcurrentDeploymentException,
    "IdempotentParameterMismatchException": IdempotentParameterMismatchException,
    "InternalServerException": InternalServerException,
    "InvalidParameterException": InvalidParameterException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
