# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class ConnectSchedulingError(Boto3Error):
    _SERVICE = "connectscheduling"


class AccessDeniedException(ConnectSchedulingError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(ConnectSchedulingError):
    """The request could not be processed because of a conflict with the current state of
    the resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier or ARN of the resource that is in conflict."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is in conflict."""
        return self.response.get("ResourceType")


class InternalServerException(ConnectSchedulingError):
    """The request processing failed because of an error or failure with the service."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying."""
        return self.response.get("RetryAfterSeconds")


class ResourceNotFoundException(ConnectSchedulingError):
    """The specified resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier or ARN of the resource that was not found."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that was not found."""
        return self.response.get("ResourceType")


class ServiceQuotaExceededException(ConnectSchedulingError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code of the quota that would be exceeded, for use with the Service Quotas
        API.
        """
        return self.response.get("QuotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier or ARN of the resource whose quota would be exceeded."""
        return self.response.get("ResourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource whose quota would be exceeded."""
        return self.response.get("ResourceType")

    @property
    def service_code(self) -> str | None:
        """The code of the service that owns the quota."""
        return self.response.get("ServiceCode")


class ThrottlingException(ConnectSchedulingError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The code of the quota that was throttled, for use with the Service Quotas API."""
        return self.response.get("QuotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying."""
        return self.response.get("RetryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The code of the service that owns the quota."""
        return self.response.get("ServiceCode")


class ValidationException(ConnectSchedulingError):
    """The input fails to satisfy the constraints specified by an AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The specific input fields that failed validation, when `Reason` is
        `FIELD_VALIDATION_FAILED`.
        """
        return self.response.get("FieldList")

    @property
    def reason(self) -> str | None:
        """The reason the input failed validation. Branch on this value rather than on the
        message wording.
        """
        return self.response.get("Reason")


EXCEPTIONS: dict[str, type[ConnectSchedulingError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
