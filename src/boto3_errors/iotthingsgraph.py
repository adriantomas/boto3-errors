# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTThingsGraphError(Boto3Error):
    _SERVICE = "iotthingsgraph"


class InternalFailureException(IoTThingsGraphError):
    _ERROR_CODE = "InternalFailureException"


class InvalidRequestException(IoTThingsGraphError):
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(IoTThingsGraphError):
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(IoTThingsGraphError):
    _ERROR_CODE = "ResourceAlreadyExistsException"


class ResourceInUseException(IoTThingsGraphError):
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(IoTThingsGraphError):
    _ERROR_CODE = "ResourceNotFoundException"


class ThrottlingException(IoTThingsGraphError):
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[IoTThingsGraphError]] = {
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
}
