# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class IoTWirelessError(Boto3Error):
    _SERVICE = "iotwireless"


class AccessDeniedException(IoTWirelessError):
    """User does not have permission to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(IoTWirelessError):
    """Adding, updating, or deleting the resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Id of the resource in the conflicting operation."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource in the conflicting operation."""
        return self.response.get("ResourceType")


class InternalServerException(IoTWirelessError):
    """An unexpected error occurred while processing a request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(IoTWirelessError):
    """Resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Id of the not found resource."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the font found resource."""
        return self.response.get("ResourceType")


class ThrottlingException(IoTWirelessError):
    """The request was denied because it exceeded the allowed API request rate."""
    _ERROR_CODE = "ThrottlingException"


class TooManyTagsException(IoTWirelessError):
    """The request was denied because the resource can't have any more tags."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """Name of the resource that exceeds maximum number of tags allowed."""
        return self.response.get("ResourceName")


class ValidationException(IoTWirelessError):
    """The input did not meet the specified constraints."""
    _ERROR_CODE = "ValidationException"


EXCEPTIONS: dict[str, type[IoTWirelessError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
