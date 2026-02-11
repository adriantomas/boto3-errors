# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class ComputeOptimizerError(Boto3Error):
    _SERVICE = "compute-optimizer"


class AccessDeniedException(ComputeOptimizerError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(ComputeOptimizerError):
    """An internal error has occurred. Try your call again."""
    _ERROR_CODE = "InternalServerException"


class InvalidParameterValueException(ComputeOptimizerError):
    """The value supplied for the input parameter is out of range or not valid."""
    _ERROR_CODE = "InvalidParameterValueException"


class LimitExceededException(ComputeOptimizerError):
    """The request exceeds a limit of the service."""
    _ERROR_CODE = "LimitExceededException"


class MissingAuthenticationToken(ComputeOptimizerError):
    """The request must contain either a valid (registered) Amazon Web Services access key
    ID or X.509 certificate.
    """

    _ERROR_CODE = "MissingAuthenticationToken"


class OptInRequiredException(ComputeOptimizerError):
    """The account is not opted in to Compute Optimizer."""
    _ERROR_CODE = "OptInRequiredException"


class ResourceNotFoundException(ComputeOptimizerError):
    """A resource that is required for the action doesn't exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(ComputeOptimizerError):
    """The request has failed due to a temporary failure of the server."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(ComputeOptimizerError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[ComputeOptimizerError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "InvalidParameterValueException": InvalidParameterValueException,
    "LimitExceededException": LimitExceededException,
    "MissingAuthenticationToken": MissingAuthenticationToken,
    "OptInRequiredException": OptInRequiredException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
