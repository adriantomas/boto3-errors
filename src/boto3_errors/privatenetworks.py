# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class PrivateNetworksError(Boto3Error):
    _SERVICE = "privatenetworks"


class AccessDeniedException(PrivateNetworksError):
    """You do not have permission to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class InternalServerException(PrivateNetworksError):
    """Information about an internal error."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")


class LimitExceededException(PrivateNetworksError):
    """The limit was exceeded."""
    _ERROR_CODE = "LimitExceededException"


class ResourceNotFoundException(PrivateNetworksError):
    """The resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the affected resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the affected resource."""
        return self.response.get("resourceType")


class ThrottlingException(PrivateNetworksError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(PrivateNetworksError):
    """The request failed validation."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that caused the error, if applicable."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """Reason the request failed validation."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[PrivateNetworksError]] = {
    "AccessDeniedException": AccessDeniedException,
    "InternalServerException": InternalServerException,
    "LimitExceededException": LimitExceededException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
