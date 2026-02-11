# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTEventsDataError(Boto3Error):
    _SERVICE = "iotevents-data"


class InternalFailureException(IoTEventsDataError):
    """An internal failure occurred."""
    _ERROR_CODE = "InternalFailureException"


class InvalidRequestException(IoTEventsDataError):
    """The request was invalid."""
    _ERROR_CODE = "InvalidRequestException"


class ResourceNotFoundException(IoTEventsDataError):
    """The resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(IoTEventsDataError):
    """The service is currently unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(IoTEventsDataError):
    """The request could not be completed due to throttling."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[IoTEventsDataError]] = {
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
