# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTFleetHubError(Boto3Error):
    _SERVICE = "iotfleethub"


class ConflictException(IoTFleetHubError):
    """The request conflicts with the current state of the resource."""
    _ERROR_CODE = "ConflictException"


class InternalFailureException(IoTFleetHubError):
    """An unexpected error has occurred."""
    _ERROR_CODE = "InternalFailureException"


class InvalidRequestException(IoTFleetHubError):
    """The request is not valid."""
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(IoTFleetHubError):
    """A limit has been exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(IoTFleetHubError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(IoTFleetHubError):
    """The rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[IoTFleetHubError]] = {
    "ConflictException": ConflictException,
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
