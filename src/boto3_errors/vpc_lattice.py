# Auto-generated. Do not edit manually.
from typing import Any

from boto3_errors._base import Boto3Error


class VPCLatticeError(Boto3Error):
    _SERVICE = "vpc-lattice"


class AccessDeniedException(VPCLatticeError):
    """The user does not have sufficient access to perform this action."""
    _ERROR_CODE = "AccessDeniedException"


class ConflictException(VPCLatticeError):
    """The request conflicts with the current state of the resource. Updating or deleting a
    resource can cause an inconsistent state.
    """

    _ERROR_CODE = "ConflictException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")


class InternalServerException(VPCLatticeError):
    """An unexpected error occurred while processing the request."""
    _ERROR_CODE = "InternalServerException"

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying."""
        return self.response.get("retryAfterSeconds")


class ResourceNotFoundException(VPCLatticeError):
    """The request references a resource that does not exist."""
    _ERROR_CODE = "ResourceNotFoundException"

    @property
    def resource_id(self) -> str | None:
        """The resource ID."""
        return self.response.get("resourceId")

    @property
    def resource_type(self) -> str | None:
        """The resource type."""
        return self.response.get("resourceType")


class ServiceQuotaExceededException(VPCLatticeError):
    """The request would cause a service quota to be exceeded."""
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
        """The service code."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")


class ThrottlingException(VPCLatticeError):
    """The limit on the number of requests per second was exceeded."""
    _ERROR_CODE = "ThrottlingException"

    @property
    def service_code(self) -> str | None:
        """The service code."""
        return self.response.get("serviceCode")

    @property
    def quota_code(self) -> str | None:
        """The ID of the service quota that was exceeded."""
        return self.response.get("quotaCode")

    @property
    def retry_after_seconds(self) -> int | None:
        """The number of seconds to wait before retrying."""
        return self.response.get("retryAfterSeconds")


class ValidationException(VPCLatticeError):
    """The input does not satisfy the constraints specified by an Amazon Web Services
    service.
    """

    _ERROR_CODE = "ValidationException"

    @property
    def reason(self) -> str | None:
        """The reason."""
        return self.response.get("reason")

    @property
    def field_list(self) -> list[Any] | None:
        """The fields that failed validation."""
        return self.response.get("fieldList")


EXCEPTIONS: dict[str, type[VPCLatticeError]] = {
    "AccessDeniedException": AccessDeniedException,
    "ConflictException": ConflictException,
    "InternalServerException": InternalServerException,
    "ResourceNotFoundException": ResourceNotFoundException,
    "ServiceQuotaExceededException": ServiceQuotaExceededException,
    "ThrottlingException": ThrottlingException,
    "ValidationException": ValidationException,
}
