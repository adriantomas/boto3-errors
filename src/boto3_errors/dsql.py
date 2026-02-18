# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class DSQLError(Boto3Error):
    _SERVICE = "dsql"


class AccessDeniedException(DSQLError):
    """You do not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(DSQLError):
    """The submitted action has conflicts."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """Resource Id"""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """Resource Type"""
        return self.response.get("resourceType")


class InternalServerException(DSQLError):
    """The request processing has failed because of an unknown error, exception or failure."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """Retry after seconds."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(DSQLError):
    """The resource could not be found."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID could not be found."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type could not be found."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(DSQLError):
    """The service limit was exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The service exceeds a quota."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The resource ID exceeds a quota."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type exceeds a quota."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The request exceeds a service quota."""
        return self.response.get("serviceCode")


class ThrottlingException(DSQLError):
    """The request was denied due to request throttling."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The request exceeds a request rate quota."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The request exceeds a request rate quota. Retry after seconds."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The request exceeds a service quota."""
        return self.response.get("serviceCode")


class ValidationException(DSQLError):
    """The input failed to satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that didn't validate."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason for the validation exception."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[DSQLError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
