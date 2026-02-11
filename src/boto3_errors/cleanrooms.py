# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class CleanRoomsError(Boto3Error):
    _SERVICE = "cleanrooms"


class AccessDeniedException(CleanRoomsError):
    """Caller does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def reason(self) -> str | None:
        """A reason code for the exception."""
        return self.response.get("reason")


class ConflictException(CleanRoomsError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the conflicting resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the conflicting resource."""
        return self.response.get("resourceType")

    @property
    def reason(self) -> str | None:
        """A reason code for the exception."""
        return self.response.get("reason")


class InternalServerException(CleanRoomsError):
    """Unexpected error during processing of request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(CleanRoomsError):
    """Request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The Id of the missing resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the missing resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(CleanRoomsError):
    """Request denied because service quota has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_name(self) -> str | None:
        """The name of the quota."""
        return self.response.get("quotaName")

    @property
    def quota_value(self) -> float | None:
        """The value of the quota."""
        return self.response.get("quotaValue")


class ThrottlingException(CleanRoomsError):
    """Request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"


class ValidationException(CleanRoomsError):
    """The input fails to satisfy the specified constraints."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """A reason code for the exception."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """Validation errors for specific input parameters."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[CleanRoomsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
