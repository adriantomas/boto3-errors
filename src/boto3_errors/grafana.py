# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class grafanaError(Boto3Error):
    _SERVICE = "grafana"


class AccessDeniedException(grafanaError):
    """You do not have sufficient permissions to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(grafanaError):
    """A resource was in an inconsistent state during an update or a deletion."""
    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that is associated with the error."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")


class InternalServerException(grafanaError):
    """Unexpected error while processing the request. Retry the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """How long to wait before you retry this operation."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(grafanaError):
    """The request references a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that is associated with the error."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(grafanaError):
    """The request would cause a service quota to be exceeded."""
    _ERROR_CODE = "ServiceQuotaExceededException"

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def resource_id(self) -> str | None:
        """The ID of the resource that is associated with the error."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The type of the resource that is associated with the error."""
        return self.response.get("resourceType")

    @property
    def service_code(self) -> str | None:
        """The value of a parameter in the request caused an error."""
        return self.response.get("serviceCode")


class ThrottlingException(grafanaError):
    """The request was denied because of request throttling. Retry the request."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The value of a parameter in the request caused an error."""
        return self.response.get("retryAfterSeconds")

    @property
    def service_code(self) -> str | None:
        """The ID of the service that is associated with the error."""
        return self.response.get("serviceCode")


class ValidationException(grafanaError):
    """The value of a parameter in the request caused an error."""
    _ERROR_CODE = "ValidationException"

    @property
    def field_list(self) -> list[Any] | None:
        """A list of fields that might be associated with the error."""
        return self.response.get("fieldList")

    @property
    def reason(self) -> str | None:
        """The reason that the operation failed."""
        return self.response.get("reason")


EXCEPTIONS: dict[str, type[grafanaError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
