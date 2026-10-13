# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class SageMakerTrainingSessionRuntimeError(Boto3Error):
    _SERVICE = "sagemakertrainingsessionruntime"


class ConflictException(SageMakerTrainingSessionRuntimeError):
    """The training session is in a state that cannot accept new operations. The session
    must be in `Running` or `Blocked` state to accept requests.
    """

    _ERROR_CODE = "ConflictException"


class InternalServerException(SageMakerTrainingSessionRuntimeError):
    """An internal service error occurred. Retry the request using exponential backoff."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(SageMakerTrainingSessionRuntimeError):
    """The specified training session or operation does not exist, or the operation does
    not belong to the specified training session.
    """

    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(SageMakerTrainingSessionRuntimeError):
    """The request was throttled. Retry the request after a brief wait using exponential
    backoff.
    """

    _ERROR_CODE = "ThrottlingException"


class ValidationException(SageMakerTrainingSessionRuntimeError):
    """The request is not valid. Check the request syntax and parameters. Examples include
    invalid sequence numbers, malformed client tokens, missing required fields, or
    invalid operation configuration.
    """

    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[SageMakerTrainingSessionRuntimeError]] = {
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
