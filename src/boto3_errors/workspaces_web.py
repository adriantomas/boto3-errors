# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class WorkSpacesWebError(Boto3Error):
    _SERVICE = "workspaces-web"


class AccessDeniedException(WorkSpacesWebError):
    """Access is denied."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(WorkSpacesWebError):
    """There is a conflict."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")


class InternalServerException(WorkSpacesWebError):
    """There is an internal server error."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(WorkSpacesWebError):
    """The resource cannot be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """Hypothetical identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Hypothetical type of the resource affected."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(WorkSpacesWebError):
    """The service quota has been exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def resource_id(self) -> str | None:
        """Identifier of the resource affected."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Type of the resource affected."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The originating service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The originating quota."""
        return self.response.get("quotaCode")


class ThrottlingException(WorkSpacesWebError):
    """There is a throttling error."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The originating service."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The originating quota."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """Advice to clients on when the call can be safely retried."""
        return self.response.get("retryAfterSeconds")


class TooManyTagsException(WorkSpacesWebError):
    """There are too many tags."""
    _ERROR_CODE = "TooManyTagsException"

    @property
    def resource_name(self) -> str | None:
        """Name of the resource affected."""
        return self.response.get("resourceName")


class ValidationException(WorkSpacesWebError):
    """There is a validation error."""
    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """Reason the request failed validation"""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The field that caused the error."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[WorkSpacesWebError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "TooManyTagsException": TooManyTagsException,
    "ValidationException": ValidationException,
}
