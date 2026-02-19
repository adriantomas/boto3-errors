# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class NovaActError(Boto3Error):
    _SERVICE = "nova-act"


class AccessDeniedException(NovaActError):
    """You don't have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(NovaActError):
    """The request could not be completed due to a conflict with the current state of the
    resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that caused the conflict."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that caused the conflict."""
        return self.response.get("resourceType")


class InternalServerException(NovaActError):
    """An internal server error occurred. Please try again later."""
    _ERROR_CODE = "InternalServerException"

    @property
    def reason(self) -> str | None:
        """The reason for the internal server error."""
        return self.response.get("reason")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the request."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(NovaActError):
    """The requested resource was not found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that wasn't found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that wasn't found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(NovaActError):
    """The request would exceed a service quota limit."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The code for the specific quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The identifier of the resource that exceeded the quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of resource that exceeded the quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The service code for the quota that was exceeded."""
        return self.response.get("serviceCode")


class ThrottlingException(NovaActError):
    """The request was throttled due to too many requests. Please try again later."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The quota code related to the throttling."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying the throttled request."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The service code where throttling occurred."""
        return self.response.get("serviceCode")


class ValidationException(NovaActError):
    """The input parameters for the request are invalid."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """The list of fields that failed validation."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the validation failure."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[NovaActError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
