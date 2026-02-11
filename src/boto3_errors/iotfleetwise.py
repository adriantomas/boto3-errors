# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTFleetWiseError(Boto3Error):
    _SERVICE = "iotfleetwise"


class AccessDeniedException(IoTFleetWiseError):
    """You don't have sufficient permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(IoTFleetWiseError):
    """The request has conflicting operations. This can occur if you're trying to perform
    more than one operation on the same resource at the same time.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource(self) -> str | None:
        """The resource on which there are conflicting operations."""
        return self.response.get("resource")

    @property
    def resource_type(self) -> str | None:
        """The type of resource on which there are conflicting operations.."""
        return self.response.get("resourceType")


class DecoderManifestValidationException(IoTFleetWiseError):
    """The request couldn't be completed because it contains signal decoders with one or
    more validation errors.
    """

    _ERROR_CODE = "DecoderManifestValidationException"

    @property
    def invalid_signals(self) -> list[Any] | None:
        """The request couldn't be completed because of invalid signals in the request."""
        return self.response.get("invalidSignals")

    @property
    def invalid_network_interfaces(self) -> list[Any] | None:
        """The request couldn't be completed because of invalid network interfaces in the
        request.
        """
        return self.response.get("invalidNetworkInterfaces")


class InternalServerException(IoTFleetWiseError):
    """The request couldn't be completed because the server temporarily failed."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the command."""
        return self.response.get("retryAfterSeconds")


class InvalidNodeException(IoTFleetWiseError):
    """The specified node type doesn't match the expected node type for a node. You can
    specify the node type as branch, sensor, actuator, or attribute.
    """

    _ERROR_CODE = "InvalidNodeException"

    @property
    def invalid_nodes(self) -> list[Any] | None:
        """The specified node type isn't valid."""
        return self.response.get("invalidNodes")

    @property
    def reason(self) -> str | None:
        """The reason the node validation failed."""
        return self.response.get("reason")


class InvalidSignalsException(IoTFleetWiseError):
    """The request couldn't be completed because it contains signals that aren't valid."""
    _ERROR_CODE = "InvalidSignalsException"

    @property
    def invalid_signals(self) -> list[Any] | None:
        """The signals which caused the exception."""
        return self.response.get("invalidSignals")


class LimitExceededException(IoTFleetWiseError):
    """A service quota was exceeded."""
    _ERROR_CODE = "LimitExceededException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that was exceeded."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that was exceeded."""
        return self.response.get("resourceType")


class ResourceNotFoundException(IoTFleetWiseError):
    """The resource wasn't found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that wasn't found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that wasn't found."""
        return self.response.get("resourceType")


class ThrottlingException(IoTFleetWiseError):
    """The request couldn't be completed due to throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota identifier of the applied throttling rules for this request."""
        return self.response.get("quotaCode")

    @property
    def service_code(self) -> str | None:
        """The code for the service that couldn't be completed due to throttling."""
        return self.response.get("serviceCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the command."""
        return self.response.get("retryAfterSeconds")


class ValidationException(IoTFleetWiseError):
    """The input fails to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason the input failed to satisfy the constraints specified by an Amazon
        Web Services service.
        """
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that fail to satisfy the constraints specified by an Amazon
        Web Services service.
        """
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[IoTFleetWiseError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "DecoderManifestValidationException": DecoderManifestValidationException,
    "InternalServerException": InternalServerException,
    "InvalidNodeException": InvalidNodeException,
    "InvalidSignalsException": InvalidSignalsException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
