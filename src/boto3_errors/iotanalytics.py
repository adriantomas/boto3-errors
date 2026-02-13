# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class IoTAnalyticsError(Boto3Error):
    _SERVICE = "iotanalytics"


class InternalFailureException(IoTAnalyticsError):
    """There was an internal failure."""
    _ERROR_CODE = "InternalFailureException"


class InvalidRequestException(IoTAnalyticsError):
    """The request was not valid."""
    _ERROR_CODE = "InvalidRequestException"


class LimitExceededException(IoTAnalyticsError):
    """The command caused an internal limit to be exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceAlreadyExistsException(IoTAnalyticsError):
    """A resource with the same name already exists."""
    _ERROR_CODE = "ResourceAlreadyExistsException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_arn(self) -> str | None:
        """The ARN of the resource."""
        return self.response.get("resourceArn")


class ResourceNotFoundException(IoTAnalyticsError):
    """A resource with the specified name could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"


class ServiceUnavailableException(IoTAnalyticsError):
    """The service is temporarily unavailable."""
    _ERROR_CODE = "ServiceUnavailableException"


class ThrottlingException(IoTAnalyticsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


EXCEPTIONS: dict[str, type[IoTAnalyticsError]] = {
    "InternalFailureException": InternalFailureException,
    "InvalidRequestException": InvalidRequestException,
    "LimitExceededException": LimitExceededException,
    "ResourceAlreadyExistsException": ResourceAlreadyExistsException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceUnavailableException": ServiceUnavailableException,
    "ThrottlingException": ThrottlingException,
}
