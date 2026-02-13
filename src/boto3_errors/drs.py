# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class drsError(Boto3Error):
    _SERVICE = "drs"


class AccessDeniedException(drsError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ConflictException(drsError):
    """The request could not be completed due to a conflict with the current state of the
    target resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("resourceType")


class InternalServerException(drsError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds after which the request should be safe to retry."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(drsError):
    """The resource for this operation was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(drsError):
    """The request could not be completed because its exceeded the service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def quota_code(self) -> str | None:
        """Quota code."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """Service code."""
        return self.response.get("serviceCode")


class ThrottlingException(drsError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """Quota code."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> str | None:
        """The number of seconds after which the request should be safe to retry."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """Service code."""
        return self.response.get("serviceCode")


class UninitializedAccountException(drsError):
    """The account performing the request has not been initialized."""
    _ERROR_CODE = "UninitializedAccountException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ValidationException(drsError):
    """The input fails to satisfy the constraints specified by the AWS service."""
    _ERROR_CODE = "ValidationException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that failed validation."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """Validation exception reason."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[drsError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UninitializedAccountException": UninitializedAccountException,
    "ValidationException": ValidationException,
}
