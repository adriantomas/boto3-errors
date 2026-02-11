# Auto-generated. Do not edit manually.
from __future__ import annotations

from typing import Any

from boto3_errors._base import Boto3Error


class NotificationsContactsError(Boto3Error):
    _SERVICE = "notificationscontacts"


class AccessDeniedException(NotificationsContactsError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(NotificationsContactsError):
    """Updating or deleting a resource can cause an inconsistent state."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID that prompted the conflict error."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type that prompted the conflict error."""
        return self.response.get("resourceType")


class InternalServerException(NotificationsContactsError):
    """Unexpected error during processing of request."""
    _ERROR_CODE = "InternalServerException"


class ResourceNotFoundException(NotificationsContactsError):
    """Your request references a resource which does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that wasn't found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that wasn't found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(NotificationsContactsError):
    """Request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that exceeds the service quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that exceeds the service quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code for the service quota exceeded in Service Quotas."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The code for the service quota in Service Quotas."""
        return self.response.get("quotaCode")


class ThrottlingException(NotificationsContactsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """Identifies the service being throttled."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Identifies the quota that is being throttled."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds a client should wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(NotificationsContactsError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason why your input is considered invalid."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The list of input fields that are invalid."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[NotificationsContactsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
