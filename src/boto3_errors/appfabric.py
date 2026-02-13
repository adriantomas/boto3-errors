# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class AppFabricError(Boto3Error):
    _SERVICE = "appfabric"


class AccessDeniedException(AppFabricError):
    """You are not authorized to perform this operation."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(AppFabricError):
    """The request has created a conflict. Check the request parameters and try again."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")


class InternalServerException(AppFabricError):
    """The request processing has failed because of an unknown error, exception, or failure
    with an internal server.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The period of time after which you should retry your request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(AppFabricError):
    """The specified resource does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(AppFabricError):
    """The request exceeds a service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The code of the service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The code for the quota exceeded."""
        return self.response.get("quotaCode")


class ThrottlingException(AppFabricError):
    """The request rate exceeds the limit."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The code of the service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The code for the quota exceeded."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The period of time after which you should retry your request."""
        return self.response.get("retryAfterSeconds")


class ValidationException(AppFabricError):
    """The request has invalid or missing parameters."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason for the exception."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The field list."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[AppFabricError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
