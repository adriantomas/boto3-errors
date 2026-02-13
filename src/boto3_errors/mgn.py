# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class mgnError(Boto3Error):
    _SERVICE = "mgn"


class AccessDeniedException(mgnError):
    """Operating denied due to a file permission or access check error."""
    _ERROR_CODE = "AccessDeniedException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ConflictException(mgnError):
    """The request could not be completed due to a conflict with the current state of the
    target resource.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def resource_id(self) -> str | None:
        """A conflict occurred when prompting for the Resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """A conflict occurred when prompting for resource type."""
        return self.response.get("resourceType")

    @property
    def errors(self) -> list[Any] | None:
        """Conflict Exception specific errors."""
        return self.response.get("errors")


class InternalServerException(mgnError):
    """The server encountered an unexpected condition that prevented it from fulfilling the
    request.
    """

    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The server encountered an unexpected condition that prevented it from fulfilling
        the request. The request will be retried again after x seconds.
        """
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(mgnError):
    """Resource not found exception."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def resource_id(self) -> str | None:
        """Resource ID not found error."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Resource type not found error."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(mgnError):
    """The request could not be completed because its exceeded the service quota."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def resource_id(self) -> str | None:
        """Exceeded the service quota resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Exceeded the service quota resource type."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """Exceeded the service quota service code."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Exceeded the service quota code."""
        return self.response.get("quotaCode")

    @property
    def quota_value(self) -> int | None:
        """Exceeded the service quota value."""
        return self.response.get("quotaValue")


class ThrottlingException(mgnError):
    """Reached throttling quota exception."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """Reached throttling quota exception service code."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """Reached throttling quota exception."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> str | None:
        """Reached throttling quota exception will retry after x seconds."""
        return self.response.get("retryAfterSeconds")


class UninitializedAccountException(mgnError):
    """Uninitialized account exception."""
    _ERROR_CODE = "UninitializedAccountException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")


class ValidationException(mgnError):
    """Validate exception."""
    _ERROR_CODE = "ValidationException"

    @property
    def code(self) -> str | None:
        return self.response.get("code")

    @property
    def reason(self) -> str | None:
        """Validate exception reason."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """Validate exception field list."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[mgnError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "UninitializedAccountException": UninitializedAccountException,
    "ValidationException": ValidationException,
}
