# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTEventsError(Boto3Error):
    _SERVICE = "iotevents"


class InternalFailureException(IoTEventsError):
    """An internal failure occurred."""
    _ERROR_CODE = "InternalFailureException"


class InvalidRequestException(IoTEventsError):
    """The request was invalid."""
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(IoTEventsError):
    """A limit was exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(IoTEventsError):
    """The resource already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_arn(self) -> str | None:
        """The ARN of the resource."""
        return self.response.get("resourceArn")


class ResourceInUseException(IoTEventsError):
    """The resource is in use."""
    _ERROR_CODE = "ResourceInUseException"


class ResourceNotFoundException(IoTEventsError):
    """The resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(IoTEventsError):
    """The service is currently unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(IoTEventsError):
    """The request could not be completed due to throttling."""
    _ERROR_CODE = "ThrottlingException"


class UnsupportedOperationException(IoTEventsError):
    """The requested operation is not supported."""
    _ERROR_CODE = "UnsupportedOperationException"


EXCEPTIONS: dict[str, type[IoTEventsError]] = {
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceInUseException": ResourceInUseException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
    "UnsupportedOperationException": UnsupportedOperationException,
}
