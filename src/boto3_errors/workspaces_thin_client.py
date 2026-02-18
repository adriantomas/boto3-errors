# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WorkSpacesThinClientError(Boto3Error):
    _SERVICE = "workspaces-thin-client"


class AccessDeniedException(WorkSpacesThinClientError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(WorkSpacesThinClientError):
    """The requested operation would cause a conflict with the current state of a service
    resource associated with the request. Resolve the conflict before retrying this
    request.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource associated with the request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource associated with the request."""
        return self.response.get("resourceType")


class InternalServerException(WorkSpacesThinClientError):
    """The server encountered an internal error and is unable to complete the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the next request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(WorkSpacesThinClientError):
    """The resource specified in the request was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource associated with the request."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource associated with the request."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(WorkSpacesThinClientError):
    """Your request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code for the quota in Service Quotas."""
        return self.response.get("quotaCode")

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
        """The code for the service in Service Quotas."""
        return self.response.get("serviceCode")


class ThrottlingException(WorkSpacesThinClientError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code for the quota in Service Quotas."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the next request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code for the service in Service Quotas."""
        return self.response.get("serviceCode")


class ValidationException(WorkSpacesThinClientError):
    """The input fails to satisfy the specified constraints."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that didn't validate."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[WorkSpacesThinClientError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
